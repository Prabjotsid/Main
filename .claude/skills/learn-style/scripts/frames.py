#!/usr/bin/env python3
"""Find the cuts in a video, pull frames, and measure the edit in numbers.

    python3 frames.py <video> --out .learn-style/<slug>

Writes into <out>:
  shots/shot_001_t0.00.jpg        one frame from the middle of every shot
  shots_grid/shot_001_t0.00.jpg   the same frame with a 10 % grid drawn on it
                                  (each line = 10 % of width/height) so caption
                                  and text positions can be read as numbers
  sheets/hook_12fps.jpg           the first --hook seconds at 12 fps, one sheet
  sheets/transition_001_t2.40.jpg 1 second around every cut at 12 fps
  cuts.json                       every number below

Numbers in cuts.json:
  cuts per 10 s (overall and per 10 s window), shot lengths (mean, median,
  min, max, each one), transition length in frames for every cut, zoom inside
  each shot (push-in / pull-out, % and % per second), and scale jump across
  each cut (a "punch-in" jump cut shows as e.g. 1.15).

The cut, transition and zoom numbers are estimates from pixel differences.
Check them against the sheets before trusting them: a fast hand wave can look
like a cut, and a soft dissolve can be missed.
"""
import argparse
import json
import math
import statistics
import subprocess
import sys
from pathlib import Path

import numpy as np

SHEET_COLS = 6
SHEET_FPS = 12


def run(cmd):
    return subprocess.run(cmd, capture_output=True, check=True)


def probe(path):
    out = run(["ffprobe", "-v", "error", "-select_streams", "v:0",
               "-show_entries", "stream=width,height,r_frame_rate:stream_side_data=rotation:format=duration",
               "-of", "json", str(path)]).stdout
    data = json.loads(out)
    st = data["streams"][0]
    num, den = st["r_frame_rate"].split("/")
    w, h = st["width"], st["height"]
    rot = 0
    for sd in st.get("side_data_list", []):
        rot = abs(int(sd.get("rotation", 0)))
    if rot in (90, 270):
        w, h = h, w
    return w, h, float(num) / float(den), float(data["format"]["duration"])


def load_gray(path, fps, w, h):
    """Whole video as small grayscale frames at a constant frame rate."""
    sw = 72
    sh = max(2, int(round(sw * h / w / 2)) * 2)
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-an",
           "-vf", f"fps={fps:.5f},scale={sw}:{sh}:flags=area,format=gray",
           "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (sw * sh)
    return np.frombuffer(raw[: n * sw * sh], dtype=np.uint8).reshape(n, sh, sw).astype(np.float32)


def find_transitions(frames, fps, hard=0.18, floor=0.012):
    """Return a list of transitions: (first_changed_frame, last_changed_frame, peak)."""
    diff = np.abs(frames[1:] - frames[:-1]).mean(axis=(1, 2)) / 255.0
    diff = np.concatenate([[0.0], diff])            # diff[i] = change from i-1 to i
    n = len(diff)
    win = max(3, int(fps * 0.75))
    trans = []
    i = 1
    while i < n:
        lo, hi = max(0, i - win), min(n, i + win + 1)
        base = float(np.median(diff[lo:hi]))
        low = max(floor, base * 4.0)
        if diff[i] <= low:
            i += 1
            continue
        j = i
        while j + 1 < n and diff[j + 1] > low:
            j += 1
        run_vals = diff[i: j + 1]
        peak, total, length = float(run_vals.max()), float(run_vals.sum()), j - i + 1
        spike = peak >= hard or (peak >= 0.06 and peak >= 8.0 * max(base, 0.004))
        # a gradual change only counts if the picture really ends up different
        a = frames[max(0, i - 2)]
        b = frames[min(n - 1, j + 1)]
        end_change = float(np.abs(a - b).mean() / 255.0)
        gradual = length >= 3 and total >= 0.15 and end_change >= 0.08
        if (spike and end_change >= 0.03) or gradual:
            trans.append((i, j, peak))
        i = j + 1
    # merge transitions closer than 0.2 s (one effect seen twice)
    merged = []
    gap = max(2, int(fps * 0.2))
    for t in trans:
        if merged and t[0] - merged[-1][1] <= gap:
            p = merged[-1]
            merged[-1] = (p[0], t[1], max(p[2], t[2]))
        else:
            merged.append(t)
    return merged


def zoomed(img, s, dy=0.0):
    """Zoom into img by factor s (>1) around the centre, shifted vertically by dy."""
    h, w = img.shape
    ch, cw = h / s, w / s
    y0 = (h - ch) / 2 + dy * (h - ch) / 2
    x0 = (w - cw) / 2
    ys = np.clip((y0 + (np.arange(h) + 0.5) * ch / h).astype(int), 0, h - 1)
    xs = np.clip((x0 + (np.arange(w) + 0.5) * cw / w).astype(int), 0, w - 1)
    return img[np.ix_(ys, xs)]


def scale_between(a, b):
    """How much bigger the picture is in b than in a. 1.0 = same framing.

    Returns (scale, confidence 0..1). Low confidence means the two frames are
    simply different pictures, not a zoom of each other.
    """
    def err(x, y):
        x = x - x.mean()
        y = y - y.mean()
        return float(np.mean((x - y) ** 2))

    def corr(x, y):
        x = x - x.mean()
        y = y - y.mean()
        d = float(np.sqrt((x * x).sum() * (y * y).sum()))
        return float((x * y).sum() / d) if d > 0 else 0.0

    e1 = err(a, b)
    if e1 < 1e-6:
        return 1.0, 1.0
    best_s, best_e, best_pair = 1.0, e1, (a, b)
    for k in range(1, 26):                           # 1.02 .. 1.50
        s = 1 + 0.02 * k
        for dy in (-0.6, -0.3, 0.0, 0.3):
            za = zoomed(a, s, dy)
            e_in = err(za, b)                        # b is a zoomed-in a
            if e_in < best_e:
                best_s, best_e, best_pair = s, e_in, (za, b)
            zb = zoomed(b, s, dy)
            e_out = err(a, zb)                       # b is a zoomed-out a
            if e_out < best_e:
                best_s, best_e, best_pair = 1 / s, e_out, (a, zb)
    if corr(*best_pair) < 0.6:                       # different pictures, not a zoom
        return 1.0, 0.0
    conf = max(0.0, 1.0 - best_e / e1)
    if abs(best_s - 1.0) < 0.03 or conf < 0.25:
        # either no zoom, or frames do not match as a zoom
        still = e1 / (255.0 ** 2) < 0.004
        return 1.0, (1.0 if still else 0.0)
    return round(best_s, 2), round(conf, 2)


def grab(path, t, dest, width, grid=False):
    vf = f"scale={width}:-2"
    if grid:
        vf += ",drawgrid=w=iw/10:h=ih/10:t=1:c=yellow@0.7"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, t):.3f}", "-i", str(path),
         "-frames:v", "1", "-vf", vf, "-q:v", "3", str(dest)])


def sheet(path, start, dur, dest, cell_w):
    start = max(0.0, start)
    n = max(1, int(round(dur * SHEET_FPS)))
    rows = math.ceil(n / SHEET_COLS)
    vf = f"fps={SHEET_FPS},scale={cell_w}:-2,tile={SHEET_COLS}x{rows}:padding=4:margin=4:color=black"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", str(path),
         "-vf", vf, "-frames:v", "1", "-q:v", "3", str(dest)])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--out", required=True)
    ap.add_argument("--hook", type=float, default=3.0, help="seconds counted as the hook (default 3)")
    ap.add_argument("--frame-width", type=int, default=540, help="width of shot frames in px")
    ap.add_argument("--cell-width", type=int, default=180, help="width of one frame on a sheet in px")
    ap.add_argument("--sensitivity", type=float, default=0.18,
                    help="lower finds more cuts, higher finds fewer (default 0.18)")
    args = ap.parse_args()

    video, out = Path(args.video), Path(args.out)
    for d in ("shots", "shots_grid", "sheets"):
        (out / d).mkdir(parents=True, exist_ok=True)
        for old in (out / d).glob("*.jpg"):
            old.unlink()

    w, h, fps, dur = probe(video)
    frames = load_gray(video, fps, w, h)
    n = len(frames)
    dur = n / fps
    trans = find_transitions(frames, fps, hard=args.sensitivity)

    # shots are the stretches between transitions
    bounds = [0] + [int(round((a + b) / 2)) for a, b, _ in trans] + [n]
    shots = []
    for k in range(len(bounds) - 1):
        s_f = bounds[k] if k == 0 else trans[k - 1][1] + 1
        e_f = (trans[k][0] - 1) if k < len(trans) else n - 1
        e_f = max(e_f, s_f)
        start, end = bounds[k] / fps, bounds[k + 1] / fps
        pad = min(2, (e_f - s_f) // 4)
        zs, zc = scale_between(frames[s_f + pad], frames[e_f - pad])
        length = end - start
        zoom_pct = round((zs - 1) * 100, 1)
        shots.append({
            "n": k + 1,
            "start_s": round(start, 2),
            "end_s": round(end, 2),
            "length_s": round(length, 2),
            "zoom_in_shot_pct": zoom_pct,
            "zoom_pct_per_s": round(zoom_pct / length, 1) if length > 0 else 0.0,
            "zoom_confidence": zc,
        })
        mid = (s_f + e_f) / 2 / fps
        name = f"shot_{k + 1:03d}_t{mid:.2f}.jpg"
        grab(video, mid, out / "shots" / name, args.frame_width)
        grab(video, mid, out / "shots_grid" / name, args.frame_width, grid=True)

    transitions = []
    for k, (a, b, peak) in enumerate(trans):
        length = b - a + 1
        before = frames[max(0, a - 2)]
        after = frames[min(n - 1, b + 2)]
        js, jc = scale_between(before, after)
        t = (a + b) / 2 / fps
        kind = "hard cut" if length <= 2 else "gradual (dissolve, wipe, whip or zoom: look at the sheet)"
        name = f"transition_{k + 1:03d}_t{t:.2f}.jpg"
        sheet(video, t - 0.5, 1.0, out / "sheets" / name, args.cell_width)
        transitions.append({
            "n": k + 1,
            "time_s": round(t, 2),
            "length_frames": int(length),
            "length_s": round(length / fps, 3),
            "kind": kind,
            "scale_jump": js,
            "scale_jump_confidence": jc,
            "looks_like": ("punch-in/out on the same shot" if jc >= 0.25 and js != 1.0
                           else "same framing (jump cut)" if jc >= 0.9 and js == 1.0
                           else "new picture"),
            "sheet": f"sheets/{name}",
        })

    hook = min(args.hook, dur)
    sheet(video, 0.0, hook, out / "sheets" / "hook_12fps.jpg", args.cell_width)

    lengths = [s["length_s"] for s in shots]
    windows = []
    for k in range(math.ceil(dur / 10)):
        lo, hi = k * 10, min((k + 1) * 10, dur)
        c = sum(1 for t in transitions if lo <= t["time_s"] < hi)
        windows.append({"from_s": lo, "to_s": round(hi, 2), "cuts": c})
    t_frames = [t["length_frames"] for t in transitions]
    zooming = [s for s in shots if abs(s["zoom_in_shot_pct"]) >= 3 and s["zoom_confidence"] >= 0.25]
    punch = [t for t in transitions if t["looks_like"].startswith("punch")]

    result = {
        "video": {"width": w, "height": h, "fps": round(fps, 3), "duration_s": round(dur, 2),
                  "aspect": f"{w}:{h}", "frames": n},
        "summary": {
            "cuts": len(transitions),
            "cuts_per_10s": round(len(transitions) / dur * 10, 2) if dur else 0,
            "shots": len(shots),
            "shot_length_s": {
                "mean": round(statistics.mean(lengths), 2),
                "median": round(statistics.median(lengths), 2),
                "min": round(min(lengths), 2),
                "max": round(max(lengths), 2),
            },
            "hook_s": hook,
            "cuts_in_hook": sum(1 for t in transitions if t["time_s"] < hook),
            "first_cut_s": transitions[0]["time_s"] if transitions else None,
            "transition_frames": {
                "median": statistics.median(t_frames) if t_frames else None,
                "max": max(t_frames) if t_frames else None,
                "hard_cuts": sum(1 for t in transitions if t["kind"] == "hard cut"),
                "gradual": sum(1 for t in transitions if t["kind"] != "hard cut"),
            },
            "zoom": {
                "shots_with_zoom": len(zooming),
                "share_of_shots_pct": round(100 * len(zooming) / len(shots), 0),
                "median_zoom_pct": (round(statistics.median([s["zoom_in_shot_pct"] for s in zooming]), 1)
                                    if zooming else None),
                "median_zoom_pct_per_s": (round(statistics.median([s["zoom_pct_per_s"] for s in zooming]), 1)
                                          if zooming else None),
                "punch_cuts": len(punch),
                "median_punch_scale": (round(statistics.median([t["scale_jump"] for t in punch]), 2)
                                       if punch else None),
            },
        },
        "cuts_per_10s_windows": windows,
        "shots": shots,
        "transitions": transitions,
        "note": "Estimates from pixel differences. Check against sheets/ before using.",
    }
    (out / "cuts.json").write_text(json.dumps(result, indent=2))
    print(json.dumps({"video": result["video"], "summary": result["summary"],
                      "cuts_per_10s_windows": windows}, indent=2))
    print(f"\nWrote {len(shots)} shot frames, {len(transitions)} transition sheets and the hook sheet to {out}/")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.stderr.write((exc.stderr or b"").decode(errors="replace"))
        sys.exit(1)

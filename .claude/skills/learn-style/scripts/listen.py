#!/usr/bin/env python3
"""Listen to a video's sound with earshot and measure the sound design in numbers.

    python3 listen.py <video> --out .learn-style/<slug> [--detail normal]

Needs the `earshot` command (see the earshot skill). Run frames.py first: its
cuts are passed to earshot so "does a sound land on the cut?" is answered for
the same cuts the rest of the notes use.

Writes into <out>:
  sound.json        numbers only, safe to copy into notes: loudness (LUFS,
                    true peak, loudness range), music (present or not, tempo),
                    sound events per 10 s, share of cuts that have a sound on
                    them and how many ms early or late it lands, silences.
  sound_timeline.txt  earshot's second-by-second listening transcript.
  sound_sheet.png   one picture: frames, sound events, spectrogram, loudness
                    and sync markers. Open it to see where sounds sit.
  earshot_timeline.json  earshot's full result.

Times, levels and sync offsets are measurements. The names earshot gives to
sounds ("whoosh", "pop") are guesses by a model and are often wrong on voice
and music: treat them as hints and say so in the notes.
"""
import argparse
import json
import shutil
import statistics
import subprocess
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--out", required=True)
    ap.add_argument("--detail", default="normal", choices=["low", "normal", "high"])
    ap.add_argument("--no-sheet", action="store_true", help="skip the picture (faster)")
    args = ap.parse_args()

    if not shutil.which("earshot"):
        print("NO_EARSHOT: the earshot command is not installed, so sound was not measured. "
              "Say that in the notes instead of guessing.")
        return 2

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    full = out / "earshot_timeline.json"

    cues = []
    cuts_file = out / "cuts.json"
    if cuts_file.exists():
        cues = [t["time_s"] for t in json.loads(cuts_file.read_text()).get("transitions", [])]
    cue_args = ["--cues", ",".join(f"{t:.3f}" for t in cues)] if cues else []

    run = subprocess.run(["earshot", "timeline", args.video, "--detail", args.detail,
                          "--out", str(full)] + cue_args, capture_output=True, text=True)
    if run.returncode != 0 or not full.exists():
        print("EARSHOT_FAILED: " + (run.stderr.strip().splitlines() or ["unknown error"])[-1])
        return 1
    (out / "sound_timeline.txt").write_text(run.stdout)
    d = json.loads(full.read_text())

    if not d.get("has_audio", True):
        sound = {"has_audio": False}
    else:
        dur = float(d.get("duration") or 0) or 1.0
        loud = d.get("loudness", {})
        music = d.get("music", {})
        events = d.get("events", [])
        clear = [e for e in events if (e.get("prominence_db") or 0) >= 6]
        kinds = {}
        for e in events:
            k = e.get("kind")
            if k:
                kinds[k] = kinds.get(k, 0) + 1
        sync = {}
        for name, block in (d.get("sync") or {}).items():
            if isinstance(block, dict) and block.get("stats"):
                sync[name] = block["stats"]
        silences = [s for s in loud.get("silences", []) if s.get("where") not in ("lead-in", "tail")]
        sound = {
            "has_audio": True,
            "duration_s": round(dur, 2),
            "loudness": {
                "integrated_lufs": loud.get("integrated_lufs"),
                "true_peak_dbtp": loud.get("true_peak_dbtp"),
                "loudness_range_lu": loud.get("lra_lu"),
                "clipped_samples": (loud.get("clipping") or {}).get("samples"),
            },
            "music": {
                "beat_confidence": music.get("confidence"),
                "tempo_bpm": music.get("tempo") if music.get("confidence") not in (None, "none") else None,
                "note": "beat_confidence none = no steady beat found (speech only, or no music)",
            },
            "sections": [{"from_s": s.get("start"), "to_s": s.get("end"), "label": s.get("label"),
                          "lufs": s.get("lufs")} for s in d.get("sections", [])],
            "sound_events": {
                "all": len(events),
                "clear_6db_over_bed": len(clear),
                "clear_per_10s": round(len(clear) / dur * 10, 1),
                "median_length_ms": (statistics.median([e["length_ms"] for e in clear if e.get("length_ms")])
                                     if any(e.get("length_ms") for e in clear) else None),
                "kinds_guessed_by_model": kinds,
            },
            "sync_of_sound_to_picture": sync,
            "sync_note": "offset = sound minus picture in ms; negative = sound arrives early. "
                         "'cues' are the cuts found by frames.py, 'cuts' are earshot's own.",
            "silences_inside": {
                "count": len(silences),
                "per_minute": round(len(silences) / dur * 60, 1),
                "median_s": round(statistics.median([s["dur"] for s in silences]), 2) if silences else None,
            },
        }
    (out / "sound.json").write_text(json.dumps(sound, indent=2))
    print(json.dumps(sound, indent=2))

    if not args.no_sheet and sound.get("has_audio"):
        sheet = out / "sound_sheet.png"
        r = subprocess.run(["earshot", "sheet", args.video, "-o", str(sheet), "--detail", "low"] + cue_args,
                           capture_output=True, text=True)
        print(f"\nsheet: {sheet}" if r.returncode == 0 and sheet.exists()
              else "\nsheet not made: " + (r.stderr.strip().splitlines() or ["unknown error"])[-1])
    print(f"timeline: {out / 'sound_timeline.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

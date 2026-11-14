#!/usr/bin/env python3
"""Read the main colours of an image, a video frame, or one box inside it, as hex.

    python3 colors.py <image>                      whole image
    python3 colors.py <image> --box 10,62,80,12    only that box
    python3 colors.py <video> --t 4.2 --box ...    a frame of a video

--box is x,y,width,height in PERCENT of the picture (the yellow grid on the
shots_grid frames marks every 10 %). Use a tight box around a caption to get
the text colour and its background/outline colour; the largest share is
usually the background, the next one the text.
"""
import argparse
import json
import subprocess
import sys

import numpy as np


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--box", default=None, help="x,y,w,h in percent")
    ap.add_argument("--t", type=float, default=None, help="timestamp in seconds (video only)")
    ap.add_argument("--top", type=int, default=6)
    args = ap.parse_args()

    vf = []
    if args.box:
        x, y, w, h = [float(v) / 100 for v in args.box.split(",")]
        vf.append(f"crop=iw*{w}:ih*{h}:iw*{x}:ih*{y}")
    vf.append("scale=160:160:force_original_aspect_ratio=decrease:flags=area")
    vf.append("format=rgb24")
    cmd = ["ffmpeg", "-v", "error"]
    if args.t is not None:
        cmd += ["-ss", f"{args.t:.3f}"]
    cmd += ["-i", args.path, "-frames:v", "1", "-vf", ",".join(vf), "-f", "rawvideo", "-"]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0 or not res.stdout:
        sys.stderr.write(res.stderr.decode(errors="replace"))
        return 1
    px = np.frombuffer(res.stdout, dtype=np.uint8).reshape(-1, 3).astype(np.int64)

    # group similar colours (5 levels of 3 bits per channel), report each group's average
    key = (px[:, 0] >> 5) * 64 + (px[:, 1] >> 5) * 8 + (px[:, 2] >> 5)
    out = []
    for k in np.unique(key):
        grp = px[key == k]
        r, g, b = grp.mean(axis=0).round().astype(int)
        out.append({"hex": f"#{r:02X}{g:02X}{b:02X}", "share_pct": round(100 * len(grp) / len(px), 1)})
    out.sort(key=lambda c: -c["share_pct"])
    print(json.dumps(out[: args.top], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

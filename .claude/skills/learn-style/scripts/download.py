#!/usr/bin/env python3
"""Fetch one reference video into a work folder.

    python3 download.py <url-or-local-file> --out .learn-style/<slug>

Local file  -> copied to <out>/source.<ext>
URL         -> downloaded with yt-dlp to <out>/source.mp4

A copy of the video is also kept as reference/<slug>.<ext> in the project
folder (the owner's library of reference reels), where <slug> is the name of
the <out> folder. Use --reference-dir to change the folder, or "" to skip.

Never uses cookies, logins or credentials. If the site wants a login, or the
download fails for any other reason, the script stops and prints a line that
starts with NEED_FILE so the person can be asked for the file instead.

Exit codes: 0 ok | 3 login needed | 4 network blocked | 5 other failure
Writes <out>/source.json (where it came from + basic video facts; no titles
or captions, because those are the creator's words).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

LOGIN = re.compile(
    r"sign in|log ?in|login required|cookies|private video|members[- ]only|"
    r"age[- ]restricted|confirm your age|not a bot|authentication|"
    r"requested content is not available|rate-limit reached|account",
    re.I,
)
NETWORK = re.compile(
    r"proxy|403|forbidden|tunnel connection failed|unable to connect|"
    r"connection (refused|reset)|timed out|name or service not known|"
    r"temporary failure in name resolution|ssl",
    re.I,
)


def probe(path: Path) -> dict:
    cmd = ["ffprobe", "-v", "error", "-select_streams", "v:0",
           "-show_entries", "stream=width,height,r_frame_rate:format=duration",
           "-of", "json", str(path)]
    try:
        data = json.loads(subprocess.run(cmd, capture_output=True, text=True, check=True).stdout)
        st = data["streams"][0]
        num, den = st["r_frame_rate"].split("/")
        return {
            "width": st["width"],
            "height": st["height"],
            "fps": round(float(num) / float(den), 3),
            "duration_s": round(float(data["format"]["duration"]), 2),
        }
    except Exception as exc:  # not a readable video
        return {"error": f"ffprobe could not read the file: {exc}"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="video URL or path to a local video file")
    ap.add_argument("--out", required=True, help="work folder for this reference")
    ap.add_argument("--reference-dir", default="reference",
                    help="folder that keeps a copy of every reference video (default: reference)")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    info = {"source": args.source}

    local = Path(args.source).expanduser()
    if local.is_file():
        dest = out / f"source{local.suffix.lower() or '.mp4'}"
        if local.resolve() != dest.resolve():
            shutil.copy2(local, dest)
        info["kind"] = "local file"
    elif re.match(r"https?://", args.source):
        dest = out / "source.mp4"
        cmd = ["yt-dlp", "--no-playlist", "--no-progress", "--no-warnings",
               "-f", "bv*[height<=1920]+ba/b", "--merge-output-format", "mp4",
               "-o", str(dest), args.source]
        run = subprocess.run(cmd, capture_output=True, text=True)
        if run.returncode != 0 or not dest.exists():
            err = (run.stderr or run.stdout).strip()
            last = err.splitlines()[-1] if err else "unknown error"
            if LOGIN.search(err):
                print(f"NEED_FILE login: this link needs a login. Ask for the video file. ({last})")
                return 3
            if NETWORK.search(err):
                print(f"NEED_FILE network: this machine cannot reach the site. Ask for the video file. ({last})")
                return 4
            print(f"NEED_FILE other: download failed. Ask for the video file. ({last})")
            return 5
        info["kind"] = "downloaded"
    else:
        print(f"NEED_FILE other: '{args.source}' is not a file here and not a link.")
        return 5

    info.update(probe(dest))
    info["file"] = str(dest)
    if args.reference_dir and "error" not in info:
        ref_dir = Path(args.reference_dir)
        ref_dir.mkdir(parents=True, exist_ok=True)
        keep = ref_dir / f"{out.name}{dest.suffix}"
        if local.is_file() and local.resolve() == keep.resolve():
            pass                                   # the file already lives in reference/
        else:
            shutil.copy2(dest, keep)
        info["reference_copy"] = str(keep)
    (out / "source.json").write_text(json.dumps(info, indent=2))
    print(json.dumps(info, indent=2))
    return 0 if "error" not in info else 5


if __name__ == "__main__":
    sys.exit(main())

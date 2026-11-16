# Where things stand

Last updated: 16 Nov 2026

## Done

- `learn-style` skill built and on `main`: download, frames, transcribe,
  listen and colour scripts, plus templates for `my-style`.
- `earshot` listening skill added (version 0.4.1, pinned) and wired into
  `learn-style` through `scripts/listen.py`.
- Remotion (13) and HyperFrames (9) official skills added, unchanged, with
  sources and licences in `THIRD_PARTY_SKILLS.md`. Files only: neither tool
  has been run yet, and no video project exists yet.
- Folder rule set: `reference/`, `raw/`, `export/` at the top of the project
  (on the Mac: `~/Desktop/editing/...`). `download.py` keeps a copy of every
  reference in `reference/`.
- First reference downloaded in the cloud session of 16 Nov:
  `reference/reel-DcYVYYno2GZ.mp4` (Instagram reel DcYVYYno2GZ, 89 s, 9:16,
  30 fps). Not measured yet. The cloud copy is temporary; download again
  from the link if it is gone.
- Cloud environment "Default": setup script installs PyTorch, earshot, yt-dlp
  and faster-whisper; network access is unrestricted.
- Scripts tested on a synthetic 14 s reel only.

## Next step

Run `/learn-style` for the first time on real references to create
`.claude/skills/my-style/`. Planned request:

- References: one style, about 3 videos plus design images
- Focus: captions, cuts, transitions, text layout
- Format: 9:16 talking reels, 45-60 s
- Finish with a one-page summary of my-style and 3 things that are uncertain

## Waiting on the owner

- The reference videos (files are most reliable; links often fail from the
  cloud) and design images.
- Brand: fonts, colours as hex codes, logo file.
- Decision: make this repository private before brand details are committed?

## Not done yet / open points

- The setup script has not yet been seen running in a fresh session.
- The scripts have not been run on a real reel; cut detection may need its
  sensitivity adjusted.
- Remotion and HyperFrames are untested here. First use needs a project
  (`npx create-video@latest` or `npx hyperframes init`); rendering needs a
  browser (cloud sessions have Chromium at `/opt/pw-browsers/chromium`).
- Owner to decide: which tool to make videos with (Remotion or HyperFrames).
- `real-sound` (the soundtrack-building companion to earshot) is not
  installed. Ask if wanted.
- Mac setup: tools are in the conda environment `whisper`; earshot and
  PyTorch are not yet installed there. This repository is not yet cloned
  there; it should be cloned as `~/Desktop/editing` so the folder rule holds.

# Where things stand

Last updated: 14 Nov 2026

## Done

- `learn-style` skill built and on `main`: download, frames, transcribe,
  listen and colour scripts, plus templates for `my-style`.
- `earshot` listening skill added (version 0.4.1, pinned) and wired into
  `learn-style` through `scripts/listen.py`.
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
- `real-sound` (the soundtrack-building companion to earshot) is not
  installed. Ask if wanted.
- Mac setup: tools are in the conda environment `whisper`; earshot and
  PyTorch are not yet installed there, and this repository is not yet cloned
  there.

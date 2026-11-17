# Where things stand

Last updated: 17 Nov 2026

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
- Six reference reels downloaded from Instagram on 16 Nov into `reference/`
  (cloud copies are temporary; the owner was sent each file; download again
  from `https://www.instagram.com/reel/<id>/` if gone). None measured yet:
  | File | Shape | Length |
  |---|---|---|
  | `reel-DcYVYYno2GZ.mp4` | 1080x1920 | 89.0 s |
  | `reel-DRHCZoLkhZy.mp4` | 1920x1080 (wide) | 12.8 s |
  | `reel-DKr2NCtT0DC.mp4` | 1080x1920 | 30.8 s |
  | `reel-DUMEuGUklxE.mp4` | 1080x1920 | 10.2 s |
  | `reel-CucNmOTAGCO.mp4` | 720x1280 | 7.5 s |
  | `reel-DX66rPHpvn_.mp4` | 1080x1920 | 9.1 s |
  First measurements (16 Nov, `frames.py` + `transcribe.py`, checked only on
  an overview of shot frames; captions, colours and sound not measured yet):
  | Reel | What it is | Cuts / 10 s | Median shot | Speech |
  |---|---|---|---|---|
  | `CucNmOTAGCO` | one dark moody shot, slow 10 % push-in, no audio track | 0 | 7.5 s | none |
  | `DKr2NCtT0DC` | talking tutorial about a big serif text hook | 2.6 | 0.9 s | 191 wpm |
  | `DRHCZoLkhZy` | wide; person walking, location changes every step | 24.3 | 0.33 s | none |
  | `DUMEuGUklxE` | moody street shots, warm/teal look | 2.9 | 2.6 s | none |
  | `DX66rPHpvn_` | slow close-ups with large serif quote text | 2.2 | 2.4 s | 159 wpm |
  | `DcYVYYno2GZ` | tutorial: word-by-word captions over cinematic clips | 1.35 | 2.4 s | 196 wpm |
  These are several different styles, and two are tutorials about a
  technique rather than examples of it. Do not average them.
- Brand sheet: the owner had no answers to its questions and asked Claude
  (17 Nov) to decide for them. Claude chose direction "Ember", fonts
  Instrument Serif + Inter Tight, cream `#F4E9D8` text with an amber
  `#E0A458` accent word, every word captioned, 30-45 s, and no music track in
  the export by default (owner adds a sound in Instagram) because no licensed
  track exists. Logo is NOT SET. All of this is in
  `.claude/skills/my-style/SKILL.md` (version 1), with one notes file per
  reference. The sheet itself: `docs/brand-sheet-draft.html`, published at
  https://claude.ai/artifact/HRpzrDLYgTyiLs5gJoWGo8. The owner can change any
  of these choices.
- Reel request (16 Nov), NOT started: turn the clips in `raw/` into an
  Instagram Reel. Cut every silence longer than 0.1 s; follow `my-style`;
  add captions, music and motion graphics; borrow technique only from
  `reference/`; show a storyboard for approval BEFORE editing; then export
  to `export/`. Nobody has looked at the raw clips yet, so what the reel is
  about is unknown: transcribe them first and tell the owner what is there.
- Cloud environment "Default": setup script installs PyTorch, earshot, yt-dlp
  and faster-whisper; network access is unrestricted.
- Scripts tested on a synthetic 14 s reel only.

## Working on the Mac (since 17 Nov)

The owner's raw clips are about 1 GB each and could not be uploaded, so work
moved to the Mac at `~/Desktop/editing` (a clone of this repository; GitHub
login done with `gh`). `setup-mac.sh` ran there on 17 Nov with this result:
ffmpeg, yt-dlp, Node and faster-whisper installed in the conda environment
`whisper`; the three folders exist; **earshot FAILED to install** (Intel Mac,
PyTorch most likely; the error text was not captured). So on the Mac sound is
"not measured" unless earshot is fixed: run `earshot doctor`, and if it is
missing, show the owner the pip error and decide together. Everything else
in `learn-style` works without it. Not yet checked on the Mac: that the
skills load and that `frames.py` / `transcribe.py` run.

## Next step

On the Mac: transcribe the clips in `raw/` (`transcribe.py`), measure them
(`frames.py`), then build the storyboard to `my-style` and show it to the
owner. Edit and export only after they approve it.

## Waiting on the owner

- Approval of the storyboard once it exists.
- Optional: a logo, a music track they have the rights to, or changes to any
  of the brand choices Claude made.

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

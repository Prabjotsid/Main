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
- Owner's 4-step request (16 Nov): 1 save references, 2 analyse what they
  share, 3 brand sheet for review ("inspired, not copied; ask before
  finalizing"), 4 proceed only after approval. Steps 1-3 done:
  - Full findings and the draft style are in `docs/brand-sheet-draft.html`,
    also published privately at https://claude.ai/artifact/HRpzrDLYgTyiLs5gJoWGo8
    (to update it from another session, pass that link as `url`).
  - It offers three directions (A Ember, B Slate, C Paper) and 7 questions.
  - Step 4 is NOT started. Do not write `my-style` or edit footage until the
    owner approves the sheet and answers the questions.
- Earlier ask, still open: edit the owner's raw footage into a cinematic
  Instagram reel. Blocked: `raw/` in the cloud was empty (footage is on the
  Mac). Needs the clips attached, or a session run on the Mac.
- Cloud environment "Default": setup script installs PyTorch, earshot, yt-dlp
  and faster-whisper; network access is unrestricted.
- Scripts tested on a synthetic 14 s reel only.

## Next step

After the owner approves the sheet: write `.claude/skills/my-style/` from it
(rules as "do X when Y", one notes file per reference using the numbers in
the sheet; re-run `frames.py`, `transcribe.py`, `listen.py` on `reference/`
if `.learn-style/` is gone), then edit the raw footage to those rules and
save the result in `export/`.

## Waiting on the owner

- Approval of the brand sheet, a direction (A, B, C or a mix), and answers
  to its 7 questions: what the reels are about / what the raw footage is,
  brand fonts + hex colours + logo, caption language and coverage, target
  length, music source, and whether the walking montage is wanted.
- The raw clips (attach in chat, or run a session from `~/Desktop/editing`).
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

# Project instructions

This repository is the permanent home for the owner's video-editing skills and
style. Sessions are temporary; this repository is not. The owner wants to come
back at any time and continue exactly where they left off.

## At the start of every session

1. Read `PROGRESS.md`. It says what is done, what is in progress and what is
   waiting on the owner.
2. Tell the owner in two or three lines where things stand and what the next
   step is, then carry on with what they ask.

## Before the end of every piece of work

Nothing that exists only inside a session survives. So before stopping:

1. Update `PROGRESS.md`: what was just done, what is half-done (with enough
   detail to continue without this conversation), and what the owner still
   has to provide. Keep it short and current; replace old status, do not
   pile up a history.
2. Commit everything worth keeping and push it to a branch. Then ask the
   owner whether to merge it into `main`, and remind them that new sessions
   only see what is on `main`. Do not merge without their yes. Always confirm
   first for anything destructive (deleting files, rewriting history, force
   pushes).
3. Say plainly if something could not be saved, and why.

## What goes where

- `.claude/skills/learn-style/` measures an editing style from references.
- `.claude/skills/earshot/` lets Claude listen to audio (third-party, pinned;
  see its `SOURCE.md`).
- `.claude/skills/remotion-*/` (13 skills) make videos in code with Remotion
  (React). Start from `remotion-best-practices`, which routes to the rest.
- `.claude/skills/hyperframes*/`, `media-use`, `figma`, `slideshow`,
  `style-sampling`, `reverse-any-video`, `remotion-to-hyperframes` make
  videos from HTML with HyperFrames. Start from `hyperframes`.
- `THIRD_PARTY_SKILLS.md` lists where every outside skill came from, its
  commit and licence. Do not edit those skill folders by hand.
- `.claude/skills/my-style/` is the owner's style, written by `learn-style`.
  Commit it every time it changes.
- `.learn-style/` is the work folder for downloaded reference footage. It is
  ignored by git on purpose: it is other people's content and must never be
  committed.
- Large video files do not belong in git. If the owner's own footage or
  exports need to persist, ask where they want them kept.

## Things to know

- This repository is public. Before committing brand details (fonts, colours,
  logo) for the first time, remind the owner once.
- Tools (yt-dlp, faster-whisper, earshot, PyTorch) are installed by the cloud
  environment's setup script, not stored here. Python and ffmpeg are in the
  base image.
- YouTube and Instagram usually refuse downloads from cloud sessions. When a
  link fails, ask the owner for the video file; do not use logins or cookies.
- When making a video, follow `my-style` (once it exists) for cuts, captions,
  transitions, zooms and sound, whichever tool renders it.
- HyperFrames sends usage statistics to HeyGen by default. The owner has not
  opted in: run its commands with `HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1`
  set, and skip the "usage beacon" and "feedback report" steps its skills
  mention, unless the owner says otherwise.
- Paid services in the HyperFrames `media-use` skill (HeyGen, ElevenLabs,
  Gemini) need the owner's own keys. Ask before using any of them, and never
  put a key in a file.
- The owner is not a programmer. Explain in plain words and give exact
  commands to copy when they need to run something.

# reel-DKr2NCtT0DC

- Source: https://www.instagram.com/reel/DKr2NCtT0DC/
- Measured: 16 Nov 2026
- Format: 1080x1920, 30.8 s, 30.0 fps; tutorial, talking to camera, then phone mock-up with screen recording
- Included in rules: yes, for the habits it shares with the others (see `SKILL.md`)

## Numbers

| Measure | Value | How measured |
|---|---|---|
| Cuts per 10 s | 2.6 | frames.py, checked on shot frames |
| Cuts per 10 s, by window | 5 / 1 / 1 / 1 | frames.py |
| Shot length median / mean / min / max (s) | 0.93 / 3.42 / 0.07 / 16.8 | frames.py |
| First cut at (s) | 3.48 | frames.py |
| Cuts in hook (first 3 s) | 0 | frames.py |
| Hard cuts (% of transitions) | 88 | frames.py |
| Other transitions: count, longest (frames) | 1, 10 | frames.py |
| Shots with push-in (%) | 0.0 | frames.py |
| Push-in amount (%) / speed (% per s) | - | frames.py |
| Punch-in cuts: count / scale | 0 | frames.py + sheets |
| Words per minute overall / while speaking | 191 / 216 | transcribe.py |
| First word at (s) / words in hook | 0.0 / 11 | transcribe.py |
| Pauses per minute / median (s) / silence share (%) | 13.6 / 0.42 / 12 | transcribe.py |
| Loudness integrated (LUFS) / true peak (dBTP) | -14.6 / -0.4 | listen.py |
| Loudness range (LU) | 3.4 | listen.py |
| Music | present; beat not detected | listen.py (model guess for genre left out) |
| Cuts with a sound within 100 ms (%) / chance (%) | 62 / 79 | listen.py |
| Sound vs cut, median offset (ms) | 27.5 | listen.py |
| Brightness mean / black level / white level (0-1) | 0.46 / 0.01 / 0.94 | 2 frames per second |
| Saturation mean (0-1) | 0.22 | 2 frames per second |
| Warm tilt (red minus blue) | 0.057 | 2 frames per second |
| Average shadows / mids / highlights (hex) | #1D1918 / #8E7673 / #D1C7D3 | 2 frames per second |
| Text style | ~ display serif, white, mixed sizes; big word ~8 % of frame height, small words ~3 % | by eye, gridded frames |
| Text position (centre, % from top) | ~ 15-30 | by eye, gridded frames |
| Text colours | ~ white only, no outline or box | by eye, gridded frames |
| Words on screen (max) | ~ 4 | by eye, gridded frames |
| Layering | ~ big word sits behind the speaker's head | by eye, gridded frames |

## Technique notes

- Hook text is on screen from the first frame and the speaker starts talking at 0.0 s.
- After the talking opening, the rest is one long screen recording inside a phone frame on a plain background.

## Could not measure

- Jump cuts inside the talking shot may be under-counted.
- Voice-to-music balance not measured.

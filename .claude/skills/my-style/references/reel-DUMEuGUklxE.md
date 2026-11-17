# reel-DUMEuGUklxE

- Source: https://www.instagram.com/reel/DUMEuGUklxE/
- Measured: 16 Nov 2026
- Format: 1080x1920, 10.23 s, 30.0 fps; moody street shots, music only
- Included in rules: yes, for the habits it shares with the others (see `SKILL.md`)

## Numbers

| Measure | Value | How measured |
|---|---|---|
| Cuts per 10 s | 2.93 | frames.py, checked on shot frames |
| Cuts per 10 s, by window | 3 / 0 | frames.py |
| Shot length median / mean / min / max (s) | 2.57 / 2.56 / 2.5 / 2.6 | frames.py |
| First cut at (s) | 2.5 | frames.py |
| Cuts in hook (first 3 s) | 1 | frames.py |
| Hard cuts (% of transitions) | 100 | frames.py |
| Other transitions: count, longest (frames) | - | frames.py |
| Shots with push-in (%) | 0.0 | frames.py |
| Push-in amount (%) / speed (% per s) | - | frames.py |
| Punch-in cuts: count / scale | 0 | frames.py + sheets |
| Speech | none | transcribe.py |
| Loudness integrated (LUFS) / true peak (dBTP) | -14.1 / -2.2 | listen.py |
| Loudness range (LU) | 1.1 | listen.py |
| Music | present; beat not detected | listen.py (model guess for genre left out) |
| Cuts with a sound within 100 ms (%) / chance (%) | 0 / 27 | listen.py |
| Sound vs cut, median offset (ms) | 126.0 | listen.py |
| Brightness mean / black level / white level (0-1) | 0.19 / 0.02 / 0.63 | 2 frames per second |
| Saturation mean (0-1) | 0.37 | 2 frames per second |
| Warm tilt (red minus blue) | 0.085 | 2 frames per second |
| Average shadows / mids / highlights (hex) | #0E0B0E / #2B231B / #826B4A | 2 frames per second |
| Text on screen | none | by eye |

## Technique notes

- Three shots of equal length (2.5-2.6 s).
- Dark warm grade: whites capped near 63 %, amber highlights, near-black shadows.
- No text.

## Could not measure

- Beat not detected; sound events did not line up with cuts.

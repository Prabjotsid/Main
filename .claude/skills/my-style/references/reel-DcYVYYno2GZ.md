# reel-DcYVYYno2GZ

- Source: https://www.instagram.com/reel/DcYVYYno2GZ/
- Measured: 16 Nov 2026
- Format: 1080x1920, 89.0 s, 30.0 fps; tutorial, voice-over over travel clips and a phone mock-up
- Included in rules: yes, for the habits it shares with the others (see `SKILL.md`)

## Numbers

| Measure | Value | How measured |
|---|---|---|
| Cuts per 10 s | 1.35 | frames.py, checked on shot frames |
| Cuts per 10 s, by window | 2 / 4 / 0 / 1 / 1 / 0 / 0 / 2 / 2 | frames.py |
| Shot length median / mean / min / max (s) | 2.4 / 6.85 / 0.77 / 27.2 | frames.py |
| First cut at (s) | 8.57 | frames.py |
| Cuts in hook (first 3 s) | 0 | frames.py |
| Hard cuts (% of transitions) | 83 | frames.py |
| Other transitions: count, longest (frames) | 2, 41 | frames.py |
| Shots with push-in (%) | 0.0 | frames.py |
| Push-in amount (%) / speed (% per s) | - | frames.py |
| Punch-in cuts: count / scale | 0 | frames.py + sheets |
| Words per minute overall / while speaking | 196 / 248 | transcribe.py |
| First word at (s) / words in hook | 0.98 / 2 | transcribe.py |
| Pauses per minute / median (s) / silence share (%) | 7.4 / 0.38 / 21 | transcribe.py |
| Loudness integrated (LUFS) / true peak (dBTP) | -14.3 / 0.2 | listen.py |
| Loudness range (LU) | 3.5 | listen.py |
| Music | present; beat not detected | listen.py (model guess for genre left out) |
| Cuts with a sound within 100 ms (%) / chance (%) | 92 / 84 | listen.py |
| Sound vs cut, median offset (ms) | 51.0 | listen.py |
| Brightness mean / black level / white level (0-1) | 0.39 / 0.0 / 0.85 | 2 frames per second |
| Saturation mean (0-1) | 0.12 | 2 frames per second |
| Warm tilt (red minus blue) | 0.019 | 2 frames per second |
| Average shadows / mids / highlights (hex) | #040405 / #63625B / #CACAC6 | 2 frames per second |
| Caption style | ~ one lowercase word at a time, bold sans, white, ~2 % of frame height | by eye, gridded frames |
| Caption position (centre, % from top) | ~ 51 | by eye, gridded frames |
| Title style | ~ heavy slanted capitals, sans, white, 2 lines, ~80 % of frame width, ~22-26 % from top | by eye, gridded frames |
| Text colours | ~ white only | by eye, gridded frames |
| Overlays | ~ camera-viewfinder frame around clips; rounded picture-in-picture card; letterboxed wide clip with spaced capitals | by eye, gridded frames |

## Technique notes

- Opens on a split-screen reveal with a title; first spoken word at 0.98 s.
- Three quick scenery clips (~0.8 s each) then long holds on screen recordings.

## Could not measure

- True peak reaches +0.2 dBTP (4 clipped samples): a flaw, not something to copy.
- Which sounds are effects is a model guess.

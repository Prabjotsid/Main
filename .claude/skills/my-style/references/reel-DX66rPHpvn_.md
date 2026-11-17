# reel-DX66rPHpvn_

- Source: https://www.instagram.com/reel/DX66rPHpvn_/
- Measured: 16 Nov 2026
- Format: 1080x1920, 9.03 s, 30.0 fps; slow close-ups with large quote text and voice-over
- Included in rules: yes, for the habits it shares with the others (see `SKILL.md`)

## Numbers

| Measure | Value | How measured |
|---|---|---|
| Cuts per 10 s | 2.21 | frames.py, checked on shot frames |
| Cuts per 10 s, by window | 2 | frames.py |
| Shot length median / mean / min / max (s) | 2.37 / 3.01 / 1.73 / 4.93 | frames.py |
| First cut at (s) | 1.73 | frames.py |
| Cuts in hook (first 3 s) | 1 | frames.py |
| Hard cuts (% of transitions) | 100 | frames.py |
| Other transitions: count, longest (frames) | - | frames.py |
| Shots with push-in (%) | 0.0 | frames.py |
| Push-in amount (%) / speed (% per s) | - | frames.py |
| Punch-in cuts: count / scale | 0 | frames.py + sheets |
| Words per minute overall / while speaking | 159 / 229 | transcribe.py |
| First word at (s) / words in hook | 0.0 / 10 | transcribe.py |
| Pauses per minute / median (s) / silence share (%) | 13.2 / 0.7 / 31 | transcribe.py |
| Loudness integrated (LUFS) / true peak (dBTP) | -14.1 / -1.8 | listen.py |
| Loudness range (LU) | 2.7 | listen.py |
| Music | present; beat not detected | listen.py (model guess for genre left out) |
| Cuts with a sound within 100 ms (%) / chance (%) | 50 / 78 | listen.py |
| Sound vs cut, median offset (ms) | 65.5 | listen.py |
| Brightness mean / black level / white level (0-1) | 0.41 / 0.06 / 0.85 | 2 frames per second |
| Saturation mean (0-1) | 0.64 | 2 frames per second |
| Warm tilt (red minus blue) | 0.336 | 2 frames per second |
| Average shadows / mids / highlights (hex) | #361F0E / #956026 / #CEA97C | 2 frames per second |
| Text style | ~ display serif, white, mixed sizes; big word ~7-9 % of frame height, small words ~2-3 % | by eye, gridded frames |
| Text position (centre, % from top) | ~ 12-35 | by eye, gridded frames |
| Text colours | ~ white only, no outline or box | by eye, gridded frames |
| Words on screen (max) | ~ 6-7 | by eye, gridded frames |
| Words per line | ~ 1-3 | by eye, gridded frames |
| Text reveal | ~ one word at a time; 5 words in the first 1.5 s; new stack on each shot | by eye, gridded frames |

## Technique notes

- Each shot carries one line of text that builds word by word in step with the voice.
- Emphasis is by size: one key word is several times larger than the rest.

## Could not measure

- Voice-to-music balance not measured.

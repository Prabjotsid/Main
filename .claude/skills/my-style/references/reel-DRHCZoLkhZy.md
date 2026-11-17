# reel-DRHCZoLkhZy

- Source: https://www.instagram.com/reel/DRHCZoLkhZy/
- Measured: 16 Nov 2026
- Format: 1920x1080, 12.77 s, 30.0 fps; wide 16:9 montage; a person walks while the location changes on every step; no voice
- Included in rules: yes, for the habits it shares with the others (see `SKILL.md`)

## Numbers

| Measure | Value | How measured |
|---|---|---|
| Cuts per 10 s | 24.28 | frames.py, checked on shot frames |
| Cuts per 10 s, by window | 22 / 9 | frames.py |
| Shot length median / mean / min / max (s) | 0.33 / 0.4 / 0.27 / 3.0 | frames.py |
| First cut at (s) | 3.0 | frames.py |
| Cuts in hook (first 3 s) | 0 | frames.py |
| Hard cuts (% of transitions) | 100 | frames.py |
| Other transitions: count, longest (frames) | - | frames.py |
| Shots with push-in (%) | 0.0 | frames.py |
| Push-in amount (%) / speed (% per s) | - | frames.py |
| Punch-in cuts: count / scale | 3 / 1.48x (match cuts on the subject, not zooms) | frames.py + sheets |
| Speech | none | transcribe.py |
| Loudness integrated (LUFS) / true peak (dBTP) | -14.1 / -7.3 | listen.py |
| Loudness range (LU) | 1.7 | listen.py |
| Music | present; beat not detected | listen.py (model guess for genre left out) |
| Cuts with a sound within 100 ms (%) / chance (%) | 29 / 27 | listen.py |
| Sound vs cut, median offset (ms) | 70.0 | listen.py |
| Brightness mean / black level / white level (0-1) | 0.53 / 0.13 / 0.91 | 2 frames per second |
| Saturation mean (0-1) | 0.23 | 2 frames per second |
| Warm tilt (red minus blue) | 0.086 | 2 frames per second |
| Average shadows / mids / highlights (hex) | #463F31 / #8F8972 / #D5CCCA | 2 frames per second |
| Text on screen | none | by eye |

## Technique notes

- Holds one location for 3.0 s, then cuts every 9-10 frames with the walker kept at the same place and size in frame (match cut).
- No text.

## Could not measure

- Sound-on-cut rate equals chance, so cuts could not be shown to follow the music.
- Beat not detected.

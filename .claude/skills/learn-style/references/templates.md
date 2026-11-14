# Layouts for the files learn-style writes

Two files are written into `.claude/skills/my-style/`. Keep these layouts so a
later run can merge by reading the tables back.

## 1. Notes file: `references/<slug>.md`

One per reference video or design image. Numbers and technique only: no quoted
captions or speech, no description of their logo, no frames.

```markdown
# <slug>

- Source: <link or file name>
- Measured: <date>
- Format: <9:16>, <length s>, <fps> fps, <talking head / b-roll / design image>
- Included in rules: yes | no (<why>)

## Numbers

| Measure | Value | How measured |
|---|---|---|
| Cuts per 10 s | 4.2 | frames.py, checked on sheets |
| Cuts per 10 s, by window | 6 / 4 / 4 / 3 / 4 | frames.py |
| Shot length median / mean / min / max (s) | 2.1 / 2.4 / 0.6 / 5.8 | frames.py |
| First cut at (s) | 1.4 | frames.py |
| Cuts in hook (first 3 s) | 2 | frames.py |
| Hard cuts (% of transitions) | 90 | frames.py + sheets |
| Other transitions: kind, length (frames) | whip, 6 | sheets |
| Shots with push-in (%) | 30 | frames.py |
| Push-in amount (%) / speed (% per s) | 8 / 3.5 | frames.py |
| Punch-in cuts: count / scale | 7 / 1.15x | frames.py + sheets |
| Words per minute overall / while speaking | 172 / 205 | transcribe.py |
| Words in hook (first 3 s) | 9 | transcribe.py |
| Pauses per minute / median (s) | 6 / 0.4 | transcribe.py |
| Caption words on screen median / max | 3 / 5 | ~ counted on 12 shots |
| Caption lines | 1 | ~ |
| Caption reveal | 1 word at a time | sheets + word times |
| Caption position (centre, % from top) | 68 | grid |
| Caption width (% of frame) | 80 | grid |
| Caption cap height (% of frame height) | 3.5 | ~ grid |
| Caption alignment | centre | |
| Font class / weight / case | geometric sans / black / ALL CAPS | ~ by eye |
| Outline or box | 4 px black outline at 540 px wide | ~ |
| Text colours (hex) | #FFFFFF text, #FFE600 highlight, #000000 outline | colors.py |
| Distinct text colours | 2 | |
| Top / bottom clear margin (% of height) | 12 / 20 | grid |
| Text elements on screen at once (max) | 2 | |
| Loudness integrated (LUFS) / true peak (dBTP) | -14.2 / -1.0 | listen.py |
| Loudness range (LU) | 4.1 | listen.py |
| Music: present / tempo (bpm) / level under voice (dB) | yes / 96 / ~14 | listen.py, sheet |
| Sound effects per 10 s (not speech) | 2.5 | ~ timeline + sheet |
| Cuts with a sound within 100 ms (%) / chance (%) | 85 / 40 | listen.py |
| Sound vs cut, median offset (ms) | 30 early | listen.py |
| Effect kinds and where they land | likely whoosh on topic change, pop on caption | ~ model guess, checked on sheet |
| First non-speech sound at (s) | 0.4 | timeline |

## Technique notes

Short bullets on *how* things are done that a number does not capture, e.g.
"highlight colour lands on the last word of each caption", "punch-in happens
on the first stressed word after a pause".

## Could not measure

List anything missing and why.
```

Use `-` for a measure that does not apply (a design image has no cuts). Keep
the row labels unchanged; merging matches on them.

## 2. Rules file: `SKILL.md`

```markdown
---
name: my-style
description: <User>'s editing style in numbers: cuts, captions, transitions, zooms, text layout and brand. Use whenever editing, captioning, planning or reviewing a video or design for this project, or when asked to make something "in my style".
---

# my-style

Format: <9:16 talking reels, 45-60 s>. Learned from <N> references
(see `references/`). Last updated <date>.

## Brand (given by the user; do not change without asking)

| Item | Value |
|---|---|
| Caption font | <name, weight> |
| Title font | <name, weight> |
| Text colour | <#hex> |
| Accent / highlight | <#hex> |
| Outline / box | <#hex> |
| Background | <#hex> |
| Logo | `assets/<file>` |

Write `NOT SET - ask the user` in any slot the user has not filled.

## Rules

Each rule: **Do X when Y.** Number in the rule, range and support in brackets.

### Hook (first 3 s)
- Make the first cut by 1.4 s when the reel opens on a talking head. (range 1.1-1.8, 3 of 3)

### Cuts
- Cut about 4 times per 10 s when the speaker is on camera. (3.6-4.6, 3 of 3)
- Keep a shot under 6 s; when a sentence runs longer, add a punch-in instead of holding. (max 5.8, 3 of 3)

### Captions
- Show 3 words at a time, 5 at most, when the speaker is talking. (2 of 3)
- Place the caption centre 68 % down the frame when a face is in the upper half. (64-70, 3 of 3)
- Use the accent colour on one word per caption when that word carries the point. (2 of 3)

### Transitions
- Use a hard cut by default; use a 6-frame whip only when the topic changes. (hard cuts 90 %, 3 of 3)

### Zooms
- Punch in to 1.15x on the cut when a new point starts. (1.12-1.2, 2 of 3)

### Text layout
- Keep the top 12 % and bottom 20 % of the frame free of text. (3 of 3)

### Pace
- Speak at about 170 words per minute when recording; trim pauses longer than 0.4 s. (160-180, 3 of 3)

### Sound
- Put a short effect on the cut when the topic changes, landing within 40 ms of the cut. (85 % of cuts have a sound, chance 40 %, 2 of 3)
- Keep the music about 14 dB under the voice when someone is speaking. (12-16, 2 of 3)
- Master to about -14 LUFS with true peak under -1 dBTP. (-15 to -13.5, 3 of 3)

### Logo
- Place the logo <where and how big the references place theirs> when <when they show it>. Use the user's logo file only.

## Not from the references
- Their wording, hooks, logos, handles, footage, music tracks and sound effect files are not part of this style.

## References
- `references/<slug>.md` - one per reference
- `references/CHANGELOG.md` - what changed on each update
```

The example numbers above are placeholders to show the shape. Every number in
a real `my-style` must come from a notes file.

## 3. `references/CHANGELOG.md`

Newest entry first.

```markdown
## <date>
- Added: references/ref4-handle.md
- Changed: Cuts per 10 s 4.2 -> 4.6 (now 4 references)
- Changed: Caption position 68 % -> 66 %
- Added rule: 6-frame whip when the topic changes
- Removed rule: ...
- Brand: unchanged
```

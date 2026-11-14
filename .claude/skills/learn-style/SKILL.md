---
name: learn-style
description: Learn a video editing style from reference videos (links or files) and design images, measure it in numbers (cuts per 10 s, shot length, caption words and position, font type and weight, hex colours, transition frames, zooms, words per minute), and write or update the project skill `my-style` as "do X when Y" rules. Use this whenever the user runs /learn-style, shares reels, shorts, TikToks, YouTube links, video files or design screenshots and wants to copy, match, study, break down or "learn" how they are edited, or asks to create or update my-style, even if they never say the word "skill".
---

# learn-style

Turn reference videos and design images into a measured description of an editing
style, saved as the project skill `.claude/skills/my-style/`. Later editing work
reads `my-style` and follows it, so everything written there has to be a number
or a rule someone could act on, not an impression.

## What the user gives you

A typical request looks like this. Any part can be missing.

```
/learn-style
References (one style): <link> <link> <file> + <image files>
Focus: captions, cuts, transitions, text layout.
My brand: fonts <...>, colours <...>, logo <file>.
Format: 9:16 talking reels, 45-60 s.
When done: summarise my-style on one page + 3 things you're unsure about.
```

- **References** are treated as examples of one style. If one of them clearly
  measures differently from the rest (for example 9 cuts per 10 s where the
  others have 3), keep its notes file but say so and ask whether to leave it
  out of the rules, because averaging two styles describes neither.
- **Focus** decides where to spend the looking time. Still record every
  measurement the scripts give for free.
- **Format** sets the frame the rules are written for (aspect ratio, length).
- **My brand** is covered under "Brand" below.

## The two rules that shape everything

**1. Copy technique, never content.** The references belong to other people.
What carries over to `my-style` is how the edit is built: timing, sizes,
positions, counts, motion. What never carries over is what they made: their
sentences, hooks, jokes or caption text; their logos, watermarks, handles or
brand names as design elements; their frames, clips, music or images. In
practice:

- Describe a caption as "3 words, all caps, one word highlighted", never by
  quoting it.
- Keep downloads, frames and transcripts in the work folder `.learn-style/`.
  Nothing from there is copied into `.claude/skills/my-style/`.
- `transcript.json` exists to line captions up with speech. Read timings from
  it; do not paste text from it anywhere.
- A notes file may name the source link so the user knows which reference it
  is. That is attribution, not copying.

**2. The user's brand comes from the user.** Fonts, colours and logo in
`my-style` are the user's own, and only they know them. A reference's yellow
caption tells you "captions use one loud accent colour on a dark outline"; it
does not tell you the user's accent colour. So measure the reference's font
style and hex colours (they go in the notes as observations), but fill the
brand section of `my-style` only with what the user stated. If fonts, colours
or the logo file were not given, ask for exactly the missing ones before
writing `my-style`. If the user wants to carry on without them, write
`NOT SET - ask the user` in that slot. Do not pick a "close" font, do not
borrow the reference's hex codes, and do not use a logo you were not handed.

## Steps

Scripts live in `scripts/` next to this file. Run them by full path. Work in
`.learn-style/<slug>/` at the project root, one folder per reference, where
`<slug>` is a short name such as `ref1-handle` (add `.learn-style/` to
`.gitignore` if the project uses git: it holds other people's footage).

### 1. Get each video

```bash
python3 <skill>/scripts/download.py "<link or file path>" --out .learn-style/<slug>
```

If it prints `NEED_FILE` (login needed, site unreachable, or anything else),
do not try cookies, logins or other workarounds. Ask the user to send the
video file for that reference, say which link it was and why, and carry on
with the other references meanwhile.

### 2. Pull frames and measure the cut

```bash
python3 <skill>/scripts/frames.py .learn-style/<slug>/source.mp4 --out .learn-style/<slug>
```

This writes one frame per shot (`shots/`), the same frames with a 10 % grid
(`shots_grid/`), a 12 fps sheet of the hook and of every transition
(`sheets/`), and `cuts.json` with cuts per 10 s, shot lengths, transition
length in frames, zoom per shot and scale jump per cut.

The numbers are estimates from pixel differences, so check them: open the
hook sheet and a handful of transition sheets, and compare the number of
shots with what the shot frames show. If cuts were missed or invented, rerun
with `--sensitivity` lower (finds more) or higher (finds fewer), and record
that you did.

### 3. Transcribe and measure the speech

```bash
python3 <skill>/scripts/transcribe.py .learn-style/<slug>/source.mp4 --out .learn-style/<slug>
```

`speech.json` has words per minute (overall and while speaking), pauses, and
words in the hook. Use `--model tiny` for a quick pass or `--language` if
detection is wrong. No speech is a valid result; record it.

### 4. Look, and measure what scripts cannot

Read the frames with your own eyes. For each item below write a number. When
a value is judged by eye, mark it `~` so the reader knows.

| Measure | How |
|---|---|
| Caption words on screen | Count words per caption over at least 10 shots; give median and max. Count lines too. |
| Caption timing | Using word times in `transcript.json`: words revealed per caption step (1 word, 2-3 words, full line), and how many captions per 10 s. |
| Caption position | From `shots_grid/`: vertical centre of the caption block as % from the top, and its width as % of frame width. Note left/centre/right alignment. |
| Caption size | Height of a capital letter as % of frame height. |
| Font type and weight | Class (geometric sans, grotesque, serif, condensed, rounded, handwritten...), weight (regular / bold / black), case, outline or shadow in px relative to cap height, any box behind text. A font *name* is a guess; say "looks like". |
| Hex colours | `python3 <skill>/scripts/colors.py <frame> --box x,y,w,h` (percent box, read from the grid) for caption text, highlight word, outline/box, and background. Also count how many distinct text colours are used. |
| Transitions | From sheets + `cuts.json`: share of hard cuts, length in frames of the rest, and what kind (dissolve, whip, zoom-through, wipe). |
| Zooms | From `cuts.json`: share of shots with a push-in, % and % per second; punch-in cuts and their scale (e.g. 1.15x). Confirm on sheets. |
| Text layout | Top and bottom margins kept clear (% of height), where titles sit versus captions, how many text elements are on screen at once. |
| Hook | What changes in the first 3 s, in numbers: cuts, words spoken, when the first caption and first motion appear. |

For **design images** (thumbnails, carousels, mood boards) there is no cut to
measure. Record layout as percentages, text size as % of height, font class
and weight, and hex colours with `colors.py`. Give each image its own notes
file as well.

Only write down what you saw. If only two references show a pattern, say
"2 of 3". If something could not be measured (no captions in that reference,
transition too fast to read at 12 fps), say that instead of filling the gap.

### 5. Brand

Collect from the user: fonts (caption font and weight, title font if
different), colours as hex (text, accent/highlight, outline or box,
background), and the logo file. Ask only for what is missing, in one
question. Copy the logo file to `.claude/skills/my-style/assets/` under its
own name. See rule 2 above for what to do when something is not provided.

### 6. Write `my-style`

Read `references/templates.md` for the exact layout of both files, then write:

- `.claude/skills/my-style/references/<slug>.md`: one notes file per
  reference, numbers only.
- `.claude/skills/my-style/SKILL.md`: the rules, each written as
  **"Do X when Y"** with the number inside the rule and how many references
  support it. Use the median across references for the rule and give the
  range in brackets. Rules about colour, font and logo use the user's brand
  values, applied the way the references apply theirs.

**If `my-style` already exists, merge instead of overwriting.** Read the
existing `SKILL.md` and every notes file first. Add the new notes files,
recompute each rule from all notes files of the same format, keep the brand
section exactly as it is unless the user gave new brand values in this
request, and keep any rule the user wrote by hand (ask if a new measurement
contradicts it). Then list what changed: every rule added, removed, or whose
number moved, as `old -> new`, plus new notes files. Put the same list at the
top of `.claude/skills/my-style/references/CHANGELOG.md` with today's date.

### 7. Report back

Finish with, in this order:

1. **my-style on one page**: the rules grouped by area, with their numbers.
2. **What changed** (only when merging).
3. **3 things you are unsure about**: the three measurements you trust least
   and why (for example "caption font weight read by eye from 540 px frames",
   or "only 1 of 3 references had transitions other than hard cuts"), so the
   user knows what to check first.
4. Anything still needed from the user: files for links that needed a login,
   missing brand values.

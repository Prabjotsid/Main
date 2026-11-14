#!/usr/bin/env python3
"""Transcribe a video with faster-whisper and measure the pacing of the speech.

    python3 transcribe.py <video> --out .learn-style/<slug> [--model small]

Writes into <out>:
  speech.json      numbers only: words per minute, pauses, hook pacing.
                   Safe to copy into notes.
  transcript.json  every word with its start and end time. This is the
                   creator's own wording. Use it only to line captions up with
                   speech (how many words per caption, how early a caption
                   appears). Never copy text from it into my-style.

If the video has no speech, speech.json says so and the numbers are null.
"""
import argparse
import json
import statistics
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="small", help="tiny, base, small (default), medium, large-v3")
    ap.add_argument("--language", default=None, help="e.g. en, hi, pa. Default: detect")
    ap.add_argument("--hook", type=float, default=3.0)
    ap.add_argument("--pause", type=float, default=0.35, help="a gap this long (s) counts as a pause")
    args = ap.parse_args()

    from faster_whisper import WhisperModel

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(args.video, language=args.language,
                                      word_timestamps=True, vad_filter=True)
    words, segs = [], []
    for seg in segments:
        segs.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "text": seg.text.strip()})
        for w in seg.words or []:
            words.append({"w": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})

    dur = float(info.duration)
    (out / "transcript.json").write_text(json.dumps(
        {"warning": "Creator's own words. For timing only. Do not copy into my-style.",
         "language": info.language, "segments": segs, "words": words}, indent=2, ensure_ascii=False))

    if not words:
        speech = {"has_speech": False, "duration_s": round(dur, 2), "language": info.language,
                  "words": 0, "wpm_overall": None, "wpm_while_speaking": None}
    else:
        gaps = [words[i + 1]["start"] - words[i]["end"] for i in range(len(words) - 1)]
        pauses = [g for g in gaps if g >= args.pause]
        span = words[-1]["end"] - words[0]["start"]
        speaking = max(0.1, span - sum(pauses))
        windows = []
        k = 0
        while k * 10 < dur:
            lo, hi = k * 10, min((k + 1) * 10, dur)
            c = sum(1 for w in words if lo <= w["start"] < hi)
            windows.append({"from_s": lo, "to_s": round(hi, 2), "words": c,
                            "wpm": round(c / (hi - lo) * 60) if hi > lo else 0})
            k += 1
        # sentences: split on end punctuation, to measure words per sentence
        sent_lens, cur = [], 0
        for w in words:
            cur += 1
            if w["w"][-1:] in ".!?":
                sent_lens.append(cur)
                cur = 0
        if cur:
            sent_lens.append(cur)
        speech = {
            "has_speech": True,
            "language": info.language,
            "duration_s": round(dur, 2),
            "words": len(words),
            "wpm_overall": round(len(words) / dur * 60),
            "wpm_while_speaking": round(len(words) / speaking * 60),
            "first_word_at_s": words[0]["start"],
            "words_in_hook": sum(1 for w in words if w["start"] < args.hook),
            "hook_s": args.hook,
            "pauses": {
                "count": len(pauses),
                "per_minute": round(len(pauses) / dur * 60, 1),
                "median_s": round(statistics.median(pauses), 2) if pauses else None,
                "longest_s": round(max(pauses), 2) if pauses else None,
                "silence_share_pct": round(100 * (dur - speaking) / dur),
            },
            "words_per_sentence_median": statistics.median(sent_lens) if sent_lens else None,
            "wpm_per_10s": windows,
        }
    (out / "speech.json").write_text(json.dumps(speech, indent=2))
    print(json.dumps(speech, indent=2))


if __name__ == "__main__":
    sys.exit(main())

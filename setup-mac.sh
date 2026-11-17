#!/bin/bash
# One-time setup of this project on a Mac.
#
#   bash setup-mac.sh
#
# Run it from inside the project folder (~/Desktop/editing). It needs conda
# (Anaconda or Miniconda), which is already on the owner's Mac. It installs
# into a conda environment called "whisper" and changes nothing else.
# Safe to run again: it only adds what is missing.

# No 'set -u' here: conda's own activate scripts use unset variables and would stop the script.
cd "$(dirname "$0")"

say() { printf '\n== %s\n' "$1"; }
ok=(); failed=()

if ! command -v conda >/dev/null 2>&1; then
  echo "conda was not found. Open a new Terminal window and try again, or install Miniconda first."
  exit 1
fi
source "$(conda info --base)/etc/profile.d/conda.sh"

say "1/5  Environment 'whisper' with Python, ffmpeg, yt-dlp and Node"
if ! conda env list | awk '{print $1}' | grep -qx whisper; then
  conda create -y -n whisper -c conda-forge python=3.11 || { echo "Could not create the environment."; exit 1; }
fi
conda activate whisper
if conda install -y -c conda-forge ffmpeg yt-dlp nodejs; then ok+=("ffmpeg, yt-dlp, Node"); else failed+=("ffmpeg / yt-dlp / Node"); fi

say "2/5  faster-whisper (speech to text)"
if pip install -U faster-whisper "av<19"; then ok+=("faster-whisper"); else failed+=("faster-whisper"); fi

say "3/5  earshot (listening to sound). Optional: skipped if this Mac cannot run it"
EARSHOT="git+https://github.com/Leonxlnx/earshot@4ac3d2ac2b151e1c23376f9ce7f3047a17050013"
if python -c "import earshot" 2>/dev/null; then
  ok+=("earshot (already installed)")
elif { pip install "torch>=2.6" || conda install -y -c conda-forge "pytorch>=2.6"; } && pip install "$EARSHOT" "av<19"; then
  ok+=("earshot")
else
  failed+=("earshot (the project still works; sound will be marked 'not measured')")
fi

say "4/5  Folders"
mkdir -p reference raw export
ok+=("reference, raw and export folders")

say "5/5  Check"
for tool in ffmpeg yt-dlp node; do
  if command -v "$tool" >/dev/null 2>&1; then echo "  found  $tool"; else echo "  MISSING $tool"; fi
done
python -c "import faster_whisper; print('  found  faster-whisper', faster_whisper.__version__)" 2>/dev/null || echo "  MISSING faster-whisper"
command -v earshot >/dev/null 2>&1 && echo "  found  earshot" || echo "  not installed: earshot (optional)"

say "Result"
for x in "${ok[@]}"; do echo "  done    $x"; done
for x in "${failed[@]:-}"; do [ -n "$x" ] && echo "  FAILED  $x"; done
cat <<'MSG'

Next:
  1. Each time you open a new Terminal window, run:   conda activate whisper
  2. Then start Claude in this folder:                cd ~/Desktop/editing && claude
     (or open the Claude desktop app, choose Code, and pick the Desktop/editing folder)
  3. Put raw clips in raw/, reference reels in reference/. Edited videos go to export/.

If something above says FAILED, copy the lines printed just before it and show them to Claude.
MSG

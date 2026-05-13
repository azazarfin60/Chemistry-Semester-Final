#!/usr/bin/env bash
# Build navigation headers/footers for all boss_notes files
# and generate index.md

set -euo pipefail

DIR="/home/azaz/AntigravityData/Chemistry-Semester-Final/boss_notes"
cd "$DIR"

# Ordered file list (excluding index.md and this script)
mapfile -t FILES < <(ls -1 *.md | grep -v '^index\.md$' | sort)

TOTAL=${#FILES[@]}

# ─── Phase metadata for the index ───
declare -A PHASE_TITLES
PHASE_TITLES[01]="Chemical Kinetics"
PHASE_TITLES[02]="Chemical Equilibrium"
PHASE_TITLES[03]="Chemical Bonding"
PHASE_TITLES[04]="Colligative Properties"
PHASE_TITLES[05]="Atomic Structure"
PHASE_TITLES[06]="Thermochemistry"
PHASE_TITLES[07]="Electrochemistry"
PHASE_TITLES[08]="Solutions"
PHASE_TITLES[09]="Periodic Table"
PHASE_TITLES[10]="Acid-Base & Buffer"
PHASE_TITLES[11]="Miscellaneous"

# ─── 1. Generate index.md ───
{
    echo '# 📚 Chemistry Semester Final — Boss Notes'
    echo ''
    echo '> A high-fidelity, exam-ready master study guide covering the entire Chemistry curriculum.'
    echo '> Every sub-topic contains synthesized Core Theory, Key Derivations, Comparison Tables, Past Exam Archives (2017–2024), and strategic Exam Tips.'
    echo ''
    echo '---'
    echo ''

    CURRENT_PHASE=""
    for f in "${FILES[@]}"; do
        # Extract phase prefix (e.g. "01", "02", "11")
        phase="${f%%.*}"         # "01" from "01.1_Rate..."  or "11" from "11.00_Misc..."

        # Print phase header if new
        if [[ "$phase" != "$CURRENT_PHASE" ]]; then
            CURRENT_PHASE="$phase"
            title="${PHASE_TITLES[$phase]:-Unknown}"
            echo "### Phase ${phase}: ${title}"
            echo ''
        fi

        # Build display name from filename: strip prefix number+dot, strip .md, replace _ with space
        display="${f#*.}"            # "1_Rate_and_Rate_Law.md" or "00_Miscellaneous.md"
        display="${display%.md}"     # "1_Rate_and_Rate_Law"
        sub="${display%%_*}"         # "1" or "00"
        display="${display#*_}"      # "Rate_and_Rate_Law"
        display="${display//_/ }"    # "Rate and Rate Law"

        echo "- [${phase}.${sub} ${display}](${f})"
    done

    echo ''
    echo '---'
    echo ''
    echo '*Generated automatically. Last updated: '"$(date '+%Y-%m-%d')"'.*'
} > index.md

echo "✅ Created index.md with ${TOTAL} entries."

# ─── 2. Add navigation to each file ───
for (( i=0; i<TOTAL; i++ )); do
    f="${FILES[$i]}"

    # Determine prev/next
    if (( i == 0 )); then
        PREV_LINK="*(start)*"
    else
        prev_file="${FILES[$((i-1))]}"
        prev_display="${prev_file%.md}"
        prev_display="${prev_display//_/ }"
        PREV_LINK="[⬅ ${prev_display}](${prev_file})"
    fi

    if (( i == TOTAL-1 )); then
        NEXT_LINK="*(end)*"
    else
        next_file="${FILES[$((i+1))]}"
        next_display="${next_file%.md}"
        next_display="${next_display//_/ }"
        NEXT_LINK="[${next_display} ➡](${next_file})"
    fi

    NAV_BAR="${PREV_LINK} | [🏠 Index](index.md) | ${NEXT_LINK}"

    # Read current file content
    content=$(<"$f")

    # Check if navigation already exists (idempotent — skip if already added)
    if echo "$content" | head -1 | grep -q '🏠 Index'; then
        echo "⏭  Skipping $f (navigation already present)"
        continue
    fi

    # Build new content: nav at top + blank line + original + blank line + nav at bottom
    {
        echo "$NAV_BAR"
        echo ''
        echo '---'
        echo ''
        echo "$content"
        echo ''
        echo '---'
        echo ''
        echo "$NAV_BAR"
    } > "${f}.tmp"

    mv "${f}.tmp" "$f"
    echo "✅ Added navigation to $f"
done

echo ""
echo "🎉 Done! ${TOTAL} files updated with navigation. index.md created."

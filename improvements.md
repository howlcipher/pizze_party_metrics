# 🚀 Improvement Backlog

This document is the authoritative, ranked backlog for the Pizza Party Metrics project.

## Working Protocol

1. **Open a task journal.** Update it and commit at every milestone.
2. **Re-evaluate the model.** Pick the least expensive available model that can do the job well.
3. **Route the crafted skills.** Check the skills manifest for skills matching the task.
4. **Scan for helpful free tools.** Consider whether a free or open source tool would materially improve the work.
5. **Finish the loop.** Every code change ships with relevant automated tests. Verify the change works end to end, commit, and push.

## Ranked Backlog (best ROI first)

Pending rows are ranked by a diminishing-returns score, recomputed at every groom:

**Score = (Value × Decay) ÷ Effort**

- **Value (1–8):** pain or risk removed if the item ships.
- **Decay:** geometric halving per already-shipped item in the same theme (1.0 → 0.5 → 0.25 …).
- **Effort (1–8):** roughly log-scale; 1 = minutes, 8 = weeks.
- **ROI floor = 0.5:** items scoring below the floor stay open but are flagged ⚠️.

| # | Improvement | Status | Score (V×D÷E) | Claude model | Gemini model | ROI rationale |
| --- | --- | --- | --- | --- | --- | --- |

## Details


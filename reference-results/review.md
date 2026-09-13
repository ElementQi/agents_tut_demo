# Published PDF skill review, 12 September 2026

The author explicitly applied OpenAI's published `pdf` skill to the existing
LaTeX-generated PDF. This is a tool-executed authoring review, **not a recording
of an authenticated Codex CLI model turn**.

1. Downloaded the official skill with Skill Installer into an isolated build
   folder, then tested the student-facing Skills CLI installation in a fresh
   results project. Read the installed `SKILL.md` in this authoring session.
2. Confirmed that Codex CLI 0.154.0's actual `skills/list` response includes the
   project-local `pdf` skill, enabled at repository scope. No model turn was sent.
3. Followed its review workflow: ran
   `pdftoppm -png -r 110 -singlefile demo/reference-results/results.pdf build/results-review`.
   Opened and visually inspected the resulting full-page PNG.
4. Used pdfplumber 0.11.9 for text extraction and checked all 16 metric values
   against the CSV. Separately verified one page and a clean LaTeX layout log.

Observed layout: both grouped headers are centered above their metric columns;
dataset labels span the two model rows; numbers are aligned; the caption and
definitions are readable; no clipped text, overlapping cells, or missing labels
were observed. The LaTeX source is retained. No numeric or layout correction was
needed after the final page was rendered.

The workflow's preference for ReportLab when generating a new document does not
require replacing the editable LaTeX source of this existing PDF. The skill was
used for rendering and review. The CLI installation/discovery receipt and source
hash are in `evidence/pdf-skill-review.json` at the tutorial root.

For a live invocation in class, select PDF through `/skills` or `$pdf`, submit
the review request, and show its actual skill load, rendering call, and image
inspection. If that live step fails, label this artifact as the authoring replay.

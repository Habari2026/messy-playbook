# Micro Messes™

**Small on purpose. Big on clarity.**

Micro Messes™ are short, self-contained encounters with a single MESSY dimension. Each one takes ten or fifteen minutes. None require prior context, a coach, or a program. You pick the one that fits today and do it.

Live site: [messy-playbook.vercel.app](https://messy-playbook.vercel.app)

---

## What is MESSY?

MESSY is a five-dimension framework for navigating the kind of work and life situations that resist clean solutions. The dimensions are:

| Letter | Dimension | What it asks |
|--------|-----------|--------------|
| **M** | Monitor | Notice what's actually happening — not what you expect or fear |
| **E** | Execute | Take action that fits the situation, not someone else's plan |
| **S** | Support | Build the conditions and relationships that sustain the work |
| **S** | Surrender | Loosen your grip on control where control isn't helping |
| **Y** | Yield | Reflect, adapt, and integrate what you've learned |

Micro Messes™ are part of The MESSY Playbook™ — a broader toolkit for people who want to work and live with more honesty and less pretense.

---

## What's in this repo

```
/
├── index.html                      Main site landing page
├── micro-messes.html               Micro Messes overview page
├── micro-messes-sets.html          All Sets grid (updated with each new set)
├── micro-messes-set-00.html        Set 00: First Encounters
├── micro-messes-set-01.html        Set 01: Containing Multitudes
├── micro-messes-set-02.html        Set 02: Beyond Problem Solving
├── micro-messes-set-03.html        Set 03: What Comes Up
├── micro-messes-set-04.html        Set 04: Good Enough
├── micro-messes-set-05.html        Set 05: Something Finite
├── micro-messes-set-06.html        Set 06: Never a Solo Act
├── micro-messes-set-07.html        Set 07: Same Ground
├── micro-messes-set-08.html        Set 08: Hard to Name
├── micro-messes-set-09.html        Set 09: After the Fact
├── micro-messes-set-10.html        Set 10: The Messy Middle
├── card-pdfs/                      Pre-built PDFs, one per card (5 per set)
│   ├── micro-messes-set-00-m.pdf
│   ├── micro-messes-set-00-e.pdf
│   └── ...                         (55 PDFs total as of Set 10)
├── generate_pdfs.py                WeasyPrint PDF generator script
└── README.md                       This file
```

---

## Current sets

| Set | Name | Theme | Source |
|-----|------|-------|--------|
| 00 | First Encounters | Orientation | Live Messy Project (original) |
| 01 | Containing Multitudes | Identity | Jennifer Rosner, Massachusetts Review, 2006 |
| 02 | Beyond Problem Solving | Complexity | Russell L. Ackoff, JORS, 1979 |
| 03 | What Comes Up | Emergence | NYT Style (chaos gardening), May 2026 |
| 04 | Good Enough | Judgment | David Epstein, NYT / Herbert A. Simon, 1991 |
| 05 | Something Finite | Constraint | Igor Stravinsky, Poetics of Music, 1942 |
| 06 | Never a Solo Act | Interdependence | Hogarth & Hankin, Australian Journal of Environmental Education, 2024 |
| 07 | Same Ground | Recurrence | Carl Jung, Collected Works / Jemima Kelly, Financial Times, 2026 |
| 08 | Hard to Name | Emotional Complexity | Anthony G. Vaccaro, Affective Science, 2024 |
| 09 | After the Fact | Retrospect | Mackney & Young, Cultural Trends, 2022 |
| 10 | The Messy Middle | Transition | Tina Cook, Educational Action Research, 2009 |

---

## How a set is structured

Each set page contains five cards — one per MESSY dimension — in this order: M, E, S (Support), S (Surrender), Y.

Each card has:
- A **card name** (lowercase, 3–5 words)
- An **encounter line** — one italic sentence beginning "An encounter with..."
- A **time** (10 or 15 minutes)
- **Three steps** in plain language, second person
- A **Notice** line — one thing to pay attention to
- **No outcome required.** — always present, always sentence case

Each card links to a pre-built PDF in `/card-pdfs/` via a plain `<a download>` element. No JavaScript.

---

## How to add a new set

The short version:

1. Identify a peer-reviewed source (or a foundational primary source) with a strong human idea at its core
2. Assign a theme and check it against the existing Thematic Arc — look for gaps
3. Draft five cards (one per dimension), get approval before building HTML
4. Write the page header (three paragraphs: WHY / HOW / WHAT) and attribution
5. Build `micro-messes-set-XX.html` from the most recent set as template
6. Generate 5 PDFs using `generate_pdfs.py` (WeasyPrint required)
7. Update `micro-messes-sets.html` with the new tile
8. Update the previous set's Next → navigation link
9. Upload to GitHub in order: PDFs → new set HTML → previous set HTML → sets grid → generator script

**Never build HTML before card content and page header copy have been approved.**

---

## PDF generation

PDFs are static files generated with [WeasyPrint](https://weasyprint.org/). To regenerate or add new PDFs:

```bash
pip install weasyprint
python3 generate_pdfs.py
```

Output goes to `/card-pdfs/`. Each PDF is approximately 22–26KB. Font is Arial throughout — no exceptions.

---

## Deployment

This site is deployed via [Vercel](https://vercel.com). Pushes to `main` deploy automatically. After any upload, verify the Vercel deployment status is **Ready** before testing links.

---

## Design principles

**No outcome required.** The cards do not promise transformation. They ask for a few minutes of honest attention and nothing else.

**Grounded in real research.** Every set draws on a peer-reviewed journal article or primary source. The academic anchor is named in the attribution — not hidden, not over-explained.

**Plain language throughout.** If a sentence would confuse a smart, curious person who hasn't read the source, it gets rewritten. The ideas are rigorous; the language is not.

**Small on purpose.** Each encounter is ten or fifteen minutes. The smallness is the point — it removes the barrier of needing a block of time, a clear head, or a finished thought before you begin.

---

## Brand

**Typography**
- Web headings (h1): Playfair Display, Georgia, serif
- All other web text: Arial, sans-serif
- PDFs: Arial exclusively

**Colors**
- Brand gradient: `#667eea → #764ba2` at 135°
- Dark text: `#1e2a35`
- Body text: `#34495e`

**Breakpoint:** 820px on Micro Messes pages

---

## Part of The MESSY Playbook™

Micro Messes™ are one component of The MESSY Playbook™, a project of the Live Messy Project.

© 2026 Live Messy Project. All rights reserved.
The MESSY Playbook™ and Micro Messes™ are trademarks of the Live Messy Project.
For educational purposes and personal exploration only. Not therapy or professional counseling.

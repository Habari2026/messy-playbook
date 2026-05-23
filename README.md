# The MESSY Playbook™
**Self-Honesty for People Tired of Being Optimized**

Live site: [messy-playbook.vercel.app](https://messy-playbook.vercel.app)
© 2026 Live Messy Project. All rights reserved.

---

## What This Is

The MESSY Playbook™ is a personal development framework built on self-honesty rather than optimization. It uses five dimensions — **Monitor, Execute, Support, Surrender, Yield** — as a lens for looking at what's actually happening, rather than what should be happening.

This repo contains the full website: the homepage, all content pages, and the Micro Messes™ card sets.

---

## Micro Messes™

Micro Messes™ are short, structured self-encounters — 10 to 15 minutes each — designed to be experienced before researched. Each set contains five cards, one per MESSY dimension. Each card names an encounter, gives three steps, and asks you to notice something. No outcome required.

### Current Sets

| Set | Title | Source |
|-----|-------|--------|
| Set 00 | First Encounters | Live Messy Project (original) |
| Set 01 | Containing Multitudes | Jennifer Rosner, Massachusetts Review, 2006 |
| Set 02 | Beyond Problem Solving | Russell L. Ackoff, JORS, 1979 |
| Set 03 | What Comes Up | Chaos gardening — NYT Style, May 2026 |
| Set 04 | Good Enough | Herbert A. Simon, 1991 / David Epstein, NYT May 2026 |

### PDF Downloads

Each card is available as a static PDF download via the Save as PDF button on each set page. All 25 PDFs live in `/card-pdfs/`. They are brand-compliant, print-ready, and free for personal use.

---

## Site Structure

```
/
├── index.html                  — Homepage
├── micro-messes.html           — Micro Messes concept page
├── micro-messes-sets.html      — Set grid index
├── micro-messes-set-00.html    — Set 00: First Encounters
├── micro-messes-set-01.html    — Set 01: Containing Multitudes
├── micro-messes-set-02.html    — Set 02: Beyond Problem Solving
├── micro-messes-set-03.html    — Set 03: What Comes Up
├── micro-messes-set-04.html    — Set 04: Good Enough
├── play.html                   — Messy Plays™
├── thinking.html               — The Thinking
├── book.html                   — The Book
├── card-pdfs/                  — 25 static card PDFs
│   ├── micro-messes-set-00-m.pdf
│   ├── micro-messes-set-00-e.pdf
│   └── ... (25 total)
└── generate_pdfs.py            — WeasyPrint PDF generator script
```

---

## Stack

- **Pure HTML/CSS/JS** — no framework, no build step
- **Vercel** — auto-deploys on every GitHub commit to `main`
- **WeasyPrint** — used to generate card PDFs (Python, run locally)
- **Google Fonts** — Playfair Display (web display headings only)

---

## Dimension Colors

| Dimension | Color | Text |
|-----------|-------|------|
| M · Monitor | `#9b59b6` | white |
| E · Execute | `#e67e22` | white |
| S · Support | `#3498db` | white |
| S · Surrender | `#f1c40f` | `#856404` dark |
| Y · Yield | `#27ae60` | white |

Primary brand gradient: `#667eea → #764ba2` at 135°

---

## Key Architecture Rules

- `<div class="mobile-nav">` must always be **outside** `</nav>` — placing it inside locks Safari scrolling on all devices
- Micro Messes pages use **hex colors only** — never CSS variables from the DM Sans pages
- PDF download links are pure `<a href download>` — no JavaScript — iOS Safari blocks programmatic file saving
- GitHub uploads: always **Add file → Upload files → choose your files** — never drag-and-drop for files over ~100KB

---

## Generating New PDFs

PDFs are generated locally using [WeasyPrint](https://weasyprint.org):

```bash
pip install weasyprint
python3 generate_pdfs.py
```

Add new card entries to the `CARDS` list in `generate_pdfs.py` following the existing tuple structure, then run the script. Upload the new PDFs to `/card-pdfs/` in the repo.

---

## License

© 2026 Live Messy Project. All rights reserved.
The MESSY Playbook™ and Micro Messes™ are projects of the Live Messy Project.
For educational purposes and personal exploration only. Not therapy or professional counseling.

Free for personal use. Card PDFs may be printed and shared freely with attribution.

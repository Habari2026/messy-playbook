# The MESSY Playbook™

**Self-Honesty for People Tired of Being Optimized**

Live site: [messy-playbook.vercel.app](https://messy-playbook.vercel.app)  
Repo: [Habari2026/messy-playbook](https://github.com/Habari2026/messy-playbook)  
© 2026 Live Messy Project · All rights reserved

---

## What This Is

The MESSY Playbook™ is an anti-optimization personal development framework built around five practices: **Monitor · Execute · Support · Surrender · Yield**. This repo contains the complete static site — no build tools, no dependencies, no framework. Just HTML, CSS, and JavaScript deployed via Vercel.

---

## Site Structure

| File | Page | Purpose |
|------|------|---------|
| `index.html` | Homepage | Full site — Why MESSY, The Playbook, How It Works, FAQ, Get MESSY!, footer |
| `play.html` | Messy Plays™ | Experiential research card series — Play 01: Staying in the Mess |
| `thinking.html` | The Thinking | Research foundations, reading list, citations |
| `book.html` | The Book | Forthcoming book placeholder |
| `reality-check.html` | The MESSY Reality Check™ | Web-optimized pain point reference — all 5 dimensions |
| `messy-reality-check.pdf` | PDF Download | Pre-built print-ready PDF (generated from `reality-check-print.html`) |
| `messy-arc-graphic.svg` | Arc Graphic | Standalone SVG of the MESSY framework arc — used as thumbnail |

---

## How Updates Work

1. Make changes to the relevant file(s) locally or in Claude
2. Go to [github.com/Habari2026/messy-playbook](https://github.com/Habari2026/messy-playbook)
3. Click **Add file → Upload files → choose your files**
4. Select the updated file(s) — never drag-and-drop files over ~100KB (GitHub truncates them)
5. Add a short commit message and click **Commit changes** directly to main
6. Vercel auto-deploys within ~60 seconds

---

## Tech Stack

- **HTML / CSS / JavaScript** — no framework, no build step
- **Google Fonts** — Playfair Display + DM Sans
- **Gumroad** — Pay What You Want downloads (Self-Study Program, Taster)
- **Formspree** — Contact form handling
- **WeasyPrint** — PDF generation from `reality-check-print.html`
- **GitHub** — Version control and file hosting
- **Vercel** — Deployment and CDN (auto-deploys on every commit to main)

---

## PDF Generation

The downloadable PDF (`messy-reality-check.pdf`) is generated from a **dedicated print source file** (`reality-check-print.html`) — not from `reality-check.html`. This separation exists because web layouts and print layouts have different requirements and WeasyPrint handles them differently.

To regenerate the PDF:

```python
from weasyprint import HTML
HTML(filename='reality-check-print.html').write_pdf('messy-reality-check.pdf')
```

See `reality-check-postmortem.md` for full build instructions and lessons learned.

---

## Research Foundations

The framework is grounded in four research pillars:

1. **Manufacturing Execution Systems (MES)** — source of the MESSY acronym and operational structure
2. **Snowden & Boone / Cynefin Framework** — complexity theory applied to human experience
3. **Nehring & Röcke** — emotional complexity and the value of ambivalence
4. **Norcross et al.** — meta-research on what makes behavior change work over time

Full citations and reading list at [messy-playbook.vercel.app/thinking.html](https://messy-playbook.vercel.app/thinking.html)

---

## Gumroad Products

| Product | Link |
|---------|------|
| MESSY Taster | [livemessy.gumroad.com/l/messy-taster](https://livemessy.gumroad.com/l/messy-taster) |
| Self-Study Program | [livemessy.gumroad.com/l/messy-self-study](https://livemessy.gumroad.com/l/messy-self-study) |

---

## Key Dates

| Date | Milestone |
|------|-----------|
| 2026 Q1 | Initial site launch |
| 2026 April | Site update: nav, thinking page, scroll fix, audit |
| 2026 May | Reality Check asset, Daily Practice, Messy Plays™ launch, direct PDF download |

---

*The MESSY Playbook™ is for educational purposes and personal exploration only. It does not constitute therapy, professional counseling, or clinical advice.*

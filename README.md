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
| `micro-messes.html` | Micro Messes™ | Concept landing page — what Micro Messes are, WHY/HOW/WHAT, ecosystem progression, CTA to sets |
| `micro-messes-sets.html` | Micro Mess Sets | Grid index of all available sets — Brady Bunch tile layout, scales indefinitely |
| `micro-messes-set-00.html` | Set 00: First Encounters | Five universal anchor encounters, one per MESSY dimension |
| `micro-messes-set-01.html` | Set 01: Containing Multitudes | Five encounters inspired by Jennifer Rosner, Massachusetts Review, 2006 |
| `micro-messes-set-02.html` | Set 02: Beyond Problem Solving | Five encounters inspired by Russell L. Ackoff, JORS, 1979 |
| `reality-check.html` | The MESSY Reality Check™ | Web-optimized pain point reference — all 5 dimensions |
| `messy-reality-check.pdf` | PDF Download | Pre-built print-ready PDF (generated from `reality-check-print.html`) |
| `messy-arc-graphic.svg` | Arc Graphic | Standalone SVG of the MESSY framework arc — used as thumbnail |
| `messy-playbook-logo-vector.svg` | Brand Logo | Five-circle M·E·S·S·Y logo — transparent background, displayed in hero upper-left on homepage |

---

## Micro Messes™ Architecture

Micro Messes is a three-layer content system:

**Layer 1 — `micro-messes.html`**  
Concept landing page. Sells the format. No cards. CTA points to the sets index.

**Layer 2 — `micro-messes-sets.html`**  
Grid index of all sets. Each tile shows set number, name, one-sentence description, color-coded gradient, and dimension dots. Launches with three tiles. Scales by adding new `<a class="set-tile">` blocks.

**Layer 3 — individual set pages**  
Each set page has five cards (one per MESSY dimension) plus a set introduction. Each card has a **Save as PDF** button using a browser-native popup print window — no external dependencies.

### Set color identity
| Set | Name | Badge gradient |
|-----|------|---------------|
| Set 00 | First Encounters | `#667eea → #764ba2` (brand purple) |
| Set 01 | Containing Multitudes | `#e67e22 → #c0392b` (amber-red) |
| Set 02 | Beyond Problem Solving | `#1a5276 → #117a65` (navy-teal) |

### Adding a new set
1. Copy `micro-messes-set-02.html` and rename to `micro-messes-set-03.html`
2. Update: page title, meta description, OG tags, set number badge, h1, header-sub, source attribution (if research-anchored), all five card blocks, and the set-nav prev/next links
3. Add a new tile to `micro-messes-sets.html` with a distinct gradient
4. Update Set 02's "Next set →" nav link to point to Set 03

### Naming convention
Sets are numbered sequentially (Set 00, 01, 02…). The set name carries the theme. No sub-numbering until the library is large enough to warrant filtering on the grid page.

---

## How Updates Work

1. Make changes to the relevant file(s) locally or in Claude
2. Go to [github.com/Habari2026/messy-playbook](https://github.com/Habari2026/messy-playbook)
3. Click **Add file → Upload files → choose your files**
4. Select the updated file(s) — **never drag-and-drop files over ~100KB** (GitHub truncates them)
5. Add a short commit message and click **Commit changes** directly to main
6. Vercel auto-deploys within ~60 seconds

---

## Tech Stack

- **HTML / CSS / JavaScript** — no framework, no build step
- **Google Fonts** — Playfair Display + DM Sans (all pages include `preconnect` hints for performance)
- **Gumroad** — Pay What You Want downloads
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

### Micro Messes card PDFs
Card PDFs on set pages use a different approach — browser-native popup print window triggered by JavaScript. No WeasyPrint, no external dependency. User clicks **Save as PDF**, a styled popup opens with brand header and card content, and the browser's native print-to-PDF dialog fires. This is intentional: zero friction, works on any device.

---

## Navigation — Floating Scroll Buttons

All pages include floating ↑/↓ scroll buttons (bottom-right, gradient purple circles). Behavior is consistent across the site:

- **↑** scrolls to absolute top — appears after 400px of scroll
- **↓** scrolls to absolute bottom — appears until within 200px of the bottom

Implementation: CSS (`.float-nav` / `.float-btn` / `.float-btn.visible`), HTML (`<div class="float-nav">`), JS (`updateFloatBtns()` on scroll + load).

---

## Navigation — Architecture Notes

All 9 pages share the same nav structure and behavior. Key implementation details for future reference:

- **Position:** `position: fixed` on all pages — nav stays visible while scrolling
- **Get MESSY! button:** Placed *outside* the `<ul class="nav-links">` on all pages. The `<ul>` gets `display: none` on mobile; the CTA must live outside it to remain visible
- **CSS variables:** DM Sans pages (index, play, book, thinking) use `var(--cream)`, `var(--dark)`, `var(--mid)` etc. Micro Messes pages use hex colors. If adding dropdown CSS to any page, use that page's own color system — never mix
- **Class name:** Get MESSY! button always uses class `nav-cta` — never `nav-cta-btn`
- **First content section padding:** Must exceed nav height (~62px). DM Sans heroes use `clamp(5.5rem,...)`. Micro Messes heroes/page-headers use `5rem` minimum padding-top
- **Mobile drawer:** All 9 pages use a right-sliding panel (`translateX(100%)` → `translateX(0)`) with a dark overlay. Tapping the overlay or the ✕ button closes it. Float nav buttons hide automatically when the drawer is open (`body.nav-open .float-nav { display: none }`). Never use a drop-down pattern — it creates inconsistency across pages
- **JS brace discipline:** When modifying script blocks via regex, always verify brace balance after. Each script block must have equal `{` and `}` counts or the entire block fails silently
- **Single source of truth:** The mobile nav on `index.html` is the canonical version. To update the mobile menu on all pages, update `index.html` first, then replicate the drawer HTML, CSS, and JS to the other 8 pages using the replication script at `/tmp/replicate_nav_final.py`. Never edit individual pages independently

---

## Navigation — Explore Dropdown

All pages share an identical **Explore ▾** dropdown in the nav containing: Messy Plays™ · The Thinking · [divider] · Micro Messes™ · Insight Series (coming soon) · The Book.

**Behavior:** Click to open, click outside or press Escape to close, × button inside the menu to dismiss. Not hover-based — eliminates the gap sensitivity issue on all browsers and works correctly on touch devices.

**Active state:** The current page is highlighted inside the dropdown with `class="active"` on the relevant link.

**Mobile:** The desktop nav hides at the appropriate breakpoint and the hamburger drawer replaces it, listing all Explore items directly under an "Explore" section label.

**To add a new Explore item:** Add `<a href="newpage.html">New Page</a>` inside every `.dropdown-menu` div across all 9 HTML files, and add the corresponding link to each mobile nav drawer.

---


## Load Performance

All 9 pages are optimised for fast loading with no build tools or frameworks.

| File | Raw KB | Gzip ~KB | Load requests | Render-blocking |
|------|--------|----------|---------------|-----------------|
| index.html | 115 | 25 | 3 | 0 |
| play.html | 108 | 24 | 3 | 0 |
| book.html | 66 | 15 | 3 | 0 |
| thinking.html | 56 | 12 | 3 | 0 |
| micro-messes.html | 26 | 6 | 3 | 0 |
| micro-messes-sets.html | 23 | 5 | 3 | 0 |
| micro-messes-set-00/01/02.html | 36–37 | 8 | 3 | 0 |

The 3 load requests on every page are: preconnect to `fonts.googleapis.com`, preconnect to `fonts.gstatic.com`, and the Google Fonts stylesheet. No JavaScript libraries, no tracking scripts, no external frameworks.

Google Fonts uses `display=swap` so text renders instantly in the fallback font — no invisible text on slow connections. Vercel serves everything from a CDN edge node, so expected TTFB is 50–200ms on a standard connection.

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
| Self-Study Program | [livemessy.gumroad.com/l/messy-self-study](https://livemessy.gumroad.com/l/messy-self-study) |
| Facilitator License | [livemessy.gumroad.com/l/messy-facilitator-license](https://livemessy.gumroad.com/l/messy-facilitator-license) |
| Complete Bundle | [livemessy.gumroad.com/l/messy-complete-bundle](https://livemessy.gumroad.com/l/messy-complete-bundle) |

---

## Key Dates

| Date | Milestone |
|------|-----------|
| 2026 Q1 | Initial site launch |
| 2026 April | Site update: nav, thinking page, scroll fix, audit |
| 2026 May | Reality Check asset, Messy Plays™ launch, direct PDF download |
| 2026 May | Micro Messes™ full build — concept page, sets grid, Sets 00/01/02, PDF-per-card, inter-set nav |
| 2026 May | Scroll nav consistency pass — play.html, book.html, thinking.html updated to mirror homepage |
| 2026 May | Consistency + mobile pass — Explore dropdown on all pages, standardized footers, logo added to homepage hero, all touch targets 44px, click-based dropdown with × close button |
| 2026 May | Nav final fix — play.html dropdown CSS vars corrected, Get MESSY! moved outside hidden ul on Micro Messes pages, sticky→fixed nav on all 5 Micro Messes pages, nav-cta class standardized, play.html skip-nav + main landmark added, thinking.html float button aria-labels corrected, prefers-reduced-motion added to Micro Messes pages |
| 2026 May | Dropdown UX + book.html fix — blank nav resolved (white text on white bg from .nav-links a !important cascade), active-state underline scoped to direct nav items, × close button repositioned absolutely (eliminates whitespace above first dropdown item), all CSS var scoping verified across 9 pages |
| 2026 May | Mobile nav consistency pass — Micro Messes drop-down nav rebuilt as right-sliding panel matching DM Sans pages; play.html drawer Explore section completed; float buttons hidden when drawer open (body.nav-open); book.html hamburger visible on dark bg; JS syntax error fixed (stray closing braces in all 5 Micro Messes files) |
| 2026 May | Mobile nav final — homepage menu replicated exactly across all 9 pages; single source of truth established; JS brace errors resolved; 13-point verification check passes across all pages |
| 2026 May | Fix desktop dropdown JS conflict — const/var re-declaration in thinking.html and book.html killed entire script block; duplicate var declarations removed; main landmark added to 4 Micro Messes set pages; 49-point full audit passes |
| 2026 May | book.html layout fix — forthcoming label, headline, tagline, cards-row, and divider all had zero horizontal padding; fixed with clamp(1.5rem, 5vw, 4rem) matching site-wide padding system |

---

*The MESSY Playbook™ is for educational purposes and personal exploration only. It does not constitute therapy, professional counseling, or clinical advice.*

#!/usr/bin/env python3
"""Generate 25 Micro Messes card PDFs using WeasyPrint."""

import os
from weasyprint import HTML, CSS

OUTPUT_DIR = "/home/claude/card-pdfs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── SVG Logo ──────────────────────────────────────────────────────────────────
LOGO_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="50" height="50">
  <defs>
    <linearGradient id="gm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9b59b6"/><stop offset="100%" style="stop-color:#8e44ad"/>
    </linearGradient>
    <linearGradient id="ge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e67e22"/><stop offset="100%" style="stop-color:#d35400"/>
    </linearGradient>
    <linearGradient id="gs1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3498db"/><stop offset="100%" style="stop-color:#2980b9"/>
    </linearGradient>
    <linearGradient id="gs2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f1c40f"/><stop offset="100%" style="stop-color:#f39c12"/>
    </linearGradient>
    <linearGradient id="gy" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#27ae60"/><stop offset="100%" style="stop-color:#229954"/>
    </linearGradient>
  </defs>
  <g transform="rotate(-9, 46, 76)">
    <circle cx="46" cy="76" r="24" fill="url(#gm)"/>
    <text x="46" y="85" font-family="Arial, sans-serif" font-size="22" font-weight="900" fill="white" text-anchor="middle">M</text>
  </g>
  <g transform="rotate(6, 90, 108)">
    <circle cx="90" cy="108" r="22" fill="url(#ge)"/>
    <text x="90" y="116" font-family="Arial, sans-serif" font-size="20" font-weight="900" fill="white" text-anchor="middle">E</text>
  </g>
  <g transform="rotate(-7, 130, 62)">
    <circle cx="130" cy="62" r="26" fill="url(#gs1)"/>
    <text x="130" y="72" font-family="Arial, sans-serif" font-size="24" font-weight="900" fill="white" text-anchor="middle">S</text>
  </g>
  <g transform="rotate(8, 152, 116)">
    <circle cx="152" cy="116" r="23" fill="url(#gs2)"/>
    <text x="152" y="125" font-family="Arial, sans-serif" font-size="21" font-weight="900" fill="#856404" text-anchor="middle">S</text>
  </g>
  <g transform="rotate(-5, 128, 160)">
    <circle cx="128" cy="160" r="21" fill="url(#gy)"/>
    <text x="128" y="168" font-family="Arial, sans-serif" font-size="19" font-weight="900" fill="white" text-anchor="middle">Y</text>
  </g>
</svg>'''

# ── CSS ───────────────────────────────────────────────────────────────────────
PDF_CSS = """
@page { margin: 1.4cm 1.6cm; size: A4; }
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Arial, sans-serif; color: #2c3e50; background: #fff; line-height: 1.6; }

.print-brand {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 10px; padding: 1rem 1.35rem; margin-bottom: 1.75rem;
  display: flex; justify-content: space-between; align-items: center;
}
.print-brand-left { display: flex; align-items: center; }
.print-brand-logo-box {
  background: #ffffff; border-radius: 12px; padding: 7px;
  display: flex; align-items: center; justify-content: center;
  width: 64px; height: 64px;
}
.print-brand-right { display: flex; flex-direction: column; gap: 2px; }
.print-brand-logo { font-family: Arial, sans-serif; font-size: 1.05rem; font-weight: 700; color: #fff; }
.print-brand-set { font-size: 0.78rem; color: rgba(255,255,255,0.82); letter-spacing: 0.01em; }

.mess-card { border-radius: 14px; padding: 2rem 2rem 1.75rem; border: 2px solid; background: #fff; }
.card-top { display: flex; align-items: center; gap: 12px; margin-bottom: 0.7rem; }
.dim-badge { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; white-space: nowrap; }
.card-name { font-size: 1.3rem; font-weight: 700; color: #2c3e50; }
.card-encounter { font-size: 0.95rem; font-style: italic; color: #7f8c8d; margin-bottom: 1rem; line-height: 1.65; }
.card-time { display: inline-block; font-size: 0.75rem; font-weight: 700; color: #7f8c8d; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1.25rem; padding: 4px 12px; background: #f8f9fa; border-radius: 20px; border: 1px solid #ecf0f1; }
.steps-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; color: #7f8c8d; margin-bottom: 0.6rem; }
.steps-list { list-style: none; margin-bottom: 1.25rem; }
.steps-list li { display: flex; gap: 10px; font-size: 0.975rem; color: #34495e; padding: 7px 0; line-height: 1.7; border-bottom: 1px solid #f8f9fa; }
.steps-list li:last-child { border-bottom: none; }
.step-n { font-weight: 700; font-size: 0.8rem; min-width: 18px; padding-top: 3px; flex-shrink: 0; }
.card-notice { font-size: 0.9rem; padding: 0.8rem 1.1rem; border-radius: 8px; margin-bottom: 1.1rem; border-left: 3px solid; line-height: 1.6; }
.card-notice strong { font-weight: 700; }
.no-outcome { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; opacity: 0.65; }

.card-m  { border-color: #9b59b6; } .badge-m  { background: #9b59b6; color: #fff; } .sn-m  { color: #9b59b6; } .notice-m  { background: #f5eef8; border-color: #9b59b6; color: #2c3e50; } .out-m  { color: #9b59b6; }
.card-e  { border-color: #e67e22; } .badge-e  { background: #e67e22; color: #fff; } .sn-e  { color: #e67e22; } .notice-e  { background: #fef5ec; border-color: #e67e22; color: #2c3e50; } .out-e  { color: #e67e22; }
.card-s1 { border-color: #3498db; } .badge-s1 { background: #3498db; color: #fff; } .sn-s1 { color: #3498db; } .notice-s1 { background: #e8f4fd; border-color: #3498db; color: #2c3e50; } .out-s1 { color: #3498db; }
.card-s2 { border-color: #d4ac0d; } .badge-s2 { background: #f1c40f; color: #856404; } .sn-s2 { color: #d4ac0d; } .notice-s2 { background: #fff3cd; border-color: #d4ac0d; color: #856404; } .out-s2 { color: #856404; }
.card-y  { border-color: #27ae60; } .badge-y  { background: #27ae60; color: #fff; } .sn-y  { color: #27ae60; } .notice-y  { background: #e8f5e8; border-color: #27ae60; color: #2c3e50; } .out-y  { color: #27ae60; }

.writing-area { margin-top: 1.5rem; padding-top: 0.5rem; border-top: 1px solid #ecf0f1; }
.writing-line { border-bottom: 1px solid #dde1e7; height: 2rem; margin-bottom: 0.1rem; }
.print-foot { margin-top: 1.5rem; font-size: 0.72rem; color: #bdc3c7; text-align: center; letter-spacing: 0.03em; }
"""

# ── Card data ─────────────────────────────────────────────────────────────────
# Each entry: (filename_suffix, card_class, badge_class, step_class, notice_class, out_class,
#              badge_label, card_name, encounter, time, steps[], notice, set_label)

CARDS = [
  # ── Set 00 ──
  ("set-00-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "the unwatched corner",
   "An encounter with selective inattention — what you are deliberately not looking at.",
   "10 minutes",
   [
     "Get paper. Write \"what I'm currently not looking at\" at the top.",
     "List everything — work, relationships, health, money, your own behavior. Names only. No explanations.",
     "Read the list once without adding to it or reacting to any item.",
   ],
   "where your eyes want to skip.",
   "Set 00 — First Encounters"),

  ("set-00-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "the rough draft move",
   "An encounter with the gap between waiting to be ready and actually starting.",
   "5 minutes",
   [
     "Name the thing you have been postponing because it is not ready yet.",
     "Do the worst possible version of the first step. Right now. In 5 minutes.",
     "Stop when the time runs out, whether it is done or not.",
   ],
   "what \"not ready\" was actually protecting you from.",
   "Set 00 — First Encounters"),

  ("set-00-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "design for your worst day",
   "An encounter with the distance between the support you built and the support you are actually using.",
   "10 minutes",
   [
     "List the routines or habits you have set up to support yourself.",
     "Mark honestly which ones you used this week.",
     "Look at the one with the biggest gap. Ask: was this designed for my best day or my worst?",
   ],
   "whether you feel defensive, relieved, or both.",
   "Set 00 — First Encounters"),

  ("set-00-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "the grip inventory",
   "An encounter with the energy cost of maintaining control over something you cannot actually control.",
   "10 minutes",
   [
     "Name one thing you are currently holding tightly — an outcome, a relationship, someone's opinion of you.",
     "Write what you are afraid happens if you stop managing it for 24 hours.",
     "Don't let it go. Just look at what the holding costs.",
   ],
   "how much of your energy the grip is using.",
   "Set 00 — First Encounters"),

  ("set-00-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "the failure harvest",
   "An encounter with what only difficulty can teach.",
   "10 minutes",
   [
     "Think of something from the past week that went wrong, fell short, or surprised you badly.",
     "Write one thing it taught you that success in the same situation couldn't have.",
     "Don't write what you'll do differently. Write only what you now know.",
   ],
   "whether the teaching feels earned or thin.",
   "Set 00 — First Encounters"),

  # ── Set 01 ──
  ("set-01-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "the polish audit",
   "An encounter with what you are tidying instead of seeing.",
   "10 minutes",
   [
     "List three things you have cleaned, organized, or straightened in the last week — physical or otherwise.",
     "For each one, ask honestly: was this maintenance, or was this avoidance?",
     "If it was avoidance — name what it was keeping you from looking at.",
   ],
   "whether tidying felt like relief or like relief that something got covered.",
   "Set 01 — Containing Multitudes"),

  ("set-01-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "the unjustifiable step",
   "An encounter with action that doesn't follow logically from your plan.",
   "5 minutes",
   [
     "Name something you know you should do but can't fully rationalize.",
     "Do one small version of it right now — not because it makes sense, but because something in you already knows.",
     "Don't explain it to yourself afterward.",
   ],
   "what it feels like to act from knowing rather than reasoning.",
   "Set 01 — Containing Multitudes"),

  ("set-01-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "designed for which self?",
   "An encounter with the gap between your rational self and your irrational one.",
   "10 minutes",
   [
     "List the support structures you have built for yourself — routines, habits, systems.",
     "Ask honestly: which of these were designed for the self you think you should be?",
     "Name one thing your irrational, contradictory, fully human self actually needs that nothing on the list provides.",
   ],
   "the difference between support that performs wellness and support that actually holds you.",
   "Set 01 — Containing Multitudes"),

  ("set-01-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "the strategic unknowing",
   "An encounter with something you have been choosing not to know about yourself.",
   "10 minutes",
   [
     "Finish this sentence honestly: \"I have been avoiding finding out whether I...\"",
     "Write what you're afraid the answer is.",
     "Don't investigate it. Just sit with the fact that you already suspect.",
   ],
   "how much energy the not-knowing is costing.",
   "Set 01 — Containing Multitudes"),

  ("set-01-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "what tidiness can't teach",
   "An encounter with what a recent mess made possible.",
   "10 minutes",
   [
     "Think of a period of genuine disorder in the last few months — emotional, relational, creative, or practical.",
     "Write one thing that period made possible, revealed, or opened up that a clean outcome couldn't have.",
     "Don't reframe the mess as secretly good. Just notice what arrived inside it.",
   ],
   "whether the teaching feels like a surprise or something you already knew.",
   "Set 01 — Containing Multitudes"),

  # ── Set 02 ──
  ("set-02-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "the unconscious dilemma",
   "An encounter with the contradiction you are keeping unconscious because seeing it would require you to change.",
   "10 minutes",
   [
     "Name one situation in your life that keeps feeling stuck, circular, or unsolvable — at work, in a relationship, in yourself.",
     "Ask: what two things do you believe, want, or value that are in direct contradiction with each other inside this situation? Write both down.",
     "Read both sides without resolving the contradiction. Let them both be true at the same time.",
   ],
   "what it feels like to see both sides on paper simultaneously.",
   "Set 02 — Beyond Problem Solving"),

  ("set-02-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "the moment of death",
   "An encounter with a plan or approach you are still executing past its moment of usefulness.",
   "10 minutes",
   [
     "Name one plan, approach, or commitment you are still carrying forward — at work, in a relationship, in a personal project.",
     "Write the date you think it actually stopped working. Not when you acknowledged it — when it actually stopped.",
     "Look at the gap between that date and today.",
   ],
   "what you have been spending to keep it alive.",
   "Set 02 — Beyond Problem Solving"),

  ("set-02-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "learning over optimizing",
   "An encounter with whether your support system is designed to produce optimal outcomes or to help you learn and adapt.",
   "10 minutes",
   [
     "Describe one support structure in your life — a habit, a system, a person you rely on regularly.",
     "Ask honestly: is this designed to produce a specific outcome, or to help you stay curious and adapt when things change?",
     "Name one kind of surprise or failure this support system has no room for.",
   ],
   "whether your support system can learn, or only perform.",
   "Set 02 — Beyond Problem Solving"),

  ("set-02-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "managers do not solve problems",
   "An encounter with something you are still trying to solve that is actually a mess — a dynamic system of interacting problems with no single right answer.",
   "10 minutes",
   [
     "Name something you have been trying to solve — a recurring problem, a persistent conflict, a situation that keeps returning no matter what you do.",
     "Map the other problems it is connected to. Write at least three. Follow the connections outward.",
     "Look at what you've written and ask: is this a problem with a solution, or a system I have been living inside?",
   ],
   "what changes when you stop calling it a problem.",
   "Set 02 — Beyond Problem Solving"),

  ("set-02-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "we experience messes",
   "An encounter with what the unabstracted, lived experience of a recent mess taught you that your analysis of it couldn't.",
   "10 minutes",
   [
     "Think of a recent mess — not what it cost you or what you learned from it, but what it felt like from the inside while it was happening.",
     "Write two or three things only that lived experience could have taught you — things your retrospective analysis of the same events couldn't have surfaced.",
     "Don't extract lessons. Just describe what being inside the mess made visible.",
   ],
   "whether the experience and the analysis are even describing the same event.",
   "Set 02 — Beyond Problem Solving"),

  # ── Set 03 ──
  ("set-03-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "what the soil already knows",
   "An encounter with the conditions you are already living inside that you stopped noticing a while ago.",
   "10 minutes",
   [
     "Go outside or to a window. Find something growing without your help — a weed, a volunteer plant, something in a crack. Just look at it for two minutes.",
     "Write one thing it tells you about the conditions where you live — sun, neglect, moisture, disruption. Let the plant be data.",
     "Ask: what in your own life is growing without your help right now?",
   ],
   "whether the unmanaged growth is the most honest data you have.",
   "Set 03 — What Comes Up"),

  ("set-03-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "throw it",
   "An encounter with an action you have been postponing until conditions are more certain.",
   "10 minutes",
   [
     "Name one thing you have been waiting to start — a conversation, a project, a decision — until you knew more, had more, or felt more ready.",
     "Identify the smallest version of that action you could take today. The one that doesn't require certainty first.",
     "Do it, or commit to doing it before the day ends. Don't optimize it first.",
   ],
   "whether the waiting was about readiness or about avoiding the irreversibility.",
   "Set 03 — What Comes Up"),

  ("set-03-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "soil, sun, water",
   "An encounter with the conditions you have been creating versus the outcomes you have been trying to produce.",
   "10 minutes",
   [
     "Name one area of your life where you have been working hard but not seeing results — a relationship, a habit, a project.",
     "Separate two lists: what outcomes have you been chasing, and what conditions have you actually been tending? Write both.",
     "Ask: if you stopped chasing the outcome and only tended the conditions, what would you do differently tomorrow?",
   ],
   "the difference between controlling outcomes and creating conditions.",
   "Set 03 — What Comes Up"),

  ("set-03-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "you don't get to choose what comes up",
   "An encounter with something you planted — in a relationship, at work, in yourself — that grew into something you didn't intend.",
   "10 minutes",
   [
     "Name one thing you worked on deliberately that produced an unexpected result. Not a failure — just not what you planned.",
     "Describe what actually came up instead, as specifically as you can. Resist interpreting it.",
     "Ask honestly: is what came up worse than what you planned, or just different?",
   ],
   "whether \"different from what I planned\" has been living in your head as \"wrong.\"",
   "Set 03 — What Comes Up"),

  ("set-03-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "the volunteer",
   "An encounter with something useful or true that arrived without being invited.",
   "10 minutes",
   [
     "Think of the last week or month. What showed up without your arranging it — a conversation, an insight, a connection, a feeling you didn't expect?",
     "Write it down as specifically as you can. Don't interpret it yet.",
     "Ask: what made you available to receive it when it arrived?",
   ],
   "whether the most useful things in this period were planned or volunteered.",
   "Set 03 — What Comes Up"),

  # ── Set 04 ──
  ("set-04-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "how you actually decide",
   "An encounter with your own tendencies as a decision-maker.",
   "10 minutes",
   [
     "Think about a significant decision you made in the last year — a job, a relationship, a purchase, a path. Write down how you made it. Did you consider a few options and choose, or did you keep searching for something better?",
     "Simon observed that humans cannot evaluate every available option — there are too many, our information is incomplete, and our minds aren't built to weigh them all. So we satisfice: we consider a limited set of options, choose one that is good enough, and move on. Write one honest sentence about whether you satisfice or maximize in this area of your life.",
     "Name one area where you satisfice well. Name one where you can't seem to stop searching.",
   ],
   "whether your searching is serving you — or haunting you.",
   "Set 04 — Good Enough"),

  ("set-04-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "the good enough move",
   "An encounter with action that doesn't wait for certainty.",
   "10 minutes",
   [
     "Simon lived by one mantra: \"The best is the enemy of the good.\" He wore one brand of socks, owned one black beret, ate the same breakfast every morning, and lived in the same house for 46 years. He wasn't being eccentric. He was protecting his attention for the work that mattered. Name one recurring decision in your life that is consuming more attention than it deserves.",
     "Decide it now. In one sentence. For the next 30 days.",
     "Write down what that decision has been costing you — in time, energy, or mental space.",
   ],
   "what becomes available when one small decision is already made.",
   "Set 04 — Good Enough"),

  ("set-04-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "what your constraints are protecting",
   "An encounter with the possibility that your limits are doing something useful.",
   "15 minutes",
   [
     "Simon's daughter Katherine said her father \"simplified his life in terms of his daily habits, thus eliminating the need to make little decisions about everything.\" That simplification freed his attention for the people and work that actually mattered to him. Name one real constraint in your life right now — time, energy, money, capacity.",
     "Ask: what does this constraint force you to prioritize? What gets your full attention because of it, not in spite of it?",
     "Sit with this question: if this constraint disappeared tomorrow, what would you risk losing focus on?",
   ],
   "whether the constraint is only a problem — or also a structure.",
   "Set 04 — Good Enough"),

  ("set-04-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "searching for the best",
   "An encounter with the exhaustion of not being able to stop comparing.",
   "10 minutes",
   [
     "Simon argued that searching for the best is itself a cost — one most people forget to account for. Name one area of your life where you are still searching for the optimal answer. A decision, a path, a version of yourself.",
     "Write down how long you've been searching. Be honest.",
     "Don't resolve it. Just sit with this: what has the search cost you so far?",
   ],
   "the difference between genuine discernment and the performance of thoroughness.",
   "Set 04 — Good Enough"),

  ("set-04-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "saving it for what matters",
   "An encounter with the freedom that comes from deciding in advance.",
   "10 minutes",
   [
     "Simon's core insight was simple: stop spending cognitive resources on decisions that don't deserve them. Save them for the work that does. Write down the three things that matter most to you right now — the places where your best thinking genuinely needs to go.",
     "Now identify one decision you are currently maximizing (searching endlessly for the perfect answer) that has nothing to do with those three things.",
     "Set a good-enough standard for it. Write it down in one sentence.",
   ],
   "whether the energy you free up actually goes where you intended.",
   "Set 04 — Good Enough"),

  # ── Set 06 ──
  ("set-06-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "you are also being watched",
   "An encounter with the limits of your own point of view.",
   "15 minutes",
   [
     "Choose a space you know well. Spend five minutes moving through it normally, noticing what you notice.",
     "Now ask: what in this space has been noticing you — or adapting to you, or waiting for you to leave? Look for evidence: worn paths, marks, traces, behaviors that happen when you're absent or present.",
     "Write one sentence from the point of view of something that shares this space with you.",
   ],
   "the difference between observing a situation and being observed within one.",
   "Set 06 — Never a Solo Act"),

  ("set-06-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "become a participant",
   "An encounter with a situation you can't stay outside of.",
   "15 minutes",
   [
     "Go somewhere something is happening without you — plants growing, water moving, people passing, a room filling up. Don't bring a task. Don't decide in advance what role you'll play.",
     "At some point, let yourself be pulled in. Follow whatever catches your attention, even if it seems beside the point. Don't redirect toward something more useful.",
     "After you leave, notice what from this encounter keeps surfacing in your thinking. Don't chase it — just notice when it returns.",
   ],
   "what keeps coming back after the encounter is officially over.",
   "Set 06 — Never a Solo Act"),

  ("set-06-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "you are already an ecosystem",
   "An encounter with the ninety percent of you that isn't you.",
   "10 minutes",
   [
     "Sit with this for two minutes: the microorganisms living in and on your body currently outnumber your human cells roughly ten to one. You are not a solo entity moving through an environment. You are a mess hall — an ecosystem of lives, constantly living and dying together.",
     "Think of a situation you're currently navigating — something you'd describe as \"what I need to figure out.\" List everything non-human that is actually part of this situation, even if it doesn't count as a variable in your normal framing.",
     "Ask: whose interests does my version of this situation assume? Who or what gets left out when I call this my problem?",
   ],
   "how much of what you call your thinking is happening through and with others.",
   "Set 06 — Never a Solo Act"),

  ("set-06-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "wrong questions",
   "An encounter with the possibility that you're asking the wrong thing.",
   "10 minutes",
   [
     "Write down a question you've been carrying — something you're trying to work out or understand, in work or life.",
     "Ask: who does this question center? Whose point of view does it assume is the right one to take? Write two versions of the question that shift the center to someone or something else in the situation.",
     "Sit with the rewritten questions. Don't answer them. Notice whether they open the situation differently.",
   ],
   "how the shape of a question determines what kinds of answers are even possible.",
   "Set 06 — Never a Solo Act"),

  ("set-06-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "process that resists analysis",
   "An encounter with making that doesn't produce anything.",
   "15 minutes",
   [
     "Make something with whatever is immediately available — arrange objects, make marks, move things around. Start before you decide what you're making.",
     "At some point you will feel the pull to make it legible — to yourself or to someone imagined. When you feel that pull, do something that makes the thing harder to explain, not easier.",
     "When time is up, don't document it. Let it be a process that existed and is now complete.",
   ],
   "the difference between making something and making something for something.",
   "Set 06 — Never a Solo Act"),
]


def html_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def build_html(card):
    (slug, card_class, badge_class, step_class, notice_class, out_class,
     badge_label, card_name, encounter, time, steps, notice, set_label) = card

    steps_html = ""
    for i, step in enumerate(steps, 1):
        steps_html += f'''<li><span class="step-n {step_class}">{i}.</span><span>{html_escape(step)}</span></li>\n'''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Micro Mess — {html_escape(card_name)}</title>
<style>{PDF_CSS}</style>
</head>
<body>

<div class="print-brand">
  <div class="print-brand-left">
    <div class="print-brand-logo-box">{LOGO_SVG}</div>
  </div>
  <div class="print-brand-right">
    <span class="print-brand-logo">The MESSY Playbook&#x2122;</span>
    <span class="print-brand-set">Micro Messes&#x2122; &middot; {html_escape(set_label)}</span>
  </div>
</div>

<div class="mess-card {card_class}">
  <div class="card-top">
    <span class="dim-badge {badge_class}">{html_escape(badge_label)}</span>
    <span class="card-name">{html_escape(card_name)}</span>
  </div>
  <p class="card-encounter">{html_escape(encounter)}</p>
  <span class="card-time">&#x23F1; {html_escape(time)}</span>
  <p class="steps-label">The Mess</p>
  <ol class="steps-list">
{steps_html}  </ol>
  <div class="card-notice {notice_class}"><strong>Notice:</strong> {html_escape(notice)}</div>
  <p class="no-outcome {out_class}">No outcome required.</p>
</div>

<div class="writing-area">
  <div class="writing-line"></div>
  <div class="writing-line"></div>
  <div class="writing-line"></div>
  <div class="writing-line"></div>
</div>
<p class="print-foot">messy-playbook.vercel.app &middot; Free for personal use &middot; No outcome required.</p>

</body>
</html>"""


def generate_all():
    success = 0
    errors = []
    for card in CARDS:
        slug = card[0]
        filename = f"micro-messes-{slug}.pdf"
        filepath = os.path.join(OUTPUT_DIR, filename)
        html_content = build_html(card)
        try:
            HTML(string=html_content).write_pdf(filepath)
            print(f"  ✓  {filename}")
            success += 1
        except Exception as e:
            print(f"  ✗  {filename}: {e}")
            errors.append((filename, str(e)))

    print(f"\n{success}/{len(CARDS)} PDFs generated.")
    if errors:
        print("Errors:")
        for f, e in errors:
            print(f"  {f}: {e}")


if __name__ == "__main__":
    generate_all()

#!/usr/bin/env python3
"""Generate 65 Micro Messes card PDFs using WeasyPrint (Sets 00-12)."""

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

  ("set-05-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "what's actually in the way",
   "An encounter with the difference between real obstacles and invented ones.",
   "10 minutes",
   [
     "Write down what you're stuck on. Then list every reason you can't move forward yet.",
     "Go through the list. For each reason, ask: is this real, or is it a condition I made up? Mark each one honestly.",
     "Pick the one real constraint. Set the rest aside for now.",
   ],
   "which reasons feel the most solid — and why.",
   "Set 05 — Something Finite"),

  ("set-05-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "work the small space",
   "An encounter with what becomes possible when you limit your options on purpose.",
   "10 minutes",
   [
     "Choose something you're working on. Give yourself one rule: use only what you already have. No new research, no new tools, no waiting for better conditions.",
     "Set a timer for 10 minutes. Work only inside that rule.",
     "When the timer stops, write down one thing that happened that wouldn't have happened without the limit.",
   ],
   "whether the limit felt like a wall or like a frame.",
   "Set 05 — Something Finite"),

  ("set-05-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "borrow the frame",
   "An encounter with structure that already exists and how it might hold your work.",
   "15 minutes",
   [
     "Think of a format or routine from a completely different part of your life — a recipe, a sports drill, a meeting format, a daily habit. Write it out as simple steps.",
     "Take something you're currently working on. Try fitting it into that borrowed structure, step by step.",
     "Write down what fits, what doesn't, and what surprised you.",
   ],
   "what the borrowed structure makes easier.",
   "Set 05 — Something Finite"),

  ("set-05-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "let the limit lead",
   "An encounter with the idea that more freedom doesn't always mean better results.",
   "10 minutes",
   [
     "Think of something you've been putting off because conditions aren't right yet — not enough time, resources, or information. Write it down.",
     "Assume those conditions will never improve. Write one sentence about what you could do right now, with exactly what you have.",
     "Read that sentence back. Notice how it feels different from waiting.",
   ],
   "what you would start if you stopped waiting for better conditions.",
   "Set 05 — Something Finite"),

  ("set-05-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "the shape it wants",
   "An encounter with what your work is already telling you about how it wants to go.",
   "10 minutes",
   [
     "Pick something you're working on. Write down the constraints that are fixed and can't change.",
     "Instead of working against those fixed points, treat them as the shape of the work. Write down what they make possible rather than what they block.",
     "Notice if the work looks different from this angle.",
   ],
   "what the constraint has been protecting all along.",
   "Set 05 — Something Finite"),

  ("set-06-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "you are also being watched",
   "An encounter with the limits of your own point of view.",
   "15 minutes",
   [
     "Choose a space you know well. Spend five minutes moving through it normally, noticing what you notice.",
     "Now ask: what in this space has been noticing you — or adapting to you, or waiting for you to leave? Look for evidence: worn patches, marks, things that have shifted, behaviors that change when you're around or away.",
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
     "Go somewhere something is already happening without you — a conversation in progress, people working together, a room filling up, something being made or cooked or built. Don't bring a task. Don't decide in advance what role you'll play.",
     "At some point, let yourself be pulled in. Follow whatever catches your attention, even if it seems beside the point. Don't redirect toward something more useful.",
     "After you leave, notice what from this encounter keeps surfacing in your thinking. Don't chase it — just notice when it returns.",
   ],
   "what keeps coming back after the encounter is officially over.",
   "Set 06 — Never a Solo Act"),

  ("set-06-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "you are already an ecosystem",
   "An encounter with everything that's shaping your thinking right now.",
   "10 minutes",
   [
     "Before you do anything else, take stock of your current conditions: How much sleep did you get? When did you last eat? What's the mood in the room — at home or at work? What happened in the last two hours? Write it down quickly, just facts.",
     "Now think of something you're currently stuck on. Look at your conditions list. How many of those things are actively shaping how you're thinking about it right now?",
     "Ask: if the conditions were different — better sleep, different space, different time of day — would this problem look the same? What part of this is really you deciding, and what part is the conditions you happen to be inside?",
   ],
   "how much of what feels like a personal conclusion is actually a snapshot of a moment.",
   "Set 06 — Never a Solo Act"),

  ("set-06-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "wrong questions",
   "An encounter with the possibility that you're asking the wrong thing.",
   "10 minutes",
   [
     "Write down a question you've been carrying — something you're trying to work out or understand, in work or life.",
     "Look at your question. Who are you picturing when you imagine solving it? Is that person — or that angle — actually the right place to start? Write two versions of the question that put someone or something else at the center.",
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
     "At some point you will feel the urge to make it make sense — to yourself or to someone you're imagining showing it to. When you feel that urge, do something that makes the thing harder to explain, not easier.",
     "When time is up, don't document it. Let it be a process that existed and is now complete.",
   ],
   "the difference between making something and making something for something.",
   "Set 06 — Never a Solo Act"),

  # ── Set 07 ──
  ("set-07-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "coming back to yourself",
   "An encounter with the emotional territory you thought you had already left behind.",
   "15 minutes",
   [
     "Name one feeling or pattern that has reappeared in your life recently — something you thought you had dealt with. Write it down without judging whether it should still be here.",
     "Consider when you first encountered this feeling or pattern. Write one sentence about what was happening then. Don't look for causes. Just place it in time.",
     "Ask yourself: what do you know now that you didn't know the last time you were here? Write two or three things that are genuinely different about you, even if the feeling isn't.",
   ],
   "whether the return feels like failure or like evidence.",
   "Set 07 — Same Ground"),

  ("set-07-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "one small revolution",
   "An encounter with the action you keep arriving back at.",
   "10 minutes",
   [
     "Name one thing you have tried to do — a habit, a practice, a change — that keeps slipping. Don't explain why it slipped. Just name it plainly.",
     "Do the smallest possible version of that thing right now. Not a plan to do it. The thing itself, scaled down until it takes less than three minutes.",
     "Write one sentence about what it felt like to do it again, knowing you have been here before.",
   ],
   "whether starting again feels lighter when you stop calling it starting over.",
   "Set 07 — Same Ground"),

  ("set-07-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "the witness",
   "An encounter with someone who has seen you circle this before.",
   "15 minutes",
   [
     "Think of one person who has known you long enough to have watched you work through a recurring difficulty. It doesn't have to be someone you talk to often.",
     "Write down what you think that person would say about where you are now versus where you were the last time this came up. Not what they would say to comfort you — what they would actually observe.",
     "Consider what you would need to say to bring them fully current. You don't have to say it today. Just write it.",
   ],
   "whether your pattern looks different from the outside than it does from inside it.",
   "Set 07 — Same Ground"),

  ("set-07-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "the return is the path",
   "An encounter with repetition as the mechanism, not the obstacle.",
   "15 minutes",
   [
     "Write down one thing you keep returning to that you have been treating as a sign of failure. A worry, a conflict, a way of responding that you thought you had outgrown.",
     "Read what you wrote and ask: what if returning to the same ground is not a sign that you haven't moved? Growth doesn't always travel in a straight line away from difficulty. Sometimes it circles back through the same territory — but from a slightly different height each time. What changes if you apply that idea to what you just wrote?",
     "Write one sentence describing what the return looks like if it is part of the process rather than proof that the process has failed.",
   ],
   "whether accepting the loop makes it easier or harder to move through it.",
   "Set 07 — Same Ground"),

  ("set-07-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "higher on the spiral",
   "An encounter with what the same ground looks like from a different height.",
   "15 minutes",
   [
     "Think of something you have been through before — a loss, a conflict, a stretch of difficulty — that you are now, in some form, going through again. Describe it in one sentence.",
     "List three things you can bring to it this time that you couldn't bring the last time you were here. Skills, perspectives, relationships — anything real and specific.",
     "Write one sentence about what you are ready to put down now that you were still carrying then.",
   ],
   "whether you are above or below where you were.",
   "Set 07 — Same Ground"),

  # ── Set 08 ──
  ("set-08-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "without a label",
   "An encounter with what you feel before you name it.",
   "10 minutes",
   [
     "Think of a moment from the last 24 hours when you felt something but couldn't quite describe it, or when you named it quickly and moved on. Write down what happened.",
     "Sit with the feeling for two minutes without reaching for a word. Notice whether there's more than one thing happening, or whether the feeling shifted as the moment unfolded.",
     "Write what you can: not a label, but what it was actually like. Where you felt it. Whether it stayed steady or changed.",
   ],
   "whether the feeling became clearer or more complicated when you gave it more room.",
   "Set 08 — Hard to Name"),

  ("set-08-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "before it settles",
   "An encounter with acting when you don't yet know how you feel.",
   "10 minutes",
   [
     "Think of something you've been putting off. Not because it's too hard, but because you're not sure how you feel about it yet.",
     "Do one small piece of it. Five minutes of work is enough. While you're moving, notice what the feeling does.",
     "When you stop, write one sentence. Not about how you feel now, but about what the feeling did while you were working. Did it shift? Sharpen? Disappear?",
   ],
   "whether moving changed the feeling, or just revealed it more clearly.",
   "Set 08 — Hard to Name"),

  ("set-08-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "let it be mixed",
   "An encounter with someone else's complicated feeling.",
   "15 minutes",
   [
     "Think of someone carrying something complicated right now. Not clearly happy or sad, or changing from one day to the next. Write down the single word you'd normally use to describe what they're going through.",
     "Now write three to four sentences about what doesn't fit that word. The parts that are harder to see, or that seem to contradict the simple version.",
     "The next time you're with them, try asking about one of those parts. Not to fix it, just to acknowledge it's there.",
   ],
   "whether they seem surprised that you noticed the harder-to-name part.",
   "Set 08 — Hard to Name"),

  ("set-08-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "not knowing",
   "An encounter with a feeling you can't identify.",
   "10 minutes",
   [
     "Find a feeling you currently have that you can't name. Something present but unclear. If nothing surfaces immediately, sit quietly for two minutes. Something will.",
     "Stay with it without trying to resolve it. Set a timer for five minutes. When you want to label it, notice the impulse. But don't follow it yet.",
     "When the timer ends, write one phrase that gets close. Not a single word, but a phrase. \"Something like dread but also curiosity\" counts. Accuracy matters less than honesty.",
   ],
   "whether the not-knowing itself has a texture. Heavy or light, familiar or strange.",
   "Set 08 — Hard to Name"),

  ("set-08-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "what the combination tells you",
   "An encounter with what two feelings together reveal that neither one alone would.",
   "15 minutes",
   [
     "Think of a time when you felt two things at once: proud and embarrassed, relieved and sad, grateful and resentful. Pick one specific moment.",
     "Write about each feeling separately: two to three sentences each. What was the proud part actually about? What was the embarrassed part about? Don't try to reconcile them.",
     "Read both back. Notice whether the combination points to something that a single label would have missed entirely.",
   ],
   "what the contradiction was protecting or pointing toward.",
   "Set 08 — Hard to Name"),

  # ── Set 09 ──
  ("set-09-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "from here",
   "An encounter with what you can see about something now that you couldn't see while you were in it.",
   "15 minutes",
   [
     "Think of something you've been through that you'd describe differently today than you did at the time. Not a crisis — just something you lived through and have some distance from now. Write one sentence about how you described it then.",
     "Write one sentence about how you'd describe it now. Don't worry about which version is more accurate. Just notice that there are two.",
     "Write down one specific thing you can see from here that you genuinely couldn't see from there. Not a lesson. Just something that's visible now that wasn't before.",
   ],
   "whether the distance feels like clarity, or just a different kind of partial view.",
   "Set 09 — After the Fact"),

  ("set-09-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "write it down now",
   "An encounter with the version of events you're living inside right now.",
   "10 minutes",
   [
     "Think of something significant you're currently in the middle of — a project, a decision, a change. Write three to four sentences about it as honestly as you can. Not how you'd explain it to someone else. What it actually feels like from inside it, today.",
     "Add one sentence at the end: \"What I cannot see yet is...\" Write whatever comes, even if it's just \"I don't know.\"",
     "Put the date on it. Keep it somewhere you'll find it in three to six months.",
   ],
   "whether writing the present version feels different from how you'd tell this story later.",
   "Set 09 — After the Fact"),

  ("set-09-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "the second conversation",
   "An encounter with what someone close to you might only be able to tell you later.",
   "15 minutes",
   [
     "Think of someone who recently came through something significant — a project, a transition, a hard stretch. Not still in crisis. Write down how they described it at the time, or how they've described it to you since.",
     "Think about what they haven't said yet. Not what they're hiding — just what might not be visible to them yet. The part that tends to surface weeks or months after. The low. The question. The thing they'll mention one day in passing and you'll think: that was always there.",
     "The next time you're with them, leave a little more space than usual. Not to extract information. Just to make room for what hasn't surfaced yet.",
   ],
   "whether you find yourself listening differently when you're not only listening for what they already know.",
   "Set 09 — After the Fact"),

  ("set-09-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "the low you didn't mention",
   "An encounter with how you actually felt after something ended, now that some time has passed.",
   "10 minutes",
   [
     "Think of something that ended with a sense of accomplishment or relief — a project, a goal reached, a long effort finally done. Write down how you described it at the time. What did you tell people?",
     "Now write what you didn't report. The low that arrived after. The restlessness. The sense that something had been lost in the push to the finish. You don't have to have felt all of these. Write whatever is true.",
     "Sit with both versions. You do not need to correct the first one. Just let the second one exist alongside it.",
   ],
   "whether naming the unreported part feels like relief, or like disloyalty to the version you told at the time.",
   "Set 09 — After the Fact"),

  ("set-09-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "from this distance",
   "An encounter with what retrospect makes possible that the moment itself didn't.",
   "15 minutes",
   [
     "Think of something you went through that, at the time, felt primarily like pressure, uncertainty, or just getting through it. Not the hardest thing you've ever faced — just something demanding that is now behind you. Write one sentence about what it felt like from inside it.",
     "Write two to three things you understand about that period now that you couldn't have articulated then. Not lessons. Just things that are clearer from here — why something happened, what you were actually carrying, what you were quietly learning without knowing it.",
     "Read what you wrote and ask: does any of this apply to something you're in right now?",
   ],
   "whether the hindsight feels like wisdom, or just like knowing how the story ended.",
   "Set 09 — After the Fact"),

  # ── Set 10 ──
  ("set-10-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "the old map",
   "An encounter with the understanding you've been navigating by — and where it has stopped matching the territory.",
   "10 minutes",
   [
     "Think of a situation that keeps feeling confusing or stuck. Write it down in one sentence.",
     "Ask: what did you used to think about this that no longer quite fits? Write that down — the old explanation, the old story, the old assumption.",
     "Notice whether you have been trying to force the old understanding back into place, or waiting for a new one to arrive fully formed.",
   ],
   "what it feels like to name the gap without immediately trying to fill it.",
   "Set 10 — The Messy Middle"),

  ("set-10-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "move anyway",
   "An encounter with one thing you can do from inside the confusion — before it clears.",
   "10 minutes",
   [
     "Name something you have been waiting to act on until you understood it better. Not a practical obstacle — a feeling that you don't yet know what you actually think or want.",
     "Ask: what would you do next if you accepted that the understanding might only come from moving, not from more thinking?",
     "Write down one action that feels possible from where you are now — not from where you want to be.",
   ],
   "whether waiting for clarity has become its own kind of stalling.",
   "Set 10 — The Messy Middle"),

  ("set-10-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "someone to stay in it with",
   "An encounter with the difference between someone who helps you tidy the mess up and someone who helps you work through it.",
   "15 minutes",
   [
     "Think of something confusing or unresolved you are currently carrying. Who have you talked to about it?",
     "For each person, ask honestly: did they help you understand it better, or help you feel better about it? Both matter — but they're different things.",
     "Think of one person who tends to keep the conversation going rather than closing it down. What would it look like to bring this mess to them?",
   ],
   "whether you have been seeking comfort over clarity — and whether that has been a deliberate choice.",
   "Set 10 — The Messy Middle"),

  ("set-10-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "put it down for now",
   "An encounter with an explanation you have been holding on to because the alternative is not knowing.",
   "10 minutes",
   [
     "Name something you have already decided — a reason something happened, a story about why things are the way they are, a conclusion you landed on quickly.",
     "Ask: what would you have to sit with if you set that explanation down for now? Not permanently — just for today.",
     "Set it down. Don't replace it with another explanation. Just notice what is actually there without the frame.",
   ],
   "whether the explanation has been more about comfort than accuracy.",
   "Set 10 — The Messy Middle"),

  ("set-10-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "what staying in it made possible",
   "An encounter with something that only became visible because you didn't resolve the confusion too soon.",
   "15 minutes",
   [
     "Think of a time you stayed in genuine confusion — about a situation, a relationship, a decision — longer than was comfortable, and came out the other side seeing it differently.",
     "Write down what staying in that middle actually produced. Not a general lesson — something specific that shifted.",
     "Ask: what would have been lost if you had resolved it earlier?",
   ],
   "whether the confusion and the clarity were part of the same process, not opposites.",
   "Set 10 — The Messy Middle"),

  # ── Set 11 ──
  ("set-11-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "the shape of the problem",
   "An encounter with the question you haven't asked yet.",
   "10 minutes",
   [
     "Think of something that's been bothering you — at home, at work, or both. Write it down in one sentence, the way you'd normally describe it.",
     "Read it back and ask: what does this leave out? Where does the problem \"start\" in your version — and is that actually where it starts?",
     "Write a second sentence describing the same situation, but from a different starting point. Make it as different from your first version as you can.",
   ],
   "how the second version changes what feels solvable.",
   "Set 11 — Outside the Frame"),

  ("set-11-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "move the line",
   "An encounter with a different starting point.",
   "10 minutes",
   [
     "Take a problem you've been working on without much progress. Write down what you've been trying to fix.",
     "Ask yourself: what if the problem starts earlier than I think? Or later? Or somewhere I haven't been looking? Pick one and write a new version of the problem from that new starting point.",
     "Compare the two versions. What becomes possible in the second one that wasn't in the first?",
   ],
   "what the second version opens up that the first one didn't.",
   "Set 11 — Outside the Frame"),

  ("set-11-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "someone else's line",
   "An encounter with a different view of where the problem lives.",
   "15 minutes",
   [
     "Think of a situation where you and someone else are stuck — at home, at work, anywhere. You both care about it, but you're not getting anywhere together.",
     "Ask them one question: \"Where does this start for you?\" In person, by message, however works. Listen without explaining your own view.",
     "Notice whether they're describing the same problem or a different one. You don't need to agree. Just take in what they're seeing.",
   ],
   "when two people draw a problem differently, they're often not disagreeing about facts — they're starting from different places.",
   "Set 11 — Outside the Frame"),

  ("set-11-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "two versions at once",
   "An encounter with sitting in the gap.",
   "10 minutes",
   [
     "Think of a situation where you and someone else each seem to be describing a different problem — even though you're talking about the same thing. Write down both versions: how you see it, and how they seem to see it.",
     "Sit with the fact that both might be true — or that neither fully captures what's actually happening. Don't try to merge them or decide who's right.",
     "Notice what it feels like to hold two definitions of the same situation at once, without resolving them.",
   ],
   "the discomfort here is useful. It means you're taking both versions seriously.",
   "Set 11 — Outside the Frame"),

  ("set-11-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "what comes into view",
   "An encounter with a wider picture.",
   "10 minutes",
   [
     "Return to the situation you started with — the way you first described it. Write it down again, in your own words.",
     "Write what you've noticed since you began this set. Has the shape of the problem shifted? What's come into view that wasn't there before?",
     "Write one thing you might do differently now that you're working with a wider version of the situation. Keep it small and specific.",
   ],
   "the situation didn't change. What changed is the space you're working in.",
   "Set 11 — Outside the Frame"),

  ("set-12-m",
   "card-m", "badge-m", "sn-m", "notice-m", "out-m",
   "M · Monitor", "the score you keep",
   "An encounter with a number that started running the show.",
   "10 minutes",
   [
     "Name a number you check often, at home or at work. Steps walked, hours billed, likes, weight, money saved, emails cleared. Write it down.",
     "Underneath that number, what were you actually after? Write the real thing in plain words: feeling healthy, doing good work, staying close to people.",
     "Be honest about the last week. Did you serve the number, or the thing underneath it? Note one moment where the two pulled apart.",
   ],
   "how easy it is to keep score and forget what the score was ever for.",
   "Set 12 — What Counts"),

  ("set-12-e",
   "card-e", "badge-e", "sn-e", "notice-e", "out-e",
   "E · Execute", "the easy win",
   "An encounter with the shortcut that hits the number but misses the point.",
   "10 minutes",
   [
     "Pick a number you're expected to hit, at home or at work: a count, a quota, a target, a streak.",
     "Notice a shortcut you've slipped into that moves the number without doing the real thing. Padding a report, busywork that looks productive, hitting the step count by pacing the kitchen.",
     "Do the honest version once instead, even if it scores worse. Aim at the goal the number was standing in for.",
   ],
   "how often the easy way to win the number is the long way from the goal.",
   "Set 12 — What Counts"),

  ("set-12-s1",
   "card-s1", "badge-s1", "sn-s1", "notice-s1", "out-s1",
   "S · Support", "someone else's scoreboard",
   "An encounter with the target shaping someone else's choices.",
   "15 minutes",
   [
     "Think of someone whose behavior toward you is shaped by a number: a coworker chasing a target, a kid chasing a grade, anyone working to a quota.",
     "Ask yourself, or ask them directly: what does hitting that number make them do? What does it make them skip?",
     "Notice where the number and the real goal point in different directions, and whether you've been judging them by the number too.",
   ],
   "how a target meant to help can quietly push the real goal aside.",
   "Set 12 — What Counts"),

  ("set-12-s2",
   "card-s2", "badge-s2", "sn-s2", "notice-s2", "out-s2",
   "S · Surrender", "drop the target",
   "An encounter with a goal you're ready to stop chasing.",
   "10 minutes",
   [
     "Name a number you set as a goal for yourself: a target weight, a savings figure, a follower count, a deadline you keep moving.",
     "Ask whether chasing it still helps, or whether it's become its own thing, separate from why you set it.",
     "If it's stopped helping, let it go for now. Keep the direction it pointed you in, but drop the number. Write down the direction with no number attached.",
   ],
   "what loosens when the target is no longer the point.",
   "Set 12 — What Counts"),

  ("set-12-y",
   "card-y", "badge-y", "sn-y", "notice-y", "out-y",
   "Y · Yield", "what you can't count",
   "An encounter with what matters but won't be measured.",
   "10 minutes",
   [
     "Think about a part of your life that matters a lot: a relationship, your health, a piece of work, your home.",
     "Write down what's good about it right now using no numbers at all. Just describe it, the way you'd tell a friend.",
     "Sit with the fact that none of that showed up as a number, and it still counts. Maybe it counts most.",
   ],
   "how much of what matters never makes it onto a scoreboard.",
   "Set 12 — What Counts"),
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

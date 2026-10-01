---
name: apple-ux-ui
license: MIT
description: "Design and review interface behavior, layout, wording, and accessibility using Apple's eight design principles and Human Interface Guidelines, with explicit adaptations for web and other platforms. Use for screens, components, forms, dialogs, dashboards, navigation, onboarding, and UX critiques. Includes topic references and an optional live HIG fetcher. Not a visual theme or component library."
metadata:
  author: Mikhail Kim
  version: "1.0.1"
  source: https://developer.apple.com/design/human-interface-guidelines/design-principles
  fetched: 2026-09-14
---

# Apple UX/UI: design principles as working rules

Apple states eight design principles and says they form the foundation for the guidance throughout
the Human Interface Guidelines. This skill carries those principles and the HIG rules that
instantiate them, written platform-neutral wherever the source allows, so they apply to web apps,
desktop and mobile alike; where Apple's guidance is Apple-specific, a rule gives the Apple form and
its generic equivalent. It is a rule set for deciding and reviewing how an interface behaves — not a
visual identity, not a component library, not an implementation guide. It is self-contained: no
other skills, account, API key, or service are required to use the references. Load one to three
reference files by task; do not load the entire library into the model context.

These are independent summaries and adaptations of selected Apple guidance, not the full HIG.
Apple-specific conventions remain labelled; adaptations are marked `[translation]`. The reference
snapshot is dated 2026-09-14. Fetch a live source when currency or exact wording matters.

## The eight principles

Apple's statement of each principle, with its sub-rules. There is no one right way to apply them:
they are tools for weighing competing priorities, and the judgement stays with you.

- **Purpose — "Make something meaningful."**
  - Create value — keep asking, at every stage, what the product is for and whether the design serves that.
  - Keep focused — prioritise the few features that match how people want to use it, and make those truly great.
  - Find new ways to solve the problem — investigate existing solutions instead of re-creating them, and let the design show what sets this one apart.
- **Agency — "Let people do things their own way."**
  - Stay out of the way — get people directly to the task or the content; be unobtrusive and present when needed.
  - Give people the freedom to explore — no locked flows or modes, and any guided flow easy to skip or escape.
  - Help people recover from mistakes — build forgiveness in, keep people informed, and never let the unexpected cost them their time or work.
- **Responsibility — "Act in people's best interest."**
  - Be fully transparent about what the product does and why — clear intentions from the first interaction, a rationale with every permission request, and plain statements of what you collect and how you use it.
  - Keep people's information safe — collect only what the product needs to function, handle it with care, and anticipate misuse and harm.
- **Familiarity — "Build on what people know."**
  - Use concepts that people know — draw on both the real world and other software.
  - Keep visuals and interactions consistent — once an appearance or a behaviour is established, apply it throughout.
  - Provide clear feedback — show when controls are available, indicate when content changes, and use the platform's own patterns to raise alerts and offer choices.
- **Flexibility — "Adapt to diverse contexts and needs."**
  - Design for everyone — treat accessibility as a priority from the start, and take the range of people's experiences, perspectives and needs into account.
  - Preserve a person's context — keep content and controls in consistent, predictable positions and use natural animation to ease transitions.
  - Consider a variety of input methods — voice, touch, keyboard, pointer and more, so people can work the way that suits them.
  - Approach every platform with intention — give each one the same level of care instead of porting one design everywhere.
- **Simplicity — "Be clear and direct."**
  - Include just what's necessary — simplicity is not minimalism; keep the important things close by and let the others fall away.
  - Be concise — choose exactly the words you need to convey a concept or label a control.
  - Establish hierarchy — make form and function readily apparent, so people know where they are and what comes next.
- **Craft — "Care about every detail."**
  - Quality sets the tone — be deliberate with each decision and hold a bar for visuals, animation, wording and audio.
  - Experiment and iterate — prototype early, discard what does not work, and test in real-world settings.
  - Maintain your craft — shipping is not the finish line; keep the interface current and the quality bar high.
- **Delight — "Make it human."**
  - Identify the emotion you want to inspire — and let that feeling shape the design.
  - Create defining moments — find the character in interactions that already exist, from a button press to an error message.
  - Don't mistake delight for decoration — people are trying to accomplish a task, so no flourish may stand in front of it.
  - Consider the whole — delight emerges as the sum of the care spent on the other seven principles.

[HIG: design-principles]

## Working procedure

1. **State the purpose in two lines before drawing anything** — who this is for, what matters most
   to them, and what is deliberately left out. Everything later is checked against it, and the
   exclusions stay written down beside it so they do not creep back as small additions.

2. **Pick the level.** A quick check, or the hand-over of a finished change →
   `references/review-checklist.md`. A design decision, a trade-off between two defensible options,
   a critique that has to justify itself, or a brief for a UI builder → `references/principles.md`.
   A topic → the routing table below.

3. **Load one to three of the topic files at most.** Context is spent only where the topic matches;
   needing a fourth usually means the task should be split into two.

4. **When principles conflict, decide.** Record the trade-off in the design note, the pull request
   or the builder's brief in one line — which principle won, which was given up, and what is worse
   as a result. Never resolve a conflict by doing half of each.

5. **Before reporting a UI change done, run the quick twelve from the checklist against the rendered
   result, not the code.** Name the sizes, appearances and platforms you actually looked at, and say
   which checks you could not run rather than implying coverage.

6. **When a rule needs its full context, fetch the live page:** `python3 scripts/hig.py <slug>` from
   this skill's directory, or `python3 scripts/hig.py --list <section>` to find a slug. The helper
   needs Python 3.10+ and internet access; `curl` is a fallback if Python's request fails. It extracts
   text, omits images, and simplifies some document structures. Open the original page for visual
   examples. A fetch does not update the saved references. If network or execution is unavailable,
   use the local references, state their date, and do not imply that you checked the live source.

## Routing

The two general files answer *why* and *whether it holds up*; the ten topic files are loaded by task.

| Task | Load | Why |
|---|---|---|
| Reviewing a screen, flow or component; handing over a UI change | `references/review-checklist.md` | The quick twelve, then 7–10 pass/fail checks per principle with blocker / major / minor severities, plus how to report a finding, a hand-over check and the scope of a review. |
| A design decision, a trade-off, a critique, a brief for a builder | `references/principles.md` | The eight principles in depth with the WWDC26 reasoning, questions to ask per principle, seven named tensions with tie-breakers, and a three-line template for recording a decision. |
| Laying out a screen; navigation structure; containers; search; windows; scrolling | `references/layout-and-navigation.md` | Hierarchy, grouping, margins and safe areas, adaptivity driven by available space; tab bars, sidebars, split views, columns and outlines; lists, tables, collections, boxes, disclosures; search placement and behaviour; full screen; scroll rules. |
| A dialog, confirmation, destructive action, permission prompt, toast or notification | `references/modality-alerts-notifications.md` | When modality is justified; a decision list across alert / action sheet / sheet / popover / panel / inline; alert anatomy, copy and button order; dismissal that never loses work; notification urgency, permission and badges. |
| A type scale, a palette, a dark appearance, icons, images, how much brand | `references/typography-color-visuals.md` | Legibility floors and a reference type scale; semantic colour, the stated contrast numbers, appearance coverage; dark as its own design; depth and materials; icon and symbol sets; artwork; brand restraint; assembling the visual system. |
| Reporting status; animation; waiting and progress; launch; haptics and sound | `references/motion-feedback-loading.md` | Matching feedback to significance; motion with a job to do and reduced motion; designing the wait away, placeholders, determinate progress, cancel and pause; gauges and rating indicators; the first frame; haptics and audio as second channels. |
| Interface text; help and tips; first run; settings; accounts; ratings | `references/writing-help-onboarding-settings.md` | Voice, terminology and concision; labels, buttons and links; capitalisation; error and empty-state copy; help in context, tips, tooltips; skippable onboarding; what belongs in settings; account, sign-in and deletion rules; when to ask for a rating. |
| A form, wizard, checkout, editor, settings pane — any screen that collects values | `references/forms-and-data-entry.md` | Cutting fields before styling them; labels versus placeholders; which control fits which decision (toggle, radio, segmented, picker, slider, stepper, combo box); keyboards and handwriting; validation timing; sensitive input; never losing typed data; undo and redo. |
| Buttons, menus, toolbars, gestures, keyboard, pointer, focus, drag and drop | `references/actions-menus-and-input.md` | Hit targets, button labels, roles and states; menu labels, order, submenus, context and edit menus; toolbars and the desktop menu bar; standard gestures with visible alternatives; full keyboard operability; focus and selection; drag and drop; sharing; file commands. |
| Accessibility, inclusive language and imagery, right-to-left, privacy, an AI feature | `references/accessibility-inclusion-privacy.md` | Perception, operation and cognitive load; screen-reader semantics; inclusion and localisation; right-to-left mirroring rules; permission timing and purpose strings; credentials and accounts; generated content, disclosure, confidence, corrections and mistakes. |
| A dashboard, report, metric card, data grid or chart | `references/data-and-charts.md` | Chart versus table versus a single figure; marks, axes and honest scales; titles, units and legends; colour with a second channel; gauges; table structure, sorting and number alignment; non-visual equivalents; honest-numbers rules. |
| Choosing platforms; porting a design; a web app; an Electron or Capacitor shell | `references/platforms-and-web.md` | Five facts to read off a platform; phone, tablet, desktop, watch and TV, each with the three rules that break first on a port, then headset and folding devices in brief; window conventions; being switched away from; touch-to-desktop porting; web, installed-app and shell translation. |
| The exact wording of a rule, or a HIG page this skill distilled | `scripts/hig.py` | Fetches available HIG page text as Markdown — `python3 scripts/hig.py feedback` — and `--list components` enumerates slugs. |

## Briefing agents

- **Name this skill and the exact files in the brief.** An agent does not inherit the conversation,
  so a reading list it has to guess at is one it will replace with its own taste.
- **A builder gets `references/principles.md` plus the one or two topic files its work touches**, and
  the screen's purpose and recorded trade-offs restated in the brief.
- **A critic gets `references/review-checklist.md` plus the same topic files**, and reports findings
  as `screen or file:line — what fails — which check — severity — how to reproduce`.
- **Put the acceptance criteria in the brief:** which sizes, appearances, platforms and text sizes to
  check, and which of them are blockers.
- **Require checks against the rendered interface, and require the agent to say what it could not
  run.** A review of the diff finds naming problems, not contrast, focus order or truncation.

## Web and other platforms

- The eight principles apply everywhere; only their mechanics change with the platform.
- Where Apple says "the system", read "the platform's conventions" — for a web page that is the
  browser plus the host OS (Back and the URL as state, zoom, text selection, right-click, the OS
  text-size and appearance settings); for an Electron or Capacitor shell, the shell follows the host
  platform while the content inside it follows the rules in the other reference files.
- Per platform and per shell, the details are in `references/platforms-and-web.md`.

## Source tags

- `[HIG: slug]` — stated on that Human Interface Guidelines page,
  `https://developer.apple.com/design/human-interface-guidelines/<slug>`; several slugs mean the rule
  is drawn from all of them.
- `[WWDC26-250]` — stated in Apple's talk "Principles of great design", WWDC26 session 250,
  `https://developer.apple.com/videos/play/wwdc2026/250/`.
- `[translation]` — this skill's own guidance: an Apple rule carried to the web, a shell or another
  platform, or an inference the sources do not state. It is never Apple's, and never presented as
  Apple's.

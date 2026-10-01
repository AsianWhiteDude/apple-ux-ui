# The eight principles in depth

Apple states eight design principles — Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight — and says there is no one right way to apply them: they are tools for weighing competing priorities on the way to a good design. This file is the "why" under every other file in the skill. Load it for a design decision, a trade-off between two defensible options, a critique that has to justify itself, or a brief handed to a UI builder; load `references/review-checklist.md` instead when all you need is a pass/fail check on a finished screen. Each principle below carries Apple's statement, the sub-rules restated as imperatives, the reasoning from the WWDC26 talk, and questions that turn the principle into a check on a concrete design. Every rule anywhere in this skill should be traceable to one of these eight. A tag on a single bullet governs that bullet: the tag line closing a list covers only the bullets that carry no tag of their own, so a `[translation]` bullet inside an otherwise sourced list is this skill's own inference and never Apple's. [HIG: design-principles] [WWDC26-250]

## 1. Purpose — "Make something meaningful."

Design starts with intention: work out what matters most to the people you are designing for, make those things great, and the rest of the design has something to answer to. [HIG: design-principles]

- **Design with intention: settle what matters most to people before settling how anything looks or behaves.** Appearance and behaviour are consequences of that decision, not substitutes for it. [WWDC26-250]
- **Settle whether what you are making has purpose before drawing a sketch or writing a line of code.** That question comes before the first screen, not after it. [WWDC26-250]
- **Write that purpose down in two lines — who this is for, what matters most to them, what is deliberately left out.** Everything later gets checked against it. The written artefact is this skill's own device for keeping the check available to the next person; the sources ask for the thinking, not for a document. [translation]
- **Ask at every stage what the product is for and whether the design still serves that.** Purpose is not a kickoff exercise; it is the recurring question that keeps a feature list honest.
- **Prioritise the few features that match how people actually want to use the product, and make those truly great.** Spreading effort evenly across everything produces a product with no clear use.
- **Treat each feature as a request for someone's time, attention and trust.** Those are things you cannot afford to waste, so a feature that asks for them must give back more than it takes. [WWDC26-250]
- **Decide explicitly what not to include.** Choosing what to build is largely a matter of deciding what to leave out, so the exclusion is a design decision in its own right. [WWDC26-250]
- **Keep those exclusions written down beside the purpose** so they do not creep back in as "small additions" at the next review. [translation]
- **Investigate existing solutions and do not re-create them.** Name what sets this product apart and let the design express that difference rather than a copy of what already exists.

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- What is this screen for, in one sentence, and for whom?
- Which element on it carries the purpose? If that element were removed, would the screen still have a reason to exist?
- What does this feature ask of the person — time, attention, trust — and what does it return?
- What did we decide not to build here, and where is that written down?
- Does this already exist, in this product or in software the person already uses? What do we add by doing it again?
- If only one feature of this product could survive, which is it — and does this work make it better or only wider?

[HIG: design-principles] [WWDC26-250]

## 2. Agency — "Let people do things their own way."

An interface is there so people can get their own work done: leave them free to act, keep them informed, and make mistakes cheap to undo. [HIG: design-principles]

- **Get people to the task or the content directly.** The best designs are unobtrusive and present when needed, so remove anything that stands between arrival and the first useful action.
- **Offer choices instead of one predetermined path.** People are far more engaged when they control their own route; let them dive in and explore at their own pace. [WWDC26-250]
- **Do not lock people into a flow or a mode.** Features should be reachable without completing a sequence first.
- **Make any guided flow easy to skip or escape** so a person can reach the main experience quickly.
- **Keep people informed about what the interface is doing on their behalf,** including work that continues in the background.
- **Build forgiveness in, and make it cheap.** Undo an action or return to a previous state; recovering from the unexpected must not cost a person their time or their work.
- **Design for the accidental case as the normal case.** People send, change and delete things by accident constantly; the design question is not whether that happens but what it costs when it does. [WWDC26-250]
- **Let forgiveness be visible before the action, not only after it.** Confidence that anything can be recovered is what makes people willing to explore, and that confidence has to be legible in the interface. [WWDC26-250]
- **Double-check a destructive action before it happens** — confirm it is what the person actually means to do. [WWDC26-250] How that confirmation is worded and built is in `references/modality-alerts-notifications.md`.
- **Interrupt only for a big mistake about to happen.** Interruptions spent on status or encouragement use up the attention you will need for the one that matters. [WWDC26-250]

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- Can a person reach the main task without passing through anything first?
- What is the most destructive thing possible on this screen, and exactly how is it reversed?
- Is there any state here that cannot be left? Where is the way out, and is it visible?
- Does this interruption prevent a big mistake, or does it only report something?
- After an action completes, does the person know what happened and where the result went?
- If a person changes their mind mid-flow, what have they lost?

[HIG: design-principles] [WWDC26-250]

Undo, redo and destructive-action confirmation as controls are detailed in `references/forms-and-data-entry.md` and `references/modality-alerts-notifications.md`.

## 3. Responsibility — "Act in people's best interest."

The work has real effects on people's lives; trust is earned by prioritising safety and privacy and by being transparent about what the product does and why. [HIG: design-principles]

- **Make the product's intentions clear from the first interaction.** The first screen is where the relationship starts, so it should say what this is and what it will do.
- **Ask for a permission at the moment the feature needs it, with the reason attached.** A prompt thrown at launch, before anyone knows what the product does, is the interface version of demanding a phone number from a stranger. [WWDC26-250]
- **Collect only what the product needs to function, and say what each item is for.** "Privacy is a human right"; volume of data collected is not a measure of a relationship.
- **Handle collected data with care and anticipate misuse.** Put protections in place against abuse and unintended consequences, not only against error.
- **Protect the people affected by the product, not only the people using it.** A feature reaches bystanders too — the person on the other end of a message, someone sharing the account, someone in the photo. [WWDC26-250]
- **Run three questions over every feature: how could this be misused, who would be harmed, how do we prevent it.** Ask them of the feature working as designed, not only of it failing. [WWDC26-250]
- **Expect an intelligent feature to produce something inaccurate or unexpected, and put something between that output and the person.** Previews, confirmations and disclaimers are the usual safeguards; an allergy logged in a recipe app is the case to keep in mind — a plausible suggestion can cause real harm. [WWDC26-250]
- **Remove a feature when the risk to people outweighs its value.** Cutting it is a legitimate design outcome, not a failure to solve the problem. [WWDC26-250]

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- What does this screen collect, and would we be comfortable saying out loud, at that moment, what it is for?
- What happens when the person declines? Does the product still do something useful?
- Who is harmed if this feature works exactly as intended, in the hands of the wrong person?
- What is the worst output this model could produce here, and what stands between it and a real-world consequence?
- Is anything here designed to make the trusting choice easier than the private one?
- Could this feature be turned on someone who is not using the product, and what limits that?

[HIG: design-principles] [WWDC26-250]

Privacy, transparency and generated-content rules as practice live in `references/accessibility-inclusion-privacy.md`.

## 4. Familiarity — "Build on what people know."

People arrive with a lifetime of knowledge about the physical world and other software; grounding a design in established patterns and applying them consistently makes it feel immediately usable. [HIG: design-principles]

- **Draw on concepts people already hold, from the real world and from other software.** Familiarity is borrowed understanding; it costs the person nothing to use.
- **Ground the design in established physical and digital patterns so first use feels like arriving somewhere known.** Familiarity is not nostalgia; it is the shortest path from opening the product to being competent in it.
- **Use metaphor, and keep it between too literal and too abstract.** A good metaphor lets people predict what a thing will do; too literal and they cannot tell what it represents, too abstract and the idea does not land. [WWDC26-250]
- **Do not give a known symbol a new meaning.** A trash can that does not delete, or a redrawn delete icon that loses recognition, breaks the one thing the symbol was worth. [WWDC26-250]
- **For common actions, use the metaphor people already know and make it do what they expect.** Reserve invention for what is genuinely new about the product. [WWDC26-250]
- **Make things that look the same behave the same.** Three identical buttons that navigate, toggle and open a dialog leave no pattern to learn.
- **Keep an element in the same place across screens and devices.** Constant placement removes a decision every time; people stop thinking about where to look. [WWDC26-250]
- **Once an appearance or a behaviour is established, apply it throughout.** Consistency is what makes the next, unseen interaction predictable.
- **Show when a control is available and indicate when content changes.** Feedback is part of familiarity: people stay informed and in control because signals mean the same thing every time.
- **Use the platform's established patterns to raise alerts and offer choices** (on Apple platforms, the system alert and its equivalents; on any platform, that platform's own convention) rather than a bespoke dialog of your own design.

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- What does this control look like it will do, to someone who has never used the product?
- Is there an established pattern for this, and what do we gain by departing from it?
- Does anything that looks alike here behave differently?
- Is this icon's meaning the one it carries in other software?
- After a change, what tells the person something changed — and would the same signal be used elsewhere for the same kind of change?

[HIG: design-principles] [WWDC26-250]

## 5. Flexibility — "Adapt to diverse contexts and needs."

Use is as varied as the people doing it, and a design that admits this is one more people feel invited into. [HIG: design-principles]

- **Treat accessibility as a priority from the start.** Designing inclusively reaches the broadest audience and produces a better experience for everyone, not a parallel one for some.
- **Take the range of people's experiences, perspectives and needs into account deliberately.** Get curious about the audience: age, languages spoken, novice or expert, whether they rely on accessibility features. You will not solve for everyone on day one, but you can name who you considered. [WWDC26-250]
- **Be mindful of experiences other than your own.** The team's devices, habits, language and abilities are not the audience's; unstated assumptions about them get built into the interface.
- **Design for the contexts, not just the device.** The same task changes shape at home, on a run, or hands-free while driving; list the contexts the interface must survive and check it in each. [WWDC26-250]
- **Support as many input methods as the platform offers** — voice, touch, keyboard, pointer and more — so people can work the way that suits them.
- **Keep content and controls in consistent, predictable positions as the layout adapts,** so a person's context survives a change of size, orientation or platform.
- **Use natural animation to carry people across a transition** rather than cutting between states and making them re-orient.
- **Give every platform you support the same level of care, and let each one use what makes it distinct.** A single layout ported everywhere feels at home nowhere.
- **Let people personalise what you cannot decide for them.** Where no single arrangement works for everyone, allow controls to be rearranged or unused ones hidden. Flexibility is an investment; it is what proves the design had them in mind. [WWDC26-250]

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- Which three contexts must this work in, and has it been tried in each?
- Does it work by keyboard alone? By voice? With one hand? With the largest text setting?
- When the window halves in width or the device rotates, do the primary controls stay where the person last saw them?
- Who is excluded by the way this asks for input, and is that exclusion necessary?
- Is there a choice here we are making for everyone that people should be making for themselves?

[HIG: design-principles] [WWDC26-250]

Per-platform expectations and the web translation live in `references/platforms-and-web.md`; the accessibility practice in `references/accessibility-inclusion-privacy.md`.

## 6. Simplicity — "Be clear and direct."

Take out what is unnecessary until each remaining element has earned its place; a logical structure that is easy to move through is what makes work fast. [HIG: design-principles]

- **Include just what is necessary — simplicity is not minimalism.** Keep the important things close by and let the others fall away; burying everything in one place looks minimal and behaves worse. [WWDC26-250]
- **Reduce steps, not information.** A concise interface respects time: fewer steps to the outcome, no redundancy, no detour. [WWDC26-250]
- **Use plain, natural language and strip the jargon.** The simplest phrasing tends to travel furthest and help most, so pick precisely the words a concept or a control label needs — no more.
- **Establish hierarchy with order, spacing and contrast.** When the hierarchy is right, the most important thing on the screen is the most obvious thing on the screen. [WWDC26-250]
- **Organise logically and keep navigation straightforward.** Ease comes from a structure people can hold in their head, not from fewer visible things.
- **Make form and function apparent: prefer recognisable controls and a consistent structure** that tells people where they are and what comes next.
- **Let the screen answer, without being asked, what deserves attention, what is interactive, and how to act on it.** A clear design answers all three; if one has no answer, the screen is not clear yet. [WWDC26-250]
- **Add context when a decision needs it.** A play/pause control that also shows position and time remaining is simpler than one that does not, because the person can decide without leaving. Simple means exactly enough, not as little as possible. [WWDC26-250]
- **Distil information to its essence.** Complex data may read better as a graphic; long content may read better summarised, leaving people free to attend to the part they came for. [WWDC26-250]
- **Make every element justify itself.** If it does not clarify the point, it is competing with the thing that does.

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- What is the one thing this screen wants the person to notice, and is it visibly first?
- How many steps does the main task take, and which of them exists only for us?
- Which element could be removed with nothing lost? Remove it.
- Is anything hidden here purely to keep the surface clean, at the cost of people finding it?
- Is there information missing that the person needs in order to decide without navigating away?

[HIG: design-principles] [WWDC26-250]

Wording rules as practice live in `references/writing-help-onboarding-settings.md`; hierarchy and structure in `references/layout-and-navigation.md`.

## 7. Craft — "Care about every detail."

The design reflects how much you care; quality sets the tone, and the work of getting there is iteration and maintenance rather than a final polish pass. [HIG: design-principles]

- **Be deliberate in every decision, and hold a bar for visuals, animation, wording and audio.** Quality is read from the details, and it is read quickly.
- **Fix the four tells of rushed software: a delay after a tap with no response, jittery scrolling, misaligned elements, and a layout that breaks on rotation or resize.** People read these as fragility, and fragility makes them doubt the results the product gives them. [WWDC26-250]
- **Start from good materials: type that holds up across devices, colour that adapts between light and dark surroundings, clear graphics and iconography, and animation that answers immediately and naturally.** Craft is built out of these the way a physical object is built out of its materials; a weak one cannot be polished away later. [WWDC26-250]
- **Judge the interface the way people judge a physical object.** A door that will not close properly, a shirt that unravels in the wash — shortcuts are obvious, and the software equivalents are read just as fast. A meticulously made design does the opposite: it inspires confidence in the results the product produces. [WWDC26-250]
- **Prototype early, try alternatives, and discard what does not work.** Set a high bar per feature, refine it, and try again; craft comes from iteration, and iteration needs time in the plan.
- **Test in real-world settings, not on the demo path,** and hold the result to durability, reliability and performance.
- **Treat shipping as the middle of the work, not the end.** Keep the interface abreast of what the platform can now do and of how it now looks, and hold the same bar while doing it: design is an ongoing commitment.
- **When new platform features or hardware appear, examine whether they belong in this experience.** Evolving with the platform is what gives a design longevity and makes people feel supported. [WWDC26-250]

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- Does every tap get a response before the person wonders whether it registered?
- Does the layout survive rotation, a resize to half width, and the largest text setting?
- Is anything misaligned, inconsistently spaced, or off by a pixel in a place people look often?
- What was prototyped and thrown away here? If nothing, has the first idea been tested at all?
- What in this interface is now behind the platform, and when does it get revisited?

[HIG: design-principles] [WWDC26-250]

Response, motion and loading practice lives in `references/motion-feedback-loading.md`; materials in `references/typography-color-visuals.md`.

## 8. Delight — "Make it human."

What stays with people is how using the product felt. Decide which emotions belong in this experience, then deliver them in a way that is satisfying and enriching rather than decorative. [HIG: design-principles]

- **Name the emotion the experience should produce, and let it shape the design.** Energised, calm, confident, thrilled — software does not all feel the same, and the target feeling decides many small choices. [WWDC26-250]
- **Choose the emotions that are right for this experience, not emotions that are pleasant in general.** A meditation tool that energises and a fitness tool that soothes are both mis-tuned, however well made.
- **Find the character in moments that already exist.** A button press, an empty state, an error message: each is a chance to show what the product stands for, without adding anything new to the screen.
- **Do not add delight at the end.** Confetti and flourishes tacked on after the fact are decoration, not delight; the feeling comes from the whole experience being considered. [WWDC26-250]
- **Never let a flourish stand between a person and their task.** People are here to accomplish something; delight pursued for its own sake gets in the way of the core purpose.
- **Choose the register deliberately and apply it consistently** — some designs want a restrained practical touch, others some whimsy; experiment to find the balance rather than defaulting to either.
- **Read delight as a result, not a feature.** It is the sum of the care already spent elsewhere — people free to act, safe to explore, working with patterns they recognise, on something they could shape to themselves. Get the other seven principles right and the product feels delightful without a dedicated feature for it. [WWDC26-250]

[HIG: design-principles] [WWDC26-250]

### Questions to ask
- In one word, how should a person feel while using this? Does anything on the screen contradict it?
- Which existing moment in this flow is worth giving character to, and does that cost the person anything?
- Would removing this flourish make the task faster? If yes, why is it here?
- Does the tone here match the tone three screens back?
- If the animation and the illustrations were stripped out, would the experience still be good?
- Is this product's delight the sum of its considered decisions, or a layer applied over a mediocre flow?

[HIG: design-principles] [WWDC26-250]

## Tensions

There is no formula that combines the principles into a guaranteed answer, and leaning into one will sometimes feel like compromising another; they exist to help weigh competing priorities, and the judgement stays with the designer. So decide, name what was given up, and move on — do not split the difference silently. The pairs below are drawn from the two sources; where a bullet proposes a way to break the tie, that part is this skill's own reasoning and is tagged as such. [HIG: design-principles] [WWDC26-250]

- **Purpose against Flexibility.** Every additional context, input method and personalisation option is real work and more surface to keep crafted; supporting everything dilutes the few things meant to be great. Flexibility is an investment — spend it where people's contexts actually differ, and let Purpose decide which contexts are in scope. [HIG: design-principles] [WWDC26-250] [translation]
- **Simplicity against Agency.** Choices are how people take control, and each choice is another element on the screen. Keep the choice that changes someone's outcome; move the rest to where they are looked for, and remember that hiding function to look minimal is not simplicity. [HIG: design-principles] [WWDC26-250] [translation]
- **Delight against Simplicity.** Character is worth screen time only while it does not obstruct the task; when a moment of delight adds a step or a wait, Simplicity wins and the character moves to a moment that was already there. [HIG: design-principles] [translation]
- **Familiarity against Purpose and novelty.** Purpose asks for new ways to solve the problem; Familiarity asks you not to reinvent what people already know. The workable line from the talk: use the known metaphor for common actions, and spend the novelty on what is genuinely distinct about the product. [HIG: design-principles] [WWDC26-250]
- **Responsibility against Delight and engagement.** Engagement that comes from agency is earned; engagement that comes from interruptions, pressure or data you did not need is borrowed against trust. When a feature's risk outweighs its value, removing it is the answer even if it was the memorable part. [HIG: design-principles] [WWDC26-250]
- **Craft against shipping.** Quality takes time and craft comes from iteration, but shipping is not the finish line either. Ship the smaller thing at full quality rather than the larger thing rushed, and put the remainder on the maintenance path. [HIG: design-principles] [WWDC26-250] [translation]
- **Agency against Responsibility.** Freedom to act and protection from harm pull apart exactly where an action is irreversible or affects other people. Default to freedom, and reserve the interruption for the big mistake — a real loss, a safety risk, or an effect the person cannot take back. [HIG: design-principles] [WWDC26-250] [translation]

### How to weigh one
- Restate the purpose of the screen first. Simplicity is stripping away what does not serve that core purpose, and delight pursued for its own sake must not get in the way of it — so a Simplicity or Delight move that obstructs the purpose is already answered. Beyond those two, neither source ranks the principles: they are tools for weighing competing priorities, and the judgement is yours. [HIG: design-principles] [WWDC26-250]
- The four steps below are this skill's own tie-breakers, not an Apple ranking of the eight. [translation]
- Check the cost of being wrong: a Responsibility or Agency failure costs a person data, work or trust, while a Simplicity or Delight failure costs a little friction. Let the asymmetric cost break the tie. [translation]
- Prefer the option that stays reversible, so the decision can be revisited against real use instead of argument. [translation]
- State the trade-off in one clause before building it. If it cannot be stated that way, the conflict is not understood yet and the design is not ready. [translation]
- Never resolve a conflict by doing half of each. Two half-measures cost the surface of both options and deliver the benefit of neither. [translation]

## Recording a decision

When principles conflict, write the outcome in the design note, the pull request or the builder's brief. Three lines, in the design's own vocabulary, so the next person does not re-open a settled question: [translation]

```
Decision: <what we do> — <screen / component / flow>.
Principle: <principle that won> over <principle given up>, because <reason in one clause>.
Cost and revisit: <what is worse as a result> — revisit when <observable condition>.
```

- **Name the principle that lost, not only the one that won.** A decision recorded as "we chose simplicity" cannot be checked later; "simplicity over agency, the per-item override is gone" can. [translation]
- **State the revisit condition as something observable** — a support pattern, a usage number, a platform capability arriving — so the trade-off is a decision rather than a permanent verdict. Design is an ongoing commitment, and a recorded trade-off is what makes revisiting it cheap. [HIG: design-principles] [translation]
- **Keep the record next to the work,** in the project's decisions file or the brief for the agent that will build it. A trade-off nobody can find gets re-litigated at the next review. [translation]

Filled in, for a bulk-delete flow that lost its per-item confirmation: [translation]

```
Decision: delete selected items in one action, no per-item confirmation — Library, bulk selection.
Principle: Simplicity over Agency's caution, because confirming twenty items costs more than the mistake does.
Cost and revisit: an accidental bulk delete is possible — undo covers it for 30 days; revisit if restores from undo become common.
```

## Deliberately omitted

- Page furniture from `design-principles`: the change log, the Resources link block, and the page's own framing sentences — no rule to distil from them.
- The presenters' staged dialogue in the transcript (the hand-off joke, the phone-number skit, the on-stage mistake) — illustration rather than guidance; the rules those bits illustrate are kept under Agency, Responsibility and Familiarity.
- "Reliable and secure SDKs" as a craft ingredient — an engineering-stack requirement with no interface rule a reviewer could check.
- Device-specific illustrations (AirPods and a watch on a run, hands-free driving, the Mac window control at the top left, quick touch on a phone versus deep pointer workflows on a desktop) — kept only as generic examples of context, placement and input; the per-platform guidance itself belongs to `references/platforms-and-web.md`.
- The talk's closing invitation to read the Human Interface Guidelines — not a design rule.

## Sources

- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- WWDC26 session 250, "Principles of great design" (transcript) — https://developer.apple.com/videos/play/wwdc2026/250

# Review checklist

This file is the pass/fail list a critic or a self-review runs over a finished screen, flow or component, and the hand-over check before a UI change is reported as done. Load it for any review, however small; load `references/principles.md` instead when the question is which design to choose rather than whether this one holds up. The checks are grouped by the eight principles — Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight — so that every finding names the principle it violates and each check reads as one instance of that principle rather than as generic UX advice. The checks that most often reach blocker severity belong to Agency (people lose work or cannot escape), Flexibility (people cannot perceive or operate the interface) and Responsibility (people are misled or put at risk). Run every check against the interface as it renders, not against the code that produced it.

### Severity

- **blocker** — a person loses work, cannot recover, cannot perceive or operate the interface, is misled about a consequence, or is exposed to real-world harm.
- **major** — a principle is clearly violated in a main flow: the path works, but the design is wrong where it matters.
- **minor** — polish; a review is accepted with minors outstanding as long as they are listed. `[translation]`

## Quick twelve

Run these twelve on every change, including a one-screen one. They catch most defects and take minutes.

1. **Name the purpose of the change in one line and check that every element on screen serves it.** Fail: major. `[HIG: design-principles]` `[WWDC26-250]`
2. **Check that the most likely action is the most obvious one and reads as a verb.** Pass when one — at most two — prominent action per view, labelled with what it does. Fail: major. `[HIG: buttons, layout]`
3. **Try to lose data: type, navigate away, cancel, dismiss, fail a request.** Pass when nothing typed disappears silently and an irreversible destructive action is confirmed first. Fail: blocker. `[HIG: modality, alerts, entering-data]`
4. **Read every error message.** Pass when it names what happened and what to do next, appears next to the problem, and blames nobody. Fail: major. `[HIG: writing]`
5. **Operate the whole screen with the keyboard alone, then with a screen reader.** Pass when every control is reachable with the keyboard and named for the screen reader `[HIG: accessibility]`, and when the current stop is visibly focused `[translation]`. Fail: blocker.
6. **Measure contrast and remove colour.** Pass when text up to 17 pt reaches 4.5:1 (3:1 at 18 pt or bold) and no state, status or category is carried by colour alone. Fail: blocker. `[HIG: accessibility, color]`
7. **Raise text to the largest accessibility size.** Pass when nothing clips, overlaps or truncates away meaning, and the hierarchy still reads. Fail: blocker. `[HIG: accessibility, typography, layout]`
8. **View the screen in light, dark and increased-contrast appearances.** Pass when every colour still separates content from background in all three. Fail: major. `[HIG: color]`
9. **Load the screen on a slow connection.** Pass when something appears immediately, the rest of the interface stays usable, and progress is shown when the wait is real. Fail: major. `[HIG: loading]`
10. **Count the modal layers and find the way out of each.** Pass when modality earns its place, the modal task is short and un-nested, its title names the task, dismissal is obvious, and no modal sits on top of another. Fail: major. `[HIG: modality]`
11. **Trigger every new permission request.** Pass when it fires at the moment the feature needs it and its copy says specifically why. Fail: major; blocker if the copy or the screen before it misleads. `[HIG: privacy]` `[WWDC26-250]`
12. **Turn on reduce motion, then interrupt every animation.** Pass when motion is reduced or replaced, and nothing makes a person wait for an animation to end. Fail: major. `[HIG: motion, accessibility]`

## Purpose

*«Make something meaningful» — intention, focus, and deciding what not to build. These checks ask whether the screen deserves to exist in this form.* `[HIG: design-principles]`

- **Look for the written purpose of the screen.** Pass when one line names who it is for and what matters most there. Fail: major. `[HIG: design-principles]`
- **Look for what was deliberately left out.** Pass when the change records at least one thing not included and why. Fail: minor. `[WWDC26-250]`
- **Price each added feature in the person's time, attention and trust.** Pass when what it returns is worth more than what it asks. Fail: major. `[WWDC26-250]`
- **Compare prominence with importance.** Pass when the features the product exists for are the ones given the best position and the most work. Fail: major. `[HIG: design-principles]`
- **Check every element against the purpose.** Pass when removing an element would cost a person something they need. Fail: major. `[HIG: design-principles]` `[WWDC26-250]`
- **Check that an existing solution was not re-created.** Pass when the design reuses the established pattern or states what it does differently and why. Fail: minor. `[HIG: design-principles]`
- **Look for data that would read better distilled.** Pass when dense numbers are summarised or drawn when that is what the person actually needs. Fail: minor. `[WWDC26-250]`

## Agency

*«Let people do things their own way» — freedom to act, knowing what is happening, and easy recovery from mistakes.* `[HIG: design-principles]`

- **Walk every guided flow looking for the exit.** Pass when each step can be skipped or escaped into the main experience. Fail: major; blocker when there is no way out at all. `[HIG: design-principles, onboarding]`
- **Take an uncommon, irreversible, destructive action.** Pass when it is confirmed first and the confirmation names the consequence. Fail: blocker. `[HIG: alerts, feedback]` `[WWDC26-250]`
- **Take a common, expected, recoverable deletion.** Pass when it happens without a warning, because the loss is what the person asked for. Fail: minor. `[HIG: alerts, feedback]`
- **Undo the last few actions.** Pass when undo repeats without an arbitrary cap, names its action in the label, groups incremental adjustments sensibly, and scrolls or highlights so the restored result is visible. Fail: major. `[HIG: undo-and-redo]`
- **Count the interruptions in the flow.** Pass when the interface interrupts only before a mistake a person would regret, never to report status, news or an unactionable message. Fail: major. `[HIG: alerts, feedback]` `[WWDC26-250]`
- **Reach the main content from a cold start.** Pass when defaults let someone begin immediately, non-essential setup and non-essential permissions are postponed, teaching happens in context, a skipped tutorial stays findable later, and no non-essential setup step or licence text stands between launch and value. Fail: major. `[HIG: onboarding, settings, privacy]`
- **Try to move around out of order.** Pass when features are reachable without following one prescribed path. Fail: major. `[HIG: design-principles]`
- **Wait out anything that dismisses itself.** Pass when a view or control that auto-dismisses can also be dismissed — and its information recovered — by an explicit action. Fail: major. `[HIG: accessibility]`
- **Enter a wrong value, then a right one.** Pass when the problem is reported as it is entered, next to the field, and a required-data gate stays visibly closed until the data is there. Fail: major. `[HIG: entering-data, writing]`
- **Look for a rating, review or purchase prompt.** Pass when none appears before the person has had a chance to get something out of the product. Fail: major. `[HIG: onboarding]`

## Responsibility

*«Act in people's best interest» — transparency about what the product does and why, and protection of what people entrust to it.* `[HIG: design-principles]`

- **Trigger each permission request and read its copy.** Pass when it fires at the moment of need as one active, specific sentence about what the data is for. Fail: major. `[HIG: privacy]` `[WWDC26-250]`
- **Compare what is requested with what the feature needs.** Pass when nothing extra is asked for and the request is as narrow as the feature allows. Fail: major. `[HIG: privacy]`
- **Inspect any screen shown before a system permission request.** Pass when it has exactly one button, that button obviously opens the real request, and it offers no incentive, no imitation of the request and no other exit. Fail: blocker. `[HIG: privacy]`
- **Deny every permission and keep using the feature.** Pass when the interface says what is unavailable and keeps working in a reduced form instead of dead-ending. Fail: major. `[translation]`
- **Follow a password or secret through the interface.** Pass when entry is obscured, password fields are never prefilled, and nothing sensitive is stored or logged in the clear. Fail: blocker. `[HIG: entering-data, privacy]`
- **Check the authentication path.** Pass when it uses platform-provided sign-in, passkeys or credential autofill rather than a scheme of its own, and does not rest on a password alone. Fail: major. `[HIG: privacy]`
- **Ask how the feature could be misused, who would be harmed, and what prevents it.** Pass when the answers exist and the safeguard is in the design — or the feature was cut. Fail: blocker when real-world harm is possible. `[WWDC26-250]`
- **Make a generated or inferred result act on something that matters.** Pass when a preview, confirmation or stated limitation stands between an unreliable result and its consequence, and constraints a person has already given are honoured. Fail: blocker. `[WWDC26-250]`
- **Read the wording of every warning.** Pass when it states the actual consequence in a neutral tone, without accusation and without softening the severity. Fail: major. `[HIG: alerts]`

## Familiarity

*«Build on what people know» — established patterns, consistent behaviour and clear feedback.* `[HIG: design-principles]`

- **Identify each component as standard or custom.** Pass when alerts, choices and other system patterns use the platform's own components instead of look-alikes. Fail: major. `[HIG: design-principles, modality]`
- **Find two elements that look alike and use both.** Pass when they behave alike; things that look the same must do the same kind of thing. Fail: major. `[WWDC26-250]`
- **Compare the position of recurring controls across screens.** Pass when the same action sits in the same place everywhere, so nobody has to look for it twice. Fail: major. `[HIG: design-principles]` `[WWDC26-250]`
- **Check every metaphor and icon against its conventional meaning.** Pass when a familiar symbol does its familiar thing — a trash can deletes — and no established symbol is re-purposed or redrawn past recognition. Fail: major. `[HIG: buttons]` `[WWDC26-250]`
- **Change something and watch for the signal.** Pass when availability, state changes and content updates are all visible without the person asking, with status shown near the thing it describes. Fail: major. `[HIG: design-principles, feedback]`
- **Ask for something the interface cannot do.** Pass when it says the command cannot run and why, instead of failing silently. Fail: major. `[HIG: feedback]`
- **Receive one piece of feedback with the screen out of view and the sound off.** Pass when important feedback exists in more than one channel — text, colour, sound, haptics — not one only. Fail: blocker when the information is otherwise unavailable. `[HIG: feedback, accessibility]`
- **Collect the words used for one concept across the flow.** Pass when the term never changes, multi-step flows label their steps consistently from start to done, and one capitalisation rule is applied per kind of element. Fail: minor. `[HIG: writing, alerts]`
- **Press and hold each custom control.** Pass when it has a pressed state `[HIG: buttons]` and shows whether it is currently available `[HIG: design-principles]`, plus a focused state wherever focus exists `[translation]`, so it never feels dead. Fail: major.
- **Use the platform's standard gestures and shortcuts inside the change.** Pass when none has been redefined to mean something else. Fail: major. `[HIG: undo-and-redo, accessibility]`

## Flexibility

*«Adapt to diverse contexts and needs» — design for everyone, preserve context, support every input method.* `[HIG: design-principles]`

- **Resize to the narrowest and widest layouts the interface can appear in.** Pass when nothing clips, overlaps or strands a control offscreen at either end. Fail: major. `[HIG: layout]`
- **Check what drives the layout.** Pass when it responds to the space actually available (Apple's size classes; breakpoints elsewhere) rather than to a device name or an orientation. Fail: major. `[HIG: layout]`
- **Shrink the window and count the features.** Pass when the same functionality remains reachable and only the amount visible at once changes. Fail: major. `[HIG: layout]`
- **Scale text to the largest accessibility size (about 200 percent; 140 percent on watch-sized screens).** Pass when adjacent views stack, rows grow, meaningful icons grow with the text, primary elements stay near the top and no meaning is truncated away. Fail: blocker. `[HIG: accessibility, typography]`
- **Perform every gesture-only action another way.** Pass when core functionality is reachable through more than one kind of physical interaction, and frequent actions need only the simplest gesture. Fail: blocker. `[HIG: accessibility]`
- **Complete the main task with the keyboard alone.** Pass when the task can be finished from the keyboard and no system-defined shortcut is overridden `[HIG: accessibility]`, and when focus stays visible, follows the order of the layout and is never trapped `[translation]`. Fail: blocker.
- **Play any media with the sound off.** Pass when captions, subtitles or a transcript carry the spoken and audio-only information. Fail: blocker. `[HIG: accessibility]`
- **Rotate, resize or move between platforms mid-task.** Pass when content and controls stay in predictable places and transitions animate rather than jump. Fail: major. `[HIG: design-principles, layout]`
- **Look for the controls people would want rearranged or hidden.** Pass when a layout that cannot suit everyone is personalisable rather than imposed. Fail: minor. `[WWDC26-250]`
- **Review who is missing.** Pass when the change was weighed against a range of ages, languages, expertise levels and assistive-technology users, not one imagined person. Fail: major. `[HIG: design-principles, accessibility]` `[WWDC26-250]`

## Simplicity

*«Be clear and direct» — include just what is necessary, be concise, establish hierarchy.* `[HIG: design-principles]`

- **Count the choices visible at once.** Pass when everything present is needed now and the rest sits behind disclosure, a menu or a nested view. Fail: major. `[HIG: layout, design-principles]`
- **Look at the screen for one second and name the most important thing.** Pass when order, spacing and contrast make it unmistakable. Fail: major. `[HIG: layout]` `[WWDC26-250]`
- **Check grouping and alignment against the real relationships.** Pass when related items are grouped by spacing, a container or a separator, and indentation marks what is subordinate. Fail: minor. `[HIG: layout]`
- **Cut the words.** Pass when nothing repeats, no jargon survives, "we" is gone from error copy, and possessives are dropped where context already carries them. Fail: minor. `[HIG: writing]` `[WWDC26-250]`
- **Count the steps to the outcome.** Pass when no step could be removed, defaulted or merged. Fail: major. `[HIG: entering-data]` `[WWDC26-250]`
- **Count the data the form asks for.** Pass when anything obtainable from the system or an earlier answer is prefilled, lists of options replace free typing wherever they can, and pasting or dragging a value in works. Fail: major. `[HIG: entering-data]`
- **Count the typefaces and the prominent buttons.** Pass when typefaces are few and prominent buttons number one or two per view, with style rather than size marking the preferred option. Fail: minor. `[HIG: typography, buttons]`
- **Read every setting.** Pass when each is a choice someone must actually make, defaults suit most people, no system-wide setting is duplicated, task-specific options live in the task itself, and settings open the way the platform's people expect. Fail: major. `[HIG: settings]`
- **Ask what is missing that would make the screen simpler.** Pass when the context needed to decide — elapsed time, remaining amount, current state — is present, even if that means adding an element. Fail: major. `[WWDC26-250]`
- **Look for functionality buried to keep the screen bare.** Pass when what people need is findable without hunting; minimal is not the same as simple. Fail: major. `[WWDC26-250]`

## Craft

*«Care about every detail» — quality of materials, iteration, and keeping the work current.* `[HIG: design-principles]`

- **Exercise every interactive element through all its states.** Pass when default, pressed and in-progress states are all defined and distinct `[HIG: buttons]` and an unavailable control reads as unavailable `[HIG: design-principles]` — plus focused and hover states wherever keyboard focus or a pointer exists `[translation]`. Fail: major.
- **Measure the hit regions and the gaps between them.** Pass when every interactive element has a hit region of at least 44×44 pt — 60×60 pt in visionOS — and spacing around it of roughly 12 pt for a bordered control, about 24 pt for one without, so neighbours are not hit by accident. A control drawn smaller than the bar (a macOS 28×28 pt button) passes only when padding carries its region to it; hit region versus platform control size is set out in `references/accessibility-inclusion-privacy.md`. Fail: major. `[HIG: buttons, accessibility]` `[translation]`
- **Rotate the device and resize the window mid-task.** Pass when the layout survives instead of scrambling. Fail: major. `[HIG: layout]` `[WWDC26-250]`
- **Scroll fast and tap the slowest control.** Pass when scrolling stays smooth and no tap leaves a person waiting with no response — a control whose work takes time shows its own progress. Fail: major. `[HIG: buttons]` `[WWDC26-250]`
- **Start the screen with nothing cached.** Pass when placeholder text or graphics appear at once, the rest of the interface stays usable, progress is determinate whenever the length is known, and an unavoidably long wait gives something worth reading. Fail: major. `[HIG: loading]`
- **Inspect the text rendering.** Pass when no text falls below the platform minimum (11 pt on iOS, 10 pt on macOS; the equivalent elsewhere), light weights are avoided at small sizes, and leading suits the number of lines. Fail: major. `[HIG: typography, accessibility]`
- **Watch one feedback animation closely.** Pass when it is brief, precise, moves in the direction the gesture implies, and is absent from interactions that happen constantly. Fail: minor. `[HIG: motion]`
- **Scale and letterbox the images.** Pass when artwork fills its frame without its aspect ratio being changed, and colour profiles are applied so colours land as intended. Fail: minor. `[HIG: layout, color]`
- **Ask what it was tested on.** Pass when the screen was seen at several sizes, in more than one localisation and text size, and its colours checked in bright and dim light. Fail: major. `[HIG: layout, color]`
- **Compare against the rest of the product and the platform's current patterns.** Pass when the change does not leave this screen on a pattern everything else has moved off, and nothing is a pixel out of alignment with its neighbours. Fail: minor. `[HIG: design-principles]` `[WWDC26-250]`

## Delight

*«Make it human» — the emotion the experience aims for, carried by ordinary moments rather than decoration.* `[HIG: design-principles]`

- **Name the feeling the screen should produce.** Pass when the change states it and the visuals, wording and timing support it. Fail: minor. `[HIG: design-principles]` `[WWDC26-250]`
- **Read the ordinary moments — empty state, error, confirmation, end of flow.** Pass when each carries the product's character and helps, rather than reading like a status code. Fail: minor. `[HIG: design-principles, writing]`
- **Time every flourish.** Pass when no animation, celebration or decoration stands between a person and their task. Fail: major. `[HIG: design-principles, motion]` `[WWDC26-250]`
- **Empty every list the change can produce.** Pass when the blank screen says what to do next and offers the control to do it, and holds nothing crucial that vanishes once content arrives. Fail: major. `[HIG: writing]`
- **Match tone to situation.** Pass when serious moments are straightforward and no error apologises with "oops" or hides behind cheer. Fail: minor. `[HIG: writing]`
- **Count the confirmations of success.** Pass when only genuinely significant completions are confirmed, because people already expect the rest to work. Fail: minor. `[HIG: feedback]`
- **Walk the whole flow once, end to end, as a person would.** Pass when freedom to act, safety to explore, familiar patterns and adaptation hold together across the flow and not only per screen. Fail: minor. `[HIG: design-principles]` `[WWDC26-250]`

## How to report

- **Write one finding per line as `screen or file:line — what fails — which check — severity — how to reproduce`.** The location, the check and the reproduction are what let someone else confirm the finding without asking you.
- **Name the check by its principle and its opening words.** "Flexibility / Scale text to the largest accessibility size" is traceable; "accessibility issue" is not.
- **Drop any finding you could not reproduce.** A claim that fails to reproduce costs the next reader more than it is worth; if it depends on conditions, put them in the reproduction.
- **Quote the failing condition, not your preference.** The pass condition of the check is the standard; a finding that cannot be stated as a failed pass condition is taste.
- **Order findings blocker, major, minor.** The first line of the report is the worst thing found.
- **Write no praise and no summary of what works.** A review exists to list what fails; everything else dilutes it.
- **Accept with minors outstanding, listing them.** Blockers and majors in the changed area are fixed first; minors are recorded and carried.
- **Report, do not rewrite.** State the failing condition and let the author choose the fix; a reviewer's own redesign is not a finding. `[translation]`

## Hand-over check

- **Open the change in the running interface and complete the task it changes, end to end.** A change verified only in a diff or a unit test is not verified. `[translation]`
- **Run the quick twelve against what you see.** Anything failing is either fixed now or reported with its severity in the hand-over. `[translation]`
- **Say which principles the change traded against each other and which one won.** One line; a trade-off nobody wrote down is one the next person will undo. `[HIG: design-principles]`
- **Name the sizes, appearances and platforms you actually looked at.** Claiming a layout adapts after seeing one width is the most common false report. `[HIG: layout]`
- **List the checks you could not run and why.** Untested at large text sizes, untested with a screen reader, untested in dark appearance — say so rather than implying coverage.
- **Say what still fails.** Outstanding minors belong in the hand-over, not in someone else's later bug report.
- **Leave the interface reproducible.** The branch, the URL, the seeded data and any setting you changed. `[translation]`

## Scope of a review

- **Check what the change touched plus its immediate neighbours.** The changed screens, the flow that reaches them and the components they share — unless a full audit was asked for. `[translation]`
- **Run the quick twelve over the whole changed area first, then the per-principle sets where the change is risky.** A form change earns Agency and Simplicity; a visual change earns Flexibility and Craft; a new dialog earns Agency and Familiarity. `[translation]`
- **Check the rendered interface at the sizes and appearances it will really be used in.** Reading the diff finds naming problems, not contrast, focus order or truncation. `[translation]`
- **Review the state a person can actually reach.** Seeded happy-path data hides empty states, long strings, failures and slow responses, which is where most blockers live. `[translation]`
- **Do not reopen decisions already recorded.** A recorded trade-off is re-examined only with new evidence; re-litigating it is not a finding. `[translation]`
- **Push topic depth to the reference file that owns it.** `references/accessibility-inclusion-privacy.md`, `references/forms-and-data-entry.md`, `references/modality-alerts-notifications.md`, `references/motion-feedback-loading.md`, `references/typography-color-visuals.md`, `references/layout-and-navigation.md`, `references/actions-menus-and-input.md`, `references/writing-help-onboarding-settings.md`, `references/data-and-charts.md` and `references/platforms-and-web.md` hold the rules; this file holds only the checks. `[translation]`

## Deliberately omitted

- **Watch-specific rules** (avoid indeterminate loading indicators, no more than two or three controls in a row, wrist-flip autorotation) — tied to a screen worn on the wrist, with no general form to check. `[HIG: feedback, loading, layout, buttons]`
- **Spatial-computing comfort rules** (peripheral motion, ~0.2 Hz oscillation, billboarded text, 60 pt button spacing, glass window materials) — meaningful only in a head-worn display.
- **TV overscan insets and the column-grid tables** — numbers for a screen viewed across a room; the general rule, respect the safe area, is kept under Flexibility.
- **macOS-only button varieties** (square or gradient, help, image and flexible-height push buttons, spring loading) — a component inventory rather than a review check; it belongs in `references/actions-menus-and-input.md`.
- **Liquid Glass material behaviour and scroll edge effects** — an Apple material with no generic equivalent to check; the general rule, keep controls distinguishable from content, is kept under Simplicity.
- **Colour-management and type specification tables** (P3 versus sRGB, True Tone, Dynamic Type size tables, tracking values, the SF and New York families) — implementation specifications. The numbers that do generalise — minimum text sizes, contrast ratios, 44×44 pt targets — are kept.
- **Store and framework surfaces** (the Core Location location button, App Store privacy details, Accessibility Nutrition Labels, App Review rules on tracking screens) — distribution artefacts rather than interface checks; the underlying rule against misleading someone before a permission request is kept under Responsibility.
- **Game-specific guidance** (frame-rate targets, difficulty accommodations, custom loading views, background asset downloads) — outside the scope of an interface review.
- **Assistive Access layout rules for iOS and iPadOS** — a platform mode with its own guidance; its general lessons, one interaction per screen and fewer non-critical elements, are covered by the Simplicity checks.

## Sources

- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- `feedback` — https://developer.apple.com/design/human-interface-guidelines/feedback
- `accessibility` — https://developer.apple.com/design/human-interface-guidelines/accessibility
- `layout` — https://developer.apple.com/design/human-interface-guidelines/layout
- `writing` — https://developer.apple.com/design/human-interface-guidelines/writing
- `entering-data` — https://developer.apple.com/design/human-interface-guidelines/entering-data
- `modality` — https://developer.apple.com/design/human-interface-guidelines/modality
- `alerts` — https://developer.apple.com/design/human-interface-guidelines/alerts
- `undo-and-redo` — https://developer.apple.com/design/human-interface-guidelines/undo-and-redo
- `loading` — https://developer.apple.com/design/human-interface-guidelines/loading
- `motion` — https://developer.apple.com/design/human-interface-guidelines/motion
- `color` — https://developer.apple.com/design/human-interface-guidelines/color
- `typography` — https://developer.apple.com/design/human-interface-guidelines/typography
- `privacy` — https://developer.apple.com/design/human-interface-guidelines/privacy
- `onboarding` — https://developer.apple.com/design/human-interface-guidelines/onboarding
- `settings` — https://developer.apple.com/design/human-interface-guidelines/settings
- `buttons` — https://developer.apple.com/design/human-interface-guidelines/buttons
- WWDC26 session 250, «Principles of great design» — https://developer.apple.com/videos/play/wwdc2026/250/

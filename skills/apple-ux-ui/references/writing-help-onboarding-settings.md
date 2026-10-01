# Writing, help, onboarding, settings

This file covers the words in an interface and the moments that are made almost entirely of words: microcopy and labels, error messages and empty states, contextual help and tips, onboarding and the first run, settings, accounts and sign-in, and asking for a rating. Load it when you are writing or reviewing any interface text, designing a first-run experience, adding a settings area, or deciding what to ask a person for and when. Its rules are instances of five of the eight principles: **Simplicity** (include just what's necessary; be concise — choose exactly the words you need to convey a concept or label a control), **Familiarity** (use concepts people already know, and keep language patterns consistent so behaviour is predictable), **Agency** (defaults that work, guided flows that are easy to skip or escape, nothing standing between a person and the task), **Responsibility** (be transparent about what the product does and why, and ask for data with a reason at the moment of need) and **Delight** (a human voice, and character in ordinary moments such as an error message). Neighbouring files own the adjacent decisions: which surface delivers a message — `references/modality-alerts-notifications.md`; field controls and validation mechanics — `references/forms-and-data-entry.md`; type, colour and text-scaling craft — `references/typography-color-visuals.md`; perceived launch speed and loading — `references/motion-feedback-loading.md`; permission and AI-transparency detail — `references/accessibility-inclusion-privacy.md`.

## Writing

*Serves Simplicity (be concise; exactly the words you need), Familiarity (the vocabulary people already have) and Delight (a human voice, including in the unglamorous moments).*

### Voice, tone and terminology

- **Decide the product's voice before you write screens.** Name who you are talking to and how you want them to feel — a banking tool conveys trust and stability, a game conveys excitement — and let that fix the vocabulary.
- **Keep a list of the terms you use, and use one term per concept.** Consistent language plus a voice that reflects the product's values is what makes an interface feel cohesive rather than assembled.
- **Vary tone with the situation, not voice with the screen.** Reaching a goal and failing a payment deserve the same vocabulary in different registers; consider what the person is doing both in the world and in the product.
- **Build language patterns and return to them.** Once a phrase names an action, that phrase names it everywhere; consistency builds familiarity and makes the next screen cheap to write.
  [HIG: writing]
- **Speak plainly and naturally.** Strip jargon, avoid redundancy, get to the point — the simplest way to say something is usually the most universal and the most helpful.
  [HIG: writing, design-principles] [WWDC26-250]
- **Use the words people already use for the thing.** People arrive with a lifetime of real-world and other-software vocabulary; borrowing it is what makes an interface understandable without instruction.
- **Do not rename a standard action.** If the action deletes something, call it Delete and give it the symbol people associate with deleting; creative liberty with a familiar label costs the instant recognition you were relying on and surprises people in the wrong way.
- **Let the emotion you want drive the wording, and treat ordinary moments as where character shows.** Delight is not flourishes added at the end — a button label or an error message is exactly where the product's spirit is either present or missing.
  [HIG: design-principles] [WWDC26-250]

### Clarity and concision

- **Check every word and delete the ones that are not working.** If fewer words say the same thing, use fewer; read the line out loud when you are unsure.
- **Write for everyone.** Choose simple language with accessibility and localization in mind, and avoid jargon and gendered terminology.
- **Put the most important information first on each screen.** Consider what the screen is for, order its elements by importance, and format the text so it can be read rather than decoded.
- **Move a second idea onto a second screen.** When a screen is carrying more than one idea, break it up and design the flow of information across the screens deliberately.
  [HIG: writing]
- **Let the words answer the three questions people arrive with:** what do I pay attention to, what can I interact with, and how do I interact.
  [WWDC26-250]
- **Cut steps, not only words.** A concise interface respects time by reducing the number of steps to a result, not just the character count of its labels.
- **Add words when they remove doubt.** A play/pause control gains, not loses, by showing where you are and how much time is left; sometimes simple means supplying the context a person needs to decide.
  [WWDC26-250]
- **Use possessive pronouns sparingly, and never "we".** "Favorites" says what "Your Favorites" says, shorter; "Unable to load content" is clearer than "We're having trouble loading this content", because nobody knows who "we" is. If you use *my* or *your*, do not switch perspective mid-product.
  [HIG: writing]
- **Match the words to the device and its input.** Never write "click" for a touch screen or "tap" for a pointer; describe each device's gestures correctly. Small screens and screens read from a distance both demand brevity, and a screen in a shared room may be read by more people than the one you are addressing.
  [HIG: writing, offering-help]

### Labels, buttons and links

- **Label a button with a verb that names what will happen.** "Send" beats "Let's do it!"; prioritise clarity over being clever or cute.
- **Write link text that describes its destination.** "Learn more about UX writing" instead of "Click here" — this matters most to people moving through links with a screen reader.
- **Use active voice and clear labels to carry people from step to step.** Active, action-oriented wording is what makes a flow navigable.
  [HIG: writing]
- **Name a control by the action it starts, not by its mechanism.** Descriptions that begin with a verb — "Restore default settings", "Add or remove a language" — tell people what they get.
  [HIG: offering-help]

### Capitalization and multi-step flows

- **Choose a capitalization style per element type and apply it consistently.** Title case reads formal, sentence case reads casual; pick one per element type (for example title case for all alerts, sentence case for all headlines) and keep it, noting that some components carry their own guidance.
- **Fix the vocabulary of a multi-screen flow before you build it.** Open with wording such as "Get Started", move with one chosen word — "Continue" or "Next", not both — and mark the end with "Done" so completion is unmistakable.
  [HIG: writing]

### Errors and blank screens

- **Help people avoid the error first.** An error message is the fallback, not the mechanism.
- **Show the message as close to the problem as possible.** A message far from its cause makes people hunt for what to change.
- **Say what to do, not what is wrong.** "Choose a password with at least 8 characters" is help; "That password is too short" is commentary. Instruct rather than scold: "Use only letters for your name" beats "Don't use numbers or symbols", and "Invalid name" helps nobody.
- **Do not blame and do not perform.** Avoid blame, and skip interjections such as "oops" or "uh-oh" — they are unnecessary and read as insincere when someone is frustrated.
- **When wording cannot rescue an error that will hit many people, redesign the interaction.** Treat a message you cannot write well as evidence about the design.
- **Give a blank screen a next step.** An empty state — a cleared to-do list, an empty bookmarks folder — is a chance to welcome and orient; say what to do and provide the button or link to do it. Keep nothing crucial there, because the state is temporary and will vanish.
- **Choose the delivery method by urgency, importance and context.** Decide whether the message needs immediate action and how much supporting information it needs before choosing inline text, an alert, an action sheet or a notification; see `references/modality-alerts-notifications.md`.
  [HIG: writing]

### Static text on screen

- **Use a label for a small amount of uneditable text, a text field for a small amount of editable text, and a text view for long, editable or specially formatted text.** Reaching for the heaviest control by default costs you layout and legibility.
- **Let static text do the orienting.** Text in a button says what the button does; text in a list row describes the item, often beside a symbol or image; text in a view introduces a control or names a task people can perform there — together they tell people the current context and what comes next.
- **Raise the keyboard that matches the content wherever text is editable.** A text view or field that brings up the wrong keyboard turns a short entry into a chore; see `references/forms-and-data-entry.md`.
- **Let people select and copy text that has value.** An error message, a serial number, a location or an IP address is something people need to paste elsewhere.
- **Prefer the system font and keep text scalable.** Labels and text views support the platform's text-size setting (Apple's Dynamic Type) by default; if you restyle them or use a custom font, verify legibility, and test with accessibility options such as bold text on.
- **Use the platform's ranked text colours instead of inventing greys.** Apple defines four label levels — primary information, supplemental text, unavailable items, watermarks — so relative importance is expressed in one vocabulary; see `references/typography-color-visuals.md`.
  [HIG: labels, text-views]
- **Label every input and add hint text that shows the format.** An example such as "name@example.com", or a description such as "Your name", tells people how to enter the information; mechanics live in `references/forms-and-data-entry.md`.
  [HIG: writing]

## Offering help

*Serves Simplicity (help is what an interface needs when it is not yet self-evident, so keep it small) and Agency (guidance offered, never imposed, and always escapable).*

### Help in context

- **Let the task's size decide the form of help.** A one- or two-step task wants an inline view that describes it succinctly; a complex, multistep task may want a tutorial that teaches the larger goal.
- **Tie help to the action the person is taking right now, and make it easy to dismiss or avoid.** Help nobody asked for and cannot escape is an interruption.
- **Do not document standard components.** Describe what a standard control does *in your product* instead. Only a unique control, or an input device used in a non-standard way, needs orientation — and there, prefer animation or a graphic to a long description.
- **Keep help language and imagery true to the device in hand.** Do not show a game controller to someone holding a remote, and do not tell a phone user to click or a desktop user to tap.
- **Make all help content inclusive.** See `references/accessibility-inclusion-privacy.md`.
- **Do not let documentation carry the interface.** If a control needs a lot of text to explain, simplify the control; approachable and intuitive comes first, contextual help second.
  [HIG: offering-help]

### Tips

- **Use a small transient tip to teach a new or less obvious feature, or a faster route.** Its job is to get someone to try the feature, not to inform them in general.
- **Keep a tip to one or two sentences, action-oriented, and about this feature only.** Nothing promotional, nothing about another flow: promotional means anything that advertises or sells, or is not aligned with what the person is doing now.
- **Tip only features that take a few simple steps.** More than about three actions is too complicated for a tip and belongs in help or a tutorial.
- **Pick the tip's form by what must stay visible.** A popover tip preserves the content flow; an inline tip keeps surrounding information visible; an annotation-style tip points at a specific element; a hint-style tip suits guidance not tied to one control.
- **Gate tips by eligibility and frequency.** Do not tip a feature someone already uses, and when there is more than one tip set a cadence — for example at most one a day.
- **Reuse the symbol people already associate with the feature, and do not duplicate an image the tip points at.** Apple's form is the filled variant of the symbol.
- **Give a tip a button when there is somewhere useful to go.** The feature's settings, a setup flow, or more detail — a tip that only talks wastes the moment.
  [HIG: offering-help]

### Tooltips on pointer platforms

- **On platforms with a pointer, give controls a tooltip that describes only that control.** It appears on hover (Apple calls it a help tag in user documentation); somebody asking about one control does not want a tour of its neighbours.
- **Begin with a verb, leave out the control's own name, and stay brief — roughly 60 to 75 characters.** Sentence fragments and dropped articles are fine; remember that translation lengthens text.
- **Use sentence case and omit ending punctuation** unless your product's style requires it; sentence case reads more approachable.
- **Vary the tooltip by state when the state changes what the control does.**
  [HIG: offering-help]

## Onboarding and first run

*Serves Agency (a guided flow that is easy to skip or escape, and good defaults instead of setup), Responsibility (make intentions clear from the first interaction and give a rationale before asking for anything) and Craft (a first run that feels ready, not rushed).*

### Onboarding

- **Aim for a product people understand by using it, and treat onboarding as the fallback.** When it is necessary, make the flow fast, enjoyable and optional.
- **Run onboarding after launching completes; it is not part of the launch experience.**
- **Teach through interactivity.** People retain what they have done; give them a safe place to perform the action, find the feature or try the mechanic rather than watching a description of it.
- **Prefer a set of context-specific tips over one front-loaded tour.** A tip next to the area it describes lets someone learn one thing while making progress; a tour asks them to memorise everything before they have done anything.
- **If a prerequisite flow is unavoidable, keep it brief and free of memorisation.** Teach too much and people feel overwhelmed and remember less.
- **Make a separate tutorial optional, do not re-present it after a skip, and keep it easy to find later** — in a help, account or settings area. A guided flow that must exist must be easy to skip or escape.
- **Teach your product, not the platform.** People came to learn what you do, not how the device works.
- **Do not make the first run wait on a download.** Package enough content that someone can start interacting immediately, whether they take the onboarding or skip it.
  [HIG: onboarding, design-principles]

### Launch and the first screen

- **Launch instantly.** People want to interact right away and often will not wait more than a couple of seconds.
- **Where the platform uses a launch screen, make it nearly identical to the first real screen.** Match the current orientation and appearance mode; if the first screen begins as a solid colour, show only that colour — mismatched elements produce an unpleasant flash.
- **Keep text and branding out of the launch screen.** Text there is never localized, and the launch screen is not a branding opportunity or an "About" window; its only job is to make the product feel ready. Logos belong there only if they are a fixed part of the first screen.
- **If you need a splash screen, show it at the start of onboarding** — or immediately after launch when there is no onboarding — **and only long enough to take in at a glance.** Anything longer reads as a delay you are imposing.
- **Design a splash screen to communicate succinctly at a glance**, not to be read: it is one graphic carrying branding or a single necessary message, and it is a separate thing from the launch screen.
- **Restore the previous state in detail when the product restarts.** Scroll position, window size and location, the view someone left: never make people retrace steps to get back to where they were.
- **Launch in the orientation the device is already in.** If you support one orientation only, launch in it and let people rotate; handle both directions of rotation correctly.
  [HIG: launching, onboarding]

### What to ask for, and when

- **Ship defaults good enough that nobody has to configure anything first.** Postpone non-essential setup and customization steps so people can start immediately.
- **Ask for a permission at the moment the feature needs it, with the reason.** The exception is access the product cannot function at all without; fold that into onboarding, where you can show why it is needed and what granting it gives.
- **Never throw permission prompts at launch.** A prompt before anyone knows what the product does is the interface equivalent of a stranger demanding your phone number and saying they will explain once they have it.
- **Let people experience the product before you ask for a rating or a purchase.** Engagement first, requests after.
- **Leave licensing and agreements to the distribution channel where you can.** If they must appear in the first run, integrate them so they do not disrupt it.
  [HIG: onboarding, design-principles] [WWDC26-250]

## Settings

*Serves Simplicity (only what genuinely needs a choice), Flexibility (people personalise what a single design cannot get right for everyone) and Familiarity (the platform's own settings conventions and system-wide choices).*

### What belongs in settings

- **Choose defaults that give the best experience to the largest number of people.** Detect and decide — for example set graphics quality from the device — instead of opening with a questionnaire; done well, most people never adjust anything.
- **Minimize the number of settings you offer.** Too many make a product feel less approachable and make the one setting somebody wants harder to find.
- **Never use a setting to ask for something you can detect.** A connected controller or accessory, or whether the system is in dark appearance, is something to read, not to ask about.
- **Do not reimplement system-wide settings.** People manage accessibility accommodations, scrolling behaviour and authentication globally and expect every product to honour those choices; a local copy implies the global setting might not apply here, and that changing yours might change other products.
- **Reserve the settings area for general, infrequently changed options.** Opening settings means suspending the task, so what lives there should be things like interface style, save behaviour, window configuration or account options.
  [HIG: settings]

### Where a setting lives

- **Put a task-specific option in the screen it affects.** Showing or hiding part of a view, reordering a collection, filtering a list: in a settings area these lose their context, force people to leave the task, and hide the result until they return.
- **Add only the rarest options to the system-provided settings surface, and provide a button that opens it directly.**
- **Open settings the way the platform does.** On desktop that is the platform's settings shortcut (Command-comma on Apple platforms) and a Settings item in the application menu rather than a toolbar button, which would spend toolbar space people need for frequent commands; in games people reach for Escape.
- **Keep the settings area's own navigation stable, and always show which section is active.** People rely on a settings interface that does not move to find what they need; on desktop a non-customizable toolbar of panes does this, the window title names the visible pane, and reopening restores the pane last used.
- **Group related settings and give every group a name.** Apple's desktop form is a settings window whose toolbar switches between views — panes — each holding one group of related settings.
  [HIG: settings]
- **Keep the path to any one setting short: prefer a flat set of named groups, each reachable in one move.** Apple states no rule about depth — the corpus blames poor findability on the *number* of settings — so treat this as the skill's own extension of that reasoning: a deep tree hides a setting the way a long list does. [translation]

### Labelling settings

- **Label a setting as practically as possible, and describe what it does when it is on.** People infer the off state; there is no need to spell out that nothing happens.
- **Add a short explanation only when the label cannot carry the meaning on its own.**
- **Never describe where a setting is — link to it.** Give a direct button or link instead of directions a person has to follow.
  [HIG: writing, settings]

## Accounts

*Serves Agency (nothing between a person and the value of the product), Responsibility (ask for identity and data only when needed, keep it safe, and let people leave) and Familiarity (the platform's trusted sign-in).*

### Asking for an account

- **Require an account only if your core functionality needs one.** Otherwise let people use the product without one; an account is a convenience for reaching their own content, not a toll.
- **Delay sign-in as long as you can.** People abandon products that demand sign-in before anything useful happens — let a shopping app be browsed freely and ask only at checkout.
- **Explain the benefit in the sign-in view itself.** A brief, friendly statement of why the account is required and what it gives is the difference between a barrier and an offer.
- **Ask for the minimum, and let awkward entry move to a better device.** Where input is painful — a remote-driven TV screen, a tiny display — collect as little as possible, offer to continue on another device, and let stored credentials autofill.
  [HIG: managing-accounts]

### Sign-in and authentication

- **Prefer passwordless sign-in.** A passkey lets someone create an account or sign in with just a user name, removing password creation and entry; a platform identity provider (Apple's form is Sign in with Apple) gives a consistent sign-in people already trust and one fewer credential to remember. If you must keep passwords, add two-factor authentication.
- **Name the authentication method in the button.** "Sign In with Face ID" rather than a generic "Sign In" tells people what is about to happen.
- **Refer only to methods available on this device.** Check capabilities and use the right term rather than naming a biometric the hardware does not have.
- **Do not add a product-level switch for biometric sign-in.** People enable biometrics at the system level, so an in-product copy is redundant and confusing.
- **Do not borrow a term the platform reserves for its own credential.** Apple's example: avoid "passcode" for your account credential, or people will think you are asking for the code that unlocks their device.
- **On a shared device, do not ask the current person to identify themselves every time.** Share the credential and keep profiles and data separate instead.
- **Where the platform holds the credential, do not offer a redundant sign-out.** If you must show one, send people to the place that actually owns the account, and never point them at privacy controls as if those were a sign-out.
  [HIG: managing-accounts]

### Deleting an account

- **If people can create an account in the product, they must be able to delete it — not merely deactivate it.** Understand and comply with your region's deletion and right-to-be-forgotten requirements as well.
- **Put the deletion entry point where people will find it.** Offer it in the product, or a direct link to the page that performs it; do not bury it in a privacy policy or terms page.
- **Keep both deletion paths equivalent.** Do not make the in-product flow longer or more complicated than the website's.
- **If deletion can be scheduled for later, also offer immediate deletion.** People may want to use remaining services or wait for a renewal date, but the choice stays theirs.
- **Say when deletion will complete, and notify people when it has.** Deletion can take a while; silence during it is the part people experience as broken.
- **Explain what happens to billing.** A subscription billed by the store may keep renewing until it is cancelled, independently of the account, so say how to cancel and manage purchases — and support deletion even for people who did not purchase through you.
- **If law forces you to keep data or follow a specific process, describe that plainly.** People can accept a constraint they can see.
  [HIG: managing-accounts]

## Asking for ratings and feedback

*Serves Agency (the request never blocks the task and "no" is final) and Responsibility (the honest way to earn a good rating is a good experience, not a well-timed nag).*

- **Ask only after someone has demonstrated engagement.** A completed level or a significant task is the moment; how often they return, how many features they explore and how many tasks they finish are the signals. Never ask on first launch or during onboarding — there is no opinion yet to give, and asking early invites a negative one.
- **Never interrupt a task to ask.** Look for a natural break or stopping point; a request landing mid-flow feels like a burden.
- **Space requests, and do not pester.** Leave a week or two between asks, and only ask again after further engagement.
- **Prefer the platform's own review prompt where one exists.** Apple's is consistent and non-intrusive, can be answered or dismissed with a single tap, is capped by the system at three appearances per product per 365 days, and can be switched off entirely by the person — respect that "no" rather than routing around it.
  [HIG: ratings-and-reviews, onboarding]

## Translation to web and other platforms

Every bullet in this section is the skill's own translation of the rules above to the web and to web-hosted shells. Apple does not state them in these terms.

### Microcopy checklist for a web form

- **Give every field a visible, persistent `<label>`, and use the placeholder only as a format hint.** The hint disappears the moment someone types, so it cannot carry the field's name.
- **Name the submit button after its action** — "Create account", "Send invite" — never "Submit" or "OK".
- **Render each error in the field's own error slot, link it with `aria-describedby`, and phrase it as the fix.** One summary at the top of a long form, linking to the first bad field, plus per-field messages.
- **Keep link text meaningful out of context.** Assistive technology lists links without their surrounding sentence.
- **Say where the person is in the `<title>` and the first heading**, in that order of importance, so tabs, history and screen readers all describe the same place.
- **Keep one glossary of interface terms in the repository** and reference it from components and translation files, so a term cannot drift between screens.
- **Record the capitalization rule per element type in the design system**, not in each contributor's head.
- **Give every empty state a heading, one explanatory line and one primary action.**
  [translation]

### The same surfaces on the web and in shells

- **Ask for a browser permission from the click that needs it, never on page load.** Notification, location, camera and clipboard prompts are one-shot in practice; a denial is expensive to reverse.
- **Keep a guest path to real value before any account wall**, and make account deletion a real action in the account area rather than an email request.
- **Use the URL as your state restoration.** Filters, tab, sorting, pagination and — where it matters — scroll position belong in the URL so a reload or a shared link lands in the same place.
- **Do not build a splash screen for a web page.** There is no launch screen to match, so render the real first screen as early as you can, skeletal if necessary; see `references/motion-feedback-loading.md`.
- **Make settings a flat page of labelled groups with a linkable anchor per group**, so help and tips can deep-link to a setting instead of describing where it is.
- **Put tooltips on hover *and* focus, and never put information only in a tooltip** — touch users and keyboard users must get it another way.
- **Ask for feedback after a completed task, not on a timer, a scroll depth or an exit-intent modal.**
- **In an Electron or Capacitor shell, let help and settings follow the host platform.** A desktop shell gets a Settings item in the application menu with the platform's shortcut; a mobile shell keeps settings as a screen inside the app; see `references/platforms-and-web.md`.
  [translation]

## Deliberately omitted

- `patterns/launching` — tvOS auto-starting live playback and the static layered launch screen: TV-app-specific, with no generic equivalent.
- `patterns/launching` — visionOS launching into the Shared Space before a full space: spatial platform only.
- `patterns/settings` — the macOS settings-window chrome rule about dimming the minimize and maximize buttons: a specific Apple window-control detail; the generic part (a settings window sized to its pane, opened by shortcut) is kept.
- `patterns/settings` — the watchOS rule that apps add no settings to the system Settings app and surface a few essentials in the main view: watch-only.
- `patterns/ratings-and-reviews` — resetting the App Store summary rating on a new release: a store-listing trade-off, not interface design.
- `patterns/managing-accounts` — TV provider system-level authentication and its sign-out routing, and watchOS iCloud Keychain synchronisation: Apple-service specific; the generic rules (no redundant sign-out, credentials that autofill, minimal entry on remote-driven screens) are kept.
- `components/labels` — the watchOS date and timer text components and their use in complications: watch-face specific.
- `components/labels` — the API names of the four system label colours: colour tokens belong to `references/typography-color-visuals.md`; the ranked-importance rule is kept here.
- `components/text-views` — tvOS substituting text fields for editable text: TV-only input model.
- `patterns/offering-help` — visionOS tooltips triggered by gaze, and the Siri Remote rotated-90-degrees example: spatial and remote-specific illustrations of rules already stated.
- Developer APIs named by these pages (TipKit, RequestReviewAction, passkey and Sign in with Apple frameworks, UserDefaults): implementation documentation, not design rules; the design rules they serve are kept above.

## Sources

- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- `writing` — https://developer.apple.com/design/human-interface-guidelines/writing
- `offering-help` — https://developer.apple.com/design/human-interface-guidelines/offering-help
- `onboarding` — https://developer.apple.com/design/human-interface-guidelines/onboarding
- `launching` — https://developer.apple.com/design/human-interface-guidelines/launching
- `settings` — https://developer.apple.com/design/human-interface-guidelines/settings
- `ratings-and-reviews` — https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews
- `managing-accounts` — https://developer.apple.com/design/human-interface-guidelines/managing-accounts
- `labels` — https://developer.apple.com/design/human-interface-guidelines/labels
- `text-views` — https://developer.apple.com/design/human-interface-guidelines/text-views
- `WWDC26-250` «Principles of great design» — https://developer.apple.com/videos/play/wwdc2026/250/

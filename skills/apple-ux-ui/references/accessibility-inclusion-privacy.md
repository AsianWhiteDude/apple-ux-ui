# Accessibility, inclusion and privacy

This file covers the rules that decide whether an interface works for everyone and whether it deserves trust: accessibility (perception, operation, cognition), inclusion (language, imagery, assumptions, localisation), right-to-left layout, privacy and permissions, accounts and sign-in, and the design of AI and machine-learning features. Load it when a screen is being built or reviewed for accessibility, when copy or imagery describes people, when the product asks for data or a permission, when an account or sign-in flow is designed, or when a feature is powered by a model. It serves **Flexibility** most directly — design for everyone, support many input methods, adapt to contexts other than your own — together with **Responsibility** (transparency about what the product does and why, safety, collecting only what is needed) and **Familiarity** (use the platform's own accessibility features and consent patterns instead of inventing private ones). **Agency** appears wherever a person must be able to refuse, correct or revert; every rule below is an instance of one of those four principles, not a generic checklist. For type scale and contrast craft see `references/typography-color-visuals.md`; for motion settings and loading feedback see `references/motion-feedback-loading.md`; for control choice and validation see `references/forms-and-data-entry.md`.

## Accessibility as the starting point

- **Treat accessibility as a requirement from the first sketch, not a pass before release.** An accessible interface reaches a larger audience, and the qualities that make it accessible — being intuitive, perceivable and adaptable — are the same qualities that make it good for everyone.
- **Make the interface intuitive: familiar, consistent interactions with no learning tax.** People should not have to memorise anything private to your product to perform a basic task.
- **Make it perceivable: never carry information on one sense alone.** Anything conveyed by sight must also be reachable by hearing or touch, and anything conveyed by sound must also be visible or felt.
- **Make it adaptable: follow the system accessibility settings and let people personalise what matters.** Text size, contrast, motion and input method belong to the person, not to the layout.
- **Audit the built interface with the platform's accessibility inspector, not by reading the code.** The inspector shows how the product represents itself to assistive technology, which is where most defects actually live.
[HIG: accessibility]

### Vision and legibility

- **Let people enlarge text by at least 200 percent (140 percent on a watch-class screen) without losing content or function.** Support the system text-size setting (Apple's Dynamic Type; on the web, relative units and browser zoom) or provide an equivalent in-product control.
- **Scale icons and glyphs with the text they sit beside.** An enlarged label next to a fixed 16-point icon reads as a broken layout and leaves the icon illegible for the person who enlarged the text.
- **Use the platform's recommended default and minimum type sizes for custom styles.** Apple's values: iOS and iPadOS 17 pt default / 11 pt minimum, macOS 13 / 10, tvOS 29 / 23, visionOS 17 / 12, watchOS 16 / 12.
- **Size thin weights up.** A light or thin custom face needs more than the recommended size to stay readable, because weight affects legibility as much as size does.
- **Meet a contrast minimum for every text and icon against its background.** Apple points at the WCAG Level AA values its inspector checks — 4.5:1 for text up to 17 pt, 3:1 at 18 pt, 3:1 for bold text — and also names APCA as a measure; use a standard calculator rather than judging by eye.
- **If the default palette cannot meet the minimum, ship a higher-contrast scheme that switches on with the system increase-contrast setting.** Check contrast in light and dark appearances separately; passing one says nothing about the other.
- **Prefer the platform's semantic colours over hard-coded values.** They carry accessible variants that adapt when someone turns on increased contrast or changes appearance.
- **Never let colour be the only carrier of meaning or state.** Add a distinct shape, icon, label or pattern; red-green and blue-orange pairings in particular are unreadable for many people.
- **Where colour is the content, let people recolour it.** Chart series, status palettes and game characters are the cases worth making customisable, because there is no single palette that works for every kind of colour vision.
[HIG: accessibility]

### Hearing and the second channel

- **Never put dialogue or critical information in audio alone.** Anything a person must hear to proceed is a barrier for someone deaf or hard of hearing and for anyone in a noisy or silent place.
- **Synchronise text with time-based media: captions for audible information, subtitles for dialogue in a chosen language.** Both are live equivalents of the sound, so they must track the media rather than sit beside it.
- **Give visual-only information a spoken form, and long media a transcript.** Audio descriptions narrate what is only shown, in the natural pauses; a transcript lets someone review or search a podcast or a long video as a whole.
- **Let people restyle that text.** Caption and subtitle presentation is an accessibility setting, not a branding decision.
- **Pair every meaningful sound with a haptic and a visual cue.** A success chime or error sound reaches nobody with audio off; the same event should also be felt and seen.
- **Point to off-screen action visually, not only with sound.** When audio guides someone toward where to act, add an on-screen indicator at that place.
[HIG: accessibility]

### Mobility, targets and input methods

- **Give every interactive element a hit region of at least 44×44 pt — 60×60 pt in visionOS.** That is the region a fingertip, pointer, eye or remote has to land in. [HIG: buttons] It is the one target bar this skill uses, and it holds on the web and on desktop too. [translation]
- **Read a platform's control sizes as what you draw, not as what can be hit.** Apple's defaults and absolute floors: iOS, iPadOS and watchOS 44×44 pt default with a 28×28 pt floor; macOS 28×28 / 20×20; tvOS 66×66 / 56×56; visionOS 60×60 / 28×28. Draw at or above the default and never below the floor.
- **Where the drawn control is smaller than the hit region — a macOS 28×28 pt button, an icon at a platform floor — carry the region to 44×44 pt with padding, not by enlarging the graphic.** Hit region and control size measure two different things about one control: what any input must land in, and what the platform's density lets you draw. Apple states them on separate pages and leaves the relation implicit. [translation]
- **Treat spacing between targets as seriously as target size.** Roughly 12 points of padding around a bezelled element, and roughly 24 points around the visible edges of an unbezelled one, keeps people from hitting the wrong control.
- **Use the simplest possible gesture for anything done often, and never require multi-finger or two-handed custom gestures.** Repetitive complex gestures are uncomfortable for many people and hard to remember for everyone.
- **Give every gesture a visible on-screen equivalent.** If swiping dismisses a view, a button must dismiss it too, so that assistive devices and limited dexterity are not dead ends.
- **Label every element well enough that it can be operated by voice.** Voice control drives the interface by speaking the names of things; unnamed or generically named controls cannot be spoken.
- **Expose the product's important repeatable tasks to the system's voice and automation layer.** When a task can be started by speaking or from a shortcut, people who cannot comfortably navigate to it still reach it.
- **Make the whole interface operable from the keyboard alone, and do not override system shortcuts.** Full keyboard access is an accessibility feature before it is a power-user feature.
- **Support the platform's alternative input technologies and test with them switched on.** Switch control, head or eye pointer control, full keyboard access and screen readers all depend on correctly labelled elements; verify on a device rather than assuming.
[HIG: accessibility]

### Cognitive load, time and motion

- **Keep actions simple, consistent and drawn from system behaviour.** Custom gestures and one-off patterns must be learned and retained, which costs every person something and costs some people the feature.
- **Avoid interface that disappears on a timer; dismiss by explicit action instead.** Auto-dismissing views punish anyone who needs longer to read and anyone navigating with assistive technology, which traverses a screen more slowly.
- **Never autoplay audio or video without visible controls to stop it, and honour a global opt-out.** Playback that starts by itself and cannot be stopped quickly is both an accessibility and a trust failure.
- **Respect the system reduce-motion setting by cutting automatic and repetitive animation.** Tighten springs to remove bounce, track animation to the gesture, avoid animating depth in z-order layers, replace axis transitions with fades, and avoid animating in and out of blurs.
- **Be sparing with fast, blinking or flashing effects, and respond to the dim-flashing-lights setting in video playback.** In excess these cause distraction and dizziness, and for some people seizures.
- **Offer a streamlined mode for people who need less at once.** Apple's form is Assistive Access; the generic rule is the same — strip to core functionality and remove non-critical workflows.
- **In that mode, put one interaction on a screen and confirm twice before anything hard to recover from.** Deleting a file is the example: two deliberate confirmations, not one.
- **Where a task has a difficulty or precision floor, let people lower it.** In games that means adjustable difficulty, reaction time and control assistance; elsewhere it means longer timeouts, larger targets and assisted input.
[HIG: accessibility]

## Screen readers and semantics

- **Give every key element a descriptive label, and keep the labels current as the interface changes.** Default labels on system controls are generic; the label should say what this control does here, not what kind of control it is.
- **Describe meaningful images, and only what the image itself adds.** Surrounding text and captions are already read out, so repeating them wastes the listener's time.
- **Exclude purely decorative images from the accessibility tree.** Silence is the correct description for an element that carries no information, and it reduces the noise the listener has to wade through.
- **Make charts and infographics fully available non-visually.** Give each one a concise description of what it conveys, and expose every interaction that reveals more detail; see `references/data-and-charts.md`.
- **Give every screen a unique, descriptive title and accurate section headings.** The title is the first thing a screen reader announces on arrival, and headings are how people build a map of the content.
- **Declare grouping, order and linkage that the eye gets from layout.** Proximity and alignment mean nothing to a screen reader; an image and its caption must be grouped so they are read as one item rather than as two lists.
- **Make every custom control supply its own label, value, state and actions.** System controls arrive with most of that; anything you draw yourself arrives with none of it, which is where accessibility defects concentrate.
- **Order the accessible tree by the reading order of the active language and locale.** A screen reader traverses in that order, so a visual arrangement that contradicts it produces nonsense.
- **Announce visible content and layout changes.** A silent change leaves the person with a mental model that no longer matches the screen.
- **Let people navigate by element type — headings, links, form controls.** Apple's rotor is one implementation; the rule is that long content must be traversable without listening to all of it.
- **Never make a custom gesture the only path to a feature.** With a screen reader on, gesture input may be intercepted by the assistive layer and never reach your view at all.
[HIG: voiceover, accessibility]

## Inclusion

- **Treat inclusion as iterative work and re-examine your own assumptions as you go.** Understanding of how other people think and feel keeps changing, so this is a pass you repeat, not a box you tick.
- **Aim past inoffensive.** A product that offends nobody can still be incomprehensible or irrelevant to most people; the target is an experience everyone can use, not an absence of complaints.
- **Use empathy as an investigation: look for the word or image that means something you did not intend.** Start from the goals and perspectives of the people you are designing for, not from your own reading of your own screen.
[HIG: inclusion]

### Language and tone

- **Write plainly and check the tone from perspectives other than your own.** Style communicates as much as wording: an academic register tells people without that education that the product is not for them.
- **Address the person as "you" and avoid "the user" or "the player".** Third-person labels make the product feel distant; reserve "we" and "our" for the company, since claiming a personal relationship can read as condescending.
- **Define a specialised term before using it, or replace it with plain language.** Undefined jargon excludes everyone outside the field, and plain wording also translates better.
- **Replace colloquialisms and idioms with literal language.** They are culture-bound, hard to translate, and some — "peanut gallery", "grandfathered in" — carry exclusionary origins most writers do not know about.
- **Use humour only where you have judged the cost.** Jokes are subjective, resist translation, irritate on repeat encounters and land wrongly for some readers.
- **Do not use a disability as a metaphor for a negative quality, and write about people before their disability.** When writing about a specific person or community, use the terms they use for themselves.
[HIG: inclusion]

### People, assumptions and imagery

- **Remove unnecessary gender from copy by rewriting rather than by pairing pronouns.** "Subscribers can post recipes" beats "a subscriber can post his or her recipes", and it survives localisation into gendered languages.
- **Use non-gendered figures for a generic person, and let people customise avatars and characters.** A generic person should read as human, not as a man or a woman.
- **Ask for gender only when the product genuinely needs it, and then offer non-binary, self-identify and decline-to-state.** Where you address people by name, let them state their pronouns instead of inferring them.
- **Portray a real range of ages, bodies, abilities, and racial and cultural backgrounds in imagery and examples.** People who see nobody like themselves conclude, correctly, that the product was not designed for them.
- **Avoid stereotyped roles.** Only male doctors and female nurses, or hero and villain archetypes that track real-world prejudice, reproduce the prejudice in your product.
- **Review the settings and objects you depict, not only the people.** Conspicuous affluence reads as out of touch in most contexts; familiar, relatable places and things welcome more people.
- **Hunt for assumptions in anything you ask people to answer.** Security questions about college subjects or a first car assume experiences many people never had; universal substitutes ("your favourite activity", "the name of your first friend") exclude nobody.
- **Do not encode one shape of family, household or relationship in a data model or in copy.** A narrow default definition propagates into every label and image the feature shows.
- **Design for disability as a spectrum, including temporary and situational.** Vision ranges from colour blindness and light sensitivity to blindness; hearing loss can last a week; a noisy train disables audio for everyone on it.
- **Do not assume a disability removes someone's interest in the experience.** That assumption is what shrinks the audience, not the disability.
- **Apply the same imagery rules outside the product.** Screenshots, help content and marketing are where people decide whether the experience is for them, so the range of people shown there matters as much as in the interface.
- **Be approachable: require no prior skill to start, and give a path to depth.** Present a straightforward interface and build learning into it — an onboarding flow beginners can follow step by step and everyone else can skip; see `references/writing-help-onboarding-settings.md`.
[HIG: inclusion]

### Languages, regions and formats

- **Prepare the interface for other languages and regions before translating anything.** People expect their own language for text and their own region's formatting for dates, times and money.
- **Write in a way that survives localisation.** Plain language, no unnecessary gender, no culture-specific references and no text baked into graphics all reduce the cost of every later locale.
- **Use an icon set that ships localised and bidirectional variants.** Apple's SF Symbols is that set on Apple platforms; on other platforms choose or build one with the same property, because hand-made glyphs become a localisation debt.
- **Verify that colour-as-meaning carries the same meaning in every locale you ship.** White reads as mourning in some places and as purity in others, so a colour-coded status can invert.
- **Let people choose the language for the product independently of the device where the platform allows it.** Multilingual people do not use one language for everything.
[HIG: inclusion, right-to-left]

## Right-to-left layout

- **Rely on the framework's automatic mirroring first, then fine-tune.** System components and standard layouts flip on their own; hand-tuning is for currencies, numerals and mathematical symbols that automation gets wrong.
- **Match text alignment to the interface direction when the system has not done it.** Content left-aligned in a left-to-right context is right-aligned in a right-to-left one.
- **Align a paragraph by its own language, not by the surrounding context.** Three or more lines of left-to-right text right-aligned make the start of each line hard to find; one- and two-line blocks still follow the context.
- **Align every item in a list the same way, including items in another script.** Mixed alignment in a scrollable list destroys scanning.
- **Never reverse the digits inside a single number.** A phone number, a card number or "541" keeps its digit order in every language and context.
- **Reverse the order of a sequence of numerals that shows progress or counting, without flipping the numerals themselves.** The same applies to any numeral sequence that communicates a specific order.
- **Identify the right numeral system per locale only when numbers are the subject.** Number-centric content needs that research; everything else should use the system's own number formatting.
- **Flip controls that move a value from a start to an end — sliders, progress indicators, ratings — and swap the glyphs at each end with them.** People read forward progress as moving in their own reading direction.
- **Flip navigation controls that move through a fixed order.** In a right-to-left context the back control points right, and next and previous swap sides.
- **Do not flip a control that refers to a real direction or points at an on-screen area.** A control that means "to the right" points right in every locale.
- **Visually balance adjacent Latin and right-to-left text.** Arabic and Hebrew have no capitals, so next to all-caps Latin they look small; roughly two points of extra size restores the balance.
- **Do not flip photographs, illustrations or artwork.** Flipping usually changes the meaning and, for licensed images, may breach the licence; make a new version if reading direction matters to the image.
- **Reverse the positions of images whose order is meaningful.** Chronological, alphabetical or ranked sets keep their meaning only when their sequence mirrors with the layout.
- **Flip an interface icon that represents text, reading direction, or forward and backward motion.** Left-aligned bars standing for text become right-aligned; a speaker's sound waves emanate the other way.
- **Localise an icon that must contain real letters or words, or design one that needs no text.** Signature, rich-text and text-cursor glyphs are the common cases; an icon using letters for an unrelated concept should be redrawn without them.
- **Never flip a logo or a universal mark.** A mirrored logo confuses people and can have legal consequences, and marks like the checkmark are expected to look the same everywhere.
- **Do not flip icons that depict real-world objects unless the object indicates direction.** A clock looks the same everywhere, and a right-handed tool does not need mirroring because most people are right-handed.
- **Decide complex custom icons component by component, weighing overall balance.** A negation slash or a badge that belongs to the visual language stays put; a badge depicting your own mirrored UI flips with it; a tool keeps its orientation while its base image flips.
[HIG: right-to-left]

## Privacy and permissions

- **Request only the data a feature actually needs, and make each request as narrow as the feature allows.** Asking for more than the feature uses, or asking before the person has shown interest in it, is what makes a product hard to trust.
- **Know which categories require consent before you design the flow.** Personal data such as location, health, finance and contacts; content people created, from messages to photos; protected resources such as Bluetooth peripherals, local networks and home automation; device capabilities such as camera and microphone; and the advertising identifier behind tracking.
- **Ask at the moment of need, with the reason visible in that moment.** Prompting at launch, before anyone knows what the product does, is the pattern people recognise as extraction — it is the interface equivalent of demanding a phone number from a stranger and refusing to say why.
- **Ask at launch only when the product cannot function without the data.** A navigation product asking for location on first run is understood; a note-taking product asking for contacts is not.
- **Say plainly what the data is for, in a short active sentence.** Apple's purpose string sits between the product name and the allow and deny buttons; make it specific, complete, sentence case and easy to understand.
- **Judge the wording against what it actually justifies.** Apple's own three examples are the test: a string naming the activity and the reason — recording at night to detect snoring — earns a decision; "needed for a better experience" is a vague passive non-answer; "Turn on microphone access" is an instruction with no reason in it at all.
- **Be transparent about what is collected and how it is used, including tracking.** People withhold data whose use they do not understand, and honouring privacy features they already rely on — relayed email addresses, mail privacy — is part of the same bargain.
- **Process data on the device when the device can do the work.** Local processing avoids the round trip and the risk that comes with it.
- **Adopt the platform's own privacy and security protections instead of building your own.** System encryption, key management and secure storage are audited; a private scheme is not.
- **Treat a grant as revisable, not permanent.** The system keeps the decision and the reason you gave, and people change it there; your interface must behave correctly when a permission it had is gone.
- **Precede a system permission prompt only with a screen that explains and opens it — one button, titled "Continue" or "Next".** A second action, an escape hatch, or a button titled "Allow" turns the explanation into manipulation of the choice.
- **Never dress a screen up to steal the answer to a permission prompt.** Offering an incentive, imitating the system prompt, showing a picture of it, or annotating the screen behind it are all designs meant to harvest a tap people did not mean to give.
- **Where a feature needs data once, offer a one-time share instead of a standing permission.** Apple's location button grants access at the moment of the task; the generic rule is to prefer the narrowest, shortest grant that does the job.
- **Keep the rest of the product working when a permission is refused, and never nag.** A refusal is an answer: features that do not depend on the data must keep working, and the refused feature should state what it could do if allowed rather than re-asking. [translation]
[HIG: privacy] [WWDC26-250]

### Credentials and stored data

- **Do not rely on a password alone.** Prefer passkeys; where passwords remain, add two-factor authentication, and use biometric identification to protect a session that stays signed in.
- **Store secrets in the platform's secure store, never in plain text.** File permissions are not encryption, and a keychain also gives people a predictable experience for their own secrets.
- **Do not invent an authentication scheme.** System-provided passkeys, platform sign-in and credential autofill are stronger than anything hand-rolled and are already familiar.
[HIG: privacy]

### Accounts and sign-in

- **Require an account only when core functionality genuinely needs one.** An account that is not needed is a barrier placed in front of the value the product was supposed to deliver.
- **Delay sign-in as long as possible.** People abandon products that demand an account before they have done anything useful; let them browse or try first, ask at the purchase, and in a commerce flow offer account creation after checkout rather than before it.
- **State the reason and the benefit in the sign-in view itself.** A short, friendly sentence about what the account gives them belongs where the demand is made, not in a marketing page.
- **When an account is mandatory, set it up first, then offer the ways to sign in.** Explaining the requirement, creating the account and choosing an authentication method are three steps in that order.
- **Name the authentication method in the control, and only name methods available on this device.** "Sign In with Face ID" tells people what will happen; referencing a method the hardware lacks is a dead end.
- **Do not add a product-level switch for biometric sign-in, and do not call your credential a "passcode".** Biometrics are a system setting, and "passcode" makes people think you are asking for the one that unlocks their device.
- **Offer a private sign-in option prominently.** Apple's Sign in with Apple relays a random address to the person's real inbox; give any such option a control no smaller than the other sign-in buttons and do not push it below the fold.
- **Respect a relayed or masked address: never ask for the real one.** If support flows need an identifier, show the relayed address in the product or identify the person by order number or phone number instead.
- **Do not ask for a password from someone using a passwordless identity.** The absence of a password is the feature.
- **Let people link an existing account to the private sign-in option.** They keep the data they already have and gain the convenience; suggest the link when a shared address matches, or from account settings afterwards.
- **Put people into the product the moment sign-in completes.** A welcome and the feature they came for, not a questionnaire for data that is not required yet.
- **Show the current sign-in method in account settings.** People need to know which identity they are using before they can manage it.
- **Mark additional data as required or optional, and say why.** Legal or contractual requirements must be stated as such; optional data needs a stated benefit, and declining it must not lock anyone out of their account or any other feature.
- **Ask for optional data later, in the context where it pays off.** A phone number requested at "text me when it ships" is a fair trade; the same request at sign-up is not.
- **Never ask again for data a payment or platform flow has already handed you.** A name and address collected during checkout are collected; asking a second time reads as carelessness.
- **Show people the data you received from them.** Welcoming them by the name or address they shared demonstrates the use, and data you never display invites the question of why you asked.
- **Where text entry is expensive, ask for the minimum or hand the step to another device.** On a remote, a watch or a kiosk, typing an address is punishing; suggest credentials from a nearby device or continue the sign-up on the web.
- **Let people delete the account, not merely deactivate it, from inside the product.** If deletion must happen on the web, link to it directly and do not bury the link in a policy document.
- **Keep the in-product and web deletion flows equivalent.** Making one path longer is a dark pattern with extra steps.
- **Offer scheduled deletion alongside immediate deletion, and report progress.** People may want to use up the services they have already paid for; when deletion takes time, say when it will finish and tell them when it has.
- **When law forces you to keep data, say exactly what is kept and what the process is.** Health records and similar obligations are legitimate, and describing them plainly is the difference between a constraint and a broken promise.
- **Explain what deletion does and does not do to billing.** Subscriptions billed by the platform continue until cancelled, so the flow must say what the person still has to do.
[HIG: managing-accounts, sign-in-with-apple]

## AI and machine-learning features

### Responsibility and safety

- **Interrogate the feature before building it: how could this be misused, who would be harmed, how do I prevent it.** With a model in the loop the same input can produce different output, and you cannot enumerate the requests people will make.
- **Anticipate output that causes real-world harm and design the safeguard, not the happy path.** A recipe feature that knows about a logged allergy must not be able to suggest the allergen; previews, confirmations and disclaimers help, and removing the feature is the right answer when the risk outweighs the value.
- **Test with hostile and careless input before shipping.** Out-of-scope, vague, sensitive and deliberately harmful requests are the ones that produce the incident; run them, write down the policy, and fix what they reveal.
- **Ask people for the attributes a feature needs rather than inferring them.** Models favour the most common data in their training, so inferred gender, relationships or culture arrive as stereotypes; test the feature across a diverse set of people.
- **Honour the requests that are in scope and handle sensitive material with care.** A feature that silently refuses ordinary requests, or answers a sensitive one as if it were ordinary, both break the same trust.
- **Offer a generative feature only where it delivers clear, specific value.** Time saved, communication improved, creative reach extended — a model added because it is available is a cost with no return.
[HIG: generative-ai, machine-learning] [WWDC26-250]

### Transparency and control

- **Label where the product uses AI, at the content it generated.** Nobody should be able to mistake generated content, or a conversation with a model, for the work of a person.
- **Match disclosure to the rules of every region you ship in.** Regulation on generated content differs by market and is part of the design, not a legal afterthought.
- **State up front what the feature can and cannot do.** A short introduction and a plain explanation of why poor results happen keep expectations from outrunning the model.
- **Guide the first request with example inputs.** A few diverse, predefined prompts show what the feature is for far faster than instructions do, and they raise the quality of what people ask for.
- **Say that generated content can be wrong, and scope what you ask the model to produce.** Hallucinated output arrives with the same confident surface as correct output; do not use generated content where being wrong would misinform or harm someone, and do not ask for facts the model cannot verify.
- **Keep the decision with the person: let them dismiss, revert, retry or edit anything generated.** Put those controls next to the output, and acknowledge visibly when a correction has taken effect.
- **Confirm before an irreversible or significant action taken on someone's behalf, and never automate a destructive one.** Deleting photos or making a purchase are not candidates for automation, whatever the confidence.
- **Coach people out of a blocked or poor result instead of failing silently.** Say that the request could not be used, and show an example of one that would work.
- **Offer meaningfully different alternatives where a choice helps.** Several distinct results let the person close the gap between what the model understood and what they wanted.
- **Report what is happening during generation in specific words, not "Processing…".** "Finding substitutions for ingredients" makes a real wait purposeful; for the wait itself see `references/motion-feedback-loading.md`.
- **Keep feedback on output voluntary, easy and out of the way.** A thumbs-up and thumbs-down pair with an optional detailed path is enough; never gate the experience behind rating it, and act on what you receive.
- **Give the feature a non-AI fallback wherever one is possible.** People turn these features off, models become unavailable, and the core task should survive both.
- **Treat availability as a design case, not an error case.** Device capability, network and battery can all remove a model; the screen must still make sense when it is gone.
- **Choose on-device or server processing as a privacy decision as much as a capability one.** On-device keeps information local, responds fast and works offline; when a server is required, process what you can locally, minimise what leaves, show what is shared, and say what is stored or used for training.
- **Get explicit permission before sending personal content to a model, and offer a way to opt out later.** Use the minimum data, remember that output can leak sensitive input, and check the stricter rules that apply to products aimed at children.
- **Avoid reproducing copyrighted work.** Curate inputs, prefer models with protections, and constrain prompts away from imitating a named style or source.
- **Separate the model from the experience so it can be replaced.** Capabilities move quickly; plan for fine-tuning, retesting and a new base model without redesigning the interface around it.
[HIG: generative-ai]

### Model-driven features: role, feedback and mistakes

- **Decide the feature's role before designing its UI, because the role sets the accuracy bar.** Critical or complementary, working on private or public data, proactive or reactive, visible or invisible, improving dynamically or only on update — the more central the feature and the more sensitive the data, the less forgiving people are.
- **Design the experience as an interpretation of data, not as scripted responses to a fixed set of cases.** Behaviour follows what the model receives, so expect the data and the metrics to change when the experience has to change.
- **Hold a proactive feature to a higher relevance bar than a reactive one.** Nobody asked for its results, so tolerance for a weak one is lower; that often means more data before it is worth showing at all.
- **Account for an invisible feature being unable to report its own reliability.** People who do not know the feature exists will not judge it or send feedback, so its quality has to be measured elsewhere.
- **Prefer implicit signals over asking, and when you do ask, make it voluntary.** Explicit feedback costs the person an action; request it only when behaviour cannot tell you what you need.
- **Describe each feedback option by its consequence, in plain words.** "Suggest less pop music" or "Mute politics for a week" tells people what will happen; "dislike" does not, and does not translate.
- **Do not read favouriting or reactions as answers to your question.** People use those for their own purposes, so they are implicit signals about behaviour, not explicit feedback about your results.
- **Use an icon in a feedback option only to clarify it, never as the whole option.** An icon alone cannot convey how much or for how long.
- **Act on feedback immediately and persist it.** Hidden content must stay hidden everywhere in the product, or the person learns that giving feedback is pointless.
- **Use feedback to fix when and where results appear, not only what appears.** A good suggestion at the wrong moment is still a bad experience.
- **Secure behavioural data and let people restrict its flow.** Tell people how information is gathered and shared; effects that cross from one product into another surprise people and cost trust.
- **Combine several signals before inferring intent, and prefer recent signals.** A single interaction rarely means what it looks like, and tastes change; fall back to history only when there is nothing recent.
- **Update predictions on a cadence that matches the person's mental model.** Typing suggestions should change as they type; recommendations that churn continuously make considering any one of them impossible.
- **Do not let personalisation close the world down.** Reinforcing current behaviour improves the short term and narrows the long term, and what people can reach in your product is not the whole of what they might want.
- **Withhold private or sensitive suggestions on devices people share.** Accounts and screens get handed around; a recommendation can expose what someone did not choose to disclose.
- **Re-read implicit signals after a UI change.** Moving a control changes how often it is used without changing its value, so the numbers shift for reasons that have nothing to do with preference.
- **Use calibration only when the feature cannot work without that first information.** If behaviour or one explicit question can supply it, do not make people perform a setup ritual.
- **Design calibration as a short guided task: state the benefit, collect the minimum, show the goal and progress, confirm success.** Ask once, early; avoid asking for anything people would have to look up or find physically hard to do.
- **Help immediately and without blame if calibration stalls.** Give an actionable next step; never imply the person did something wrong, and never leave them stuck.
- **Let people cancel calibration at any point and edit or delete what they gave afterwards, outside the calibration flow.** Control over the data is what makes providing it safe.
- **Assume the feature will be wrong and match the remedy to the consequence.** A bad keyboard suggestion is an annoyance; a route that misses a flight is not, and the correction tools must be proportionate.
- **Make frequent and predictable mistakes trivial to correct, with the same controls the feature used.** Showing which control produced the automated result lets people refine or undo it without learning anything new.
- **Give a correction immediate effect, persist it, and allow a correction of the correction.** Making people redo the same fix is the fastest way to lose them.
- **Prefer guided corrections over freeform ones.** A list of alternatives costs less effort than a blank field; offer freeform where the person's intent genuinely cannot be enumerated.
- **Never treat correction as a substitute for quality.** If fixing the output is more work than doing the task by hand, people stop using the feature.
- **Take extra care with proactive features.** Nobody asked for them, so their mistakes feel intrusive and read as a loss of control.
- **Address a mistake without adding UI wherever you can.** A correction affordance disappears into the interface; an attribution that is itself wrong multiplies the original error.
- **Check what reducing one class of mistake does to the others.** Improving recognition of one thing often degrades another, so track overall accuracy, not the case you were staring at.
- **Learn from a mistake only when learning improves results.** Some corrections encode a one-off, and training on them makes behaviour less predictable.
- **Keep the number of presented options small, diverse, ordered with the most likely first, and easy to tell apart.** Every extra option is evaluation work; where options look alike, describe the difference rather than listing them.
- **Select the first option by default when that speeds people up, and group options into scannable categories when there are too many for one view.** Both reduce the reading a choice costs.
- **Show confidence only when you have verified that it tracks quality, and translate it into something people can act on.** "Because you've read mysteries" beats "97% match"; semantic bands like "high chance" beat raw numbers except where numbers are the subject, as in weather or sport.
- **Change the presentation at different confidence bands.** High confidence can show the result outright; lower confidence should ask the person to confirm before the product acts on it.
- **Suppress low-confidence results in proactive features.** Set a threshold below which the feature says nothing rather than guessing out loud.
- **Keep attributions factual, neither too specific nor too general, and free of jargon.** "Because you've read nonfiction" reasons about a result; "Because you love nonfiction" claims to know a feeling, and an over-precise attribution reads as surveillance.
- **Name the limitations where they will be met.** Set expectations before use when a rare limitation has serious effects, demonstrate how to get good results — placeholder text that shows what can be asked — explain why a poor result happened, and suggest an alternative route instead of showing nothing.
- **Steer people mid-interaction when conditions are spoiling the result.** Saying "move closer" or "more light" while they are using the feature beats reporting a failure after it, and it teaches the limitation instead of hiding it.
- **Tell people when a limitation is lifted.** They have already learned to avoid that interaction and will not come back to it on their own.
[HIG: machine-learning, generative-ai]

## Translation to web and other platforms

Every rule in this section is this skill's translation of the guidance above to the web and to web-hosted shells; none of it is Apple's wording.

- **Use the native element before reaching for a role.** A real button, link, input and heading carry name, role, state and keyboard behaviour for free; `role=` plus handlers reimplements them badly. [translation]
- **Give every control an accessible name.** A visible label wired with `for`/`id` where possible, `aria-label` or `aria-labelledby` for icon-only controls, and never a name that exists only as a placeholder. [translation]
- **Expose state as well as name.** `aria-expanded`, `aria-current`, `aria-invalid` and `aria-describedby` for the error text are how the non-visual version of a control stays in step with the visual one. [translation]
- **Structure the page with one `h1`, a nested heading order and landmark regions.** This is the web form of unique titles and accurate section headings, and it is what screen-reader navigation traverses. [translation]
- **Announce dynamic changes with a polite live region, or move focus to the new content.** An updated total, a validation summary or a toast that only appears visually does not exist for a screen reader; see `references/modality-alerts-notifications.md`. [translation]
- **Announce route changes in a single-page app.** Set the document title and move focus to the new view's heading, since no page load tells assistive technology that anything happened. [translation]
- **Mark decorative images `alt=""` and give meaningful ones real alternative text.** For a chart, expose the underlying numbers as a table or an accessible summary beside it. [translation]
- **Size type in relative units and let the layout reflow at 200 percent zoom; never disable user scaling.** `maximum-scale` or `user-scalable=no` in the viewport tag removes the main text-scaling mechanism the web has. [translation]
- **Keep targets, spacing and focus order intact when the layout reflows to one column.** Heavy zoom and narrow viewports are the same case, and controls that overlap or reorder there fail exactly the people who need them. [translation]
- **Honour `prefers-reduced-motion`, `prefers-contrast`, `prefers-reduced-transparency`, `prefers-color-scheme` and `forced-colors`.** These are the browser's channel for the same system settings the platform rules assume. [translation]
- **Keep the same 44×44 hit region in CSS pixels, with clear gaps between regions.** Pointer precision is not a property of the device class; a laptop with a touchscreen has both. [translation]
- **Keep a visible focus ring, a DOM order that matches the visual order, no focus traps, an Escape that closes what it opened, and a skip link to the main content.** Removing the outline without replacing it is the most common keyboard-accessibility defect on the web. [translation]
- **Group related choices in a `fieldset` with a `legend`, and never force a choice that excludes people.** A required gender or title field with two options is the usual offender; add a decline option or drop the field. [translation]
- **Set `lang` on the document and on any span in another language, and drive direction with `dir` and logical CSS properties.** `margin-inline-start`, `padding-inline`, `inset-inline` and `text-align: start` mirror automatically; `left` and `right` do not. [translation]
- **Do not mirror with `transform: scaleX(-1)` on photographs, logos or marks.** Mirror the layout, and supply a separate asset when an image genuinely must change. [translation]
- **Ask in the page before triggering a browser permission prompt, and trigger it from a real user gesture.** Browser prompts carry no purpose string, so the explanation has to be in your own UI, and a prompt fired on load is usually dismissed for good. [translation]
- **Delay the notification permission request until the person has asked for something that needs it.** A push prompt on first paint trains people to deny by reflex. [translation]
- **When a permission is already blocked at browser level, explain the state and how to change it.** The browser will not ask again, so re-calling the API does nothing visible and looks like a broken button. [translation]
- **Keep consent decisions per feature and show them in the product's own settings.** People who cannot see what they agreed to cannot revise it. [translation]
- **Use `autocomplete` tokens on credential and address fields, prefer WebAuthn passkeys, and keep tokens out of `localStorage`.** This is the web form of not inventing an authentication scheme; see `references/forms-and-data-entry.md`. [translation]
- **Ship captions as a `<track kind="captions">`, put a transcript beside long-form media, and never autoplay with sound.** Muted autoplay still needs a visible control that stops it. [translation]
- **Put the label on generated content next to the content, not only in a page footer.** A global "AI-assisted" notice does not tell anyone which paragraph came from a model. [translation]
- **Make account deletion reachable from account settings inside the product.** A deletion that requires emailing support is a deactivation flow wearing a different word. [translation]
- **Drive the finished page once with the keyboard alone and once with a screen reader before calling the change done.** Both passes take minutes and catch the defects that no static reading of the markup will; see `references/review-checklist.md`. [translation]
- **In an Electron or Capacitor shell, ask in the web layer before the OS prompt appears, and respect the accessibility settings the host exposes to the webview.** The shell inherits the host platform's permission model and its accessibility settings; the content inside follows the rules above. See `references/platforms-and-web.md`. [translation]

## Deliberately omitted

- **visionOS comfort guidance** (field of view, head-anchored content, peripheral motion, large repetitive gestures) — headset ergonomics with no equivalent on a screen; per-platform material lives in `references/platforms-and-web.md`. [HIG: accessibility]
- **Accessibility Nutrition Labels, App Store privacy details and App Store Connect metadata** — store-submission declarations, not interface design. [HIG: accessibility, privacy]
- **Location button appearance options** (title variants, filled or outlined glyph, corner radius, low-contrast warnings) — the API surface of one Apple control; the generic rule, a one-time share at the moment of need, is kept. [HIG: privacy]
- **Sign in with Apple button construction** (140×30 pt minimum, logo artwork and padding, black and white variants, title capitalisation, custom-button rules) — Apple brand-asset rules that do not generalise; the private-sign-in behaviour is kept. [HIG: sign-in-with-apple]
- **TV provider system-level accounts and tvOS sign-out routing** — account plumbing specific to one device class. [HIG: managing-accounts]
- **macOS Developer ID signing, app sandboxing and fast user switching; visionOS ARKit permissions and camera behaviour** — distribution and platform mechanics rather than interface rules. [HIG: privacy]
- **Named Apple accessibility integrations** (Siri and Shortcuts, Music Haptics, Audio Graphs, the VoiceOver rotor API, the braille keyboard) — their design intent is kept as the generic rules on voice and automation, non-visual channels and navigating by element type; the integrations themselves are Apple-only. [HIG: accessibility, voiceover]
- **Dataset and model engineering** (dataset curation and licensing, retraining cadence, Foundation Models availability) — model-build practice, not interface design; the parts people see — bias testing, disclosure, fallback, replaceability — are kept. [HIG: generative-ai]
- **Loading and latency treatments for generation** — the rule that a real wait needs specific feedback is kept here; skeletons, determinate progress and background generation belong to `references/motion-feedback-loading.md`. [HIG: generative-ai]

## Sources

- design-principles — https://developer.apple.com/design/human-interface-guidelines/design-principles
- accessibility — https://developer.apple.com/design/human-interface-guidelines/accessibility
- buttons — https://developer.apple.com/design/human-interface-guidelines/buttons
- inclusion — https://developer.apple.com/design/human-interface-guidelines/inclusion
- right-to-left — https://developer.apple.com/design/human-interface-guidelines/right-to-left
- privacy — https://developer.apple.com/design/human-interface-guidelines/privacy
- voiceover — https://developer.apple.com/design/human-interface-guidelines/voiceover
- managing-accounts — https://developer.apple.com/design/human-interface-guidelines/managing-accounts
- sign-in-with-apple — https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple
- generative-ai — https://developer.apple.com/design/human-interface-guidelines/generative-ai
- machine-learning — https://developer.apple.com/design/human-interface-guidelines/machine-learning
- WWDC26-250, «Principles of great design» — https://developer.apple.com/videos/play/wwdc2026/250/

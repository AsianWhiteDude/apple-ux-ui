# Forms and data entry

This file covers everything between a person and a field: how much to ask for, which control fits which decision, how labels and hints are written, when to validate, how to handle sensitive input, how not to lose what was typed, and how undo and redo make entry safe to attempt. Load it when you design or review a form, a settings pane, a wizard, an editor, a sign-up or a checkout flow, or any screen that collects values. It serves **Agency** above all (freedom to act, recovery from mistakes, no trap), then **Simplicity** (ask only what is necessary, every field earns its place), **Familiarity** (standard controls that behave as people already expect), **Flexibility** (every input method: typing, choosing, pasting, dictating, handwriting), and **Responsibility** wherever the data is personal. Every rule below is an instance of one of those principles; where a rule is this skill's own extension to the web or to non-Apple platforms it is tagged `[translation]` and is not presented as Apple's guidance.

## Ask for the minimum

### Cut fields before you style them

- **Fetch what you can instead of asking for it.** Do not ask for anything the system, the account, or an already-granted permission can supply — settings, location, calendar, contact details. Ask permission for the source when that is cheaper for the person than typing. `[HIG: entering-data]`
- **Treat every added field as a bill sent to the person.** Each one asks for time, attention and trust, so deciding what to collect is mostly deciding what to leave out. `[WWDC26-250]`
- **Count the steps, then remove some.** A concise interface respects time by reducing how many actions a task takes; two screens that could be one are a design defect, not a preference. `[WWDC26-250]`
- **Get people to the task instead of through a preamble.** The most helpful thing an interface usually does is put the person directly on the task or content at hand; an entry flow that front-loads explanation is in the way. `[HIG: design-principles]`
- **Look at how the task is already solved before inventing a flow for it.** Study the existing solutions rather than re-creating them, and let what actually differentiates the product show in the design. `[HIG: design-principles]`
- **Prioritise the fields that match how people actually use the product.** Focus comes from aligning with the main use, not from collecting everything a stakeholder can imagine wanting. `[HIG: design-principles]`
- **Offer a choice instead of a text field whenever the set of valid answers is known.** Picking from a list is faster and less error-prone than typing, even with a keyboard at hand; use a picker, a menu or another selection control. `[HIG: entering-data, text-fields]`
- **Accept pasting and dropping into every field that holds data people already have somewhere else.** Supporting both removes retyping and makes the interface feel part of the system rather than a walled form. `[HIG: entering-data]`
- **Prefill fields with reasonable defaults.** A sensible default removes a decision and speeds entry; a prompt in the field such as `username@company.com` shows the expected shape at the same time. `[HIG: entering-data]`
- **Cut typing hard on any device where typing is slow.** Long passages or many fields are painful on a TV remote or a watch-sized screen (Apple's examples); gather the same information with buttons or lists, and show a text field only when nothing else will do. `[HIG: text-fields]`
- **Mark required data as required and gate the step on it, rather than failing a submit.** Keep a Next or Continue button unavailable until the required values are present, so the requirement is visible before the person commits to it. `[HIG: entering-data]`
- **Add a step only when it removes a worse cost.** Simplicity sometimes means adding information rather than removing it — a summary or review before a consequential submit tells people what they are about to commit to. `[WWDC26-250]`
- **Design the safeguards for entry that can cause real harm.** Ask what happens when a value is wrong or a generated suggestion is wrong, and answer with previews, confirmations or removing the feature — not with hope. `[WWDC26-250]`

## Labels, hints and field shape

- **Give every field a visible label, not just a placeholder.** Placeholder text disappears the moment typing starts, so a field carrying only a placeholder loses its meaning exactly when the person needs it; keep a separate label beside or above the field and use the placeholder for the hint. `[HIG: text-fields, entering-data]`
- **Use the placeholder or an introductory label to show the expected format.** Show the shape of the answer (`username@company.com`, a date pattern) instead of describing it in a sentence. `[HIG: entering-data, text-fields]`
- **Choose exactly the words a label needs and no more.** The shortest accurate label is usually the most universal and the most helpful; a label that hedges makes the field ambiguous. `[HIG: design-principles]`
- **Make the form state where a person is and what comes next.** Hierarchy, recognisable controls and a consistent structure are what tell people how to reach the outcome. `[HIG: design-principles]`
- **Make the primary action the most obvious element on the screen.** A clear layout answers three questions — what to attend to, what is interactive, how to interact — with order, spacing and contrast. `[WWDC26-250]`
- **Size a field to the amount of text you expect.** Field width is a signal people read: a short field asks for a short answer. Keep widths consistent for fields of the same kind and vary them only where the content genuinely differs. `[HIG: text-fields]`
- **Space stacked fields far enough apart that each label clearly belongs to one field.** Stack vertically where the layout allows, and keep the group aligned so the form reads as one column rather than a grid of boxes. `[HIG: text-fields]`
- **Introduce a group of controls with one label when the relationship is not self-evident.** A label above a checkbox group, a slider or a combo box states what the whole set is about; align it with the first control in the group. `[HIG: toggles, sliders, combo-boxes]`
- **Use a single-line field for small specific values and a multi-line text view for prose.** A name, an address line or an email belongs in a text field; anything paragraph-shaped needs a text view. `[HIG: text-fields]`
- **Decide what happens to text longer than the field — clip, wrap or truncate — then give people a way to read the rest.** On pointer platforms an expansion tooltip on hover shows the full value of a clipped field; on any platform, never let truncation be the only state in which a value is ever seen. `[HIG: text-fields, entering-data]`
- **Show a clear affordance for erasing a field.** A clear control at the trailing end of a field beats holding the delete key, especially on touch. `[HIG: text-fields]`
- **Use the two ends of a field for different jobs.** The leading end indicates what the field is for; the trailing end offers extra functions such as clearing the field or bookmarking (Apple's examples). Keep that division consistent across the form. `[HIG: text-fields]`

### Where form controls live

- **Keep form controls in the content area, not in the window chrome.** Switches, checkboxes and radio buttons belong in the body of a window or view; putting them in a toolbar or a status bar confuses a setting with an action. `[HIG: toggles]`
- **Put the same control in the same place on every step and every screen.** Consistent placement is what lets people act without looking for the control first; a submit button that moves between steps costs them attention on every step. `[WWDC26-250]`
- **Space a horizontal group of options by its longest label and apply that spacing to all of them.** Uneven gaps make a set of options read as unrelated controls. `[HIG: toggles]`
- **Do not reassign the meaning of a control or icon people already know.** A familiar symbol used for an unfamiliar action removes recognition instead of adding personality; for common actions, use the metaphor people already hold. `[WWDC26-250]`
- **Use the same control for the same kind of decision throughout the product.** Once an appearance or a behaviour is established, apply it everywhere; that consistency is what lets people predict a control they have not met yet. `[HIG: design-principles]`
- **Keep controls in predictable positions as the layout adapts, and ease the change with natural transitions.** Preserving context is what makes a form feel like the same product at another size or on another platform. `[HIG: design-principles]`
- **Make a form survive rotation and window resizing.** A layout that breaks when the device turns reads as fragile and makes people doubt the whole product; check a half-filled form at every size you support. `[WWDC26-250]`
- **Let people who use a long form often reshape it.** No single arrangement of many controls fits everyone; where the workflow is repetitive, letting people reorder or hide the controls they never use is worth the investment. `[WWDC26-250]`

## Choosing the control

### Pick by the shape of the decision

- **Two opposing states for one thing → a toggle**: a switch where it reads as a setting, a checkbox where settings nest. `[HIG: toggles]`
- **One of two to about five labelled, mutually exclusive options → radio buttons.** `[HIG: toggles]`
- **One of a few closely related options that change one object, state or view → a segmented control.** `[HIG: segmented-controls]`
- **One of many known values → a pull-down button for a short list, a picker for a medium-to-long one, a searchable list or table for a very large one.** `[HIG: pickers]`
- **A known value or a custom one → a combo box**, a field paired with a list. `[HIG: combo-boxes]`
- **A value in a continuous range where the result matters more than the number → a slider**; add a field when the exact number matters too. `[HIG: sliders, steppers]`
- **Small incremental changes to a number that is already displayed → a stepper beside that field.** `[HIG: steppers]`
- **Free text → a text field for a short specific value, a text view for prose.** `[HIG: text-fields]`

### A pair of opposing states

- **Use a toggle only for state — on or off — that affects content or a view.** If the decision is "which of these", it is not a toggle; use a pop-up button or another selection control instead. `[HIG: toggles]`
- **Make it unmistakable which setting a toggle governs.** Usually the surrounding row supplies that context; when it does not, add a label naming the state being controlled. `[HIG: toggles]`
- **Make the on and off appearances differ in more than colour.** Add or remove a fill, a shape or an inner mark such as a checkmark or a dot, because not everyone can perceive a colour difference. `[HIG: toggles]`
- **Prefer a checkbox to a switch when settings form a hierarchy.** Checkboxes align and indent well, so a parent checkbox can visibly govern subordinate ones; a switch carries more visual weight and suits a setting you want to emphasise or a group-level power switch (Apple's macOS forms). `[HIG: toggles]`
- **Show a mixed state when a parent control's children disagree.** A control that governs several subordinate checkboxes needs a third appearance for "some on"; rendering partial state as off misreports the data. `[HIG: toggles]`
- **Do not swap an existing checkbox for a switch.** Once a control is established in an interface, changing its form costs people their learned pattern for no functional gain. `[HIG: toggles]`
- **Do not put a radio button into a mixed state.** Additional options, or a checkbox, express partial state more clearly than a dash in a circle. `[HIG: toggles]`
- **Where a state belongs on a button rather than in a row, let the button carry the state.** An icon button with a distinctly different background when active reads as on or off without a separate label; keep the two appearances obviously different. `[HIG: toggles]`
- **If you recolour a switch, keep the two states clearly distinguishable.** A brand accent is acceptable in place of the system colour only when it still contrasts with the off appearance. `[HIG: toggles]`

### One of a few

- **Use radio buttons for two to about five mutually exclusive options, each with its own label.** They make every option readable at once; beyond roughly five they eat the layout, so move to a pop-up button. `[HIG: toggles]`
- **Express a single on/off setting as one checkbox, not one radio button.** The presence or absence of the checkmark states the current value at a glance. `[HIG: toggles]`
- **Use a segmented control for closely related choices that affect one object, state or view.** It keeps the group intact regardless of view size and shows the current selection at a glance. `[HIG: segmented-controls]`
- **Keep a segmented control to one type: selection state or actions, never both.** Mixing a selectable segment with an action segment in the same control destroys the pattern people just learned from it. `[HIG: segmented-controls]`
- **Cap a segmented control at about five to seven segments, and about five on a phone-sized screen.** More segments are hard to parse and slow to hit. `[HIG: segmented-controls]`
- **Use either text or icons in one segmented control, and keep segment content similar in size.** Segments are usually equal width, so mixed content types and wildly different widths look broken. Label segments with nouns or noun phrases. `[HIG: segmented-controls]`
- **Explain icon-only segments.** Add introductory text, a label under each segment, or a hover or gaze tooltip, because a row of bare icons is a guessing game. `[HIG: segmented-controls]`
- **Use a segmented control to switch between closely related subviews, not between the main sections of a product.** Top-level sections belong in tabs or a sidebar — see `references/layout-and-navigation.md`. `[HIG: segmented-controls]`
- **On desktop, switch views in the main content area with a tab view, not a segmented control,** and keep segmented controls for toolbars and inspector panes. `[HIG: segmented-controls]`

### One of many

- **Use a picker for a medium-to-long list of values, something lighter for a short one and something searchable for a very long one.** A short list is better served by a pull-down button, and a very large set by a list or table that can scroll, index and be filtered. `[HIG: pickers]`
- **Order the values so people can predict what is hidden.** Much of a picker's content is off-screen, so an alphabetised or otherwise obvious order lets people travel to a value instead of hunting for it. `[HIG: pickers]`
- **Show the picker next to the value it edits instead of switching views.** Present it in place, in a popover or at the edge of the window near the field, so the person keeps the context they are editing. `[HIG: pickers]`
- **When space is tight, show the current value as a control that opens the full editor.** A compact trigger displaying today's date, which expands into a calendar and time editor, costs one line instead of a wheel stack. `[HIG: pickers]`
- **Match the date control to the job: typing a known date, or browsing for one.** A textual control suits specific known values in little space; a calendar-style control suits browsing days or picking a range. `[HIG: pickers]`
- **Coarsen granularity when precision is not wanted.** A minute list does not have to offer all sixty values; an interval that divides evenly into sixty (quarter hours, five minutes) is faster and still exact enough. `[HIG: pickers]`
- **Ask only for the components of a compound value you need.** Apple's date controls come in date, time, date-and-time and countdown modes; a time you will discard is a field you did not need. `[HIG: pickers]`
- **Let people adjust every part of a compound value before it commits.** In a compact date editor, day and time are edited together and confirmed by leaving the editor, so nothing is stored half-changed. `[HIG: pickers]`
- **Let the locale decide the order and presentation of date and time components.** Which components appear and in what order depends on the language and region, so never hard-code a component order. `[HIG: pickers]`
- **Use a combo box — a field plus a list — when most people will pick a known value but some need their own.** Populate the field with a meaningful default drawn from the list (it need not be the first item), and keep list items no wider than the field so nothing is truncated. `[HIG: combo-boxes]`
- **Seed that list with the most likely values.** People value the convenience of the common choices as much as the freedom to type something else. `[HIG: combo-boxes]`

### A value in a range

- **Keep the low end of a slider where people expect it: leading side for horizontal, bottom for vertical.** The direction is a cross-app convention; inverting it makes every value read backwards. `[HIG: sliders]`
- **Pair a slider with a numeric field, and a stepper, when the range is wide or the exact value matters.** The slider gives the coarse move, the field the exact number, the stepper the single increment. `[HIG: sliders, steppers]`
- **Let the slider's ends say what the value means.** Small and large icons at the two ends, or a short label, communicate the dimension being changed without a legend. `[HIG: sliders]`
- **Add tick marks, and label at least the extremes, when people need to locate a specific value.** Labels can be numbers or words; label intermediate ticks only where the scale is non-linear or otherwise confusing. `[HIG: sliders]`
- **Update the affected content live as the slider moves.** Seeing the result while dragging is what makes a slider better than a number field. `[HIG: sliders]`
- **Use a circular slider only for values that wrap or continue indefinitely,** such as an angle or a rotation count; use a linear slider between a fixed start and end. `[HIG: sliders]`
- **Never leave a stepper without a visible value next to it.** The control shows no value of its own, so the field or label it changes must be unambiguous. `[HIG: steppers]`
- **Offer a coarse increment when the range is large.** A modifier that steps by a larger multiple (Apple's macOS convention is Shift-click for ten times the increment) saves dozens of clicks. `[HIG: steppers]`

### Specialised values

- **Use the platform's own colour picker for colour input.** A system picker gives a familiar interface and, on Apple platforms, a palette people have saved across apps; accept colours dropped onto the well too. `[HIG: color-wells]`
- **Confirm that a colour control is active, and show the chosen colour in it afterwards.** Highlight on activation and update the swatch on selection, so the control itself reports the current value. `[HIG: color-wells]`
- **Use a token field where a field holds a list of entities rather than free text.** Convert text into a selectable token (recipients, tags, filters), suggest matches as people type, and attach a context menu to each token for editing and detail. `[HIG: token-fields]`
- **Offer more than one way to commit a token, and delay suggestions slightly.** A separator character and Return should both turn text into a token; suggestions that appear on the first keystroke distract people mid-word. `[HIG: token-fields]`
- **Make an image slot editable in the ways people expect of one.** Support dragging an image in, copy and paste with the standard menu items and shortcuts, and deletion; restore the default image when the slot is cleared and cannot be empty. `[HIG: image-wells]`
- **Give code and PIN entry its own focused screen with a stated purpose.** State in a title and prompt why the digits are needed, obscure the digits as they are entered, and use a digit-only keyboard. Apple's form is the tvOS digit entry view; the generic equivalent is a full-screen PIN or one-time-code step. `[HIG: digit-entry-views, entering-data]`

## Keyboards and input methods

- **Support every input method the device offers rather than optimising for one.** People choose typing, selecting, pasting, dictating, pointing or handwriting by situation, and supporting the range is what makes a form usable by more people. `[HIG: entering-data, design-principles]`
- **Let people dictate wherever they can type.** Voice is one of the input methods Apple names alongside touch and keyboard; a field that cannot be filled by speaking excludes everyone who works that way. `[HIG: design-principles]`
- **Show the keyboard that matches the content.** Declare the field's semantic content type so the system can present the right keys — numbers, email, URL, phone — and refine its corrections; a numeric field with an alphabetic keyboard is a defect, not a detail. `[HIG: virtual-keyboards, text-fields]`
- **Prefer a keyboard whose keys are optimised for the task.** An email field earns the `@` and `.com` keys; a quantity field earns a number pad. The saving is per character, so it compounds. `[HIG: virtual-keyboards]`
- **Label the confirm key with the action it performs.** When a field starts a search, the Return key should say so, so the last step of entry is not a guess. `[HIG: virtual-keyboards]`
- **Keep the focused field and its neighbours visible when an on-screen keyboard appears.** Use the platform's keyboard layout guidance so the layout moves with the keyboard instead of hiding the field being filled. `[HIG: virtual-keyboards]`
- **Place any accessory controls above the keyboard only when they serve the current task,** and position them with the platform's layout guidance so they sit where people expect them. `[HIG: virtual-keyboards]`
- **Replace the standard keyboard only when a custom input view is self-evidently better for the task,** as a spreadsheet's numeric pad is; otherwise people will wonder why they cannot get their keyboard back. Keep the feedback they expect, including the standard key sound the system lets them silence globally. `[HIG: virtual-keyboards]`
- **Do not duplicate keys the system already provides.** The emoji, globe and dictation keys stay the system's, and repeating them leaves people unsure which one works. `[HIG: virtual-keyboards]`

### Handwriting and stylus entry

- **Let handwriting work wherever text is accepted, with no mode to enter first.** A person should be able to write straight into a field, search box or editable area without tapping a tool first; password fields are the exception. `[HIG: apple-pencil-and-scribble]`
- **Accept the mark the instant the stylus touches the screen.** Requiring a button press or a mode change before a stroke registers breaks the one metaphor a stylus has. `[HIG: apple-pencil-and-scribble]`
- **Make every control respond to the same pointer that marks.** If a stylus can draw but cannot press your buttons, the controls look broken or the device looks dead. `[HIG: apple-pencil-and-scribble]`
- **Hold the field still while someone is writing in it.** Do not move, resize or autoscroll a field mid-stroke — that feels like losing control of where the input is going; defer any layout change until the person pauses. `[HIG: apple-pencil-and-scribble]`
- **Give handwriting room, and get out of its way.** Enlarge a small field before writing begins rather than during it, hide placeholder text as soon as a stroke lands, and suppress inline autocompletion that would overlap the handwriting. `[HIG: apple-pencil-and-scribble]`
- **Make the stylus manipulate what it touches, and nothing elsewhere.** Feedback must appear under the tip immediately; an action that fires on a distant part of the screen reads as a malfunction. `[HIG: apple-pencil-and-scribble]`
- **Never let an imprecise input commit a change.** Hover, squeeze and double-tap gestures fire accidentally, so bind them to previews and mode switches, not to actions that modify or destroy content; if such a gesture does change content, it must be trivially undoable. `[HIG: apple-pencil-and-scribble]`
- **Preview with a representative value, not an extreme one.** A hover preview of a mark or a value is most informative near the middle of its range; the extremes are either invisible or occlude what they describe. `[HIG: apple-pencil-and-scribble]`
- **Respect the person's system-level gesture settings, and never turn a custom gesture mode on by default.** If you add one, make the current mode visible so your response never looks random. `[HIG: apple-pencil-and-scribble]`
- **Design the entry area for both hands.** Do not park controls where a writing hand will cover them, and let people move them when you cannot be sure. `[HIG: apple-pencil-and-scribble]`

## Validation and errors

- **Validate as people go, not when they press submit.** Checking each value as it is entered and reporting the problem immediately lets people fix it in place; a lengthy form that reveals all its objections at the end is the failure case Apple names. `[HIG: entering-data]`
- **Pick the validation moment per field.** Some values are only judgeable once the field is left (an email address), and some must be judged before the person leaves it (a new user name or password, whose rules constrain what may be typed at all). `[HIG: text-fields]`
- **Constrain the input instead of complaining about it wherever you can.** A numeric formatter that accepts only digits — and displays the value with the right decimals, percentage or currency — prevents a whole class of errors; but never assume one presentation, because formatting varies by locale. `[HIG: entering-data, text-fields]`
- **Say what happened, where, and what to do, in a neutral voice.** Name the situation specifically and usefully; "Error" or an error number tells the person nothing, and an oblique or accusatory tone makes a fixable problem feel like a wall. Full wording rules are in `references/writing-help-onboarding-settings.md`. `[HIG: alerts]`
- **Do not raise an alert for something the field itself can say.** An interruption that carries information but no action is resented; show the problem next to the value it concerns. Interruption rules live in `references/modality-alerts-notifications.md`. `[HIG: alerts]`
- **Give a confirmation button a name that states what it does.** "Delete", "Erase", "Convert" tell people what they are agreeing to; a generic acknowledgement leaves it ambiguous whether they are accepting or merely acknowledging. `[HIG: alerts]`
- **Report availability and change as they happen.** Show which controls are currently available, and signal when content changes as a result of entry, so nobody has to guess whether an action registered. `[HIG: design-principles]`
- **Make a control respond the moment it is used, even when the work behind it takes time.** A button that goes quiet before acknowledging input is exactly what a rushed product feels like; progress and latency rules are in `references/motion-feedback-loading.md`. `[WWDC26-250]`
- **State a field's rules before people can break them,** such as password requirements shown next to the field rather than revealed by a rejection. `[translation]`
- **Let people reveal what they typed into an obscured field when they choose to,** so a mistyped credential is fixable without retyping it blind. `[translation]`
- **Make focus move between fields in the order people read them.** Tab order that jumps around a form breaks keyboard and assistive-technology entry alike; verify it rather than trusting the default. `[HIG: text-fields]`

## Sensitive data

- **Obscure sensitive input as it is typed.** Use a secure field that shows one placeholder mark per character for passwords and similar data, and secure digit entry for codes. `[HIG: entering-data, digit-entry-views]`
- **Never prefill a password field.** Require the person to enter it, or authenticate with biometrics or the system credential store. `[HIG: entering-data]`
- **Assume someone else can see the screen.** Apple states one platform behaviour here: in visionOS the system-provided text field shows entered data to the wearer only, and a secure text field blurs automatically when people use AirPlay to stream their content. `[HIG: entering-data]`
- **Treat mirroring, projection and screen sharing on every other platform as unmasked.** iOS, iPadOS and macOS send a secure field to an external display, a projector or a video call exactly as it renders, so hide or blank sensitive fields yourself while a session is streamed, recorded or shared, and never leave a credential on screen when someone is about to share it. `[translation]`
- **Ask for personal data at the moment it is needed, with the reason stated.** A request fired at launch, before the product has shown what it does, is the interface equivalent of demanding a stranger's phone number; wait for the moment, ask only for what is necessary, and say what it is for. `[WWDC26-250]` `[HIG: design-principles]`
- **Say what you collect and how it will be used, at the point of collection.** Being clear about intentions from the first interaction is what earns the permission you are about to request. `[HIG: design-principles]`
- **Collect only what the product needs to function, and handle it as if it could be misused.** Fewer stored fields is fewer ways to harm someone; anticipate the misuse before you ship the field. Broader privacy and consent rules are in `references/accessibility-inclusion-privacy.md`. `[HIG: design-principles]`
- **Put a field inside an interruption only when input is what resolves it.** An alert may carry a field to unlock or authenticate; it is not a place to collect data you could have asked for in the flow. `[HIG: alerts]`

## Never lose what people typed

- **Treat entered data as preserved unless the person cancels or deletes it.** Save periodically while they work, and when the view closes or the app goes to the background, rather than making saving something they must remember. `[HIG: file-management]`
- **Confirm before closing a view that would discard typed content.** Whether the person used a dismiss gesture or a button, explain what would be lost and offer a way to keep it, such as saving. `[HIG: modality]`
- **Show that there are unsaved changes whenever saving is manual.** If explicit saving exists at all, its state must be visible in the window or title, so nobody closes the view on a wrong assumption. `[HIG: file-management]`
- **Keep entry short and single-path when it happens in a modal view.** A modal data-entry task that grows into a hierarchy makes people lose the context they suspended; keep one path through it, and one obvious exit. `[HIG: modality]`
- **Present a form modally only when modality buys something.** Modality suspends the person's context and demands an action to leave, so a form that could live in place should live in place. `[HIG: modality]`
- **Do not place a button where it can be mistaken for the one that dismisses the view.** Inside a modal entry task, a mis-hit on the way out is precisely where typed data disappears. `[HIG: modality]`
- **Name the task in the modal view that hosts the entry.** A title that says which task this is lets someone who was interrupted mid-form find their place again. `[HIG: modality]`
- **Keep entered values through a rotation, a window resize or a switch to another app and back.** `[translation]`

### Multi-step entry

- **State the number of steps and the current position before the first step, not after it.** `[translation]`
- **Let people move back a step without discarding what they entered, and forward again without retyping.** `[translation]`
- **Validate each step as the person leaves it, so a problem never surfaces two steps later.** `[translation]`
- **Persist partial entry outside the view's lifetime** — a draft that survives a reload, a crash or a switch to another task — because a long form is exactly where loss hurts most. `[translation]`
- **Keep one decision per step rather than splitting one decision across steps,** so that going back never means unpicking half an answer. `[translation]`
- **Make a guided flow skippable and escapable.** People should not be locked into a sequence of steps or modes; offer a way through to the main experience at every step. `[HIG: design-principles]`

## Undo and redo

- **Make actions reversible so exploration is safe.** People accidentally send, change and delete things; forgiveness through easy undo is what makes them feel free to try, and confident they can recover. `[WWDC26-250]` `[HIG: design-principles]`
- **Name the action in the undo and redo affordance.** "Undo Typing" or "Redo Bold" lets a person predict the outcome; a bare "Undo" invites repeated undoing until something visibly changes. `[HIG: undo-and-redo]`
- **Show the result of an undo.** If the restored or reverted content is off-screen, scroll to it or highlight it — otherwise the undo looks like it did nothing and gets repeated until real damage is done. `[HIG: undo-and-redo]`
- **Allow many levels of undo.** People expect to walk back every action since a logical boundary such as opening or saving; an arbitrary limit is a defect, not a safeguard. `[HIG: undo-and-redo]`
- **Collapse a run of related micro-adjustments into one undo step,** and offer a way to revert everything since the last boundary, so nobody has to undo forty slider nudges one at a time. `[HIG: undo-and-redo]`
- **Prefer the platform's own undo affordances and shortcuts to your own buttons.** Support the standard shortcut and menu location first (on macOS, undo and redo at the top of the Edit menu, Command-Z and Shift-Command-Z); add visible undo buttons only where the platform offers no route, and then use the standard symbols in a toolbar. `[HIG: undo-and-redo]`
- **Do not redefine a standard undo gesture.** Reusing a gesture the system has already assigned to undo makes the whole interface unpredictable. `[HIG: undo-and-redo]`
- **When undo is triggered by an ambiguous gesture, name what will be undone and let people cancel.** A shake or a multi-finger swipe is easy to perform by accident, so it should propose the undo rather than perform it silently. `[HIG: undo-and-redo]`
- **When the surrounding chrome cannot host undo in a compact layout, put undo and redo in a toolbar** and keep the standard gesture working as well. `[HIG: apple-pencil-and-scribble, undo-and-redo]`
- **Do not confirm a common, expected, undoable action, even a destructive one.** Deleting a message is the point of pressing delete; confirming it every time trains people to dismiss dialogs unread. Confirm the uncommon and the irreversible instead. `[HIG: alerts]`
- **Double-check a genuinely destructive action, and interrupt only for a big mistake.** An interruption spent on a small risk buys nothing when the large one arrives. `[WWDC26-250]`

## Translation to web and other platforms

Everything in this section is this skill's own mapping, not Apple guidance.

- **Set the input type and `inputmode` so mobile browsers show the right keyboard,** and `enterkeyhint` so the confirm key names the action (`search`, `send`, `next`, `done`). `[translation]`
- **Put an `autocomplete` token on every field a browser or password manager could fill** — `name`, `email`, `tel`, `postal-code`, `one-time-code`, `current-password`, `new-password`. This is the web form of declaring a field's semantic content type. `[translation]`
- **Use a real `<label for>` for every control, keep the placeholder for the format hint, and put longer hints in an element referenced by `aria-describedby`.** `[translation]`
- **Wrap a radio or checkbox group in `<fieldset>` with a `<legend>`,** so the group's own label is announced with each option. `[translation]`
- **Turn autocapitalisation and spellcheck off on codes, usernames and email addresses, and on for names and prose.** `[translation]`
- **Use `type="password"` with `autocomplete="new-password"` when creating a credential, and never render a value into a password field.** `[translation]`
- **Prefer native controls — `<select>`, `<input type="range">`, checkbox, radio, `<input type="date">`, `<datalist>` for a combo box — to custom widgets.** A custom control has to reproduce keyboard operation, focus, state announcement and platform behaviour before it is equal to the one it replaced. `[translation]`
- **Do not split one value across several inputs.** A card number, a phone number or a code in four boxes breaks paste, autofill and screen-reader reading order; use one field and format it. `[translation]`
- **Validate on blur, re-validate on input once a field is already invalid, and never mark a field wrong on its first keystroke.** Debounce asynchronous checks such as "name taken" so the verdict does not flicker. `[translation]`
- **On a failed submit, move focus to the first invalid field, show each message next to its field, set `aria-invalid`, and link the message with `aria-describedby`.** `[translation]`
- **Announce asynchronous validation results in an `aria-live` region,** so someone using a screen reader learns the verdict without leaving the field. `[translation]`
- **Never block a submit silently.** A disabled submit button needs a visible reason next to the thing that is missing. `[translation]`
- **Keep the focused field visible above the mobile keyboard:** scroll it into view on focus, and avoid fixed footers and `100vh` layouts that the keyboard overlaps — use `100dvh` or the visual-viewport height. `[translation]`
- **Keep form state outside the DOM so back, reload and a failed request do not clear it** — step state in the URL, a draft in local storage — and warn before navigating away with unsaved input. `[translation]`
- **Never clear a form after a failed submit,** and never silently truncate at `maxlength`; tell people what the limit is and how far past it they are. `[translation]`
- **Do not intercept the browser's text-level undo.** For app-level reversal, offer an explicit Undo — a toast carrying an Undo action beats a confirmation dialog for anything reversible. `[translation]`
- **Format and parse numbers, dates and currency through the platform's locale facilities, and store canonical values** (ISO dates, minor currency units), never the formatted string. `[translation]`
- **Apply input masks on blur rather than while typing,** so the caret does not jump and pasted values still land intact. `[translation]`
- **Do not autofocus a field on a page people arrive at by scrolling,** and never steal focus while someone is typing elsewhere. `[translation]`
- **On a file input, state the accepted types and the size limit before the pick, and accept dropped files as well as picked ones.** `[translation]`
- **Keep labels above fields and the form in a single column at narrow widths,** so nothing depends on a two-column alignment that has collapsed. `[translation]`
- **In an Electron or Capacitor shell, wire the host platform's Edit menu and shortcuts to your undo stack,** so the shell behaves like the desktop or mobile app it appears to be — see `references/platforms-and-web.md`. `[translation]`
- **Hit targets, focus rings and keyboard operability for the controls in a form are covered in `references/actions-menus-and-input.md`;** they apply to every control above. `[translation]`

## Deliberately omitted

- `components/selection-and-input` — an index page that lists the input components and carries no guidance of its own; every component it lists is covered above.
- Apple Pencil Pro hardware gestures in detail (barrel roll, squeeze force behaviour, the configurable double-tap modes) and PencilKit canvas specifics such as dark-mode colour adjustment — hardware- and framework-bound with no generic equivalent; the transferable rules (imprecise input must not modify content, previews rather than actions) are kept.
- Custom system-wide keyboard extensions, including the guidance on teaching people to install and switch to them — an Apple app-extension model, not a rule about a product's own forms.
- Device-specific keyboard presentation (tvOS linear and grid keyboards, the visionOS keyboard in its own movable window, watchOS dictation-or-handwriting entry, Digital Crown picker scrubbing) — the transferable rule, minimise typing where typing is expensive, is kept instead.
- Apple material naming for keyboard accessory views (Liquid Glass) — a visual-material rule; see `references/typography-color-visuals.md`.
- macOS spring loading on segmented controls and the mini-switch control size in grouped forms — trackpad- and API-specific with no cross-platform meaning.
- The tvOS caution about focusable elements placed near a segmented control — focus-engine behaviour specific to that platform.
- The iOS guidance to use a volume view rather than a slider for audio volume — an Apple media component; see `references/motion-feedback-loading.md`.
- Alert anatomy, button order and dismissal mechanics — not omitted from the skill but owned by `references/modality-alerts-notifications.md`; only the error-copy, in-alert-input and confirmation rules that bear on data entry appear here.

## Sources

- design-principles — https://developer.apple.com/design/human-interface-guidelines/design-principles
- entering-data — https://developer.apple.com/design/human-interface-guidelines/entering-data
- selection-and-input — https://developer.apple.com/design/human-interface-guidelines/selection-and-input
- text-fields — https://developer.apple.com/design/human-interface-guidelines/text-fields
- pickers — https://developer.apple.com/design/human-interface-guidelines/pickers
- toggles — https://developer.apple.com/design/human-interface-guidelines/toggles
- segmented-controls — https://developer.apple.com/design/human-interface-guidelines/segmented-controls
- sliders — https://developer.apple.com/design/human-interface-guidelines/sliders
- steppers — https://developer.apple.com/design/human-interface-guidelines/steppers
- combo-boxes — https://developer.apple.com/design/human-interface-guidelines/combo-boxes
- color-wells — https://developer.apple.com/design/human-interface-guidelines/color-wells
- digit-entry-views — https://developer.apple.com/design/human-interface-guidelines/digit-entry-views
- virtual-keyboards — https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards
- token-fields — https://developer.apple.com/design/human-interface-guidelines/token-fields
- image-wells — https://developer.apple.com/design/human-interface-guidelines/image-wells
- undo-and-redo — https://developer.apple.com/design/human-interface-guidelines/undo-and-redo
- apple-pencil-and-scribble — https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble
- alerts — https://developer.apple.com/design/human-interface-guidelines/alerts
- modality — https://developer.apple.com/design/human-interface-guidelines/modality
- file-management — https://developer.apple.com/design/human-interface-guidelines/file-management
- WWDC26 session 250, «Principles of great design» — https://developer.apple.com/videos/play/wwdc2026/250/

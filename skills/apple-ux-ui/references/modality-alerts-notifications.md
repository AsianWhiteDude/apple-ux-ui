# Modality, alerts, and notifications

This file covers interruption: when to take over the screen and when not to, which container to use (alert, action sheet, sheet, popover, panel, inline), how to write an alert that is worth reading, how to let people out of a modal state without losing work, and how to send notifications people keep switched on. Load it when a design adds a dialog, a confirmation, a destructive action, a permission request, a toast or a push notification — or when a review finds a flow that traps people. Every rule below is an instance of four of the eight principles: **Agency** (stay out of the way, give an easy escape, build in forgiveness), **Familiarity** (use the system's patterns for alerts and choices, and give clear feedback), **Responsibility** (warn before irreversible loss, ask for permission with a reason) and **Simplicity** (exactly the words a decision needs, nothing more).

## When modality is justified

- **Take over the screen only when there is a clear benefit to the person.** Modality pulls someone out of their context and demands an explicit action to leave, so it has to earn that: making sure critical information is seen and acted on, offering choices about the action just taken, scoping one distinct task without losing the previous context, or supporting concentration on a complex one.
- **Keep a modal task simple, short and streamlined.** A complicated modal task makes people lose track of the work they suspended, especially when the modal view hides the context they came from.
- **Never build an app inside your app.** A hierarchy of views inside a modal task makes it hard to retrace steps; if subviews are unavoidable, provide a single path through them and no button that could be mistaken for the one that dismisses the whole thing.
- **Title a modal view with the task it performs.** People may not return to their previous context right away; a title naming the task — plus a line of guidance when the task needs it — tells them where they are and what finishing means.
- **Use a full-screen modal presentation only for in-depth content or a genuinely multistep task.** Media viewing, a camera view, document markup or photo editing earn the whole window because it removes distractions; a two-field form does not.

[HIG: modality]

- **Match the level of interruption to the significance of the information.** Status works best delivered passively, where people can look at it when they want it; only something like a warning about losing work justifies interrupting them so they can avoid the problem.
- **Put status feedback next to the thing it describes.** An unread count and a last-updated line in the toolbar of the list they belong to give people the information without an interruption and without leaving their context.
- **Deliver important feedback in more than one channel.** Colour, text, sound and haptics together mean the message still arrives when someone has silenced the device, looked away, or is listening with a screen reader.
- **Interrupt only when someone is about to make a big mistake.** Interruptions can be genuinely helpful there, and people appreciate being saved from disaster — but that is the whole budget.

[HIG: feedback] [WWDC26-250]

## Choosing the presentation

Work down this list and stop at the first match.

- **Alert — critical information needed right away.** A problem, a warning that an action may destroy data, or confirmation of a purchase or another important action the person initiated. An alert is normally unexpected and may appear on top of everything else, including other modal views, which is exactly why it must be rare. [HIG: alerts, modality]
- **Action sheet or confirmation dialog — choices about an action the person just initiated.** It is expected, and it offers two or more ways forward (discard the draft, or save it); an alert cannot offer those alternatives, it can only confirm or cancel. [HIG: action-sheets]
- **Sheet — one scoped task closely tied to the current context.** Supplying the information an action needs, choosing where to save something, or a short task completed before returning to the parent view. [HIG: sheets]
- **Popover — a small amount of information or a few related tasks, transient.** It appears from the control that revealed it and disappears after use, so it costs no permanent space the way a sidebar or a panel does. [HIG: popovers]
- **Floating panel or inspector pane — supplementary controls for the active window or selection, non-modal.** Apple's form is a macOS panel (Fonts, Colors, Inspector); the generic equivalent is a utility window or an inspector pane that stays open while people keep working. [HIG: panels, sheets]
- **A separate window or full-screen mode — a self-contained or prolonged task.** On platforms with windows, editing a document belongs in its own window and viewing media in full screen, not in a sheet. [HIG: sheets, modality]
- **Inline, no modality — everything else.** If the information is not actionable, put it in the relevant context as an indicator people can choose to learn more from, rather than an alert. [HIG: alerts, feedback]

Three boundaries that are easy to get wrong:

- **Use an action sheet, not a menu, when the choice follows an action.** People expect choices to appear when their action needs clarifying; they expect a menu only when they chose to reveal it. [HIG: action-sheets]
- **Never use a popover to warn people.** A popover can be missed or closed by accident, so a warning belongs in an alert. [HIG: popovers]
- **Use an alert, not a notification, for an error message.** People know both patterns; using the wrong one only creates confusion about how urgent the thing is. [HIG: notifications]

## Getting out: dismissal and recovery

- **Always give an obvious way to dismiss a modal view, in the place the platform puts it.** On iOS, iPadOS and watchOS people look for a button in the top bar or swipe down; on macOS and tvOS they look for a button in the main content view. An ambiguous exit is the same as no exit.
- **Confirm before closing when closing would lose work the person created.** Whether they used a gesture or a button, explain the situation and offer the ways to resolve it — saving, for instance — rather than discarding silently.
- **Never stack modality on modality.** Let people dismiss one modal view before presenting the next; only an alert may appear over another modal view, and never over another alert.

[HIG: modality]

- **Never lock anyone into a flow.** People should be able to move through the interface and reach features without being trapped in a specific flow or mode; when a guided flow is genuinely necessary, make it easy to skip or escape so they can get to the main experience quickly.
- **Make recovery cheap.** People send, change and delete things by accident constantly; when they know an action can be reversed they explore freely, and recovering from the unexpected must not cost them their time or their work.

[HIG: design-principles] [WWDC26-250]

## Alerts

### Use them rarely

- **Make every alert essential and, where possible, actionable.** Alerts interrupt by design, and they lose their force if they carry unimportant information; each one should offer information that matters and an action worth taking.
- **Do not use an alert merely to inform.** An interruption that cannot be acted on is resented; find a way to say it in context instead — an unobtrusive indicator people can follow when they care.
- **Do not alert for common, undoable actions, even destructive ones.** Deleting a message or a file is the intended result and can be undone; alert instead when the destructive action is uncommon and cannot be undone, in case it was initiated by accident.
- **Warn only about data loss that is unexpected and irreversible.** The Finder does not confirm every file thrown away, because losing it is exactly what the person asked for.
- **Never show an alert when the app starts.** Nobody has any context yet; make important information discoverable in the interface, and on a startup problem such as a missing network connection show cached or placeholder data with a quiet label describing the situation.
- **Show only one alert at a time.** Two alerts on screen at once cannot be reasoned about, and the second one will be dismissed unread to get at the first.

[HIG: alerts, feedback, modality]

### Anatomy and copy

- **State the situation in the title: what happened, in what context, and why.** Be specific and complete without being verbose; "Error" or "Error 329347 occurred" tells people nothing, and a title wrapping past two lines will not be read.
- **Add informative text only when it adds value.** If it is needed, keep it to short, complete sentences with normal punctuation.
- **Be direct, neutral and approachable.** Alerts describe problems and serious situations, so do not be oblique or accusatory, and do not soften the severity into vagueness.
- **Do not explain the buttons in the body text.** If the text and the button titles are clear, the explanation is noise; if it is needed, the titles are wrong.
- **Include a text field only when the person's input resolves the situation** — a password, for example. Anything else belongs in a sheet.
- **Keep an alert to at most three buttons and short enough not to scroll.** Larger text sizes can push an alert into scrolling; a short title and an optional brief message prevent it.
- **Never ask "Are you sure?" without naming the consequence.** The title describes the situation and the button names the result, so those two carry the meaning; a bare confirmation trains people to dismiss alerts unread.

[HIG: alerts]

### Buttons

- **Title each button with the result of choosing it, in one or two words.** Prefer verbs and verb phrases tied to the alert text — "View All", "Reply", "Ignore" — with sentence-style capitalisation and no ending punctuation.
- **Avoid "OK" unless the alert is purely informational, and never use "Yes" and "No".** "OK" is ambiguous about what was understood versus what will happen; "Erase", "Convert", "Clear" or "Delete" tells the person what they are doing.
- **Always title the cancelling button "Cancel", and always include it when an action is destructive.** That gives a clear, safe way to avoid the action rather than a guess between two verbs.
- **Put the most likely choice on the trailing side of a row or at the top of a stack; put cancel on the leading side or at the bottom.** Consistent placement is what lets people act without reading twice — and what stops the wrong button being hit by muscle memory.
- **Never make Cancel the default button, and make nothing the default when you want the alert read.** A default button plus a habitual Return press is how warnings get dismissed unseen; a single-button alert that is also the default is titled "Done", not "Cancel".
- **Use the destructive style only for a destructive button people did not deliberately choose.** When the alert confirms an action they deliberately chose, styling it as destructive second-guesses their own intent; when it draws attention to destruction they did not intend, they appreciate it.
- **Offer at least one escape besides the Cancel button.** On Apple platforms that is Escape or Command-period from a keyboard (Menu on a remote); whatever the platform, a quick, conventional cancel must exist.
- **Let people suppress a repeating alert, and reserve a caution symbol for real danger.** Apple's macOS alerts can add a suppression checkbox; a caution symbol used too often loses its meaning, and it does not belong on a routine save or an empty-trash confirmation.

[HIG: alerts]

## Action sheets and confirmation dialogs

- **Offer the choices the action implies, not a yes-or-no.** Cancelling an edited draft has two reasonable outcomes — discard it or save it — and naming both is faster and safer than confirming one of them.
- **Use them sparingly.** They still interrupt the current task to deliver their choices, and interruptions people stop reading are worse than no interruption at all.
- **Keep the title to a single line, and add a message only if the action's context does not already explain the choice.** A long title gets truncated or forces scrolling.
- **Include a cancel item whenever a choice can destroy data, in the place the platform puts it** — the bottom of the list on most Apple platforms, the upper-left corner on watchOS.
- **Style destructive choices as destructive and put them where they are most noticeable** — the top of the list on Apple platforms. The style and the position are what stop an accidental pick.
- **Keep the list short enough not to scroll.** Every extra button costs time and attention, and scrolling a stack of buttons invites a mis-tap; Apple's watchOS ceiling of four items including cancel is a good limit anywhere.

[HIG: action-sheets]

## Sheets

- **Use a sheet for one scoped task and return people to the parent view when it ends.** A sheet whose close button leads to another sheet leaves people unable to say where they are.
- **Show one sheet at a time.** If something inside a sheet needs another one, close the first and, if it still matters, present it again afterwards.
- **Always give Done a companion.** Pair it with Cancel — or with Back inside a multi-step flow — so that completing the task is not the only exit; relying on Done alone is restrictive and misleading. Do not show Cancel, Done and Back all at once.
- **Keep the dismiss controls in their conventional positions, and never use Back to dismiss.** On iOS and iPadOS, Cancel sits on the leading edge of the top bar and Done on the trailing edge; Back moves one step inside the flow.
- **Support the platform's dismiss gesture, and confirm when unsaved input would be lost.** People expect to swipe a sheet away; if there are unsaved changes when the gesture starts, present the save-or-discard choices rather than dropping the work.
- **Make resizability visible.** Apple's sheets rest at detents (roughly half height and full height) and show a grabber that both signals "draggable" and lets assistive technology resize the sheet; whatever the mechanism, do not hide the fact that a panel can be made bigger.
- **Present a sheet at a size that preserves the parent context, and allow resizing when people need a clearer view.** Avoid a sheet that covers nearly all of its window; on the desktop pick a sensible default size, and let people bring other windows of the app forward without dismissing the sheet first.
- **Centre a sheet on a dimmed parent at a predictable default size.** Apple's iPadOS page and form sheet styles do exactly this, and the dimming is what tells people the parent view is not accepting input until they finish.
- **Prefer a separate window, a full-screen presentation or an immersive mode for complex or prolonged flows.** Document editing works better in its own window; media works better full screen.
- **Use a non-modal presentation when the auxiliary controls keep affecting the main task.** A split-view pane, a desktop panel, or a non-modal sheet lets people act on the parent view without dismissing anything — and a panel, not a sheet, is right when people provide input and watch the result repeatedly, as in find and replace.

[HIG: sheets]

## Popovers and panels

- **Keep a popover to a few related tasks, and no bigger than those need.** It disappears after use, so a long-lived or many-step task does not belong in it.
- **Point the popover at whatever opened it.** Its arrow should aim as directly as possible at that control, and it should cover neither the control nor content people need while using it.
- **Let a popover light-dismiss, and add a close button only when it clarifies.** It normally closes when people click or tap outside it or pick an item; Cancel or Done is worth adding when leaving with or without saving needs to be explicit. Keep it open while multiple selections are being made, until people dismiss it deliberately.
- **Save the work when a non-modal popover closes by itself.** People dismiss popovers by accident all the time; discard changes only when they choose an explicit Cancel.
- **Show one popover at a time, never one out of another, and put nothing on top of it except an alert.** If one must replace another, close the first — and let a single click move between the popovers of neighbouring toolbar buttons instead of forcing a dismiss-then-open.
- **Animate a size change instead of swapping the popover.** A condensed and an expanded view of the same content should read as one thing growing, not as a replacement.
- **On a narrow layout use a sheet instead of a popover.** Reserve popovers for wide views; in a compact width use the available space with a full-screen modal view.
- **Name the thing, not the container, in help text.** Write "select Show", not "select the Show button at the bottom of the popover" — people do not know the container's name.

[HIG: popovers]

- **Use a floating panel for supplementary controls over the content they change.** Apple's form is the macOS panel — Fonts, Colors, Inspector; the generic equivalent is a utility window or inspector pane, less prominent than a document window. Prefer direct adjustment controls such as sliders and steppers over fields that require typing and selecting.
- **An inspector follows the selection; an Info view does not.** Use a panel or a split-view pane for details that update as the selection changes, and a regular window when the contents must stay put.
- **Title a panel with a short noun, bring panels forward with the app, and hide them when the app is inactive.** The title bar is also how people position it; a panel that lingers over another app's window is in the way.
- **Prefer a standard panel to a dark, translucent HUD.** Use a HUD only in media-oriented contexts, when a standard panel would obscure essential content, or when no standard controls are needed; keep it small, use colour sparingly, do not cover the content it adjusts, and keep one style when the app changes modes.

[HIG: panels]

## Paged flows and the status bar

- **Use page indicators only for a flat, ordered set of pages.** They express position in a sequence, not hierarchy or non-sequential relationships; for anything more complex use a sidebar or a split view.
- **Centre the indicators near the bottom edge, and keep them under about ten.** More than roughly ten dots cannot be counted at a glance; for more peers than that use an arrangement such as a grid that people can navigate in any order.
- **Make the current position unmistakable, and let the control hint that more pages exist.** A solid indicator for the current page against equidistant dots, shrinking at the edges when there are more than fit, lets people estimate where they are without counting.
- **Keep a paged full-screen collection free of other controls.** Page indicators are designed for content-rich pages that are peers; extra controls in that space make it hard to keep track of focus while moving between pages.
- **Keep indicator images plain and uncoloured, and use at most two kinds.** Custom colours cut the contrast that marks the current page, and several different images force people to memorise meanings; one distinct image for one special page is the limit.

[HIG: page-controls]

- **Keep the device status bar legible and put nothing interactive behind it.** Content showing through a transparent status bar makes it unreadable, and controls under it look tappable but are not; blur or obscure what sits beneath it.
- **Hide the status bar only temporarily, for full-screen media, and bring it back on a simple, discoverable gesture** such as a single tap. Hiding it permanently forces people to leave the app to check the time or their connection.

[HIG: status-bars]

## Notifications

### What to send

- **Send only timely, high-value information that can be understood at a glance.** People switch notifications on to get quick updates; anything that needs explaining is not a notification.
- **Never repeat a notification for the same event because nobody answered.** People attend to notifications when it suits them; duplicates fill the list and are a direct cause of someone turning your notifications off entirely.
- **Do not tell people to go and perform a task in your app.** They cannot remember the instruction once the notification is gone; offer the action on the notification itself or say nothing.
- **Handle the case where your interface is already open.** Present the information so it is discoverable but not invasive — increment a count, quietly insert the new item into the list people are looking at — instead of an interruption about something already on screen.
- **Keep private content out of notification text.** You cannot know who is looking at the screen; also write preview-hidden text that names the kind of event ("New comment", "Shipment") without revealing its content.

[HIG: notifications]

### Urgency, permission and settings

- **Ask permission before sending anything, and treat the answer as binding.** People can change the decision later and can silence everything; a design that only works with notifications granted is broken by default.
- **Ask at the moment of need, with the reason.** A permission prompt thrown up the second something launches, before anyone knows what the product does, is how trust is lost; wait for the moment where the reason is self-evident and state it. [WWDC26-250]
- **Represent urgency honestly.** Apple's four levels — passive, active (the default), time-sensitive and critical — decide whether an alert waits for a summary or breaks through; claiming a high level for low-priority information is how an app loses its permission.
- **Reserve the breaking-through level for what is happening now or within the hour** — a security issue, a delivery arriving. The first time one arrives, the system explains what that level does and offers a way to turn it off, and it repeats that offer from time to time.
- **Reserve the highest level for health and safety.** Critical notifications override even silent mode, are extremely rare, and require an entitlement from Apple; on any platform, treat "overrides the person's quiet settings" as requiring that bar.
- **Respect quiet periods and delivery schedules.** Focus and scheduled summaries exist because people do not always want to be interrupted; the notification is still there the moment it arrives, so nothing is lost by letting it wait.
- **Never send marketing without explicit opt-in, and never at an urgent level.** Describe what you would send, give a clear way to opt in or out, and keep promotional content out of the levels that break through.
- **Put notification settings inside the product.** People who granted permission must be able to change the kinds they receive without leaving for system settings.

[HIG: managing-notifications]

### Content, actions and badges

- **Write a short title that adds context, and a body in complete sentences.** Use the title for the useful specific — a headline, an event name, a subject — in title-style capitalisation with no ending punctuation; if all you have is a generic label, let the system show your app name instead. Do not pre-truncate the body; the system truncates.
- **Leave your app's name and icon out of the content.** The system already shows a large version of the app icon at the leading edge of every notification (a communication notification shows the sender's image badged with a small one), so repeating them spends the little space a notification has.
- **Offer up to a few actions that finish the task without opening the app,** each labelled with a short phrase naming the result and paired with a simple, recognisable icon. Do not add an action that merely opens the app — tapping the notification already does that.
- **Prefer non-destructive actions, and give enough context for any destructive one.** A destructive action should look distinct and be impossible to trigger by reflex.
- **Treat sound as reinforcement, never as the message.** A short, distinctive sound helps someone notice a notification when they are not looking; people may not hear it at all, so nothing may depend on it.
- **Badge only the number of unread notifications, keep it current, and never let it be the only channel.** Do not badge weather, dates, prices or scores; clear it as soon as people have seen the items; and do not fake a badge with a custom image, because people who turned badges off will be rightly annoyed.

[HIG: notifications]

## Translation to web and other platforms

Everything in this section is this skill's translation of the guidance above to the web and to web-hosted shells. Apple does not state these rules; the reasoning is Apple's, the mechanics are the platform's.

- **Use the platform's real dialog primitive.** `<dialog>` opened with `showModal()` makes the rest of the page inert, closes on Escape and keeps focus inside; a hand-rolled overlay of divs reproduces none of that and is where focus traps and unreachable buttons come from. [translation]
- **Move focus into the dialog when it opens and back to the control that opened it when it closes.** Otherwise keyboard and screen-reader users are dropped at the top of the document and lose their place — the web version of destroying a person's context. [translation]
- **Make Escape and a visible close control both work, on every dismissible dialog.** A dialog with no keyboard exit is the web's version of trapping someone in a modal view; treat it as a blocker, not a polish item. [translation]
- **Use toasts only for passive status, never for a decision or a data-loss warning.** A toast is the web's ambient status channel — announce it through a polite live region so it is not silent for screen readers — while anything that must be read and acted on belongs in a dialog or inline next to the control. [translation]
- **Guard unsaved work at every exit the browser actually offers**, not only at your own close button: the back gesture, a route change and closing the tab (`beforeunload`) all need the same save-or-discard choice. [translation]
- **Give a linkable or reloadable modal a URL, and make the back button dismiss it.** People use the back button as the universal escape; a modal outside history either cannot be shared or swallows the gesture. [translation]
- **Request notification permission at the moment of need, after the person has seen what the product does — never on load** — and make a denied permission degrade to an in-page inbox or digest rather than a dead feature. [translation]
- **Use the platform's light-dismiss popover mechanism** (the `popover` attribute with `popovertarget`, anchored to its trigger) rather than a click-outside listener, and keep it anchored visually to the control that opened it. [translation]
- **Never block the page with an interstitial for marketing, a newsletter or a survey.** It is an alert at launch with none of the justification, and it is the fastest way to teach people to dismiss your dialogs without reading. [translation]
- **In an Electron or Capacitor shell, follow the host platform's dialog conventions.** Use a native message box for app-level alerts and quit confirmations, in-window sheets for content tasks, the system back gesture as dismissal on mobile — and remember the web content inside the native window still needs Escape, focus handling and safe-area insets. [translation]
- **Respect safe-area insets so nothing sits under the OS status bar or the home indicator** (`env(safe-area-inset-*)`), and put nothing interactive in those strips. [translation]
- **Name the dialog for assistive technology, not only for the eye.** The title that identifies the modal task must be the dialog's accessible name (`aria-labelledby` on the heading), or screen-reader users enter an unnamed box and cannot tell what they are in. [translation]
- **The web's badge is the document title and the favicon — and it is never the only channel.** Show the count where the page itself can be seen too, because a tab title is invisible the moment the tab is not in front. [translation]
- **Express destructive styling in more than colour.** A red button plus a specific verb; colour alone fails for a large share of people — see `references/accessibility-inclusion-privacy.md`. [translation]

Related files: `references/motion-feedback-loading.md` for status, progress and haptics as feedback channels; `references/writing-help-onboarding-settings.md` for permission and settings copy; `references/accessibility-inclusion-privacy.md` for permission timing, ARIA and colour-independence; `references/actions-menus-and-input.md` for menus and button states; `references/layout-and-navigation.md` for windows and full-screen modes.

## Deliberately omitted

- `components/presentation.md` — an index page whose one-line definitions of each presentation component feed the decision list above; it states no rules of its own.
- watchOS short-look and long-look notification interfaces, the sash, and the 18 %-opacity content background (`components/notifications`) — watch-specific layout with no generic equivalent; the double-tap ordering rule is folded into "prefer non-destructive actions".
- Communication notifications, SiriKit intents, and the mechanics of Focus and the Ring/Silent override (`patterns/managing-notifications`) — Apple system integration; the generic rules kept are honest urgency and respect for quiet settings.
- visionOS sheet placement and Full Space transitions, and the alert accessory-view dimensions (`components/sheets`, `components/alerts`) — spatial-platform geometry with no cross-platform meaning.
- macOS panel housekeeping: excluding panels from the Window menu's documents list, suppressing the minimize button, and how to name panels in help documentation (`components/panels`) — menu-bar and terminology detail; the menu bar belongs to `references/actions-menus-and-input.md`.
- Detachable popovers on macOS (`components/popovers`) — a desktop-only conversion of a popover into a panel with no equivalent elsewhere.
- Page-control scrubbing, the automatic/prominent/minimal background styles, and watchOS vertical pagination with the Digital Crown (`components/page-controls`) — control-level API and platform-input detail.
- From `patterns/feedback`: confirming that a significant task completed, telling people when a command cannot be carried out and why, and the watchOS rule against indeterminate progress indicators — these are response-and-progress rules owned by `references/motion-feedback-loading.md`; this file keeps only the alert, warning and interruption-level rules.

## Sources

- `patterns/modality` — https://developer.apple.com/design/human-interface-guidelines/modality
- `patterns/feedback` — https://developer.apple.com/design/human-interface-guidelines/feedback
- `patterns/managing-notifications` — https://developer.apple.com/design/human-interface-guidelines/managing-notifications
- `components/presentation` — https://developer.apple.com/design/human-interface-guidelines/presentation
- `components/alerts` — https://developer.apple.com/design/human-interface-guidelines/alerts
- `components/action-sheets` — https://developer.apple.com/design/human-interface-guidelines/action-sheets
- `components/sheets` — https://developer.apple.com/design/human-interface-guidelines/sheets
- `components/popovers` — https://developer.apple.com/design/human-interface-guidelines/popovers
- `components/panels` — https://developer.apple.com/design/human-interface-guidelines/panels
- `components/page-controls` — https://developer.apple.com/design/human-interface-guidelines/page-controls
- `components/notifications` — https://developer.apple.com/design/human-interface-guidelines/notifications
- `components/status-bars` — https://developer.apple.com/design/human-interface-guidelines/status-bars
- `getting-started/design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- WWDC26 session 250, "Principles of great design" — https://developer.apple.com/videos/play/wwdc2026/250/

# Actions, menus, and input

This file covers how people *act*: buttons, menus of every kind, toolbars and the desktop menu bar, gestures, keyboard,
pointer, focus and selection, drag and drop, sharing, and document commands. Load it when designing or reviewing
controls and the paths that reach them. Every rule is an instance of four principles — **Familiarity** (recognisable
controls that behave and sit where people expect), **Agency** (direct manipulation, several routes to every action,
nothing important hidden behind one secret move), **Flexibility** (touch, pointer, keyboard, voice and assistive tech
all reach the same functionality), and **Craft** (precise states and immediate feedback). Data entry, undo and redo are
in `references/forms-and-data-entry.md`; confirmation dialogs and destructive warnings in
`references/modality-alerts-notifications.md`.

## Consistency and metaphor

- **Make things that look the same behave the same.** If one button navigates, another toggles and a third opens a modal,
  there is no pattern left to learn.
- **Keep an action in the same place across screens and devices.** Stable placement lets people act without thinking about
  where to look.
- **Use the metaphor people already hold for a common action, and do not redraw it.** A trash glyph means delete; using it
  for something else destroys the recognition you were relying on.
- **Build forgiveness into every action: easy undo, and a double-check before something destructive.** Interrupt only when
  someone is about to make a big mistake.
- **Let people rearrange controls, or hide the ones they never use.** No single layout suits everyone.
  [WWDC26-250]

## Buttons

### Recognisability and targets

- **Give every interactive element a hit region of at least 44×44 points — 60×60 in visionOS — with clear space around it.**
  The region any input has to land in, fingertip to remote. [HIG: buttons] The same bar holds on web and desktop; carry a smaller drawn control to it with padding, not a bigger graphic, and see `references/accessibility-inclusion-privacy.md` for hit region versus platform control size. [translation]
- **Give a button a discernible shape and fill when it sits on content.** An enclosed, contrasting shape reads as a control;
  text alone does not — unless a toolbar, menu or alert already supplies the surface.
- **Keep one visual style for one meaning.** Where the platform reserves an appearance for a state — in visionOS a white
  fill with black content means "toggled on" — do not spend it on anything else.
  [HIG: buttons]

### Content and labels

- **Make each button state its purpose through a symbol, a text label, or both.** Nobody should press a control to learn
  what it does.
- **Use the familiar icon for a familiar action.** Share, trash and search glyphs are already understood; a reassigned one
  misleads.
- **Write a text label when words beat a picture: a verb first, in title-style capitalisation** — "Add to Cart".
- **Append a trailing ellipsis when activating the control opens somewhere else to collect input.** That is the system's
  signal that more information is needed before anything happens.
- **Give an icon-only button a name people can obtain without guessing.** Desktop platforms reveal a tooltip on hover;
  everywhere, the name must exist for assistive technology (`references/accessibility-inclusion-privacy.md`).
  [HIG: buttons]

### Roles, hierarchy, states

- **Use a prominent style for the most likely action, and allow one or two prominent buttons per view.** More raises
  cognitive load and slows the decision.
- **Signal the preferred option by style, not size.** Same-size buttons read as a coherent set; two sizes side by side read
  as a mistake.
- **Mark the most likely action as primary so Return confirms it** — and, in a sheet or alert, closes the view.
- **Never make a destructive action the primary button; style it distinctly instead.** Prominent buttons get pressed unread,
  so keep the default on the safe choice; the system colours a destructive role red.
- **Always give a custom button a pressed state.** Without one it feels unresponsive and people press twice.
- **Show progress inside the control when an action is not instantaneous.** An in-button activity indicator with a changed
  label ("Checkout" → "Checking out…") explains the delay where it happens.
- **Keep view-level action buttons beside the view they affect, not in the window frame.** A control that adds table rows
  belongs at the table's edge; window-level commands belong in the toolbar.
  [HIG: buttons]

## Menus

### Labels

- **Label an action item with a verb or verb phrase** — "Close", "Duplicate", "Select".
- **Use title-style capitalisation and drop articles:** "View Settings", not "View the Settings".
- **Append an ellipsis when the command needs more input before it can finish.**
- **Show unavailable commands as unavailable rather than removing them.** A dimmed item still teaches that the command
  exists, and a menu whose every item is unavailable must still open.
  [HIG: menus]

### Icons in menus

- **Use the system's own icon for a common action** — Share, Print, Copy, Delete, Search — wherever it appears.
- **Add item icons sparingly and for a reason:** frequent actions, key features, locations, devices, visual operations like
  rotate, user content. If no icon clearly fits an item, give it none.
  [HIG: menus, context-menus]

### Order, grouping, length

- **Put important and frequently used items first.** People scan from the top and stop at the first plausible match.
- **Group related commands and divide groups with a separator.** Keep a family together even when its members differ in
  importance: "Paste and Match Style" belongs beside Copy and Cut.
- **Keep menus short enough to read.** Split a long menu or factor a repeated term into a submenu; a list people build
  themselves (history, recents) may be long, and scrolling it is acceptable.
  [HIG: menus]

### Submenus

- **Use submenus sparingly and keep them one level deep.** Each hides its contents and adds a step; two levels are hard to
  navigate with any input device.
- **Consider a submenu when one term repeats across three or more items** — "Sort by Date / Score / Time" becomes "Sort by ▸
  …" — keeping the shared term in the parent label so people can predict the contents.
- **Keep a submenu openable even when everything inside it is unavailable**, and prefer a submenu to indented items, which
  express no relationship.
  [HIG: menus, context-menus]

### Items that carry state

- **Prefer one item whose label describes the current state to two items for two states** — "Hide Map" while visible.
- **Add a verb when a state label could read as either a state or an action** — "Turn HDR On", not "HDR On" — or show both
  items when seeing both states at once helps, leaving the inapplicable one unavailable.
- **Use a checkmark to show that an attribute is in effect.** Checkmarks are the fastest thing to scan for.
  [HIG: menus]

### Context menus

- **Fill a context menu with the few commands most likely to be wanted right here**, not advanced or rare ones, and keep it
  scannable without scrolling.
- **Never let a context menu be the only route to a command.** It is hidden by default, so every item must also exist in the
  visible interface — a toolbar, an inline control, or the app's menus.
- **Hide unavailable items here instead of dimming them** — the opposite of a regular menu, because a context menu shows
  only what applies to the current selection.
- **Put the most frequently used items nearest where the menu was opened**, reversing the order when it opens above rather
  than below the target.
- **Keep to about three separator groups, and do not repeat keyboard shortcuts here.** The context menu is already the
  shortcut; key equivalents belong in the main menus.
- **Place destructive items last and mark them as destructive.** Position plus the system's red treatment is what prevents
  an accidental tap.
- **Do not offer both a context menu and an edit menu on the same item.** People and the system both have to guess.
  [HIG: context-menus]

### Edit menus and clipboard commands

- **Prefer the system's editing menu to a custom one repeating the same commands.** People know its contents; a parallel
  copy is redundant and confusing.
- **Let people open it with the interaction the platform already defines** — touch and hold, secondary click. Nobody wants
  to learn a custom move for a standard task.
- **Show only commands that apply:** no Copy with nothing selected, no Paste with nothing to paste.
- **Let people select and copy content text that is not editable** — a caption, a status — while leaving control labels
  unselectable.
- **Name deletions precisely:** "Delete" removes, "Cut" copies to the clipboard and then removes.
- **Rely on undo rather than confirmation for menu commands.** Menus act immediately; the safety net is reliable undo and
  redo (`references/forms-and-data-entry.md`).
  [HIG: edit-menus]

### Menus attached to a button

- **Use an options menu for a flat set of mutually exclusive states** (Apple: pop-up button): it closes on choice and shows
  the current selection. Use an actions menu (pull-down button) for commands, multi-select, or a submenu.
- **Give an options menu a sensible default and a label that predicts its contents**, plus a "Custom…" item with short
  explanatory text when a few people occasionally need values the list does not hold.
- **Keep a view's primary actions out of an actions menu.** Anything that must be found immediately cannot live behind a
  control people have to open first.
- **List about three or more items in an actions menu.** For one or two use plain buttons or a toggle; a very long list
  slows the search. Give the menu a title only if it adds meaning.
- **Mark a destructive item and confirm it on a separate surface.** A confirmation that appears elsewhere and needs
  deliberate dismissal is what stops accidental data loss.
- **Weigh an overflow or "More" control's convenience against its cost in discoverability.** An ellipsis tells nobody what
  is inside.
  [HIG: pop-up-buttons, pull-down-buttons]

## Toolbars

- **Put the commands that support the view's main tasks in the toolbar, and nothing else.** People must be able to
  distinguish and hit each item.
- **Decide in advance which items collapse into overflow as the view narrows**, and never ship a default layout that already
  overflows. Where the platform provides an overflow menu, use it rather than building one.
- **Never let the toolbar be the only home of a command.** It can be customised, narrowed or hidden, so every toolbar action
  needs a second route — the menu bar on desktop, a menu or inline control elsewhere.
- **Group items by function and frequency, and keep to about three groups.** More reads as clutter even on a wide screen;
  keep grouping and placement consistent across platforms and screen sizes.
- **Give navigation and critical actions — Done, Close, Save — their own visually distinct section.** Their placement is
  what makes them findable under pressure.
- **Allow exactly one prominent primary action, on the trailing side.** One focal point per bar.
- **Insert space between text-labelled items.** Adjacent text buttons run together, and a text label beside a symbol reads
  as one combined control.
- **Use the platform's standard back and close symbols; do not relabel them as words.** A custom version must look, behave
  and appear consistently throughout.
- **Prefer recognisable symbols to words, except for actions a symbol cannot express** — "Edit" is clearer as text. Skip
  borders around symbols; the bar is already the container.
- **Let people customise the toolbar in an app with many commands or long sessions** — editing commands in particular vary
  by person and project.
- **Title each window usefully: a short phrase, under about 15 characters, never the app's name.** Leave it empty when the
  content already says where you are.
- **Hide bars for a distraction-free mode only in context, and always with a reliable way back.**
  [HIG: toolbars]

## Desktop command surfaces

- **On desktop, provide a complete menu-bar command surface — every command, including ones reachable elsewhere.** It is
  where people look first in an unfamiliar app, where shortcuts become visible, and how keyboard-only users reach
  functionality.
- **Use the standard menus in the standard order** (App, File, Edit, Format, View, app-specific, Window, Help), providing a
  menu even when you support only part of its standard contents.
- **Always show the same set of items and disable what does not apply.** A vanishing command cannot be learned.
- **Support the standard shortcut for every standard command you include**, and keep menu titles short — one word where
  possible.
- **Name what undo will reverse:** "Undo Paste and Match Style", "Undo Typing". A bare "Undo" makes people test it.
- **Never make a modifier-revealed (dynamic) item the only way to do something.** Require a single modifier, keep such items
  in menu-bar menus rather than context or dock menus, and leave a visible path.
- **Where the menu bar can be hidden, ensure every function is also reachable in the interface itself**, and never treat it
  as the home for whatever did not fit elsewhere.
- **If you add a status-area item (Apple: a menu bar extra), show a menu rather than a popover and let people decide whether
  it appears.** Never rely on its presence or predict its position.
- **Offer a small number of high-value shortcuts from the app's outside surface** — a Dock menu on desktop, Home Screen
  quick actions on mobile (up to four) — and duplicate every one inside the app.
- **Write each outside-surface item as a succinct title stating the result** — "Directions Home", "New Message" — with no
  app name, an optional subtitle, a familiar monochrome symbol rather than an emoji, and predictable dynamic changes.
  [HIG: the-menu-bar, dock-menus, home-screen-quick-actions]

## Gestures

- **Never make a gesture the only way to do something.** People use voice, keyboard, switch control and pointers; assume
  nothing about what a given person can perform.
- **Keep standard gestures' standard meanings:** tap activates or selects, swipe reveals, dismisses or scrolls, drag moves,
  touch and hold reveals more, double tap and pinch zoom, two fingers rotate. Do not repurpose a familiar gesture, and do
  not invent one for a standard action like scrolling.
- **Respond continuously while the gesture happens.** Feedback should let people predict the result and, where it matters,
  show how far they still have to move.
- **Show when a gesture is unavailable.** With no signal people conclude the app has frozen — a locked object that simply
  does not move is a design bug.
- **Add a custom gesture only for a specialised, frequent task, and only if it is discoverable, simple, distinct, and never
  the only path.** If you cannot describe it in plain words and one picture, people will not learn it.
- **Treat shortcut gestures as accelerators over visible controls.** Keep the Back button even when an edge swipe also goes
  back; an extra tap is not a defect.
- **Stay clear of the platform's system gestures and screen edges.** A conflict reads as your app breaking the device.
  [HIG: gestures]

## Keyboard

- **Make the whole interface operable from the keyboard alone** — reach and activate every window, menu and control (Apple:
  Full Keyboard Access).
- **Respect the standard shortcuts people already own:** undo and redo, cut/copy/paste, select all, save, print, find and
  find-next, new, open, close, quit, settings, help; Escape cancels the current action and Return confirms the default.
  Redefine one only when its action is meaningless here.
- **Define custom shortcuts only for the most frequently used commands.** Too many new bindings make an app hard to learn.
- **Use modifiers as the platform does:** the command modifier first, Shift as a secondary modifier for a related command,
  the alternate modifier sparingly for power features, and avoid the control modifier, which the system uses widely itself.
- **Do not build a shortcut by adding a modifier to an unrelated command's shortcut.** Shift plus the undo shortcut must not
  mean something unconnected to undo.
- **Let the system localise and mirror shortcuts** for the connected keyboard and right-to-left layouts instead of
  hard-coding keys (`references/accessibility-inclusion-privacy.md`).
- **Keep modifier behaviour during direct manipulation consistent and input-independent.** If the alternate modifier
  duplicates a dragged object it must do so identically by touch and by pointer; arrow keys nudge by the smallest unit.
- **Write shortcut titles that stand alone**, since a flat shortcut list has no parent menu to supply context, and display
  shortcuts in the main menus rather than context menus.
  [HIG: keyboards, the-menu-bar, context-menus, pointing-devices]

## Focus and selection

- **Use the platform's own focus effects.** They are tuned to its input devices and give a predictable indicator; build a
  custom one only when genuinely necessary.
- **Never move focus without the person's interaction.** They rely on it to know where they are. When the focused element
  disappears, hide the indicator — unless they are stepping with a discrete directional input, where focus should move to a
  findable neighbour.
- **Move focus in reading order — leading to trailing, top to bottom — and group containers so it does.** If a vertical
  stack should be traversed downward before moving across, declare it as one group.
- **Make every focus state visually distinct and design the layout for all of them** — unfocused, focused, activating,
  selected, unavailable. If focusing enlarges an item, it must not crowd its neighbours.
- **Separate focus from selection when selecting would shift context.** If landing on an item would open it, require a
  second deliberate action.
- **Match the platform's expectation about what takes focus.** Where a full-keyboard-access mode already reaches every
  control, support focus for content elements — list items, text and search fields — not for buttons and toggles.
  [HIG: focus-and-selection, keyboards]

## Pointer

- **Give every interactive element a hover response, consistent across the product.** A control that does not react under
  the pointer reads as broken.
- **Do not create decorative pointer or hover effects.** People expect every change under the pointer to mean something.
- **Let the cursor shape state what is possible** — a text cursor over editable text, a link cursor over a link, an explicit
  "not allowed" shape over an invalid drop — and keep custom shapes simple.
- **Pad hit regions so targeting feels easy but not sticky.** About 12 points around a bevelled element and 24 around one
  without a bevel works well; too little demands precision, too much makes the pointer feel captured.
- **Give the same result for the same intent across touch, pointer, keyboard and eyes.** People move between inputs mid-task
  and will not learn a separate model for each.
- **Do not attach instructional text to the pointer.** If the interface needs explaining there, fix the interface; live data
  such as coordinates or an object's size while resizing is different and useful.
- **Consider scale, shadow and spacing together in a hover treatment.** Do not scale an element that cannot grow without
  overlapping neighbours, and never use shadow without scale.
  [HIG: pointing-devices]

## Drag and drop

- **Support dragging wherever content can sensibly move, and always provide a non-drag equivalent.** Dragging is
  inconvenient or impossible for many people; menu commands must do the same work, and sources and destinations must be
  exposed to assistive technology.
- **Follow the expected default: a drop inside the same container moves, into a different container copies, and between apps
  always copies.** Change it only with a reason, choosing whichever is less likely to lose data; the alternate modifier held
  at drop time forces a copy within one container.
- **Support dragging several items as a group**, including adding items to a drag already in progress.
- **Show a translucent representation of the content as soon as the drag begins** (about three points of movement) and keep
  it until the drop, so destinations stay visible underneath.
- **Show whether the destination under the content can accept it.** Highlight or show an insertion point only while the
  content is over a valid target, show an explicit "not allowed" indicator when it is not, and cue one target at a time.
- **Give visible feedback when a drop fails or lands somewhere invalid** — return the item to its source or let it evaporate
  — so nobody wonders where their content went.
- **Let people undo a drop.** Where it cannot be undone, confirm first or provide an explicit way to reverse the result
  afterwards.
- **Offer and accept the richest representation available.** Provide alternatives from highest to lowest fidelity, take the
  best form the destination supports, and extract only the relevant part of what was dropped.
- **Show progress when dropped content takes time to transfer**, with a placeholder at the drop location, and report when a
  drop starts a task such as printing.
- **Keep dropped text's attributes when both sides support them, otherwise adopt the destination's style**, and leave
  dropped content selected at the destination while updating the selection at the source.
- **Let a control activate when content is held over it** (Apple: spring loading), and let people select and start dragging
  in one motion with no forced pause.
  [HIG: drag-and-drop, buttons]

## Sharing and collaboration

- **Trigger sharing from the platform's standard Share control and show the system's own sharing surface.** People know that
  path; a parallel one only confuses. Put the control somewhere convenient and stable, such as the toolbar.
- **Do not duplicate an action the system's share surface already offers.** If your version differs, title it so the
  difference is clear — "Print Transaction" rather than a second "Print".
- **Title each custom activity with a verb phrase and a recognisable symbol**, not with a company or product name.
- **Continue a slow share in the background and show its status in the app** — and do not notify people merely because it
  finished.
- **Summarise sharing permissions in one plain phrase** — "Only invited people can edit" — keeping the set of choices small
  and grouped.
- **Show a persistent collaboration indicator once content is shared**, beside the Share control, holding only the
  essentials people need while working together.
  [HIG: activity-views, collaboration-and-sharing]

## Documents and files

- **Provide menu commands and shortcuts for New and Open, plus a visible add control.** The keyboard path and the pointed-at
  path both have to exist.
- **Save people's work without asking them to** — periodically while they edit, and when they close a file or switch away.
  Where autosaving can be turned off, show unsaved changes clearly and prompt before the document closes.
- **Respect the platform's file-system model in a custom browser.** Open at the most relevant location but let people
  navigate everywhere else, and let them choose a destination when exporting or moving.
- **Hide file extensions by default and reflect that choice in every open and save interface.**
  [HIG: file-management, the-menu-bar]

## Translation to web and other platforms

These are the skill's own translations of the rules above, not Apple guidance.

- **Use `<button>` for an action and `<a href>` for navigation; never a `div` with a click handler.** Semantics deliver
  keyboard activation, focus and the accessible role for free.
- **Keep a visible focus indicator on everything focusable.** If you remove the default ring, replace it with a clearly
  contrasting custom one; style `:focus-visible` rather than deleting outlines.
- **Give an icon-only control a real accessible name** (`aria-label` or visually hidden text) plus a `title` for the desktop
  tooltip — the web gives a bare glyph no tooltip of its own.
- **Treat the browser's right-click menu as an accelerator, never a requirement.** Do not suppress it without cause, and
  give every item in a custom context menu a visible counterpart.
- **Build an actions menu as a proper menu-button widget:** it opens on click or Enter, arrow keys move through items,
  Escape closes it, focus returns to the trigger. Use a native `<select>` for a flat set of exclusive options.
- **Never trap the keyboard.** Tab must be able to leave every widget, Escape must close every overlay, and focus must
  return to the control that opened it.
- **Do not override browser or OS shortcuts** (find, new tab, close, address bar, print, save, undo, zoom). A single-key
  shortcut needs a modifier or a switch to turn it off, since it fires while people type.
- **Assume hover may not exist.** Anything revealed only on hover needs a tap or focus path too; gate hover-only refinements
  behind `@media (hover: hover)` and treat `(pointer: coarse)` as a hint, since many devices have both.
- **Keep the same 44×44 hit region in CSS pixels on every device**, reached with padding rather than larger graphics.
- **Give HTML drag-and-drop a keyboard and menu alternative and announce the result in a live region.** Native drag events
  are unreachable for many assistive-technology users.
- **Use the platform's share API where it exists, falling back to copy-link plus mail**, and keep one Share control rather
  than a row of network buttons.
- **In an Electron or Capacitor shell, build a real native command surface:** an application menu with the platform's
  standard menus and shortcuts and a Dock or tray menu on desktop; the system back gesture and safe areas on mobile. Every
  shell command must also be reachable inside the web UI, because the shell's menus can be hidden. See
  `references/platforms-and-web.md`.
  [translation]

## Deliberately omitted

- `menus-and-actions` — an index page with no guidance of its own; every child page assigned to this file is covered above.
- visionOS button geometry and materials (three shapes, 28–64 pt sizes, 60 pt centre spacing, glass backgrounds, no custom hover effects) and menu breakthrough effects over 3D content — spatial hardware, no generic equivalent.
- visionOS context-menu height limits, vertical toolbars, pull-down menus in a bottom-edge toolbar, hand-anchored content and the palm system-overlay gesture — device-shell constraints.
- tvOS focus artwork (parallax assets for the enlarged focused state) and the advice against showing a pointer — remote-driven TV interaction; the generic part, designing every focus state, is kept above.
- watchOS double-tap primary action, capsule-only inline button shapes and the scrolling toolbar button — watch hardware.
- The macOS AppKit button taxonomy (push, flexible-height, square, image, help) and the macOS pointer catalogue — framework inventories, not rules; the generic rules they imply are kept.
- Full menu-bar item tables (File, Edit, Format, View, Window, Help) and the complete standard shortcut table — reference material; fetch with `python3 scripts/hig.py the-menu-bar` or `hig.py keyboards`.
- The Apple menu, the Services submenu and menu-bar-extra sizing — system-shell surfaces an app cannot design.
- Quick Look viewers and generators, file-provider and Finder Sync extensions, document-launcher art direction — Apple system-integration surfaces with no cross-platform form.
- SharePlay, Messages collaboration events, CloudKit and iCloud sharing objects, universal links — Apple service integrations, not interface rules.
- Home Screen quick-action icon templates and 3D Touch pressure activation — tooling and superseded hardware.
- In-game key bindings and game-controller input — game controls have their own HIG page outside this file's scope.

## Sources

- `buttons` — https://developer.apple.com/design/human-interface-guidelines/buttons
- `menus` — https://developer.apple.com/design/human-interface-guidelines/menus
- `menus-and-actions` — https://developer.apple.com/design/human-interface-guidelines/menus-and-actions
- `context-menus` — https://developer.apple.com/design/human-interface-guidelines/context-menus
- `edit-menus` — https://developer.apple.com/design/human-interface-guidelines/edit-menus
- `pop-up-buttons` — https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons
- `pull-down-buttons` — https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons
- `toolbars` — https://developer.apple.com/design/human-interface-guidelines/toolbars
- `the-menu-bar` — https://developer.apple.com/design/human-interface-guidelines/the-menu-bar
- `dock-menus` — https://developer.apple.com/design/human-interface-guidelines/dock-menus
- `home-screen-quick-actions` — https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions
- `activity-views` — https://developer.apple.com/design/human-interface-guidelines/activity-views
- `collaboration-and-sharing` — https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing
- `gestures` — https://developer.apple.com/design/human-interface-guidelines/gestures
- `keyboards` — https://developer.apple.com/design/human-interface-guidelines/keyboards
- `pointing-devices` — https://developer.apple.com/design/human-interface-guidelines/pointing-devices
- `focus-and-selection` — https://developer.apple.com/design/human-interface-guidelines/focus-and-selection
- `drag-and-drop` — https://developer.apple.com/design/human-interface-guidelines/drag-and-drop
- `file-management` — https://developer.apple.com/design/human-interface-guidelines/file-management
- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- WWDC26 session 250, «Principles of great design» — https://developer.apple.com/videos/play/wwdc2026/250/

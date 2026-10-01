# Platforms, and the web

This file covers what each platform's people expect of an interface — how the device is held or
viewed, which inputs it offers, how dense and how deep a layout can be, how long a session lasts —
together with the conventions that govern windows and being switched away from, what changes when a
touch design moves to a desktop or across two displays, and how all of it translates to the web and
to Electron or Capacitor shells. Load it when you are deciding which platforms an interface must
serve, porting a design from one to another, building a web app or a shell, or judging whether a
layout adapts honestly rather than merely stretching. The rules here are instances of two of the
eight principles: **Flexibility** — «approach every platform with intention», support as many
devices and input methods as possible, and preserve a person's context as the design adapts; and
**Familiarity** — build on what people already know, which on a given device means that platform's
own conventions, applied consistently and in consistent places. Where a rule serves Craft (the same
quality on every device) or Simplicity (density that suits the viewing distance), the source tag
says which page it comes from.

## Reading a platform before you design for it

- **Write down five facts about the target platform before drawing anything: display size and resolution, how the device is held and how far from the eyes, which input methods are available, how long a typical session lasts, and which system features people expect to work.** Apple opens every platform page with exactly these five characteristics — display, ergonomics, inputs, app interactions and system features. What they settle between them is how dense a screen may be, how large its targets must be, how deep a hierarchy may go, and how much one screen may ask of a person [translation].
- **Set the size and density of onscreen content from viewing distance and input mode, not from the pixel count.** A large display held at arm's length and a large display seen from across a room carry entirely different amounts of content.
- **Support the system features people expect on that platform instead of reimplementing them.** People interact with the system in familiar, consistent ways, and a private substitute for a system facility is one more thing to learn and one more thing that behaves differently.
[HIG: designing-for-ios, designing-for-ipados, designing-for-macos, designing-for-watchos, designing-for-tvos]

- **Give every platform you support the same level of care.** «Approach every platform with intention» — software should feel polished and at home wherever it runs, which rules out treating one platform as the real design and the rest as ports.
- **Keep content and controls in consistent, predictable positions as the design adapts across platforms and configurations, and use natural animation to ease the transitions.** This is how a person's context survives a change of device or window size.
- **Design for as many input methods as the device offers — touch, pointer, keyboard, voice, remote, controller — rather than for the one you used while building.** Each input a design ignores excludes the people who rely on it.
[HIG: design-principles]

- **Do not recycle one solution everywhere.** Familiarity is not sameness: a phone invites quick touch interactions, a desktop invites deep workflows and precise pointer control, and each device deserves a solution that uses what makes it distinct.
- **Design for the contexts a person is actually in, not only the seated ideal.** The same task — playing music, say — is done at home through speakers, on a run through earphones and a watch, and hands-free while driving; an interface that accommodates the situation works for a wider audience.
- **When no single arrangement suits everyone, let people personalise: rearrange the controls, or hide the ones they never use.** Flexibility is an investment, and this is the cheapest form of it — it also proves the design was made with them in mind.
[WWDC26-250]

## Phone (iOS)

Held in one or both hands and turned between portrait and landscape at will, viewed from no more
than a foot or two, on a medium-sized high-resolution display. Input is multi-touch, a virtual
keyboard and voice. Sessions run from a minute of checking something to an hour of media or play,
with several apps open and frequent switching between them.

- **Limit the number of controls on screen and make secondary detail and actions reachable in one interaction.** The point is to let people concentrate on the primary task and content, not to hide functionality where it cannot be found.
- **Put the controls people use most in the middle or lower area of the display, where a hand holding the device can reach them.** Support the platform's reach-friendly patterns — swipe to go back, actions revealed on a list row — rather than putting everything in a top bar.
- **Adapt without being asked to orientation changes, to the dark appearance, and to the person's text size setting** (Dynamic Type on Apple platforms; the OS text-size preference generically). These are the person's choices, not edge cases.
- **With permission, take data from platform capabilities instead of asking people to type it** — payment, biometric authentication, location — so that the phone's advantages remove work rather than add screens.
- **Ported-in designs break here in three ways first:** too many controls competing at once; primary actions parked at the top edge out of reach; and a layout that survives neither rotation nor a larger text size.
[HIG: designing-for-ios]

## Tablet (iPadOS)

A large high-resolution display that people hold, prop on a surface, or set on a stand, so the
viewing distance varies but is typically within about three feet. Input is multi-touch, a virtual
keyboard, an attached keyboard or pointing device, a stylus and voice — often two at once. Sessions
range from a few quick actions to hours of creation or play, frequently with more than one app on
screen and content dragged between them.

- **Use the extra room to elevate the content people came for: fewer modal interfaces, fewer full-screen transitions, and controls placed where they are easy to reach but not in the way.** A large display is an argument for showing more of the work, not for scaling up a phone.
- **Let people use any available input — touch, a physical keyboard or trackpad, a stylus, voice — and support interactions that deliberately combine input modes,** for example a pointer for precision with the other hand on the keyboard. Do not make any one input mandatory for a task [translation].
- **Expect more than one app on screen and content dragged between them.** Make your content draggable out and accept drops in, and never assume you own the whole display.
- **Adapt to orientation, to multitasking sizes, to appearance and to text size, and be ready to run on the desktop.** A tablet app that assumes a fixed window has no path to a desktop version.
- **Ported-in designs break here in three ways first:** a stretched phone layout with one narrow column; modal sheets where a side-by-side pane fits; and fixed widths that break the moment the window is resized for multitasking.
[HIG: designing-for-ipados]

## Desktop (macOS)

A large high-resolution display, often with more displays attached, used while stationary at a desk
from roughly one to three feet away. Input is a physical keyboard, precise pointing devices, game
controls and voice. Sessions last from a few minutes of quick tasks to hours of deep concentration,
with many apps open and constant switching between active and inactive windows. People expect a
persistent command surface (the menu bar), file management, a full-screen mode and Dock menus.

- **Show more content in fewer nested levels and with less modality, while keeping the density comfortable enough that nobody has to strain.** Spaciousness is for flattening hierarchy, not for spreading one screen's worth of content across a window.
- **Let people resize, hide, show and move your windows, and support a full-screen mode for distraction-free work.** Window management is the person's, not the app's.
- **Put every command the app can perform in the menu bar,** which is where the platform gives people easy access to all the commands they need in an app, so nothing is reachable only by direct manipulation or by a gesture.
- **Support high-precision input and keyboard-only work styles:** pixel-accurate selection and editing, and a keyboard shortcut for every action people repeat.
- **Move smoothly between active and inactive states,** because people switch between many open apps constantly and each transition is visible.
- **Support personalisation:** customisable toolbars, windows configured to show the views a person uses most, and respect for the colours and fonts they have chosen in the system.
- **Ported-in designs break here in three ways first:** commands that exist only as taps and never appear in a menu or on the keyboard; one column of touch-sized controls with deep nesting and modal screens; and a window that cannot be resized, remembers nothing, and offers no customisation.
[HIG: designing-for-macos]

## Watch (watchOS)

A small display worn on the wrist, read at less than a foot by raising the arm and operated with the
other hand; an always-on state shows information when the wrist drops. Input is a rotating crown for
vertical navigation and value inspection, plain tap, swipe and drag gestures usable in motion, and a
hardware button for an essential action performed without looking. Interactions last seconds, many
times a day, and the surfaces around the app — glanceable widgets on the face, notifications — are
used more than the app itself.

- **Fit the essential task on one glanceable screen, with the action a gesture or two away.** Apple's rule for the wrist is a quick, glanceable, single-screen interaction that delivers the critical information succinctly. A screen that asks for sustained reading rather than a glance belongs on a larger device [translation].
- **Flatten the hierarchy to the minimum and give vertical navigation to the hardware control** (the Digital Crown on Apple Watch; generically, the platform's primary scroll input). Depth is the first thing to fail on a wrist.
- **Anticipate the moment: use on-device data to offer content that is relevant now or very soon,** instead of making people navigate to it.
- **Design the surfaces outside the app as first-class — glanceable data on the face, and notifications that let people act without opening the app — while the app itself still works on its own.** Those surfaces carry most of the real use.
- **Use background colour and material to carry supporting information and hierarchy** rather than adding chrome that costs pixels.
- **Ported-in designs break here in three ways first:** an imported multi-level hierarchy; screens that need more than a glance; and no peripheral surface at all, so the app is never reached.
[HIG: designing-for-watchos]

## Television (tvOS)

A very large high-resolution display seen from eight feet or more, sometimes while people move around
the room. Input is a remote, a game controller, voice, and apps on other devices — never a pointer.
Sessions can be hours in a single experience, with picture-in-picture alongside.

- **Design for a focus model rather than a pointer: let the system gently highlight and expand items as people move among them, so they know where they are and what to do at all times.** Where people reach elements with directional input, every onscreen element must be able to take focus, focus must move through custom views in an order that makes sense, and no pointer should be shown — people expect to step through a fixed set of items, not to drag a small pointer around a huge screen. [HIG: designing-for-tvos, focus-and-selection]
- **Make everything legible and captivating from across the room:** generous type and contrast, edge-to-edge artwork, animation that is subtle and fluid, and audio that carries part of the experience.
- **Make sign-in easy and infrequent, handle a shared sign-in, and switch profiles automatically when the viewer changes.** Text entry on a remote is slow and error-prone, so treat every screen that asks for typed text as a cost to remove rather than a step to polish [translation].
- **Ported-in designs break here in three ways first:** actions that depend on hover or a pointer; type, contrast and artwork sized for a hand-held screen; and flows that demand text entry or repeated sign-in.
[HIG: designing-for-tvos]

## Headset (visionOS) — brief

Content is placed in the space around a person, who sees both virtual content and their surroundings
through the device's cameras; they mostly look at a target and confirm with a small hand gesture, and
can also touch content directly. The system places content relative to the head, so people can stay
at rest. Visual comfort outranks everything else.

- **Use an ordinary window with familiar controls for standard tasks, and reserve immersion for the content that deserves it.** For each key moment, pick the lowest level of immersion that suits it; not every moment needs to be immersive.
- **Keep content inside the field of view and positioned relative to the person, so nothing requires turning the head or moving to interact with it.** Avoid motion that is jarring, too fast, or has no stationary frame of reference.
- **Support interactions that work with the hands resting in the lap or at the sides, and keep directly touched content close and brief.** Sustained reaching is a design defect on this platform.
- **Prefer the platform's standard components, which build in accessibility support by default,** on this platform as on every other; custom controls start with none of it.
[HIG: designing-for-visionos]

## Two displays and folding poses (iPhone Duo) — brief

One device, two displays and a hinge: people use the outer display closed, open it for the larger
inner display, and hold or stand it in many poses. The lesson generalises to any interface that must
stay continuous while its canvas changes shape.

- **Keep functionality and the state of every element the same across displays and poses.** Maintain one information hierarchy, and reveal an extra level on the larger display only when the content justifies it — a list and a detail side by side instead of one at a time.
- **Build for resizing rather than for displays: size classes, layout margins and safe-area insets, no fixed widths, no dependency on a particular display.** An interface built to resize adapts to a new pose with little work.
- **Avoid extreme layout changes as the canvas changes: move only what must move.** Controls that vanish or jump are hard to find and harder to track, so prefer small adjustments to rearrangement, and keep controls in the same relative positions across poses so nobody has to relearn where actions live.
- **Respect reserved regions — the areas a camera, a hinge or window controls occupy — and keep important content and controls clear of them.** Prefer a container that adapts on its own (a split view that rebalances its panes) and an even number of grid columns so content divides cleanly.
- **Give every non-text bar item both a title and a symbol, and assign visibility priority so overflow drops the least used item first.** The title is what the system shows in overflow menus and expanded forms.
[HIG: designing-for-iphone-duo]

## Windows and being switched away from

### Window conventions

- **Treat windows as a tablet, desktop and headset concept.** Phone, watch and television interfaces are single-screen by nature, so window management rules do not apply there; on the platforms that do have windows, the person owns them.
- **Distinguish a primary window, which holds the main navigation and content, from an auxiliary window dedicated to one task.** An auxiliary window offers no navigation elsewhere and carries a button to close it when the task is done.
- **Make windows adapt fluidly to any size,** because multitasking and multi-window workflows will produce sizes you did not choose.
- **Open a new window only when it helps people multitask or preserve context, and do not make it the default.** Composing a message beside the message being answered earns a window; opening one per navigation step is clutter.
- **Offer «open in a new window» as a command people can choose** — in a context menu or the platform's File menu — rather than deciding for them.
- **Never draw your own window frame or window controls, and never imitate the system's.** A copy that does not match the platform exactly makes the whole app feel broken.
- **Give window states distinct appearances so people can see which window is in front and which one will accept their typing.** On the desktop those states are main (frontmost), key (accepts input) and inactive; standard components change appearance automatically, custom ones do not.
- **Set a minimum and a maximum size for every window,** so the layout can neither collapse into overlapping controls nor stretch into uselessness.
- **Choose an initial size and shape that suit the content and leave little empty space** — wide for slides, tall for pages — and keep leading-edge toolbar items clear of the window controls by moving them inward when those controls appear.
- **Keep critical information and actions out of a bottom bar,** because people routinely position a window so its bottom edge is off screen; use it only for a little status about the window's contents, and put more in an inspector along the trailing edge.
- **Call a window a «window» in anything a person reads.** Implementation words such as «scene» confuse people who only see windows.
[HIG: windows]

### Being switched away from

- **Assume the person can leave at any moment: save and restore their context every time.** You do not get to know when multitasking begins.
- **Pause anything that needs attention or active participation when the person switches away, and let them resume as if they never left.** A game or a video that keeps running unattended costs the person their place and their time.
- **Finish work the person started in the background — a download, an export, a long processing job — rather than cancelling it at the moment they switch away.** If the task needs no further input, complete it before suspending.
- **Yield to audio interruptions: pause indefinitely for primary audio such as music or a podcast, duck briefly for short interruptions, then restore what you were playing.** The interruption belongs to the system, not to your app.
- **Notify on completion only for work that is important or time-sensitive to the person who started it.** Routine or secondary tasks do not earn an interruption; let people find the result when they come back.
- **Support multitasking unless there is a hard reason not to** (a game, a fully immersive experience). People read an app that blocks it as broken.
- **Adapt to any configuration without expecting to know or control it.** The person chooses the arrangement; the app only receives the size.
- **On desktop-like platforms, do not stop playback because the person is looking at or working in another window.** Playback started in one window is expected to continue while another is used.
[HIG: multitasking]

## Moving a touch design to the desktop

Apple's own path for this is Mac Catalyst — a Mac version of a tablet app. The rules below are the
design work that path requires, and they apply to any touch-first design being brought to a desktop.

- **Check first that the experience does not depend on what the target platform lacks.** If the core requires motion sensors, a rear camera, handwriting or navigation, the honest answer may be that it should not be ported.
- **Do more than display the old layout in a new window.** Each platform's conventions come from the way people actually use that device, so the port is a design task, not a build setting.
- **Replace a bottom tab bar with the desktop's own structure — a sidebar, or a segmented control for a genuinely flat hierarchy — and make sure every top-level destination is still listed in the command menu.** A sidebar used on both platforms also keeps the two versions recognisable to the same people.
- **Give every gesture a pointer and keyboard equivalent:** Next and Previous buttons beside a swipe, a context menu on every object people can act on, visible keyboard focus, and shortcuts for repeated actions. Desktop users expect each object to offer its own menu of relevant actions.
- **Re-flow single-column layouts into several columns, and put an inspector beside the content instead of inside a popover.** Reflow again as the window is resized rather than switching to a different design.
- **Adopt a top-down flow: the most important actions and content near the top of the window, with what was a touch toolbar becoming the window toolbar, and every one of those commands also present in the menu bar.**
- **Relocate controls that sat along the bottom and side edges for thumb reach.** That ergonomic reason does not exist at a desk; those controls belong in the toolbar or beside the content they affect.
- **Audit type, artwork and layout when the scale factor changes, and use text styles instead of fixed font sizes.** A ported interface either renders scaled down and slightly soft, or at full size and suddenly too large; both need a pass by eye.
- **Make a platform-specific app icon** rather than shipping one rendering style everywhere.
- **Build the groundwork on the touch platform first: drag and drop, keyboard navigation and shortcuts, multiple windows, and a layout that survives arbitrary resizing.** Each of these carries over, and without them a desktop port has nothing to stand on.
[HIG: mac-catalyst]

## Translation to web and other platforms

Everything in this section is this skill's translation of the rules above to the browser and to
shells. It is not Apple guidance, and the corpus does not discuss the web.

### The web is not a platform of its own

- **Treat the browser plus the host operating system as the platform whose conventions you must follow.** A web page inherits two sets of expectations and adds none of its own that outrank them; «the system» in any Apple rule reads as «the browser and the OS the person is using». [translation]
- **Keep the browser's own affordances working: Back and Forward, the URL as state, text selection, find-in-page, zoom, right-click, open-in-new-tab, and the platform's text-size and appearance settings.** Breaking Back is the web's version of trapping someone in a modal they cannot dismiss. [translation]
- **Give every navigable state its own URL, and make a deep link land in context** with its navigation, filters and scroll position intact rather than at a bare fragment of a screen. [translation]
- **Restore scroll position and unsent form input when people come back.** On the web, leaving and returning is one keystroke, so it is the normal case, not an accident. [translation]
- **Do not imitate one platform's chrome inside a web page.** A phone-style tab bar and back chevron in a desktop browser is unfamiliar on every platform at once; use plain controls that read correctly anywhere instead. [translation]
- **When your design system and the platform's convention disagree, the platform wins for anything positional or destructive.** People's muscle memory belongs to the OS, not to your components. [translation]
- **Make the page work when it is opened in a state you did not plan: a reloaded deep link, a second tab of the same app, a restored session.** Each is one gesture away in a browser and none of them is an error. [translation]

### One layout, every size and every input

- **Treat breakpoints as size classes, not as device names.** Decide by available space — compact or regular — because a desktop window can be narrower than a tablet and a tablet wider than a laptop. [translation]
- **Assume touch and pointer are both present, on the same visit.** Hover and right-click may enhance an action but must never be the only way to reach it, and nothing may depend on a cursor existing. [translation]
- **Keep the same hit region on the web — at least 44×44 points, in CSS pixels — including in dense desktop layouts,** where a trackpad is not the only input. Padding carries a smaller drawn control to the bar; `references/accessibility-inclusion-privacy.md` sets out hit region versus platform control size. [translation]
- **Reserve space for the platform's own furniture: safe-area insets for notches and home indicators, dynamic viewport units for collapsing browser bars, and the virtual keyboard's height.** Content must never sit under the browser's or the OS's own controls. [translation]
- **Do not lock orientation, and do not treat one orientation as the real one.** People turn a device whenever it suits them, and a page that only works one way up is broken half the time. [translation]
- **On a narrow viewport, keep the primary action within thumb reach and out of the top edge;** on a wide one, move it back to where a pointer expects it. This is the phone reach rule and the desktop top-down rule applied by size, not by device name. [translation]
- **Reflow a layout as the window changes size rather than switching between two unrelated designs at a breakpoint.** A visible re-composition costs people the position they had found. [translation]
- **Test rotation, window resize and a doubled text size as routine passes, not as edge cases.** The layout rules themselves are in `references/layout-and-navigation.md`. [translation]

### Platform materials in a browser

- **Use a system font stack so interface text renders in the host platform's own UI face,** with the platform families first and a generic family last; content type can still be your own. See `references/typography-color-visuals.md`. [translation]
- **Answer the platform's appearance and accessibility preferences through media queries — colour scheme, reduced motion, contrast, reduced transparency, forced colours — rather than only offering an in-app switch.** A person who set the preference once expects every app to honour it. [translation]
- **Size text in relative units and never disable zoom.** A viewport that forbids scaling removes a platform accessibility feature from everyone who visits. [translation]
- **Follow the host platform's keyboard conventions instead of inventing your own:** the platform's own modifier key for shortcuts, Escape to dismiss, Return to confirm the default action. [translation]
- **Prefer the platform's own controls for dates, times, selects, files and colours unless a custom one is better on every input** — keyboard, pointer, touch and screen reader alike. A native control arrives with all of that already working. [translation]
- **Honour the platform's reduced-data and reduced-power hints where they exist, and make heavy visual effects the first thing to go.** Craft on the web includes not making a laptop's fan spin. [translation]

### Installed web apps

- **An installed web app loses the browser's furniture, so supply what it removed:** your own Back affordance at every depth, a visible current location in place of the URL bar, and a way to reach a link's target in a real browser tab. [translation]
- **Keep every screen addressable even without a visible address bar,** because the app will be launched from a link, a shortcut or a share long after the session that created it. [translation]
- **Restore the last state on launch rather than starting at the home screen.** An installed app is judged against native apps, which resume where the person stopped. [translation]
- **Design the update path: say when a new version has loaded, and never swap the interface underneath someone mid-task.** [translation]
- **Decide deliberately what works offline, and show the honest state rather than an empty screen.** [translation]

### Desktop shells (Electron, Tauri, and similar)

- **A shell hosts web UI inside a native window: the shell follows the host platform's conventions, and the content inside follows the rules in the other reference files.** Judge the two separately — a perfect web app in a window that behaves like nothing else on the machine still reads as foreign. [translation]
- **Use the platform's real window frame and controls rather than drawing your own.** This is the window rule above applied to a shell: an imperfect copy of the platform's controls makes the app feel broken. [translation]
- **Populate a real application menu with every command, including the standard Edit menu and its shortcuts, and wire them to the web layer.** On a desktop, the menu is where people look for anything they cannot see. [translation]
- **Persist window size, position and per-window state across launches, set a minimum and maximum size, and support more than one window when the content warrants it.** [translation]
- **Support the platform's file interactions: open and save dialogs, dragging a file in, recent documents, and a document model people can reason about.** [translation]
- **Keep the app alive and correct while it is not in front: finish started work, keep state, and restore exactly where the person left off.** [translation]
- **Give the shell the platform's own dialogs for opening, saving and confirming destructive actions,** so those moments look and behave as they do everywhere else on the machine. [translation]
- **Do not ship a browser's context menu as the app's context menu.** Reload, View Source and Inspect are not commands your app offers; replace it with a menu of the object's real actions. [translation]

### Mobile shells (Capacitor, Cordova, and similar web views)

- **Follow the host platform's navigation model.** The system Back gesture or button must do what people expect at every depth, and it must never drop someone out of the app from the middle of a flow without warning. [translation]
- **Respect safe areas, the status bar and the keyboard.** The keyboard must not cover the focused field, and the layout must not jump when it opens or closes. [translation]
- **Switch off web-page behaviours that read as broken inside an app — overscroll bounce on chrome, double-tap zoom, tap highlights, selection callouts on controls — while leaving selection and zoom available on real content.** [translation]
- **Use the platform's own facilities where they exist: native date and time pickers, the system share sheet, the camera, biometric authentication — and ask for permission at the moment of use, with the reason.** Permission timing and wording are in `references/accessibility-inclusion-privacy.md`. [translation]
- **Design the offline and slow-connection states deliberately.** A shell looks like an app, so people expect app behaviour: cached content, queued actions, and an honest statement of what has not been sent. [translation]
- **Leave system animation, haptics and sound to the platform, and check the result on the smallest supported screen at the largest supported text size.** [translation]
- **Keep scrolling and gestures native in feel: no custom scroll hijacking, no gesture that competes with the system's own edge gestures.** Jittery scrolling is the clearest signal a shell is a web page in disguise. [translation]
- **Treat the web layer's storage as a real app's storage:** survive a cold start, a backgrounded process and a lost connection without losing what the person typed. [translation]

## Choosing what to read next

- Laying out a screen, choosing a navigation structure, windows and scrolling → `references/layout-and-navigation.md`.
- Deciding whether something deserves a dialog, a sheet or a notification → `references/modality-alerts-notifications.md`.
- Type, colour, dark appearance, icons and images → `references/typography-color-visuals.md`.
- Feedback, animation, loading and launch → `references/motion-feedback-loading.md`.
- Wording, help, first run, settings and accounts → `references/writing-help-onboarding-settings.md`.
- Fields, pickers, validation and undo → `references/forms-and-data-entry.md`.
- Buttons, menus, toolbars, gestures, keyboard, pointer and drag and drop → `references/actions-menus-and-input.md`.
- Accessibility, inclusion, right-to-left, privacy and AI features → `references/accessibility-inclusion-privacy.md`.
- Charts, tables and numbers → `references/data-and-charts.md`.
- The reasoning behind a trade-off, or a brief for a builder → `references/principles.md`; a review of finished work → `references/review-checklist.md`.
[translation]

## Deliberately omitted

- **visionOS spatial specifics** — volumes and baseplates, ornaments, the mandatory glass window background, immersion levels and passthrough control, spatial audio, spatial Personas, dynamic versus fixed scaling, default window size and placement distance. These depend on head-worn hardware and eye input and have no form on a screen; the generic parts (prefer a familiar window, comfort first, hands at rest) are kept above. [designing-for-visionos, windows]
- **The Apple Vision Pro safety notice** — not for use while driving or moving through unsafe spaces, minimum age. Hardware safety, not interface design. [designing-for-visionos]
- **Wrist-hardware surfaces by name** — complications, watch faces, Always On rendering, the Digital Crown's detents, the Action button. Single-platform hardware; the transferable rules (one glanceable screen, flat hierarchy, peripheral surfaces carry the use) are kept. [designing-for-watchos]
- **Television-specific system surfaces** — Top Shelf, integration with the TV app, SharePlay, TV provider accounts, the Siri Remote's gesture catalogue. Apple-owned extension points with no generic equivalent; the focus model, legibility at distance and cheap sign-in are kept. [designing-for-tvos]
- **The phone and tablet system-feature lists** — widgets, Home Screen quick actions, Spotlight, Shortcuts, Siri, gyroscope and accelerometer input, spatial interactions. These are Apple integration points; the rule that a platform's expected system features must be supported is kept. [designing-for-ios, designing-for-ipados]
- **Mac Catalyst build and API detail** — the idiom setting in Xcode, the 77 % versus 100 % scale factors as configuration, separate asset catalogues, framework names, and the tables translating each touch gesture to a mouse or trackpad action. Build configuration rather than design; the design consequences (audit type and layout, add pointer and keyboard equivalents) are kept. [mac-catalyst]
- **iPhone Duo API and form-factor detail** — split and overlay arrangement views, the reserved-region APIs, the vertical bar layout with its placement order and the Dynamic Island, and the letterboxing rules for games. One device's hardware and its framework; the generic rules (resize, identical state across displays, no extreme layout changes, respect reserved regions, title plus symbol on bar items) are kept. [designing-for-iphone-duo]
- **Picture-in-picture and audio-session behaviour beyond the interruption rule** — ducking rules, Now Playing behaviour, per-platform playback specifics. Sound and playback feedback belong to `references/motion-feedback-loading.md`. [multitasking]
- **Game-specific platform guidance** — the corpus carries a `designing-for-games` page, which this file was not assigned; game design is outside this skill's scope.

## Sources

Corpus pages used, each at `https://developer.apple.com/design/human-interface-guidelines/<slug>`:

- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- `designing-for-ios` — https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
- `designing-for-ipados` — https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados
- `designing-for-macos` — https://developer.apple.com/design/human-interface-guidelines/designing-for-macos
- `designing-for-watchos` — https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos
- `designing-for-tvos` — https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos
- `designing-for-visionos` — https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos
- `designing-for-iphone-duo` — https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo
- `focus-and-selection` — https://developer.apple.com/design/human-interface-guidelines/focus-and-selection
- `mac-catalyst` — https://developer.apple.com/design/human-interface-guidelines/mac-catalyst
- `multitasking` — https://developer.apple.com/design/human-interface-guidelines/multitasking
- `windows` — https://developer.apple.com/design/human-interface-guidelines/windows

Talk: «Principles of great design», WWDC26 session 250 — https://developer.apple.com/videos/play/wwdc2026/250/

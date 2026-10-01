# Motion, feedback and loading

How an interface answers back: feedback for status, success, failure and warnings; motion that carries
meaning instead of decorating; the design of waiting — placeholders, progress, cancellation; status
indicators; the first frame after launch; haptics and sound as extra channels. Load it when a screen
must report what is happening (saving, syncing, uploading, generating), when you add or audit
animation, when an operation takes longer than an instant, or when a review turns up a spinner that
never resolves, a bar that freezes, or a failure that says nothing. It serves **Familiarity** —
«provide clear feedback» is one of the three Familiarity sub-rules; **Craft** — responsive animation
giving immediate, natural feedback is an ingredient of well-crafted design, and a rushed product
feels like a tap that does nothing; **Flexibility** — natural animation preserves context and motion
is never the only carrier of information; **Agency** — people stay informed and can stop what they
started; **Delight** — a defining moment can be a button press or an error message, not confetti.

[HIG: design-principles, feedback, motion] [WWDC26-250]

## Feedback

### Match the delivery to the significance

- **Choose the channel from how much the information matters.** Status sits passively in the
  interface; a warning about data loss must interrupt, since that is the only chance to avoid it.
- **Put status feedback next to the items it describes.** Information near its subject arrives without
  an extra action — a mailbox carrying its last-update time and unread count in its own toolbar.
- **Reserve interrupting alerts for critical, actionable information, never for status.** Alerts
  disrupt by design and lose force when spent on trivia: `references/modality-alerts-notifications.md`.

[HIG: feedback]

### Warnings, confirmations and refusals

- **Warn before data loss that is both unexpected and irreversible, and only then.** Interrupt when
  someone is about to make a big mistake; people appreciate help avoiding disaster.
- **Do not warn when the loss is the expected result of the action.** A file manager does not confirm
  every move to the trash; a confirmation there only trains people to click through.
- **Confirm that a significant action completed, not that every action did.** People expect success, so
  they mainly need to hear about failure; confirm a payment or a submission, not a field edit.
- **When a command cannot be carried out, show the failure and help people understand why.** Name what
  blocked it — a route request with the same start and destination should say exactly that.
- **Prefer undo to a confirmation whenever the action is reversible.** Forgiveness is what lets people
  explore; see `references/forms-and-data-entry.md` for undo scope and naming.

[HIG: feedback] [WWDC26-250]

### Feedback in more than one channel

- **Deliver important feedback through at least two of colour, text, sound, motion and haptics.** Two
  channels reach the person who silenced the device, looked away, or is using a screen reader.
- **Never let motion, colour or sound alone carry a meaning.** Each is unavailable to somebody, and on
  every platform important information must not depend on sound.
- **Announce state changes to assistive technology, not only to the eye.** A row saved or an upload
  finished must be spoken too: `references/accessibility-inclusion-privacy.md`.
- **On a surface people only glance at, avoid an animated indeterminate indicator.** A spinner tells
  them to keep watching; promise a notification instead (Apple states this for watchOS).

[HIG: feedback, motion, color, playing-audio, voiceover]

## Motion

### Motion with a job to do

- **Add motion purposefully, to support the experience rather than overshadow it.** Gratuitous
  animation distracts and can leave people feeling disconnected or physically uncomfortable.
- **Delete any animation that conveys no status, feedback, instruction or transition.** Those are what
  motion is for; anything else spends attention and returns nothing.
- **Prefer the platform's built-in motion to a custom equivalent.** System components animate
  consistently and adapt to accessibility settings and to the input method in use.
- **Do not animate interactions that happen constantly.** The platform already gives standard elements
  a subtle response; a custom animation on a frequent control charges attention every single use.
- **Keep one motion meaning one thing.** Elements that look alike have to behave alike, so a given
  transition must signal the same kind of change everywhere.

[HIG: motion] [WWDC26-250]

### Feedback motion

- **Make motion follow the gesture and the expectation it set up.** A view pulled down from the top
  should not leave sideways; motion that contradicts the gesture disorients.
- **Aim for brevity and precision in feedback animation.** A short, exactly-timed animation feels light
  and often carries the message better than a prominent one.
- **Let people cancel motion; never make them wait for an animation to finish.** Any animation endured
  more than once taxes repetition, so the next input must land mid-flight.
- **Hold a steady frame rate rather than a high peak one, and let people trade richness for battery.**
  Apple names a steady 30 to 60 fps as smooth for most games; jitter makes a product feel fragile.
- **Animate a symbol only when the animation says something.** Symbol animation is a system feature
  (Apple: SF Symbols); icon rules are in `references/typography-color-visuals.md`.

[HIG: motion] [WWDC26-250]

### Reduced motion and comfort

- **Make motion optional and keep the experience complete without it.** Not everyone can or wants to
  experience animation, so supplement visual feedback with text, haptics or audio.
- **Cut automatic and repetitive animation when a reduce-motion preference is on.** Zooming, scaling
  and motion at the edges of the screen go first (Apple's Reduce Motion setting).
- **Replace positional transitions with fades when motion is reduced.** Apple's list: tighten springs,
  track animation to the gesture, avoid depth, z-axis and blur changes, swap x/y/z moves for fades.
- **Be cautious with fast-moving or blinking animation, and never autoplay media without a stop
  control.** In excess these effects distract, cause dizziness and can trigger epileptic episodes.
- **Avoid elements that dismiss themselves on a timer.** People who read slowly or traverse the screen
  with an assistive technology lose the content; prefer dismissal by an explicit action.

[HIG: motion, accessibility]

## Loading and waiting

### Design the wait away first

- **Design the load so it finishes before people notice it.** That is the best loading experience;
  everything below is damage control for when you cannot reach it.
- **Show something as soon as possible.** An empty screen reads as a broken product, so show
  placeholder text, graphics or a skeleton of the real layout and replace parts as they arrive.
- **Let people do other things while content loads.** Load in the background so the rest of the
  interface stays usable; never freeze a whole screen for a partial load.
- **Move large downloads out of the critical path.** Schedule big assets after installation, during
  updates or at other non-disruptive times (Apple: the Background Assets framework).
- **If the wait is unavoidably long, show something worth looking at, sized to the real wait.** Tips or
  a new-feature introduction work; estimate the time left so the filler is neither cut off nor looped.

[HIG: loading]

### Progress

- **Say that content is loading, and prefer a determinate indicator whenever duration is computable.**
  Knowing the length lets a person wait, switch tasks, return later or abandon; a spinner cannot.
- **Report advancement accurately and evenly.** Ninety percent in five seconds and the last ten in five
  minutes makes people doubt the product is working, and feels deceptive.
- **Keep the indicator moving.** A stationary one reads as a frozen product; if the process has really
  stalled, replace it with feedback explaining the problem and the way out.
- **Switch indeterminate to determinate once duration is known, but never change the shape.** Going
  from a spinner to a bar disrupts the layout and hides whether it is the same operation.
- **Treat a progress indicator as transient.** It appears only while the operation runs; a permanent
  progress element is a status display, not progress.
- **Add a description only when it adds context, and keep it accurate and succinct.** Vague words like
  «loading» or «authenticating» seldom add value; name the thing being fetched or the step.
- **Put progress in a consistent place.** One reliable location across screens means people know where
  to look for the status of an operation.
- **A small spinner suits background work and tight spaces, and needs no label.** Beside a field or a
  button it reads as «this part is working» without taking over the screen.

[HIG: loading, progress-indicators]

### Stopping and refreshing

- **Offer Cancel whenever a process can be interrupted without negative side effects.** The freedom to
  stop is part of staying in control of one's own work.
- **Offer Pause as well when interrupting would discard real progress.** Losing a half-downloaded file
  to a mis-click is a cost people should not have to pay.
- **Tell people when halting costs them something, and let them confirm or resume.** A cancellation
  that destroys progress deserves the same warning as any other irreversible loss.
- **Keep content fresh automatically; a manual refresh is an addition, not the mechanism.** People
  expect periodic updates and should not be responsible for initiating every one.
- **Give a manual refresh a title only if the title carries information.** Say when the content was
  last updated rather than explaining how to refresh; the animation already shows loading.

[HIG: progress-indicators, feedback]

## Status indicators

- **Use a gauge when one value has to be read against a range.** It maps the value onto a circular or
  linear path; the capacity style fills the path up to the value instead of marking a point.
- **Label the current value and both ends of the range.** Labels make a gauge readable and a screen
  reader speaks the visible ones, so an unlabelled gauge is decoration.
- **Use colour in a gauge to reinforce meaning, not to brighten it.** A gradient can carry the range
  (hot to cold), and a fill colour that changes at a significant level says what length cannot.
- **Prefer a continuous fill to discrete segments over a large range.** Many values make segments too
  small to read, and segments fill completely rather than partially.
- **Keep a rating indicator editable in place.** When items are ranked, let people adjust the rank
  inline instead of opening a separate editing screen.
- **Keep the star, or make a custom rating symbol unmistakable.** Other shapes may not read as a
  rating, and a rating rounds to whole symbols, so never use one where a precise value matters.
- **Do not repurpose, restyle or decorate with a system status graphic.** Apple's Activity rings mean
  Move, Exercise and Stand, keep their colours and background, and never carry other data or branding.
- **Show one person's data in a personal status graphic, and label whose it is.** Mixing people into
  one progress graphic misreports all of them; a name, photo or avatar removes the doubt.
- **Do not duplicate a status the platform already reports.** A second notification of the same
  progress only confuses. Charts and tables: `references/data-and-charts.md`.

[HIG: status, gauges, rating-indicators, activity-rings]

## Launch and the first frame

- **Launch instantly; people are not willing to wait more than a couple of seconds.** Launch ends when
  the first screen is ready, so whatever happens before that is taken from the person.
- **Where the platform shows a launch screen, make it nearly identical to the first real screen.**
  Differing elements flash at the hand-off; match the current orientation and appearance mode.
- **Keep marketing off the launch screen, and logos and other branding elements too unless they are a fixed part of
  the first real screen** — when the mark is fixed there, the "nearly identical" rule above puts it on the launch screen
  as well. Keep text off it in any case: launch-screen content never changes, so it is never localised.
- **If you need a splash screen, put it at the start of onboarding, not in the launch path.**
  Onboarding follows launch and is separate and optional: `references/writing-help-onboarding-settings.md`.
- **Do not put a permission prompt in the launch path.** Asking before a person knows what the product
  does is the interface version of demanding a phone number for no stated reason.
- **Restore the previous state on relaunch.** Scroll position, selection, open windows and their
  locations — do not make people retrace steps to get back where they were.
- **Open in the configuration the person is already in.** Launch in the device's current orientation
  when both are supported; on desktop, reopen where the window was left.

[HIG: launching, onboarding] [WWDC26-250]

## Haptics and sound

- **Treat haptics and sound as reinforcement, never as the primary channel.** Match a haptic's
  intensity and sharpness to the animation it accompanies so the channels agree.
- **Use the platform's standard haptic patterns for their documented meanings.** People recognise them
  from system controls; if a documented use does not fit, use a generic pattern instead.
- **Keep one haptic meaning one thing throughout the product.** A pattern learned as failure must not
  appear on success; without a clear cause and effect a haptic is noise.
- **Prefer short haptics tied to discrete events.** Long continuous haptics dilute meaning outside
  gameplay; custom patterns combine transient taps and continuous events varied by intensity.
- **Do not overuse haptics.** One that feels right occasionally becomes tiresome when it fires
  constantly; the best is often barely noticed but missed when off.
- **Make haptics optional and check they do not disturb the device.** People must be able to mute them,
  and haptic force can interfere with the camera, gyroscope or microphone.
- **Honour silent mode: only audio the person explicitly started keeps playing.** Clicks, effects and
  soundtracks are non-essential; media playback and alarms are not.
- **Let the system volume govern the final output.** Balance your own levels against each other, but
  never reach over the person's volume setting.
- **Follow the output the person chose.** Reroute to a newly connected device without interruption and
  pause immediately when headphones are unplugged.
- **Pick the audio role that matches what sound is for, and do not silence other apps needlessly.**
  Ambient effects should mix with music someone is already playing; only essential audio interrupts.
- **Do not respond to or redefine media controls outside a real audio context.** Play, pause and skip
  behave the same everywhere; a product that does not support a control should not react to it.
- **Vary a sound people will hear hundreds of times.** Small changes of pitch and volume keep a
  repeated cue from grating, the way a keyboard sound differs on every keypress.

[HIG: playing-haptics, playing-audio, feedback]

## Translation to web and other platforms

Every bullet here is this skill's own translation, not Apple guidance.

- **Gate non-essential animation behind `prefers-reduced-motion: reduce`.** In the reduced branch keep
  opacity and colour changes; drop transforms, parallax, looping motion and scroll-driven effects.
- **Never let a transition block the next input.** Keep interface transitions short enough that a
  second click lands during them, and interrupt rather than queue.
- **Render the expected result immediately and reconcile with the server after.** Optimistic updates
  are how the web «finishes before people notice»; always pair one with a visible way back on failure.
- **Choose the wait indicator by what you know.** Skeleton where the layout is known, small inline
  spinner beside the control for a short unknown wait, determinate bar for a transfer of known size.
- **Reserve the space a placeholder occupies.** A skeleton replaced by taller content shifts the page
  under the pointer — the web form of a layout that jumps.
- **Expose status to assistive technology, not just to the layout.** `role="status"` for «Saved» or
  «Upload failed», `aria-busy` on the loading region, `<progress>` without `value` for indeterminate.
- **Make Cancel actually cancel.** It should abort the in-flight request (for example via
  `AbortController`) and restore the prior state, not merely hide the indicator.
- **Treat the first paint as the launch screen.** Ship enough shell that the first frame matches the
  loaded page, and restore route, scroll position and open panels from the URL and stored state.
- **Assume haptics and sound may never arrive.** Web vibration is coarse and often disabled and
  browsers block autoplay with audio, so both may only reinforce something already visible.
- **In an Electron or Capacitor shell, take motion and feedback timing from the host platform.** Window
  animation, haptics and system sounds belong to the OS; see `references/platforms-and-web.md`.

[translation]

## Deliberately omitted

- **visionOS motion comfort** (peripheral motion, large moving objects, translucency and contrast for
  discomfort, fades, world rotation, oscillation, a stationary frame): head-mounted only. [motion]
- **watchOS animation implementation** (SwiftUI versus WatchKit, non-customisable built-in easing): API
  detail, not a design rule. [motion]
- **Activity ring specifics** (ring semantics, published RGB label colours, black background, margin
  and enclosure rules, Watch pairing): an Apple-owned HealthKit graphic. [activity-rings]
- **Platform haptic catalogues** (macOS Alignment / Level change / Generic; the watchOS vocabulary from
  Notification to Click; Digital Crown detents): device-specific lists. [playing-haptics]
- **Audio session mechanics** (the category table with its mixing and background behaviour,
  interruption resumability, the system volume view, watchOS 64 kbps HE-AAC): developer configuration;
  the behaviours people perceive are kept above. [playing-audio]
- **visionOS Spatial Audio design** (ambient audio versus sources, fixed versus tracked sound, sounds
  for custom spatial elements, «prefer playing sound»): spatial computing only. [playing-audio]
- **Platform-specific launch cases** (tvOS static launch screens and auto-starting live playback,
  visionOS launching into the Shared Space): tied to one platform's hardware and app model. [launching]
- **macOS level-indicator variants** (the rarely used relevance style) and the accessory gauge style
  echoing watch complications: component variants; gauge presentation belongs to
  `references/data-and-charts.md`. [gauges]
- **Framework pointers** (Background Assets, GameKit large downloads, `UIRefreshControl`,
  `ProgressView`, Core Haptics API, custom game loading views): implementation, not design rules.
- **`components/status` has no guidance of its own** — it indexes Activity rings, gauges, progress
  indicators and rating indicators, all covered above. [status]

## Sources

- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- `feedback` — https://developer.apple.com/design/human-interface-guidelines/feedback
- `motion` — https://developer.apple.com/design/human-interface-guidelines/motion
- `loading` — https://developer.apple.com/design/human-interface-guidelines/loading
- `status` — https://developer.apple.com/design/human-interface-guidelines/status
- `progress-indicators` — https://developer.apple.com/design/human-interface-guidelines/progress-indicators
- `gauges` — https://developer.apple.com/design/human-interface-guidelines/gauges
- `activity-rings` — https://developer.apple.com/design/human-interface-guidelines/activity-rings
- `rating-indicators` — https://developer.apple.com/design/human-interface-guidelines/rating-indicators
- `playing-haptics` — https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- `playing-audio` — https://developer.apple.com/design/human-interface-guidelines/playing-audio
- `launching` — https://developer.apple.com/design/human-interface-guidelines/launching
- `onboarding` — https://developer.apple.com/design/human-interface-guidelines/onboarding
- `accessibility` — https://developer.apple.com/design/human-interface-guidelines/accessibility
- `color` — https://developer.apple.com/design/human-interface-guidelines/color
- `voiceover` — https://developer.apple.com/design/human-interface-guidelines/voiceover
- Principles of great design, WWDC26 session 250 — https://developer.apple.com/videos/play/wwdc2026/250/

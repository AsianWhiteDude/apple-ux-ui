# Typography, color and visuals

This file covers the visual materials an interface is made of: type, color, light and dark appearances, depth and layering, icons and symbols, app icons, images, and how much brand to let through. Load it when you are choosing a type scale or a palette, adding a dark appearance, building an icon set, placing artwork, or reviewing a screen that looks unfinished. It serves **Craft** most directly — the WWDC26 talk lists beautiful fonts, colors that adapt across light and dark environments, and clear graphics and iconography as the "high-quality materials" a crafted design is built from — and then **Simplicity** (hierarchy built from order, spacing and contrast), **Flexibility** (legible at every text size, in every appearance, for people who see color differently), **Familiarity** (semantic color and standard metaphors applied consistently), and **Responsibility** (never let color alone carry meaning). Layout, spacing and windows are in `references/layout-and-navigation.md`; animation, loading and launch in `references/motion-feedback-loading.md`; contrast and color as accessibility duties in `references/accessibility-inclusion-privacy.md`.

## Typography

Type is where hierarchy is won or lost: a strong hierarchy makes the most important thing on the screen the most obvious one, and it is built from order, spacing and contrast rather than from decoration. [WWDC26-250]

### Legibility

- **Set body text at a size most people can read without effort, and treat the platform's minimum as a floor, not a target.** Apple's defaults and minimums: iOS and iPadOS 17 pt / 11 pt, macOS 13 pt / 10 pt, tvOS 29 pt / 23 pt, visionOS 17 pt / 12 pt, watchOS 16 pt / 12 pt — and they apply to custom fonts as much as to the system font. [HIG: typography]
- **Raise sizes as viewing distance grows.** The same guidance that puts body text at 17 pt on a phone puts it at 29 pt on a television; a wall display, a kiosk or a dashboard read from across a room needs the same treatment. [HIG: typography]
- **Avoid light font weights for interface text.** Prefer Regular, Medium, Semibold or Bold; Ultralight, Thin and Light are hard to see, especially when text is small. [HIG: typography]
- **If you use a thin or delicate custom face, set it larger than the recommended minimum.** Weight changes how readable a given size is, so the floor moves up with a lighter face. [HIG: typography]
- **Test text in the conditions people actually read it in, and fix failures at the source.** When something is hard to read, increase the size, raise the contrast between the text and its background, or switch to a face designed for legibility — do not ship it and hope. [HIG: typography]
- **Maximise contrast between text and whatever sits behind it, and prefer a bolder weight to a drop shadow when text has no solid backing.** Apple states this for visionOS, where text can float without a surface to cast a shadow on; it holds anywhere text sits over imagery or video. [HIG: typography]

### Hierarchy and scale

- **Define a small, fixed set of text styles — each a combination of weight, size and leading — and build every screen from it.** A named scale is what keeps hierarchy consistent across screens and lets all text scale proportionally when the reader changes their text size. [HIG: typography]
- **Choose a style by the role the text plays, not by the size you want.** Apple's body style carries values tuned for comfortable multi-line reading; its headline style carries a size and weight that separate a heading from the content around it. [HIG: typography]
- **Express hierarchy with weight, size and color, and keep the relative distinctions intact when text sizes change.** If a headline is only one step above body at the default size, it collapses into body at the largest size. [HIG: typography]
- **Minimise the number of typefaces, even in a heavily styled interface.** Mixing faces obscures the information hierarchy, hurts readability, and makes an interface feel internally inconsistent or poorly made. [HIG: typography]
- **Create an extra level of emphasis with a bolder variant of the same style, never with a new face or a hand-picked size.** Apple exposes this as an emphasised weight per style (medium, semibold, bold or heavy). [HIG: typography]
- **Give long or wide passages looser leading, and use tight leading only where height is genuinely constrained.** Never use tight leading for three or more lines of text, even in a cramped list row. [HIG: typography]
- **Let a variable font do the optical sizing instead of picking a discrete display or text cut.** Apple's system fonts interpolate each letterform to the exact point size; specify a discrete optical size only when a design tool cannot handle the variable format. [HIG: typography]
- **Adjust tracking in static mockups so they match the running interface.** The system font adjusts tracking at every point size automatically, so an untracked mockup misrepresents what will ship. [HIG: typography]
- **Distil before you shrink.** If a block is too dense for its space, ask whether the data reads better as a graphic or a summary — sometimes clarity means adding context rather than removing it, as a play/pause control gains meaning when it also shows elapsed and remaining time. [WWDC26-250]

### A reference type scale

Apple's iOS text styles at the default text size, as a concrete starting point. Use it as a shape for a scale, not as a spec to copy: on macOS the same styles are smaller (body 13/16, large title 26/32), on tvOS far larger (body 29/36).

| Style | Size / leading (pt) | Weight |
|---|---|---|
| Large Title | 34 / 41 | Regular |
| Title 1 | 28 / 34 | Regular |
| Title 2 | 22 / 28 | Regular |
| Title 3 | 20 / 25 | Regular |
| Headline | 17 / 22 | Semibold |
| Body | 17 / 22 | Regular |
| Callout | 16 / 21 | Regular |
| Subhead | 15 / 20 | Regular |
| Footnote | 13 / 18 | Regular |
| Caption 1 | 12 / 16 | Regular |
| Caption 2 | 11 / 13 | Regular |

- **Keep the number of live styles on a screen to a handful.** Every style you add is a level of hierarchy you are claiming exists; if two levels do not differ in weight or size by a visible step, one of them is not a level. The count and the step test are this skill's own: Apple limits typefaces (above), not how many of its eleven text styles a screen draws from. [translation]
- **Derive every other size from the scale, not from the mockup you are looking at.** Ad-hoc sizes are what make a second screen look like a different product. [HIG: typography]

### Text scaling and reflow

- **Honour the reader's text-size setting throughout the interface.** Apple's form is Dynamic Type on iOS, iPadOS, tvOS, visionOS and watchOS (macOS does not support it); the generic form is respecting the platform's or the browser's text-size preference instead of fixing text in place. [HIG: typography]
- **Verify every screen at the largest accessibility text size, not just at the default.** Turn the larger accessibility sizes on and confirm the screen is still readable and operable — this is where layouts break first. [HIG: typography]
- **Scale what matters and leave the chrome alone.** Someone raising their text size wants the content they came for to get bigger, not every tab title and transient value on the screen. [HIG: typography]
- **Keep truncation to a minimum as text grows.** Aim to show as much useful text at the largest accessibility size as at the largest standard size, let labels use as many lines as they need, and don't truncate inside a scrolling region unless a detail view shows the rest. [HIG: typography]
- **Reflow the layout at large sizes instead of squeezing text.** Stack text above secondary items where a row would crowd, and reduce the number of text columns as the size grows. [HIG: typography]
- **Keep the information hierarchy and the position of primary elements stable at every text size.** Primary elements stay near the top of the view so people don't lose track of them when text is very large. [HIG: typography]
- **Grow meaningful icons along with the text beside them.** An icon that carries information has to stay readable at large text sizes; Apple's symbols scale with the text setting automatically, a custom set must be made to. [HIG: typography, sf-symbols]

### System fonts and custom fonts

- **Default to the platform's system typeface.** It is engineered for legibility across sizes, ships the range of weights and widths hierarchy needs, and picks up text scaling and accessibility settings for free. [HIG: typography]
- **Reach the system font through the platform's API rather than embedding a copy of it.** An embedded copy drifts from the platform and loses the variable-font behaviour. [HIG: typography]
- **Take the monospaced and rounded cuts from the same family as your body face.** Apple ships mono and rounded variants of its system font so you can coordinate text with soft or rounded elements, or give it an alternative voice, without leaving the family. [HIG: typography]
- **If a custom font carries your brand, prove it is legible at every size first, and give it the accessibility behaviour the system font has.** It must answer bold-text and text-scaling settings like any other text. [HIG: typography, branding]
- **Use a custom face for headlines and subheadings and the system face for body copy and captions.** System faces are designed for optimal legibility at small sizes, which is exactly where a display face fails. [HIG: branding]
- **Use a symbol rather than a word when you need to depict an object or a concept inline, especially inside a run of text.** Symbols read faster and take less space than a repeated noun. [HIG: typography, sf-symbols]
- **Match symbol weight to the weight of adjacent text unless you deliberately want one to dominate.** Apple's symbols define nine weights corresponding to the system font's for exactly this; a custom icon set needs the same discipline. [HIG: sf-symbols, icons]

Labels, empty states and the wording inside all of this are in `references/writing-help-onboarding-settings.md`.

## Color

Color here follows Familiarity and Responsibility before aesthetics: the same color must mean the same thing everywhere, and no meaning may rest on color alone.

### Color as meaning

- **Prefer the platform's own colors wherever they fit your meaning.** They already define variants for light, dark and increased contrast, adapt to vibrancy and accessibility settings, and make the product feel at home on the device — a custom color has to earn all of that by hand. [HIG: color]
- **Give each color one job and keep it.** If your brand color means "interactive", styling non-interactive text in the same or a similar color makes the interface unreadable as a system of signals. [HIG: color]
- **Name colors by role, not by hue, and use a semantic set that adapts to the current appearance.** Apple's dynamic system colors are defined by purpose — label, secondary label, placeholder text, separator, link, background levels — rather than by their values. [HIG: color]
- **Don't hard-code the values of a platform's semantic colors.** Published values are design-time reference and shift between releases; read them through the API so your interface moves with the platform. [HIG: color]
- **Don't repurpose a semantic color outside its meaning.** A separator color used as text color, or a secondary-label color used as a background, breaks the moment the platform's appearance changes. [HIG: color]
- **Build depth from the levels a semantic set gives you:** primary background for the overall view, secondary for groups inside it, tertiary for groups inside those; primary through quaternary labels for descending text importance, plus a distinct placeholder color. [HIG: color]
- **Never let color be the only thing that carries information, interactivity or state.** Add a text label, a glyph or a difference in shape so the same information survives color blindness and low-contrast viewing. [HIG: color]
- **Don't signal focus or selection with color alone either.** Apple's tvOS guidance uses scaling and responsive animation as the primary focus cues; on any platform pair the color change with a ring, a size change or a mark. [HIG: color]
- **Don't ship color combinations that make content hard to perceive.** Insufficient contrast lets icons and text blend into the background, and some pairs are indistinguishable to people who are color blind. [HIG: color]
- **Check what your colors mean to the audiences you ship to.** Red reads as danger in some cultures and as good fortune in others; confirm the message is the one you intend. [HIG: color]
- **Put color where it can actually be seen: bold text and larger areas.** Color in lightweight text or tiny elements is harder to make out and to understand — Apple states this for visionOS, where glass backgrounds make it acute, and it holds wherever backgrounds are busy. [HIG: color]
- **Use a background color when it communicates something, not as a flourish, and avoid saturated full-screen color in views that stay on screen for a long time.** Apple's example is Activity, where each view's background matches the ring it reports on. [HIG: color]
- **Keep the palette small and let it defer to the content.** A limited palette coordinated with your logo communicates brand while keeping content the loudest thing on screen. [HIG: color]
- **Expect the person's own accent color to replace yours, and never encode meaning in the accent alone.** On macOS a system accent choice overrides an app's accent everywhere except a fixed-color sidebar icon whose color carries meaning. [HIG: color]
- **When people pick colors in your interface, use the platform's color picker.** It behaves the way people expect and lets them reuse a saved set across apps. [HIG: color]

### Contrast and appearance coverage

- **Keep the contrast ratio between foreground and background no lower than 4.5:1, and aim for 7:1 for custom color pairs — especially small text.** These are the numbers Apple states. System colors help you reach a good ratio rather than guaranteeing one — the lower label levels are defined to have less contrast, and Apple tells you to keep the quaternary level off the thin and ultra-thin materials because its contrast is too low — so measure the pairs you actually ship. [HIG: dark-mode, materials]
- **Ship every color in light, dark and increased-contrast variants, even if the product launches in only one appearance.** System colors define all of these; a custom color needs light and dark plus a genuinely higher-differentiation increased-contrast option for each. [HIG: color]
- **Test the palette under real lighting, on real devices, and across color profiles.** Colors look darker and more muted in bright surroundings and brighter and more saturated in the dark; display white-point features and sRGB-versus-P3 profiles shift them again. [HIG: color]
- **Re-check nearby colors when artwork or translucency sits next to them.** A color that reads correctly on a plain background can be overpowering over an image or on a translucent bar — Maps switches its whole scheme between map and satellite mode for this reason. [HIG: color, materials]
- **Avoid similar colors in control labels over a colorful or media-rich background.** Prefer a monochromatic treatment for toolbars and tab bars there, or an accent with enough visual separation; too much color makes labels hard to read. [HIG: color]
- **Let small translucent bars take a monochrome treatment that follows the content behind them, and make large translucent surfaces more opaque.** Apple's system darkens symbols and labels over light content and lightens them over dark, and keeps sidebars more opaque to preserve legibility over complex backgrounds. [HIG: color]
- **Keep the resting state legible where content scrolls under controls.** Colorful content may pass beneath a toolbar in motion, but the default state — the top of the scroll — must be clearly readable. [HIG: color]
- **Don't overlap similar colors between the content layer and the controls above it.** Contrast at the boundary is what keeps a floating control readable. [HIG: color]

### Brand color restraint

- **Apply the accent color sparingly and deliberately.** Using a brand color broadly overwhelms the interface and dilutes its impact; reserve it for primary actions and status indicators such as unread badges or the selected tab. [HIG: branding]
- **Express brand color in the content layer rather than on the chrome.** Color in content gets picked up by translucent controls above it, which reads as brand without repainting every control. [HIG: branding]
- **Emphasise a primary action by coloring its background, not its label or symbol, and do it to one control at a time.** Coloring several control backgrounds cancels the emphasis it was meant to create. [HIG: color]
- **Reserve color on a translucent control for elements that truly benefit from emphasis** — a primary action or a status indicator — and leave the rest monochrome. [HIG: color]
- **Choose your brand color as the app accent only where the content is largely monochrome.** That is the case where it tailors the experience instead of competing with it. [HIG: color]

### Status color

- **Use one color per status, everywhere, and pair each status with a symbol or a word.** Color makes a status faster to spot; the label or glyph is what makes it legible to someone who cannot separate your green from your red. [HIG: color]
- **Let color carry meaning where the meaning is intrinsic, and keep it consistent with the world people know.** Apple's multicolor symbols do this deliberately: green for a leaf, red for data loss. [HIG: sf-symbols]
- **Never let color be the only marker of a destructive action.** A word, a glyph or a distinct shape has to carry the same warning for someone who cannot separate your red from the rest of the palette. [HIG: color]
- **Add the platform's destructive treatment on top of the color, and wording that names the consequence.** The destructive styling itself, and where the button sits, are owned by the button and alert rules — see `references/actions-menus-and-input.md` and `references/modality-alerts-notifications.md`; this file only says color is not enough. [translation]

Color that encodes data belongs to `references/data-and-charts.md`; color as an accessibility duty to `references/accessibility-inclusion-privacy.md`.

## Light and dark appearances

A dark appearance is a first-class design, not a theme: people choose it system-wide, may have it switch automatically through the day, and expect every product to follow. Flexibility is the principle at stake. [HIG: dark-mode]

- **Follow the system appearance setting rather than shipping your own appearance switch as the primary control.** An app-specific setting makes people configure the same thing twice and reads as a bug when the product ignores their system choice. [HIG: dark-mode]
- **Make the product good in both appearances, and expect it to change while running.** People also choose the automatic setting, which flips light to dark mid-session. [HIG: dark-mode]
- **Treat the dark palette as its own design, not an inversion of the light one.** Backgrounds get dimmer, foreground content gets brighter, and some colors do not invert at all. [HIG: dark-mode]
- **Use adaptive semantic colors, and define both variants of every custom color.** Apple's form is a Color Set asset with bright and dim variants; the generic form is one token per role with a value per appearance. Hard-coded, non-adapting values are the defect. [HIG: dark-mode]
- **Build dark surfaces from the palette's dim greys instead of assuming pure black, and separate layers by brightness.** iOS defines base and elevated background sets: base recedes, elevated — used for sheets, popovers and foreground windows — advances. Prefer the system backgrounds so these depth cues keep working. [HIG: dark-mode]
- **Confirm an elevated surface actually reads as elevated in your palette.** A sheet or popover in a dark appearance must be visibly lighter than the screen behind it, or the layering the platform is trying to show disappears. [HIG: dark-mode]
- **Don't assume every platform carries the same two appearances.** Apple's Dark Mode setting covers iOS, iPadOS, macOS and tvOS and is not supported in visionOS or watchOS; visionOS has no distinct Dark Mode setting because its glass adapts instead to the luminance of the objects and colors behind it. [HIG: dark-mode, materials]
- **Darken images that carry a white background so they don't glow in a dark context.** A white-backed illustration dropped onto a dark screen becomes the brightest thing on it. [HIG: dark-mode]
- **Check every full-color asset in both appearances and supply a second version only where one cannot serve both.** Combine the pair under one name so the platform picks the right one. [HIG: dark-mode]
- **Draw separate light and dark versions of an interface icon when a shape needs different edges.** An icon that needs a thin outline to separate from a light background may need none on a dark one. [HIG: dark-mode]
- **Test dark with increased contrast and reduced transparency on, separately and together.** Raising contrast in a dark appearance can reduce the difference between dark text and a dark background — readable for some people, illegible for many. [HIG: dark-mode]
- **Use the platform's label colors and its standard text views for text.** They handle vibrancy and contrast on unpredictable backgrounds better than text you draw yourself. [HIG: dark-mode]
- **Commit to a permanently dark interface only when the content justifies it.** Immersive media viewing is the case Apple names, where the interface should recede and let people focus on the media. [HIG: dark-mode]

## Depth, layering and materials

Materials are how an interface shows what floats and what is content. Used with restraint they serve Simplicity by separating controls from content; overused they compete with the content they sit on. [HIG: materials]

- **Separate the functional layer from the content layer and give each its own material.** Controls and navigation float above content on the translucent system material; app backgrounds and content-layer surfaces use the standard, more opaque materials. [HIG: materials]
- **Don't put the floating translucent material into the content layer.** It stops distinguishing controls from content and produces a confusing hierarchy — the exception the system itself makes is a transient control like a slider or toggle taking the material on while a person is actually using it. [HIG: materials]
- **Apply translucent, glass-like effects sparingly and only to the most important functional elements.** Standard components take the material automatically; hand-applying it to many custom controls distracts from the content it exists to reveal. [HIG: materials]
- **Create distinction inside the content layer with the standard, graded materials rather than with the floating one.** Apple's iOS set runs ultra-thin, thin, regular and thick; pick a step, not an effect. [HIG: materials]
- **Choose a material by its semantic purpose, never by the color it appears to give you.** System settings change a material's appearance, so a choice made on apparent color breaks under other settings. [HIG: materials]
- **Pick thickness by what has to stay legible:** thicker and more opaque for text and fine detail, thinner and more translucent to keep background context visible. [HIG: materials]
- **Guarantee legibility over rich backgrounds before reaching for the most transparent variant.** Use the blurring variant where text is dense — alerts, sidebars, popovers — and over bright media either dim the backdrop (Apple's figure is a dark layer at 35% opacity) or use controls that bring their own dimming. [HIG: materials]
- **Let foreground text and symbols on a material use the platform's vibrant colors.** They are defined per material, so text does not come out too dark, too saturated or too low in contrast. [HIG: materials]
- **Prefer translucency to large opaque fills where the surroundings matter.** In visionOS an opaque area blocks the view and makes people feel constricted; the same logic applies to any interface layered over live content. [HIG: materials]
- **Keep the default material behind a modal layer.** The contrast a material provides is what tells people a sheet is on top of something rather than a new place; modality itself is in `references/modality-alerts-notifications.md`. [HIG: materials]
- **Respect reduced-transparency and increased-contrast settings instead of designing around them.** Materials change appearance under those settings by design, so check your screens in each. [HIG: materials, dark-mode]

## Icons and symbols

An icon is a metaphor doing work: Familiarity when it reuses a meaning people already hold, Craft when the set is internally consistent, Responsibility when it is labelled for people who cannot see it.

### Designing an icon set

- **Express one concept per icon, in the simplest form people still recognise.** Too much detail makes an interface icon confusing or unreadable; prefer a familiar metaphor directly related to the action it triggers or the content it stands for. [HIG: icons]
- **Keep one size, level of detail, stroke weight and perspective across the whole set** — including where custom icons sit beside system ones — and adjust an individual icon's dimensions when its visual weight makes it look wrong next to the others. [HIG: icons]
- **Reuse the metaphors people already know for common actions instead of inventing new ones.** A trash can means delete; using it for anything else, or restyling the delete icon into something personal, costs people the instant recognition the metaphor exists to give. [WWDC26-250] [HIG: icons]
- **Keep metaphors between too literal and too abstract.** Too literal and people don't recognise what you are depicting; too abstract and the idea never arrives. A good metaphor lets someone predict what the thing will do. [WWDC26-250]
- **Optically centre asymmetric icons, adding the correction as padding in the asset so geometric centring yields optical centring.** The adjustments are tiny and show up everywhere the icon appears. [HIG: icons]
- **Draw interface icons as vectors — PDF or SVG — so the platform scales them.** Raster icons force one asset per display density. [HIG: icons, images]
- **Include text inside an icon only when a character is the clearest way to convey the concept, and then localise it.** For a passage of text, draw an abstract representation and supply a mirrored version for right-to-left contexts. [HIG: icons]
- **Draw people inclusively — prefer gender-neutral figures — and avoid imagery that only reads in one culture or language.** [HIG: icons]
- **Don't depict Apple hardware, and don't reproduce another company's products or protected marks.** Hardware designs change and date your interface; Apple's products are copyrighted, and its symbols representing Apple products cannot be customised at all. [HIG: icons, sf-symbols, app-icons]
- **Supply a selected-state variant only where the platform does not already provide one.** Standard toolbars, tab bars and buttons update the selected appearance themselves. [HIG: icons]
- **Give every custom icon and symbol an alternative text description.** It is invisible on screen and is the only way a screen-reader user learns what the control is. [HIG: icons, sf-symbols]

### Using a symbol system

- **Prefer one symbol library aligned to your type system over hand-drawn one-offs.** Apple's form is SF Symbols, whose weights correspond to the system font's and which align with text at any size; the generic equivalent is a single icon set with a defined weight per text weight. [HIG: sf-symbols]
- **Tune emphasis with the symbol's scale rather than by changing its point size.** Three scales — small, medium, large, defined against the font's cap height — change prominence while keeping weight matched to text of the same size. [HIG: sf-symbols]
- **Choose a rendering treatment deliberately and check it in every context it appears in:** one color across all layers, one color at varying opacities for depth, a small palette across layers, or intrinsic colors where the color itself carries meaning (a green leaf, red for data loss). Size and background contrast decide whether the details still read. [HIG: sf-symbols]
- **Use graduated color across layers to show a changing quantity — capacity, strength, progress — and opacity layering to show depth. Don't swap their jobs.** [HIG: sf-symbols]
- **Pick the design variant that matches the state you are communicating:** outline beside text in toolbars and lists, filled for selection and emphasis, an enclosing shape to survive small sizes, a slash for unavailable. [HIG: sf-symbols]
- **Let the component decide outline or fill where it has an opinion.** A tab bar prefers the filled variant and a toolbar the outline one; overriding that makes your screen the odd one out. [HIG: sf-symbols]
- **Let system-provided colors drive symbols so they adapt to appearance modes and accessibility settings automatically.** [HIG: sf-symbols]
- **Keep gradient rendering for larger symbols.** A gradient drawn from a single source color renders at any size but only reads at a large one; at toolbar size it costs legibility for nothing. [HIG: sf-symbols]
- **Use the script-specific variant of a symbol for the current language, and mirror direction-bearing symbols in right-to-left layouts.** Apple's set carries variants for Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic and several numeral systems, and switches them with the device language. [HIG: sf-symbols]
- **Keep a custom symbol consistent with the set it joins** in level of detail, optical weight, alignment, position and perspective — simple, recognisable, inclusive, and directly related to what it represents. [HIG: sf-symbols, icons]
- **Animate a symbol only when the movement communicates something, and keep the count low.** Purposeless or crowded symbol animation overwhelms an interface; choose animations that match the product's tone, and see `references/motion-feedback-loading.md` for motion rules. [HIG: sf-symbols]
- **Don't put a platform's symbols into your logo, app icon or any trademarked use.** Apple's terms prohibit using its symbols, or images confusingly similar to them, that way. [HIG: sf-symbols]

Buttons, toolbars and menus that host these icons are in `references/actions-menus-and-input.md`.

## App icon

Covered briefly, because an app icon is brand and craft in one asset. Per-platform production specifications are out of scope — see `## Deliberately omitted`.

- **Find one idea that captures what the product is and express it with a minimal number of shapes on a simple background.** Fine detail looks busy under system highlights and shadows and disappears at small sizes. [HIG: app-icons]
- **Keep one visually consistent icon design across every platform you ship on.** It is how people find you, and variants that diverge read as different products. [HIG: app-icons]
- **Design the background to stand out while emphasising the foreground.** A solid color or a gradient usually beats a custom background image, and a full canvas of content is not required. [HIG: app-icons]
- **Vary opacity across foreground layers to build depth, and consider filled, overlapping shapes.** Apple's own Photos icon separates its centrepiece into translucent layers for exactly this. [HIG: app-icons]
- **Include text only when it is essential to the brand.** Text in an icon doesn't localise, doesn't support accessibility, is usually too small to read and repeats the name shown beside it — and never add instructions like "Watch" or "New". [HIG: app-icons]
- **Prefer an illustration to a photo, and never use screenshots or replicas of interface components.** Photographic detail falls apart across appearances, small sizes and layers; very thin lines and sharp corners lose crispness too. [HIG: app-icons]
- **Keep the icon's core features identical across appearance variants** — default, dark, clear, tinted — basing the dark version on the light one with complementary rather than glaring colors. Swapping elements per variant makes the product hard to find. [HIG: app-icons]
- **Hand the platform unmasked, full-bleed layers in vector form, with clearly defined edges, and let it apply masking, highlights and shadows.** Pre-masked edges and baked-in effects fight the system's dynamic ones; keep primary content centred so masking never crops it. [HIG: app-icons]

## Images and artwork

Artwork is a material like type and color: Craft when it is sharp on every display, Flexibility when it survives scaling and both appearances.

- **Specify artwork in density multiples, not in pixels.** A point is an abstraction — on a 2D display it maps to a varying number of pixels, in visionOS it is an angle — so one asset per density, named by its multiple, is what keeps artwork sharp across devices you have not seen. [HIG: images]
- **Ship every bitmap at each display density you support.** Apple's scale factors are @2x for iPadOS and watchOS, @2x and @3x for iOS, @1x and @2x for macOS and tvOS, @2x or higher for visionOS; the generic rule is one asset per pixel density in play. [HIG: images]
- **Design artwork at the lowest resolution and scale up, keeping vector control points on whole values.** Points aligned at 1x stay aligned to the raster grid at 2x and 3x. [HIG: images]
- **Choose the format by content:** de-interlaced PNG for raster work, an 8-bit palette where 24-bit color is not needed, JPEG or HEIC for photos, PDF or SVG for flat icons and anything that must scale. [HIG: images]
- **Prefer vector art for flat 2D imagery wherever display size varies widely.** Bitmaps scaled up by the system stop looking sharp. [HIG: images]
- **Balance resolution against weight and runtime cost when a raster is unavoidable, and filter it well when it scales.** Every step up in resolution costs file size and performance, which shows up as a slow, unfinished-feeling interface. [HIG: images]
- **Composite a fixed background into the asset instead of shipping transparency you never use.** Keep transparency where the platform needs it to apply color — template images and interface icons. [HIG: images]
- **Embed a color profile in every image.** sRGB reproduces accurately on most displays; use Display P3 where richer photos, video or status colors matter, and supply per-color-space variants when two P3 colors or a P3 gradient collapse on an sRGB display. [HIG: images, color]
- **Test artwork on a range of real devices before shipping it.** An image that looks right at design time can arrive pixelated, stretched or visibly compressed. [HIG: images]
- **Keep text out of artwork.** Baked-in text cannot be localised, cannot be read by assistive technology and cannot scale with the reader's text setting — the reasons Apple gives for keeping text out of icons. Set it as text over the image instead. [translation]
- **Preserve the aspect ratio of photographic and illustrative content, and crop rather than stretch to fit a frame.** [translation]
- **Reserve an image's space before it loads and fill it with a neutral placeholder of the same dimensions.** Loading behaviour belongs to `references/motion-feedback-loading.md`; the visual requirement here is that nothing jumps when the image arrives. [translation]

## Brand restraint

Familiarity and Simplicity outrank brand expression in an interface: a stylised product can still be approachable if its behaviours and placements stay standard, and space spent on brand assets is space taken from content. [HIG: branding]

- **Express brand in voice and tone, in the content, and in the details of familiar components — not in extra chrome.** Word choice, punctuation and sentence rhythm carry a brand further than a painted toolbar. [HIG: branding]
- **Build on components people already know, and keep sizing, placement and behaviour familiar when you restyle one.** People then spend their attention on what is actually unique about the product. [HIG: branding]
- **Let branding defer to content.** An element whose only job is to display a brand asset is screen space the content no longer has. [HIG: branding]
- **Don't repeat the logo through the interface.** People rarely need reminding which product they are using, and the space is better spent on information and controls. [HIG: branding]
- **Keep standard placements, standard symbols for common actions, and established navigation and modality conventions however stylised the surface is.** [HIG: branding]
- **Don't use the launch screen as a brand slot.** It disappears too fast to convey anything; if you need a brand moment put it in a welcome or onboarding screen — see `references/writing-help-onboarding-settings.md` and `references/motion-feedback-loading.md`. [HIG: branding]
- **Keep other companies' trademarks out of your product's name and imagery.** Apple's rule for its own marks generalises: don't ship someone else's marks in your name or assets. [HIG: branding]

## Assembling the visual system

Decide these five things before drawing screens; every rule above is easier to hold when the system exists. The ordering and the checks in this section are this skill's own synthesis of the rules above, not Apple guidance.

- **Fix the type scale first, anchored on the platform's default body size, with a named style per level of hierarchy.** Write down the size, weight and leading of each; a level you cannot describe is not a level. [translation]
- **Define color as roles with a value per appearance — text primary, text secondary, surface, surface elevated, separator, accent, destructive, plus status colors — before choosing any hue.** A palette of hues without roles cannot be made to adapt later. [translation]
- **Choose one icon set and record which weight of it pairs with which text weight.** Two icon families on one screen is the most common visible craft failure. [translation]
- **Decide the layering model: which surfaces are content and which float above it, and what separates them** — a material, a border, or a shadow. Then use only that vocabulary. [translation]
- **Write down the asset policy: formats per content type, densities shipped, and what happens in the dark appearance.** Artwork decided per screen is how a product ends up with four kinds of placeholder. [translation]
- **Give the accent color exactly one meaning, and say what it is in one line.** "The accent marks the primary action and unread state" is a testable rule; "the accent is our brand blue" is not. [translation]
- **Specify every interactive token in all the states it will appear in — default, hover, pressed, focused, disabled — and on a colored surface.** A token with one value is a token that will be overridden locally by the first person who needs a state you didn't define. [translation]
- **Record what you deliberately left out of the system and why.** Choosing what to build is largely deciding what not to include, and the same is true of a visual language. [WWDC26-250]
- **Re-check the system against a real screen at the largest text size, in the dark appearance, and with increased contrast, before treating it as settled.** These three settings break more visual systems than any review comment. [translation]

## Translation to web and other platforms

Every bullet in this section is this skill's own translation of the rules above, not Apple guidance.

- **Set type in the platform's own UI stack when the interface should feel native, and load a webfont only where the brand needs it.** A stack like `-apple-system, "Segoe UI", Roboto, sans-serif` resolves to each OS's system face; declare a real fallback for any custom face and keep it metrically close. [translation]
- **Size text in `rem` against the browser's root size and never suppress zoom.** `rem` plus browser zoom is the web's equivalent of a system text-size setting; `user-scalable=no` or `maximum-scale=1` in a viewport meta tag removes it. [translation]
- **Keep web body copy at 16px or more and verify screens at 200% zoom and with a large default font size.** This is the web counterpart of checking the largest accessibility text size. [translation]
- **Hold running text to roughly 45–75 characters per line and give a long measure more line height.** A full-width paragraph on a desktop monitor is the web's version of text that is technically legible and practically unread. [translation]
- **Translate the reference scale into `rem` once, in one place.** Dividing Apple's default point sizes by a 16px root gives a scale that already has hierarchy in it; round the values to taste, but keep the steps. [translation]

| Style | Size (rem) | Line height |
|---|---|---|
| Large Title | 2.125 | 1.2 |
| Title 1 | 1.75 | 1.2 |
| Title 2 | 1.375 | 1.27 |
| Title 3 | 1.25 | 1.25 |
| Headline | 1.0625 (semibold) | 1.3 |
| Body | 1.0625 | 1.3 |
| Callout | 1 | 1.3 |
| Subhead | 0.9375 | 1.33 |
| Footnote | 0.8125 | 1.38 |
| Caption | 0.75 | 1.33 |

- **Define color as semantic custom properties — `--text-secondary`, `--surface-elevated`, `--separator` — with a value per appearance.** Hue-named tokens such as `--blue-500` used directly in components are what makes an appearance change impossible later. [translation]
- **Answer `prefers-color-scheme` rather than forcing one appearance, and set `color-scheme: light dark` so form controls, scrollbars and text selection follow too.** If you offer a switch, default it to the system value and persist only an explicit choice. [translation]
- **Answer `prefers-contrast` and Windows `forced-colors` with the increased-contrast variants of your tokens, and `prefers-reduced-transparency` by swapping blurred glass for an opaque surface.** [translation]
- **Never make a translucent effect the only thing separating two layers.** Give every `backdrop-filter` surface a solid background color underneath, because the filter may be unsupported or switched off. [translation]
- **Verify contrast with a checker against the numbers the corpus states — 4.5:1 minimum, 7:1 for custom pairs, small text especially.** WCAG's AA and AAA thresholds for body text coincide with those two numbers, so one measurement satisfies both. [translation]
- **Check the focus indicator's contrast in both appearances, and style `:focus-visible` rather than removing outlines.** A focus ring is a visual affordance with the same contrast duty as text. [translation]
- **Leave `-webkit-text-size-adjust` at its default (or `100%`) so mobile browsers can still apply the reader's text-size preference.** Setting it to `none` is the mobile web's way of ignoring a text-size setting. [translation]
- **Size inline SVG icons in `em` so they grow with the text beside them.** This is how an icon keeps its weight match when text scales. [translation]
- **Let controls grow with their labels instead of fixing widths to the English string.** Translations are longer, and a clipped label is a legibility failure, not a layout detail. [translation]
- **Serve raster images through `srcset`/`sizes` or `image-set()` for device pixel ratios, and use SVG for flat icons.** These are the web's scale factors. [translation]
- **Give every `<img>` explicit `width` and `height` — or an `aspect-ratio` box — so the layout does not shift when it loads, and `loading="lazy"` for anything below the fold.** [translation]
- **Write `alt` text as the accessibility description, and use an empty `alt` for purely decorative artwork.** This is the web form of an icon's alternative text label. [translation]
- **Swap artwork for the dark appearance with `<picture>` and a `prefers-color-scheme` source, or dim a bright image with a filter.** It implements the corpus rule about softening white backgrounds in a dark context. [translation]
- **Use an openly licensed icon set on the web and apply the same set-level consistency rules** — one concept per icon, one stroke weight per text weight, one family. Apple's symbols ship with its platforms under their own terms; don't re-draw them for a web app. [translation]
- **Let icons inherit text color (`currentColor` on an inline SVG) so they follow every appearance and state automatically.** An icon with a baked-in fill is the thing that stays black in dark mode. [translation]
- **Pair an icon with a visible text label whenever its meaning is not universal, and never ship an icon-only control whose tooltip is the only explanation.** A tooltip does not exist on touch. [translation]
- **In an Electron or Capacitor shell, follow the host platform's appearance and accent settings.** The shell reads the OS light/dark and contrast preferences and the web content inside it must answer the same media queries; platform conventions are in `references/platforms-and-web.md`. [translation]

## Deliberately omitted

- **The full Dynamic Type matrices and tracking tables (typography Specifications).** Eleven styles across seven standard and five accessibility sizes per platform, plus per-point-size tracking — mockup production data with no cross-platform meaning. The default-size scale is kept above; fetch the rest with `python3 scripts/hig.py typography`.
- **macOS dynamic font variants (control content, menu, menu bar, tooltip, palette fonts).** An API list for matching native macOS controls; the rule it serves — match system controls' text — is kept.
- **Named system color and gray palettes with their UIKit, AppKit and SwiftUI API names (color Platform considerations and Specifications).** API inventories, not design rules; the design rule — name colors by role — is kept. Fetch with `python3 scripts/hig.py color`.
- **visionOS-only typography and imagery rules:** 2D versus 3D text, billboarding text toward the wearer, feathered glass behind text over spatial photos, spatial photos and spatial scenes, and brightness balance in fully immersive scenes. No generic equivalent outside a head-mounted display.
- **tvOS layered images and the parallax effect, and tvOS material thickness recommendations.** Focus-driven platform chrome with no counterpart elsewhere; the general depth and layering rules are kept.
- **watchOS autoscaling-PDF scale percentages and tinted graphic complications.** Device-specific asset production.
- **macOS document icons and desktop tinting.** Desktop-only icon and window conventions; window rules live in `references/layout-and-navigation.md`.
- **App icon production specifications and tooling:** per-platform layout sizes, masking shapes and color spaces, the Icon Composer workflow, layer grouping, alternate icons, tvOS safe zones, and the visionOS concave-shape and watchOS black-background notes. Production detail rather than interface design.
- **The SF Symbols animation catalogue** (appear, disappear, bounce, scale, pulse, breathe, wiggle, rotate, replace, Magic Replace, draw on and off) **and custom-symbol production detail** (negative side margins, layer annotation, Z-order, the component library). Library-specific; the design rule — animate with purpose and sparingly — is kept, and motion belongs to `references/motion-feedback-loading.md`.
- **The table of standard SF Symbols names for common actions (icons page).** A lookup table for Apple platforms; the rule it embodies — use the established symbol for a common action — is kept.
- **Apple trademark lists and App Store marketing guidance (branding page).** Legal and store-listing material, outside interface design.
- **Liquid Glass API variants and the vibrancy-style enumerations (materials page).** Framework surface; the design rules about layering, thickness and legibility are kept.

## Sources

Corpus pages, fetched 2026-09-14:

- `typography` — https://developer.apple.com/design/human-interface-guidelines/typography
- `color` — https://developer.apple.com/design/human-interface-guidelines/color
- `dark-mode` — https://developer.apple.com/design/human-interface-guidelines/dark-mode
- `materials` — https://developer.apple.com/design/human-interface-guidelines/materials
- `icons` — https://developer.apple.com/design/human-interface-guidelines/icons
- `sf-symbols` — https://developer.apple.com/design/human-interface-guidelines/sf-symbols
- `images` — https://developer.apple.com/design/human-interface-guidelines/images
- `app-icons` — https://developer.apple.com/design/human-interface-guidelines/app-icons
- `branding` — https://developer.apple.com/design/human-interface-guidelines/branding
- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles

Talk:

- `WWDC26-250` — Principles of great design, WWDC26 session 250 — https://developer.apple.com/videos/play/wwdc2026/250/

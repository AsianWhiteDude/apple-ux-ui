# Showing data: charts, tables, numbers

This file covers the presentation of data: choosing between a chart, a table, a list and a single figure; mark types, axes and scales; titles, labels and units; colour with accessible alternatives; interactive charts that still read statically; tables and lists of values; and gauges for one value inside a range. Load it when a screen shows numbers — a dashboard, a report, a metric card, a data grid, an analytics view, a progress or capacity indicator. It serves **Simplicity** (hierarchy; include just what is necessary; distil complex data into a graphic), **Craft** (precise wording, correct alignment, clear graphics), **Responsibility** (be transparent — the picture must not claim more than the data supports), and **Flexibility** (design for everyone, so the data is reachable by sight, by sound, by keyboard and at any text size). Layout and grouping of the containers live in `references/layout-and-navigation.md`; type and colour systems in `references/typography-color-visuals.md`; loading and empty-state mechanics in `references/motion-feedback-loading.md`.

## Choosing the form of the data

- **Name the question the view answers before choosing a form.** Ask what this data is for and whether the presentation serves that purpose; a chart chosen before the question is decoration with axes. [HIG: design-principles, charting-data]
- **Use a chart when you want to say something *about* a dataset — a trend, a current state, a comparison.** Charts are visually prominent and draw attention, so spend that prominence on what people can actually learn from the data. [HIG: charting-data]
- **Use a scrollable, searchable, sortable list or table when people need the values themselves.** If you are only providing data rather than interpreting it or helping analysis, a table serves better than a chart. [HIG: charting-data, lists-and-tables]
- **Match the form to the data-driven task.** Charts earn their place on three tasks: analysing a trend across historical or predicted values, showing the current state of something that changes over time, and comparing items — or one item at different times — across categories. If the task is none of these, question the chart. [HIG: charting-data]
- **Distil before you draw.** Look for complex data that would be understood faster as a graphic, and for information you can summarise so people can focus on what they care about. [WWDC26-250]
- **Add context rather than strip it when the bare number leaves a decision unmade.** Simple does not mean minimal: sometimes the simpler presentation is the one that also shows elapsed time, the comparison period, or the remaining amount. [WWDC26-250]
- **Use a gauge when the message is one value's position inside a known range.** A gauge maps the current value onto a circular or linear path, and can also describe the range itself with endpoint labels and colour. [HIG: gauges]

## One chart, one message

- **Lead with the takeaway in a title, subtitle or annotation.** Descriptive titles, subtitles and annotations emphasise the important information and can state the actionable conclusion, so people grasp it without reading the marks. [HIG: charting-data, charts]
- **Summarise the chart's main message in text next to it.** A short headline ("light rain expected in the next hour") gives people the essential information at a glance; it does not replace accessibility labels. [HIG: charting-data, charts]
- **Keep the chart simple and let people choose to see more.** Too much data makes a chart overwhelming and hides the very relationships you wanted to show; offer levels of detail or subsets of data instead of packing everything in. [HIG: charting-data]
- **Keep the data the most prominent layer.** Descriptions, axes and grid lines provide context and must not compete visually with the marks. [HIG: charts]
- **Prefer common chart types.** People already know how to read bar and line charts, so a familiar type means they spend their effort on the data, not on the chart. [HIG: charting-data]
- **If the chart is novel, teach it at first encounter.** Introduce an unfamiliar representation on first use — for example by animating its parts in sequence and naming what each one maps to. [HIG: charting-data]
- **Ladder an interactive chart.** To teach richer interaction, offer several versions of the chart, each with more functionality than the last, rather than dropping the fully loaded version on someone first. [HIG: charting-data]
- **Let a chart carry the product's character, but never at the cost of the data's clarity.** The graphical nature of a chart is a real chance to express the personality of the experience and add visual interest; it stops being that the moment the decoration makes a value harder to read. [HIG: charting-data, design-principles]
- **Examine the data at several levels before deciding what to display.** A macro view suggests totals and averages worth showing, a mid-level view suggests useful subsets, and individual points suggest values worth calling out. [HIG: charting-data]
- **Match the chart's size to its functionality, topic and level of detail.** It must be big enough to read the labels and annotations and to support the interaction you offer; a small chart is for a glanceable snapshot or a preview of a larger version. [HIG: charting-data]
- **Use one chart type and style for charts that serve a similar purpose.** A different type or style for each chart implies the charts are unrelated and forces people to relearn; deviate only to mark a meaningful difference. [HIG: charting-data]
- **Keep type, colours, annotations, layout and wording identical across views of the same dataset.** When a small trend chart expands into a detailed one, sameness of style is what tells people it is the same data. [HIG: charting-data]

## Marks, axes and scales

### Marks

- **Choose the mark type from the claim you are making.** Bars compare values across categories or show parts of a whole, and work well over time when each value is a sum; lines show change over time and make the slope of a trend visible; points show how two properties relate and expose outliers and clusters. [HIG: charts]
- **Combine mark types only when the combination adds clarity.** Points on top of a line let people read the overall trend and the individual values at once; anything beyond that is noise. [HIG: charts]
- **Decide deliberately which visual attribute each value maps to.** A scale maps data values — numbers, dates, categories — onto visual characteristics such as position, colour or height; one bar mark can use its height for the magnitude of a value and its position for the moment the value occurred. [HIG: charts]
- **Spend position on the variable the chart is about.** Position is the attribute a reader compares most precisely — the reason a zero baseline works for bars is that people estimate values by comparing heights against it — so map the claim to position and leave colour, size and shape for secondary attributes. [translation]
- **Treat ticks and grid lines as reference points with a job.** Ticks locate important values along an axis, and a grid line extends a tick across the plot area so a mark far from the axis can still be estimated; a line that helps neither should go. [HIG: charts]

### Axes and scales

- **Use a fixed axis range when specific minimum and maximum values are meaningful for all data.** A charge level is read against 0% and 100% whatever today's value is. [HIG: charts]
- **Use a dynamic range when values vary widely and the marks should fill the plot area.** The upper bound then follows the largest value in the visible period. [HIG: charts]
- **Set the lower bound from the mark type and the use.** Bar charts usually want zero, because people compare bar heights to estimate values; a zero baseline can be wrong for a chart whose meaningful differences sit far from zero, such as heart rate. [HIG: charts]
- **Use familiar sequences for tick and grid-line labels.** 0, 5, 10 is read instantly; 1, 6, 11 follows the same rule but costs people a moment of arithmetic. [HIG: charts]
- **Tune grid-line density and weight to the chart's use.** Too many lines drown the data, too few make values impossible to estimate; if people can inspect points by interacting, use fewer lines and lighter labels. [HIG: charts]

### Fitting the plot area to the screen

- **Give the plot area the width in a compact layout.** Keep vertical-axis labels as short as clarity allows, move units into the title, and put a long category label inside the plot area when it obscures nothing. [HIG: charts]
- **Align the chart with the elements around it.** Align its leading edge with the other views on the screen; putting grid-line labels on the trailing side of each line, or the value axis on the trailing side, keeps that edge clean. Anchor any label that looks unattached to a tick. [HIG: charts]

## Labels, units and text

### Titles, units and legends

- **Write titles and labels that explain what the chart is for before anyone studies it.** Information-rich descriptions of purpose and functionality are what people relying on a screen reader, and people with some cognitive disabilities, use to decide whether to explore the chart at all. [HIG: charts]
- **State units where they cannot be missed** — in the title or on the axis, not only in a legend. Describing units outside the plot area also keeps axis labels short. [HIG: charts]
- **Add a legend only for what a mark's position cannot say.** A legend describes chart properties unrelated to a mark's position, such as colour or shape standing for different value categories. [HIG: charts]
- **Label the series directly when there is room.** A label sitting on or beside the series is read where the eye already is; a legend makes the reader travel to a key and back once per series, and that trip is paid again on every glance. [translation]
- **Keep interpretation out of data descriptions.** Words like "rapidly", "gradually" or "almost" report your reading of the data; give the actual values and let people form their own. [HIG: charts]
- **Be transparent about what the view shows and why it is there.** Being clear about what your product does and why is how it earns trust; a data view is part of that, not an exception to it. [HIG: design-principles]
- **State the scope, the source and the as-of time next to the figures.** A view that overstates its certainty, its coverage or its recency spends the trust the figures were shown to build; name which rows, which period and how fresh the data is where the numbers are read, not in a footnote elsewhere. See also Honest numbers below. [translation]
- **Avoid ambiguous formats and abbreviations in data descriptions.** "June 6" beats "6/6", and "60 minutes" or "60 meters" beats "60m". [HIG: charts]

### Text components, legibility and number formats

- **Pick the text component by the job: a label for short read-only text, a text view for long or specially formatted text, a text field when the value must be edited.** A label is uneditable text that names a control, describes a row or introduces a view; a text view scrolls and carries styling. [HIG: labels, text-views]
- **Let a label describe each row.** Within many lists, a label describes the item, often accompanied by a symbol or an image. [HIG: labels]
- **Add that symbol or image only when it carries meaning the label does not.** In a row of data the text is what gets scanned, so an icon that merely restates the label earns nothing and costs width a value could use; a status or type glyph that encodes something new earns its place. [translation]
- **Give long or specially formatted data text its own scrolling region, aligned to the leading edge in the standard text colour.** A text view can be any height and scrolls when content overflows — use it for log output, notes or a description block rather than letting a page grow without bound. Keep creative mixes of fonts, colours and alignments subordinate to readability. [HIG: text-views]
- **Rank text with the platform's label levels rather than ad-hoc greys.** Apple defines four label colours — primary, secondary, tertiary (for unavailable items) and quaternary (watermark); on other platforms use the same small set of named text tokens consistently. [HIG: labels]
- **Make useful data text selectable and copyable.** Error messages, identifiers, addresses and measured values are things people need to paste elsewhere. [HIG: labels, text-views]
- **Keep data text legible at every text size.** Prefer the system font, support the platform's text-scaling setting (Dynamic Type on Apple platforms), and test with accessibility settings such as bold text turned on before calling a dense table done. [HIG: labels, text-views]
- **Never reverse the digits inside a number.** A right-to-left interface mirrors its layout, but the digit order inside one number — an amount, a phone number, a card number — is fixed and must not flip. Which numeral system to show varies by language and region, so lean on system number formatting unless numbers themselves are your subject. [HIG: right-to-left]

## Colour and its alternatives

- **Never let colour alone carry meaning in a chart.** Add a second channel — different shapes, patterns or direct labels — so the chart works for people who do not distinguish the colours you chose. [HIG: charts]
- **Separate contiguous areas of colour.** In a stacked bar, thin separators between marks let people tell one segment from the next. [HIG: charts]
- **Spend colour on clarifying the data first, brand second.** Colour can clarify information, evoke a brand and give visual continuity — in that order of priority. [HIG: charts]

Palette construction, contrast and dark appearance: `references/typography-color-visuals.md`.

## One value in a range: gauges and capacity indicators

- **Reach for a gauge when the message is "where is this value between these two ends".** It maps the current value onto a circular or linear path, so the reading is positional and instant — a battery level, a quota used, a temperature. [HIG: gauges]
- **Pick the style from what people need to see: an indicator marking the current point, or a fill that stops at it.** The standard style shows a movable indicator on the path; the capacity style fills the path up to the value, which reads better as "how much is used or left". [HIG: gauges]
- **Write succinct labels for the current value and both ends of the range.** Not every gauge style displays all three, but a screen reader reads the visible labels, so they are what makes the gauge intelligible without sight. [HIG: gauges]
- **Give the range itself context when the range is the point.** A gauge can name the highest and lowest values it spans, so people know whether today's number is near an edge. [HIG: gauges]
- **Fill the path with a gradient only when the gradient carries meaning.** A temperature gauge running red to blue reinforces hot to cold; a gradient that means nothing is decoration in the place where a value should be read. [HIG: gauges]
- **Change the fill colour at thresholds that matter.** Shift it when the value reaches very low, very high or a defined midpoint, so the state is readable without reading the number; a sequence of colours in one indicator can mark several tiers. [HIG: gauges]
- **Use a continuous fill for large ranges and discrete segments only for small ones.** Once a range is wide, the individual segments of a discrete capacity indicator shrink past the point of being readable; note also that a segment fills completely or not at all, so a discrete indicator always rounds the value. [HIG: gauges]

## Accessibility of data

### Non-visual equivalents

- **Treat the accessibility of every chart as part of building it, not as a later pass.** A chart communicates through graphics, so it needs accessibility labels describing its values and components plus accessibility elements people can interact with. [HIG: charting-data, charts]
- **Give a chart more than one accessibility label.** Unlike an image, a chart usually needs a label per important or interactive element; decide by purpose and mark density whether to label each mark, groups of marks, or the chart as a whole when it is a small preview. [HIG: charts]
- **Write accessibility labels that serve the chart's purpose.** A route-elevation chart exists to convey terrain, so summarised segments are right; a step chart exists to give daily counts, so each bar gets its value. [HIG: charts]
- **Include the context of a value and drop what is already available elsewhere.** A bare number rarely helps: name the date, category or location, then the value, without repeating an axis name the overview already gave. [HIG: charts]
- **Refer to the axes in a consistent order throughout the product.** If descriptions always name the horizontal axis first, people stop spending attention on working out which axis is meant. [HIG: charts]
- **Provide a spoken or textual equivalent of the whole series.** Apple's Audio Graphs turns values into tones plus a high-level summary; without it you must supply the chart type, what each axis represents and the axis bounds yourself. [HIG: charts]
- **Hide visible axis and tick labels from assistive technologies.** Those labels exist for visual estimation; screen-reader users get values and trends from the accessibility labels and the series summary, so exposing both is duplication. [HIG: charts]

### Operating a chart

- **Do not let interaction be the only route to critical information.** Interact-to-reveal is a fine way to offer extra detail, but the static chart must already answer the question it was put there to answer. [HIG: charts]
- **Make chart targets comfortable.** Individual marks are often too small to hit with a finger or pointer, which hurts people with reduced motor control and annoys everyone; expand the hit target to the plot area and let people scrub across it. [HIG: charts]
- **Make an interactive chart operable by keyboard and by switch control along a logical path.** Define a predictable route through the data — along one axis rather than jumping about — and for very large datasets let focus move between subsets instead of every point. [HIG: charts]
- **Signal changes in marks or axes in more than one channel.** People who miss a change misread the chart; animate it, and also announce it for assistive technologies and for people who turned animation off. [HIG: charts]
- **On a small glanceable display, avoid requiring complex chart interaction.** Show what is useful at a glance and keep interaction simple, leaving the detailed, explorable version to the larger screen. [HIG: charts]

More on labels, contrast, motion settings and inclusive language: `references/accessibility-inclusion-privacy.md`.

## Tables and lists of values

### Structure, columns and style

- **Prefer a list or table for rows of text.** The row format makes text easy to scan and read; when items vary widely in size or you are showing many images, use a collection instead (see `references/layout-and-navigation.md`). [HIG: lists-and-tables]
- **Give every column of a multicolumn table a descriptive heading.** Head each column with a noun or a short noun phrase, capitalised in title style, ending in no punctuation; if a single-column table carries no heading, a label or a section header has to supply the context instead. [HIG: lists-and-tables]
- **Keep row text succinct.** Short text limits truncation and wrapping; when each item is long, show titles only and open the content in a detail view rather than growing the rows. [HIG: lists-and-tables]
- **Keep clipped text recognisable.** In a narrow or resizable table, truncating in the middle can preserve both the beginning and the end of a value, which is what people use to tell rows apart. [HIG: lists-and-tables]
- **Choose a list or table style that matches the data.** A grouped style uses headers, footers and extra space to separate groups of data, and platforms define styles for specific jobs; pick one and apply it consistently rather than styling each table by hand. [HIG: lists-and-tables]
- **Choose a row style that fits what a row must show** — for example a small leading image followed by a brief label — and use the same row style throughout a table. [HIG: lists-and-tables]
- **Keep "more about this" separate from "go deeper".** An info button reveals more information about the row's own content and does not navigate; drilling into a row's subviews needs a disclosure indicator, and swapping the two misleads people about where a tap will take them. [HIG: lists-and-tables]

### Sorting, resizing, selecting and editing

- **Let people sort by the column heading where sorting has value, and reverse the order on a second activation.** This is the expected behaviour of a pointer-driven multicolumn table. [HIG: lists-and-tables]
- **Let people resize columns when the data varies in width.** Resizing is how people concentrate on one area or reveal clipped values. [HIG: lists-and-tables]
- **Use alternating row backgrounds in a wide multicolumn table.** They keep the eye on one row while it crosses many columns. [HIG: lists-and-tables]
- **Use an outline with disclosure controls, not a flat table, for hierarchical data.** Nested levels need a way to expand and collapse; see `references/layout-and-navigation.md`. [HIG: lists-and-tables]
- **Match selection feedback to what selection does.** A table used for navigation keeps the selected row highlighted to show the path taken; a table of options highlights briefly and then marks the chosen item, for example with a checkmark. [HIG: lists-and-tables]
- **Let people reorder rows even when they cannot add or remove them.** Reordering is valued on its own, and on touch platforms it may sit behind an explicit edit mode. [HIG: lists-and-tables]
- **Limit rows on a very small display, but do not hide the fact that more exist.** Show the most relevant items with a way to see the rest; a truncated list with no "more" reads as a bug. [HIG: lists-and-tables]
- **Do not stack two interactive things on the same edge of a row.** An alphabetical index down the trailing side fights with trailing-side row controls such as disclosure indicators, and people hit the wrong one. [HIG: lists-and-tables]

## Deliberately omitted

- **watchOS elliptical list style and vertical page-based navigation between detail views** [lists-and-tables] — a device-specific scrolling and paging model with no generic equivalent.
- **tvOS row focus growth and corner rounding, and the image preparation it forces** [lists-and-tables] — belongs to the tvOS focus model; see `references/platforms-and-web.md`.
- **watchOS date and timer text components, and complications** [labels] — platform components that update themselves; no generic counterpart.
- **macOS level-indicator rating and relevance styles** [gauges] — rating display is covered in `references/motion-feedback-loading.md`; the relevance style is noted by Apple as rarely used.
- **The accessory gauge style for Lock Screen widgets** [gauges] — an Apple widget surface, not an interface pattern to translate.
- **Swift Charts, Audio Graphs and accessibility-notification APIs, and the developer notes on SwiftUI/UIKit/AppKit text components** [charts, charting-data, labels, text-views] — implementation detail; the design rules they support are stated above.
- **Keyboard type for an editable text view, and the tvOS note that editable text uses a text field** [text-views] — input rules live in `references/forms-and-data-entry.md`.

## Translation to web and other platforms

These are this skill's translations, not Apple guidance. All `[translation]`.

### Honest numbers

- **Right-align numeric columns and align them on the decimal separator; set them in tabular (lining) figures.** Proportional digits make columns ragged and defeat the vertical comparison a table exists for — `font-variant-numeric: tabular-nums` on the column. [translation]
- **Put the unit in the column heading, not in every cell.** "Revenue, €" once at the top is scannable; a currency symbol on 400 rows is noise. [translation]
- **Make sort, filter and time-range state visible and addressable.** Show which column sorts and in which direction, name the active filters, and put the state in the URL so a view can be shared and reloaded. [translation]
- **Say what a total covers.** A totals row that sums only the visible page, only unfiltered rows, or only complete periods must say so, or people will read it as the whole. [translation]
- **Mark incomplete and projected data.** A partial current period, an estimate or a forecast needs a visible distinction (dashed mark, lighter fill, a labelled annotation) so the chart does not report a drop that is only the day being young. [translation]
- **Declare a truncated, clipped or non-linear scale.** If the value axis does not start at zero, or is logarithmic, or clips outliers, label it; a bar chart on a truncated axis exaggerates every difference. [translation]
- **Do not mix two scales on one axis, and keep a second axis out unless both series are labelled and colour-tied to their axis.** Dual axes let any two series be made to correlate. [translation]
- **Format numbers and dates through the platform's locale API** (`Intl.NumberFormat`, `Intl.DateTimeFormat`), and spell out ambiguous dates in headings and tooltips. [translation]
- **Round consistently and say the precision.** Mixing one decimal place in the chart with three in the tooltip and none in the total makes the same figure look like three figures; pick the precision the decision needs and hold it across the view. [translation]
- **Do not let a percentage float without its base.** "+180%" on twelve events is a different fact from "+180%" on twelve thousand; show n beside the rate. [translation]

### Semantics and accessibility on the web

- **Use real table semantics for tabular data**: `<table>` with `<caption>`, `<th scope="col|row">`, and no layout tables. For a virtualised grid, keep the announced row and column counts and positions correct (`aria-rowcount`, `aria-rowindex`). [translation]
- **Give a static SVG or Canvas chart an accessible name and description** (`role="img"` plus `aria-labelledby`/`aria-describedby`), and pair a Canvas chart with a data table or text summary, since its pixels expose nothing. [translation]
- **Make interactive data points real focus stops.** Keyboard users need to move along the series with arrow keys, read each value, and leave the chart with Tab; hover-only tooltips are unreachable. [translation]
- **Offer the underlying rows.** A table view, a copyable block or a CSV export is the most reliable alternative representation of any chart, and the cheapest to maintain. [translation]
- **Never ship a chart as a bare bitmap.** An image of a chart has no values, no text scaling and no dark appearance; if an image is unavoidable, put the figures in the caption. [translation]

### Adaptivity and state

- **Respect `prefers-reduced-motion` for chart transitions and `prefers-color-scheme` for chart palettes.** Re-derive mark, grid and label colours per appearance instead of reusing light-mode hexes; see `references/typography-color-visuals.md`. [translation]
- **Give tables and charts explicit empty, loading and error states.** An empty axis frame or a zero-row grid with no message reads as breakage; see `references/motion-feedback-loading.md`. [translation]
- **Keep dense tables usable at narrow widths.** Choose one strategy — horizontal scroll with a frozen key column, or a per-row stacked card — and keep the column order the same as the wide layout. [translation]
- **Keep the plot area wider than its labels as the viewport shrinks.** Below the width where axis labels and annotations stay readable, drop to a sparkline plus the current figure rather than shipping an unreadable miniature of the full chart. [translation]
- **Hold a chart's height while its data loads.** A chart that appears at zero height and then expands shifts the page under a reader's cursor; reserve the box from the first paint. [translation]

## Sources

- `charting-data` — https://developer.apple.com/design/human-interface-guidelines/charting-data
- `charts` — https://developer.apple.com/design/human-interface-guidelines/charts
- `lists-and-tables` — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
- `labels` — https://developer.apple.com/design/human-interface-guidelines/labels
- `gauges` — https://developer.apple.com/design/human-interface-guidelines/gauges
- `text-views` — https://developer.apple.com/design/human-interface-guidelines/text-views
- `right-to-left` — https://developer.apple.com/design/human-interface-guidelines/right-to-left
- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- WWDC26 session 250, «Principles of great design» — https://developer.apple.com/videos/play/wwdc2026/250/

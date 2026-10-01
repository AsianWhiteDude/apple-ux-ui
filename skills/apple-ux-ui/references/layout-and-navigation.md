# Layout and navigation

This file covers the structure of an interface: visual hierarchy and grouping, margins and safe
areas, adaptivity across sizes and orientations, navigation structures (tab bars, sidebars, split
views, hierarchical and page-based browsing), the organisation components that hold content (lists,
tables, collections, boxes, disclosures, outlines), search, windows and full-screen modes, and
scrolling. Load it when you are laying out a screen, choosing or changing a navigation structure,
deciding which container a set of content belongs in, or adding search. The rules here are
instances of four of the eight principles: **Simplicity** — hierarchy, and including just what is
necessary, so the most important thing is the most obvious one; **Familiarity** — consistent
structure and placement, so people can predict where things are; **Flexibility** — one layout that
adapts to sizes, input methods and text sizes while preserving a person's context; and **Agency** —
freedom to move around, nothing locked into a single flow, and the interface staying out of the way
of the task. Where a rule expresses Craft or Responsibility instead, the tag says which page it
comes from and the rule says why.

## Layout fundamentals

### Hierarchy

- **Order content by relative importance, and put the most important items at the top and leading edge.** People read a layout in reading order — top to bottom, leading to trailing — so that is where attention lands first. Prefer standard components that flip this order automatically for right-to-left languages (see `references/accessibility-inclusion-privacy.md`).
- **Build hierarchy out of order, spacing and contrast, and check that the single most important item on the screen is the most obvious one.** If everything is equally prominent, there is no hierarchy; if the primary action is not what the eye reaches first, the layout has failed.
- **Make the layout answer three questions without explanation: what do I pay attention to, what can I interact with, and how do I interact with it.** Use these as the acceptance test for a screen's clarity.
- **Prefer standard system components wherever position and order matter.** They adapt their arrangement to the language's reading direction and to the space available on their own; a hand-built equivalent has to be redone for every locale and every window size.
[HIG: layout] [WWDC26-250]

- **Align elements to a common edge, and use indentation only to express subordination.** Aligned items read as related and are easier to track while scrolling; an indented item reads as belonging to the item above it, so never indent for decoration.
- **Group related items with negative space, a container shape or a separator line.** Grouping is how a layout shows which items belong together and which do not; use one device per level of grouping rather than stacking borders inside borders, which makes a view feel busy and constrained.
- **Use progressive disclosure to keep the initial view small: show the controls people use most, and put advanced or rare functionality behind a disclosure, a menu or a nested view.** Too much content and too many choices at once makes both finding information and understanding the available choices harder.
- **Reduce the number of steps between opening a view and finishing the task it exists for.** Concision is about a person's time as much as their reading: fewer steps, no redundant confirmations, no detour through a screen that only forwards people onward.
- **Turn that into a measurement: count the steps in the main flow of a view and look for one to remove.** A count is something a review can repeat and compare against the previous version; "fewer steps" on its own is not. The counting test is this skill's way of checking the rule above, not a rule Apple states. [translation]
- **Offer extra content in a scrollable section rather than another screen when the content is browsable.** A shelf of further items keeps the additional material one gesture away instead of one navigation step away, which suits media-heavy views.
- **Simplifying sometimes means adding, not removing.** A pause control plus elapsed and remaining time is simpler in use than a pause control alone, because it answers the question people actually have. Distil information to its essence rather than hiding it; every element must earn its place.
[HIG: layout, disclosure-controls, boxes] [WWDC26-250]

### Separating controls from content

- **Keep controls and navigation on a visually distinct layer above the content they act on.** A distinct layer for controls is what lets people tell chrome from content at a glance; on Apple platforms this is the Liquid Glass layer, and generically it is any consistent treatment reserved for controls only.
- **Do not use the control treatment inside the content layer.** Reusing the controls' material for content produces a confusing hierarchy where nothing reads as interactive; use ordinary background materials for content surfaces instead.
- **Apply any depth or blur effect sparingly and only to the most important functional elements.** These effects exist to draw attention to the content beneath them; on many custom controls at once they distract from it.
- **Choose a background material by what it means, not by the colour it happens to produce.** System settings change a material's appearance, so a choice made on apparent colour breaks in other contexts. Thicker, more opaque materials give better contrast for text and fine detail; thinner, more translucent ones keep a person's context visible.
- **When a full-bleed background image sits under chrome, extend it rather than crop its subject.** Mirroring and blurring the adjacent edge of the image beneath a sidebar or bar keeps the important part of the picture visible while the background still reaches the window edge.
- **Guarantee contrast for text and symbols placed over a translucent material.** Apple's system “vibrant” colours exist for this: they stay legible whatever shows through.
- **If you pick colours yourself, check them over the brightest and darkest content that can pass beneath.** The corpus states only that system vibrant colours remove the worry about a colour reading too dark, bright, saturated or low-contrast; this verification test is the skill's own. [translation]
- **Let content extend under floating bars instead of stopping at them, and separate the two with a scroll edge effect rather than an opaque band.** Use one such effect per scrolling view, and keep the effect the same height across the panes of a split layout so the tops align.
[HIG: layout, materials, scroll-views, sidebars]

### Margins, safe areas and edges

- **Respect the platform's margins, layout guides and safe areas instead of hard-coding insets.** The safe area is the part of a window that no hardware feature (camera cutout, rounded corner, home indicator) and no system bar covers; content placed outside it is clipped or unreachable, not merely tight.
- **Constrain the width of running text for readability rather than letting it span the full window.** Most platforms provide a readable-width guide for exactly this.
- **Never put critical information or critical actions at the bottom edge of a window.** People routinely drag a window so its bottom edge falls off the screen; the same applies to the bottom of a sidebar.
- **Do not place content behind a hardware cutout at the top edge, even when the pixels exist.** Text and controls there are partly invisible.
- **When the interface is viewed from a distance, inset primary content well inside the display edge.** Apple's TV guidance is 60 points from the top and bottom and 80 points from the sides, which protects content from overscan cropping and compatibility settings; on any far-viewed display, budget a similar margin.
- **Space the items of a grid consistently.** Inconsistent gaps stop a grid reading as a grid, and an irregular rhythm is much harder to scan.
- **Keep partially visible content symmetrical at both edges of a row.** Equal slivers on the left and right direct attention to the fully visible items; an uneven peek looks like a scrolling bug.
- **Leave enough space around focusable or hoverable items that the focus effect cannot overlap neighbouring content.** Focus and hover treatments grow an element, so items packed edge-to-edge collide when one is highlighted.
[HIG: layout, windows, sidebars, lockups, collections]

### Adaptivity

- **Decide the layout from the space actually available, not from the device type or the orientation.** Orientation and device idiom tell you nothing about how much room you have — a resized window, a mirrored display or a side-by-side app can be any shape. Apple expresses available space as horizontal and vertical *size classes*, each compact or regular; treat that as the shape of the decision, whatever your framework calls it.
- **Keep functionality identical as the available space changes; vary only how much of it is visible at once.** Removing a feature because the window got narrower makes the product feel broken. Use extra space to surface what was in an overflow menu, or to promote a tab bar into a sidebar; use less space to collapse in the other direction.
- **Keep the layout recognisable as the same product at every size.** A resized window is still the same app to the person using it, so the arrangement should change degree, not identity.
- **Preserve context across every size change: keep content and controls in consistent, predictable positions and use natural animation to carry people through the transition.** Rotating a device, resizing a window, adding a display or moving to another device should not make people re-find anything.
- **Be ready for larger text: let horizontally adjacent views stack vertically, and let rows grow in height rather than clip or overlap.** Text scaling is a system setting people depend on; a layout that ignores it becomes unusable rather than merely ugly. Type details are in `references/typography-color-visuals.md`.
- **Test the extremes first — the smallest and largest layouts, the longest localisation, the largest text size — then fill in between.** Most adaptivity defects show up only at an end of the range.
- **Scale background artwork to fill instead of changing its aspect ratio, and prepare art for windows far wider or taller than a standard screen.** Letterboxing and pillarboxing read as broken; distortion reads as careless.
- **Support resizing, and set minimum and maximum sizes only to stop elements overlapping or a layout becoming unwieldy — never as a way to forbid resizing.** A window that refuses to resize fights the way people arrange their workspace.
- **Let a shrinking window collapse a secondary pane, and restore the pane when the window grows again.** Making a window narrow is a request for more room for content, so folding the sidebar away at that point is usually the answer people wanted.
- **Do not rearrange a layout under someone's hands.** Change a grid or list layout in response to an explicit action, not while a person is reading or interacting with it; a layout that jumps costs people their place. A layout that breaks on rotation is one of the clearest signals of rushed work.
[HIG: layout, windows, sidebars, collections] [HIG: design-principles] [WWDC26-250]

## Navigation structures

### Choosing a structure

- **Use a flat, mutually exclusive set of top-level sections when the product has a handful of peer areas, and give each section its own persistent state.** This is what a tab bar is for: switching between top-level sections while each one remembers where the person was inside it.
- **Use a side-by-side structure when people need two or three levels of the hierarchy visible at once.** A split view shows a list and the selected item's detail together, so selecting in one pane updates the next; prefer it over pushing and popping when people compare or move between items frequently.
- **Use a drilling structure for a deep hierarchy people traverse repeatedly: columns for browsing level by level, an outline for revealing nested levels in place.** Columns suit deep hierarchies with frequent back-and-forth between levels and no need for sorting; an outline suits hierarchical data shown as rows with expandable parents. Keep the hierarchy in the first column only.
- **Prefer the compact navigation control first when space is tight, and a sidebar only when there is room for it.** A sidebar needs a lot of horizontal and vertical space; on a narrow screen the same destinations belong in a tab bar. Where the platform offers an adaptable control that presents as a tab bar in a small window and a sidebar in a large one, adopt it instead of choosing once.
- **Use a temporary presentation, not a new pane or window, for a short task someone must finish before going back.** A pane is for information people keep referring to; a brief, self-contained task belongs in a sheet or dialog — see `references/modality-alerts-notifications.md`.
- **Prefer an adjacent pane over a new window for supplementary information.** A pane keeps people in the context they were in; a new window makes them manage and re-find a second place.
[HIG: tab-bars, split-views, column-views, outline-views, sidebars]

### Making a structure behave

- **Use the navigation control for navigation only; put commands that act on the current view in a toolbar.** Mixing actions into a navigation control breaks the promise that everything in it takes you somewhere. Toolbar and button rules are in `references/actions-menus-and-input.md`.
- **Keep the navigation control visible as people move through a section.** Hiding it costs people their sense of where they are. The one accepted exception is a modal presentation, which is temporary and self-contained — see `references/modality-alerts-notifications.md`.
- **Keep the number of top-level destinations small enough to fit without an overflow list.** Weigh each additional destination against how often people need it; when destinations spill into a "More" list, the ones inside become hard to notice and reach.
- **Never disable or hide a top-level destination because its content is currently empty.** A navigation control whose items come and go feels unstable; keep the destination and explain inside it why there is nothing there yet.
- **Label every destination, and keep labels to a single word where the word is unambiguous.** An icon alone is a guess; the label is what lets people predict the section before they go there. Use a noun or short noun phrase for a pane or section label.
- **Pair each destination with a familiar symbol, and prefer a scalable symbol set over a bitmap.** Symbols from the platform's own set stay aligned with text at every weight and size and adapt to compact and regular presentations; a custom bitmap does neither. Icon rules are in `references/typography-color-visuals.md`.
- **Badge a destination only for information that genuinely needs attention now.** Badges lose all meaning once they mark routine updates. Notification and badge rules are in `references/modality-alerts-notifications.md`.
- **Let people customise which destinations appear and in what order, and let them hide ones they never use.** No single arrangement fits everyone; personalising the set is often the only honest answer to that. Keep the default set small — around five — so the arrangement survives the move between a small and a large window.
[HIG: tab-bars, sidebars, tab-views] [WWDC26-250]

### Panes, sidebars and orientation

- **Show at most two levels of hierarchy in a sidebar; if the data is deeper, put a content list between the sidebar and the detail.** Deeper nesting in a sidebar hides the very structure the sidebar exists to reveal.
- **Title each group in a two-level sidebar with a short descriptive label, and drop every word that is not doing work.** Long group titles wrap and push the destinations themselves out of view.
- **Group a long sidebar with disclosure controls so its vertical extent stays manageable.** Collapsing groups is what keeps a large set of destinations scannable.
- **Persistently highlight the current selection in every pane that leads to the detail view.** The chain of highlights is how people see the path they are on; a selection that only flashes leaves them guessing which item the detail belongs to.
- **Let people hide a pane or sidebar with the interaction their platform already uses, and give more than one way to bring it back — a control and a command with a keyboard shortcut.** Hiding panes is how people reduce distraction or make room for editing.
- **Never hide the sidebar by default.** A navigation structure people have to discover is a navigation structure most people never find.
- **Set minimum and maximum pane sizes so the divider stays visible and grabbable, and prefer a thin divider.** A divider that collapses to nothing cannot be dragged; a thick one costs content space for no gain.
- **Make sure it is still possible to move between panes logically at narrow widths.** A side-by-side structure that becomes unusable when the window shrinks is worse than one that collapses to a single pane.
- **Title the whole structure once rather than labelling each pane.** People already know how a two-pane layout works; per-pane titles restate the obvious and crowd the content.
- **Choose pane proportions that keep both panes usable and looking deliberate.** A common default gives a third of the width to the list and two-thirds to the detail; an even split is also reasonable. What matters is that neither pane is too narrow for its content.
- **Keep each pane of a tabbed area self-contained: controls inside a pane must affect only that pane.** Panes are mutually exclusive, so a control whose effects reach outside its pane breaks the model.
- **Keep a tabbed area to six panes or fewer, and inset it from the window edges.** Beyond six, tabs crowd and the layout suffers; the inset margin leaves room for controls that belong to the window rather than to one pane. A drop-down list of panes is the fallback when there are too many, at the cost of an extra click and of hiding the choices.
- **Let people drag content between panes.** Two levels of the hierarchy on screen at once is exactly the situation in which dragging is the shortest path; see `references/actions-menus-and-input.md`.
[HIG: sidebars, split-views, tab-views]

### Freedom to move, and coming back

- **Never lock a person into a flow or a mode.** Let them reach features in the order they choose; when a guided sequence is genuinely necessary, make skipping or escaping it obvious and cheap. An interface should never stand in the way of what someone is trying to do.
- **Give every screen a person can enter a visible way back to where they came from.** This is the minimum form of the freedom above: no dead ends, no screens that can only be left by quitting.
- **Put the same action in the same place on every screen, and keep identical-looking elements behaving identically.** Consistent placement is what lets people act without thinking — on a Mac, a window's close control is always in the same corner. Things that look the same must behave the same.
- **Show people where they are in a hierarchy when the location matters, and keep that indicator in the body of the window rather than in the window frame.** A path or breadcrumb control belongs next to the content it describes, not in a toolbar or status bar.
- **Remember expansion and navigation state between visits.** If someone expanded four levels of an outline to reach an item, restore that state instead of making them navigate back to the same place.
- **Assume people will switch away mid-task, and be ready to save and restore context at any moment.** Multitasking is the normal condition, not an edge case; when people come back, let them continue as if they had never left.
- **Pause anything that needs attention or participation when a person switches away, and finish work they already started in the background.** A video or a game should not run on unseen; a download or an export they asked for should complete.
- **Tell people a background task finished only when it was important or time-sensitive.** Routine completions can wait until they come back on their own; see `references/modality-alerts-notifications.md`.
[HIG: design-principles, path-controls, outline-views, multitasking] [WWDC26-250]

## Organisation components

### Choosing a container

- **Put text in a list or a table; put image-led content, or items that vary widely in size, in a collection.** Rows are what make text easy to scan and read; a grid is what makes images comparable. It is generally simpler to read textual information as a scrollable list than as a grid.
- **Use the standard row and grid layouts rather than a custom arrangement.** People expect these two; a custom layout that draws attention to itself competes with the content in it.
- **Use a box to set off one small group of related information, and keep it small relative to its container.** As a box approaches the size of the window it stops communicating separation and starts crowding everything else.
- **Do not nest boxes; express sub-grouping with padding and alignment instead.** A box border is a strong visual element, and borders inside borders make an interface feel busy and constrained.
- **Give a box a title only when the grouping needs explaining, and keep it to a short sentence-case phrase with no trailing punctuation.** The title is also what a screen reader uses to announce the group.
- **Use a table for non-hierarchical data and an outline for hierarchical data.** An outline looks like a table but adds the expand-and-collapse affordance that hierarchy needs; a table that fakes hierarchy with indentation alone cannot be collapsed.
[HIG: lists-and-tables, collections, boxes, outline-views]

### Rows, columns and disclosure

- **Keep row text short enough to read comfortably, and prefer an ellipsis in the middle of a string over clipping the end.** A middle ellipsis preserves both the beginning and the end, which is usually what makes an item recognisable.
- **When items carry a lot of text, list their titles only and reveal the rest in a detail view.** Over-large rows destroy the scannability that is the whole reason to use rows.
- **Head every column in a multi-column table or outline with a descriptive noun phrase in title case and no trailing punctuation.** Without a heading, the meaning of a column is a guess.
- **If a single-column view has no heading, give it context some other way — a label above it or a section header.** People need to know what the list is before they read it.
- **Let people sort by clicking a column heading where sorting has value, and reverse the direction when they click the already-sorted column again.** This is the behaviour people try first, so anything else reads as broken.
- **Sort a hierarchy within each level rather than flattening it.** Sorting the top level and then the children of each node keeps the structure people were navigating.
- **Let people resize columns.** Data varies in width; a fixed column that clips content gives people no way out.
- **Alternate row backgrounds in a wide multi-column table or outline.** It is what keeps the eye on one row while reading across columns; in a short or single-column list it is noise.
- **Expose hierarchy in the first column only.** Other columns carry attributes of the row; a second column that also branches makes the structure unreadable.
- **Label a disclosure with what it reveals, such as “Advanced Options”.** An unlabelled triangle asks people to open it to find out whether they needed it.
- **Place a disclosure control next to the content it expands.** The relationship between the control and what appears must be obvious the moment it opens.
- **Use at most one expanding disclosure button in a single view.** Several of them in one view multiply the number of states the view can be in, and people lose track of which part is hidden.
- **Make expanding and collapsing easy and cheap, including an expand-all path for nested containers.** People navigating an unfamiliar tree open and close a lot of nodes.
- **In an editable cell, let a single click start editing, and reserve a double click for a different action such as opening the item.** People try single-click editing first; giving the two gestures the same result wastes one of them, and swapping them surprises everyone.
- **Distinguish an affordance that reveals more information from one that navigates deeper.** An info affordance shows detail about the row in place; a navigation affordance drills in. Using one to mean the other strands people.
- **Do not stack two competing affordances on the same edge of a row.** For example, a trailing-edge index and trailing-edge row controls make each other hard to hit.
[HIG: lists-and-tables, outline-views, column-views, disclosure-controls]

### Behaviour inside a container

- **Match selection feedback to what selection does.** A row that navigates keeps a persistent highlight to show the path; a row that sets an option highlights briefly and then shows a durable mark such as a checkmark. Data-presentation rules for lists and tables — density, number alignment, totals — are in `references/data-and-charts.md`.
- **Make items easy to reach and choose.** If getting to an item takes too much work, people lose interest before they reach the content they came for — pad items enough that hover and focus effects are visible and targets are comfortable.
- **Put structural editing behind an explicit mode on touch platforms.** Selecting, deleting and reordering rows by accident is expensive; an edit mode people enter deliberately is what prevents it, and `references/forms-and-data-entry.md` covers recovery when it happens anyway.
- **Let people reorder a list even when they cannot add to or remove from it.** Reordering is often the whole value of the list, and people expect it.
- **Animate insertions, deletions and reordering.** The animation is what tells people which item moved where; without it the list simply differs from the one they were looking at.
- **Keep item sizes consistent within a row or group.** A row of cards with matching widths and heights reads as one set; mismatched sizes read as an error.
- **Show information about the selected item when a drilling structure has nothing further to show.** At the leaf of a hierarchy, a preview and the item's key attributes are more useful than an empty pane.
- **Start from the root of the hierarchy in the first column.** People rely on being able to scroll back to the start and begin again.
- **Offer a search field in a long list or outline.** Past a screenful or two, filtering beats scrolling.
- **Choose the list or table style that suits the data and the platform, and the row style that suits the content.** Grouped styles with headers and footers separate sets of data; alternating backgrounds help wide tables; a compact row with a leading image and a short label suits a browsable list. Choose from the styles the platform provides instead of inventing a row shape, because several of them exist to communicate grouping and hierarchy.
- **In a very long list, lead with the most relevant items and give people a way to see all of them.** Truncating silently makes people think data is missing; “show all” keeps both the short list and the complete one.
- **Rely on the platform's default interactions before adding your own.** Tap or click to select, press and hold to edit, swipe to scroll are already known; add a custom gesture only when the product needs it, and never as the only way to reach something — see `references/actions-menus-and-input.md`.
[HIG: lists-and-tables, collections, lockups, column-views, outline-views]

## Search

### Where search lives

- **Give search a primary, always-reachable position when finding things is a main job of the product.** A search that has to be hunted for is a search people stop using.
- **Aim for one clearly identified place that searches everything, and add local search only where it obviously filters the view it sits in.** Two searches with unclear scopes is worse than one broad search.
- **Choose the placement from the relationship you need to show.** A dedicated search section or tab suits discovery, because it gives room for suggestions and categories; search in a toolbar suits filtering results shown in an adjacent pane; an inline field suits filtering exactly the list it sits above.
- **Decide whether search is a destination or a detour, and build it accordingly.** A destination opens a landing view with suggestions and categories, which suits browsing-heavy products; a detour focuses the field immediately and returns people to exactly where they were, which suits products where search resolves in seconds.
- **Put an inline field directly above the content it searches, and pin it while that content scrolls.** Adjacency is what tells people the search applies here and not globally.
- **Place the field where the hand or pointer already is, and not over content people need while searching.** On a touch device that usually means the lower edge if there is room; move it to the top when covering the bottom of the screen would obscure a primary function.
- **Keep search in the same conceptual place on every platform you ship.** Someone who uses the product on two devices should not have to relearn where search lives; match the placement as closely as each platform's conventions allow.
- **Keep the field's placement working as the window resizes.** In a compact layout, move search above the content list rather than leaving it attached to a pane that no longer exists.
- **In a dedicated search area, focus the field on arrival — unless focusing it raises an on-screen keyboard that would cover the view.** Saving a tap is good; hiding the results is not.
[HIG: searching, search-fields]

### How search behaves

- **Start searching as the person types and refine results with each character.** Continuous refinement is what makes search feel responsive; a search that only runs on Return feels like a form submission.
- **Offer suggestions: recent searches before typing starts, predicted terms and completions while typing.** Suggestions let people type less and find more, even when results themselves are not live.
- **Use placeholder text to say what can be searched.** It is the cheapest way to set scope expectations and teach people what the index covers.
- **Show the current scope at all times.** A descriptive placeholder, a scope control or a title must make it unmistakable which collection is being searched.
- **Default to the broader scope and let people narrow it.** The broad result set is the context that makes narrowing an informed choice.
- **Offer scope controls and term tokens to narrow a search, and pair tokens with suggestions so people discover them.** A token is a search term turned into a single selectable, editable object; people cannot use tokens they never learn exist.
- **Offer more than one way to turn typed text into a token.** A delimiter such as a comma is the usual default; Return is a common addition, and people will try both.
- **Tune the delay before suggestions appear.** Suggestions that appear instantly can distract from typing; ones that appear too late arrive after the person has typed the whole term.
- **Give a token a context menu with the information and edits that fit it.** The token stands for something real — a person, a file type, a date — so the actions on it belong on it.
- **Put the most relevant results first and categorise them when there are many.** Having to scroll past irrelevant matches to reach the obvious answer is what makes a search feel broken.
- **Let people filter results after the fact.** Refining beats retyping.
- **Treat search history as private: assume someone else may see the screen, and always provide a way to clear it.** See `references/accessibility-inclusion-privacy.md`.
- **Offer a way to find content inside the open document or page, not only across the collection.** Searching a library and searching the thing you already have open are different needs, and people expect both.
- **Make content findable from outside the product too.** Index content in the system's search (Spotlight on Apple platforms) with descriptive metadata, so people can reach it without opening the app first.
[HIG: search-fields, searching, token-fields]

## Windows and full screen

- **Let every window adapt fluidly to any size.** Multiple windows, side-by-side arrangements and free resizing are the normal way people work; a fixed-size window cannot take part.
- **Distinguish a primary window from an auxiliary one.** A primary window holds the main navigation and content; an auxiliary window is dedicated to one task, offers no navigation elsewhere, and closes when the task is done.
- **Open a new window when it genuinely helps people keep two things in view, not as the default response to an action.** Composing a message next to the one being answered is worth a window; a new window for every navigation step is clutter people have to clean up.
- **Offer "open in a new window" as a choice — in a context menu or a File-type menu — rather than deciding for people.** Flexibility here costs nothing and suits people who work across several windows.
- **Where the platform has a direct way to pull an item out into its own window, support it.** A gesture or drag that expands an item into a window is faster than a menu, and people who know it will try it.
- **Keep the platform's visual distinction between the active window and the inactive ones.** People rely on that difference to know which window will take their input; system components do it for free, and a custom window has to reproduce every state or it will look broken.
- **Use the system's window frame, controls and full-screen support instead of imitating them.** A custom frame that almost matches the platform reads as broken, and the system's own implementation handles cases such as a display's camera housing for you.
- **Keep your own controls clear of the system's window controls.** When window controls appear at the leading edge of a toolbar, inset your leading items instead of letting them be covered.
- **Use the platform's own word for a window in anything a person reads.** Implementation words such as "scene" confuse people; the thing on screen is a window.
- **Restore window size and position between sessions.** People arrange windows deliberately, and rearranging them every launch throws that work away.
[HIG: windows, going-full-screen]

- **Offer a full-screen mode when concentration or immersion is the point — media, games, an in-depth editing task — and not otherwise.** People reach for it to remove distraction; on a screen that already has nothing else on it the mode adds nothing but a state to get stuck in.
- **Adjust the layout for the larger canvas, but do not resize the window yourself and do not rearrange which items exist.** Keep essential content prominent, use the extra space, and keep the change subtle enough that moving in and out of the mode is not jarring.
- **Keep essential controls available in full screen, or revealable with a familiar gesture.** Playback controls that cannot be recovered without leaving the mode defeat the mode.
- **Let people decide when to enter and when to leave full screen, and never exit on their behalf.** Prefer the platform's own control, menu item and keyboard shortcut over a custom mode picker.
- **Preserve access to the system's app-switching affordances while full screen, except in a game where an accidental swipe would be costly.** People still need to reach their other apps.
- **When you hide chrome to prioritise content, restore it on a familiar action — a tap, a swipe down, moving the pointer to the top edge — and keep anything essential for navigation visible.** Hidden controls that need a secret gesture are lost controls.
- **Pause on the way out and resume on the way back in.** Leaving a full-screen slideshow or game should not cost people the part they missed.
[HIG: going-full-screen, multitasking]

## Scrolling

- **Support the platform's default scrolling gestures, keyboard shortcuts and indicator behaviour, including its elastic feel at the ends.** People expect systemwide scrolling to work everywhere; custom scrolling that behaves differently is felt immediately as low quality.
- **Make it visible that content continues.** Show a sliver of the next item at the edge of the view, because indicators are not always on screen and a view that looks complete does not get scrolled.
- **Let the scroll indicator report position, not merely activity.** Its size and place tell people whether they are near the beginning, the middle or the end, which is how they judge how much is left; keep it where the platform puts it so it can be found.
- **Do not nest a scrolling view inside another that scrolls the same axis.** Two same-axis scrollers make it unpredictable which one moves and are hard to control. A horizontal scroller inside a vertical one is fine.
- **Use page-by-page scrolling only when the content is genuinely page-shaped, and overlap pages by a line or a row so people keep their place.** When you do, show a page indicator and suppress the continuous scroll indicator on the same axis so the two are not redundant.
- **Scroll automatically only to bring into view something the person needs right now, and only as far as necessary.** Found search text, the insertion point they just moved to, a selection they are extending: scroll to those. Never scroll content out from under someone otherwise.
- **Set sensible minimum and maximum zoom levels.** Zooming until a single character fills the view is not a useful state to offer.
[HIG: scroll-views]

## Deliberately omitted

- **visionOS spatial specifics** — volumes, baseplates, ornaments, dynamic versus fixed scaling, the mandatory glass window background, minimum 60-point control spacing for eye targeting, and Look to Scroll. These depend on head-worn hardware and eye input and have no meaning on a screen; the generic parts (support resizing, keep supplementary content in an adjacent pane, define clear scroll areas) are kept above.
- **tvOS grid specifications** — the two- through nine-column tables of unfocused content widths, 40-point horizontal and 100-point vertical spacing, and the fixed 68-point tab bar height. These are point values tied to one display distance and one focus engine; the generic rules (consistent spacing, room for focus growth, symmetrical partially hidden content, far-viewing margins) are kept.
- **Lockup subtypes** — cards, caption buttons, monograms and posters, including their tilt-with-swipe behaviour. These are tvOS focus-engine components; only the two general rules from that page (space between focusable units, consistent sizes within a group) are kept.
- **Liquid Glass and material implementation detail** — the regular and clear variants, the 35 % dimming layer for clear glass over bright content, the named vibrancy levels for labels, fills and separators, the four standard iOS material thicknesses, and macOS blending modes. These are Apple API surfaces; the transferable rules about layering, legibility over a material, and choosing by meaning rather than apparent colour are kept.
- **watchOS layout and scrolling specifics** — no more than two or three controls side by side, the elliptical list style, wrist autorotation, vertical page-based navigation between detail views, and Digital Crown scrolling. These follow from a wrist-sized display and a hardware crown.
- **Path control styles and file-system specifics** — the standard versus pop-up path control, dragging an item onto the control, and the Finder path bar. Only the general rule (show location in the hierarchy, in the window body) is kept; file handling belongs to `references/platforms-and-web.md`.
- **Systemwide search implementation** — Spotlight file importers, custom metadata plug-ins and Quick Look generators. These are developer integration tasks, not interface design; the design rule (make content findable from outside the app) is kept.
- **Audio and Picture-in-Picture behaviour from multitasking** — pausing and ducking audio on interruption. Sound belongs to `references/motion-feedback-loading.md`.
- **The two index pages** — `layout-and-organization` and `navigation-and-search` carry no guidance of their own, only the list of components beneath them; each of those components is covered above.
- **Small and mini scroll bar variants in macOS panels, and the game rule against changing the display mode on entering full screen.** Both are single-platform control specifics with no generic form.
- **Icon and colour choices for navigation items** — symbol selection, accent colour in sidebar icons, and tab-label colour against a colourful content layer. These belong to `references/typography-color-visuals.md`.

## Translation to web and other platforms

These are this skill's translations of the rules above, not Apple guidance.

- **Treat the URL as navigation state: every destination a person can reach should have an address that reloads, bookmarks and shares to the same place.** This is the web's form of "preserve a person's context". [translation]
- **Make the browser's Back and Forward behave like the platform's back.** Do not trap history, do not push a history entry for a transient state people do not want to step through, and close an overlay that changed the URL when Back is pressed. [translation]
- **Use a breadcrumb trail as the web's path control, in the page body rather than in a sticky header.** [translation]
- **Make a deep link land in context.** A shared link to a nested item should open with its parent structure around it, not on a screen with no way up. [translation]
- **Branch layout on available width with container and media queries, never on user-agent sniffing.** Breakpoints are the web's size classes; keep every feature present at every width and vary only how much is visible. [translation]
- **Give a sticky header or bottom bar the role of a toolbar or tab bar: reserve its space in the layout, keep it out of the content's way, and respect device insets with `env(safe-area-inset-*)`.** [translation]
- **Keep DOM order equal to reading order so focus order follows the visual layout.** Use CSS order and grid placement only where the visual result still matches the DOM sequence, and express panes as landmarks — `nav`, `main`, `aside` — so a screen reader gets the same structure the eye does. See `references/accessibility-inclusion-privacy.md`. [translation]
- **Express text scaling in relative units and verify the layout reflows at 200 % zoom without clipping or overlap.** `rem`-based sizing and user zoom are the web's equivalent of a system text-size setting. [translation]
- **Reserve space for images, embeds and async content so nothing shifts after it loads.** Layout shift is the web's version of a layout that jumps under people's hands; see `references/motion-feedback-loading.md`. [translation]
- **Keep page-level scrolling to the browser: no scroll hijacking, no custom scrollbars that lose the platform's feel, and horizontal overflow confined to the one wide table, diagram or code block that needs it.** [translation]
- **Give a scrolling region one primary axis, and let cross-axis content wrap or stack instead of scrolling.** Content that scrolls both ways at once is hard to read and hard to control. Apple's scrolling guidance only forbids nesting two scrollers on the same axis, so the preference for a single axis is this skill's own; apply it to a pane, a card or a table region, and where two axes are unavoidable keep one of them the outer page scroll. [translation]
- **Implement in-app search as a real search input that updates results as people type, debounced, with the query reflected in the URL.** [translation]
- **Write both the empty state and the no-results state.** An empty state says why there is nothing here and what the next step is; a no-results state repeats what was searched, offers a way to clear a filter or broaden the scope, and never shows a bare blank area. [translation]
- **On desktop, mirror the platform's structural conventions: resizable panes with keyboard-reachable dividers, remembered window and pane sizes, and Find in the expected place.** [translation]
- **In an Electron or Capacitor shell, let the shell follow the host platform and the content follow the rules above.** Window controls, the menu bar and shortcuts come from the desktop OS; safe areas and the system back gesture come from the mobile OS; everything inside the web view is still layout and navigation as described here. Details in `references/platforms-and-web.md`. [translation]

## Sources

Corpus pages used, each at `https://developer.apple.com/design/human-interface-guidelines/<slug>`:

- `design-principles` — https://developer.apple.com/design/human-interface-guidelines/design-principles
- `layout` — https://developer.apple.com/design/human-interface-guidelines/layout
- `materials` — https://developer.apple.com/design/human-interface-guidelines/materials
- `layout-and-organization` — https://developer.apple.com/design/human-interface-guidelines/layout-and-organization
- `boxes` — https://developer.apple.com/design/human-interface-guidelines/boxes
- `collections` — https://developer.apple.com/design/human-interface-guidelines/collections
- `column-views` — https://developer.apple.com/design/human-interface-guidelines/column-views
- `disclosure-controls` — https://developer.apple.com/design/human-interface-guidelines/disclosure-controls
- `lists-and-tables` — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
- `outline-views` — https://developer.apple.com/design/human-interface-guidelines/outline-views
- `split-views` — https://developer.apple.com/design/human-interface-guidelines/split-views
- `tab-views` — https://developer.apple.com/design/human-interface-guidelines/tab-views
- `navigation-and-search` — https://developer.apple.com/design/human-interface-guidelines/navigation-and-search
- `path-controls` — https://developer.apple.com/design/human-interface-guidelines/path-controls
- `search-fields` — https://developer.apple.com/design/human-interface-guidelines/search-fields
- `sidebars` — https://developer.apple.com/design/human-interface-guidelines/sidebars
- `tab-bars` — https://developer.apple.com/design/human-interface-guidelines/tab-bars
- `token-fields` — https://developer.apple.com/design/human-interface-guidelines/token-fields
- `searching` — https://developer.apple.com/design/human-interface-guidelines/searching
- `multitasking` — https://developer.apple.com/design/human-interface-guidelines/multitasking
- `going-full-screen` — https://developer.apple.com/design/human-interface-guidelines/going-full-screen
- `windows` — https://developer.apple.com/design/human-interface-guidelines/windows
- `scroll-views` — https://developer.apple.com/design/human-interface-guidelines/scroll-views
- `lockups` — https://developer.apple.com/design/human-interface-guidelines/lockups

Talk: «Principles of great design», WWDC26 session 250 — https://developer.apple.com/videos/play/wwdc2026/250/

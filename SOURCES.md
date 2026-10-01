# Sources and attribution

Apple UX/UI is an independent collection of working rules, summaries, and adaptations assembled by Mikhail Kim. Apple did not create, review, or endorse this package.

## Primary sources

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), including the [design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) and topic pages identified throughout the references.
- [Principles of great design](https://developer.apple.com/videos/play/wwdc2026/250/), WWDC26 session 250.

The saved references were assembled from selected source material on **2026-09-14**. They do not cover every HIG page or reproduce all platform, hardware, API, image, or video details. They are not automatically refreshed.

## Reading the source tags

| Tag | Meaning |
| --- | --- |
| `[HIG: buttons]` | Guidance drawn from the HIG page at `https://developer.apple.com/design/human-interface-guidelines/buttons`. Multiple slugs identify multiple supporting pages. |
| `[WWDC26-250]` | Guidance drawn from the linked WWDC talk. |
| `[translation]` | This project's adaptation to another platform, or an inference rather than an explicit Apple statement. |

Source tags identify provenance; they do not mean that every sentence is a quotation. The guidance has been reorganized and paraphrased. Short quoted phrases, source titles, and the named design principles are attributed to Apple.

## Licensing boundary

The repository's MIT license applies to original contributions, including its original code, packaging, and original explanatory wording. It does not grant rights to third-party text, trademarks, artwork, or other material owned by Apple or another party. Those rights remain with their respective owners.

No Apple logo, proprietary font, source-page archive, or full video transcript is distributed in this repository. The README illustration is original project artwork.

## Live documentation helper

`skills/apple-ux-ui/scripts/hig.py` retrieves Apple's public DocC JSON on request and converts supported text structures to Markdown. The response comes from Apple at execution time and retains a link to the original page. The helper does not download a full corpus or replace the saved references.

Images are omitted, and some layout or nesting is simplified. Consult the original page for visual examples, full presentation, and current context. Availability and document structure depend on Apple's website.

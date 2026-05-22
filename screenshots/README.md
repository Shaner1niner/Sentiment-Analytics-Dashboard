# Screenshot Candidates

This folder is reserved for recruiter-safe dashboard screenshots.

No raw screenshots were copied automatically from the source repositories. Before adding any image here, each screenshot should be manually reviewed for public safety.

## Recommended screenshots

| Target filename | Source view | Why it belongs |
| --- | --- | --- |
| `dashboard_overview_public.png` | `sentiment-dash/interactive_dashboard_fix24_public_embed.html` | Best high-level visual of the public dashboard, controls, chart area, and product surface. |
| `market_tape_context.png` | Public dashboard Market Tape module | Shows dashboard product thinking beyond a single chart. |
| `briefing_panel.png` | Public dashboard briefing module | Shows how analytics are translated into explanatory, public-safe context. |
| `chart_guide_methodology.png` | Public dashboard chart guide | Explains methodology in a recruiter-friendly way. |
| `public_context_cards.png` | `sentiment-dash/seta_public_context_cards.html` | Shows public-safe narrative/card output, useful for portfolio storytelling. |

## Public-safety review checklist

Before adding a screenshot, confirm it contains no:

- API keys, tokens, or credentials
- database URLs or local file paths
- private emails, account names, or personal identifiers
- member-only content
- unreleased premium workflow details
- raw production data that should remain private
- confidential schema/table names
- language that reads like a recommendation or certainty claim

## Recommended capture process

1. Open the source dashboard locally or from the public deployment.
2. Set the view to a public-safe asset and time range.
3. Capture a clean browser screenshot.
4. Crop browser chrome unless the URL itself is useful and public-safe.
5. Save the file using the target filename above.
6. Add the screenshot to this folder.
7. Update the main README with a visual preview section.

## Suggested README preview block

```md
## Visual preview

![Public dashboard overview](screenshots/dashboard_overview_public.png)

Additional screenshots:

- [Market Tape context](screenshots/market_tape_context.png)
- [Briefing panel](screenshots/briefing_panel.png)
- [Chart guide methodology](screenshots/chart_guide_methodology.png)
- [Public context cards](screenshots/public_context_cards.png)
```

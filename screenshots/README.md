# Screenshot Candidates

This folder is reserved for recruiter-safe dashboard screenshots.

No raw screenshots are copied automatically from the source repositories. Before adding any image here, each screenshot should be manually reviewed for public safety.

## Recommended primary screenshot

| Target filename | Source view | Use |
| --- | --- | --- |
| `dashboard_overview_public.png` | New SETA Public Dashboard / NVDA briefing view | Primary README hero screenshot. This is the strongest external-facing visual because it shows the modern product surface: controls, Market Radar, asset briefing cards, structure score, signal state, and sentiment-enhanced technical charting in one view. |

## Current supporting screenshots and additional candidates

| Target filename | Source view | Why it belongs |
| --- | --- | --- |
| `mobile_dashboard_public.png` | Mobile QA preview | Shows responsive-design review and product QA thinking beyond desktop usage. |
| `market_context_public.png` | SETA Public Dashboard market context cards | Already referenced by the main README; shows public-safe market-context explanations. |
| `market_radar_context.png` | Future SETA Public Dashboard Market Radar crop | Optional future crop for cross-asset context beyond a single chart. |
| `asset_briefing_panel.png` | SETA Public Dashboard asset briefing module | Shows how analytics are translated into explanatory, public-safe context. |
| `technical_chart_context.png` | SETA Public Dashboard chart section | Shows sentiment-enhanced technical visualization. |
| `tableau_prototype_aapl.png` | Earlier AAPL Tableau-style dashboard | Shows project evolution and earlier dashboarding capability. |
| `tableau_prototype_nvda.png` | Earlier NVDA Tableau-style dashboard | Shows asset-specific dashboard prototyping and visual iteration. |
| `tableau_prototype_tsla.png` | Earlier TSLA Tableau-style dashboard | Optional archive/evolution screenshot; use only if framed as an earlier prototype. |

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
## Dashboard preview

![SETA Public Dashboard overview](screenshots/dashboard_overview_public.png)

This dashboard view shows the public-facing SETA interface: asset controls, Market Radar, narrative briefing cards, structure score, signal state, and sentiment-enhanced technical charting.

Additional prototype views are included to show the project’s evolution from earlier Tableau-style dashboards into the current SETA public dashboard format.
```

## Notes on source repo QA assets

The `sentiment-dash` source repository includes a `qa_outputs/` folder and generated dashboard assets. Candidate screenshots from that folder should be reviewed before being copied into this public portfolio repo.

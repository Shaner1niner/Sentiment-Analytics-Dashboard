# Sentiment Analytics Dashboard

A public portfolio showcase for a sentiment-driven financial analytics dashboard. This repository is designed for recruiters, hiring managers, and professional reviewers who want to understand the project at the product, analytics, and reporting layer without exposing the private SETA engine.

## What this repository demonstrates

This repo highlights how social sentiment, engagement behavior, and market-related data can be organized into clean dashboard-ready reporting assets using Tableau, SQL, Python, and PostgreSQL-style data modeling.

It is intentionally curated to show:

- dashboard design and analytical storytelling
- sentiment and engagement reporting concepts
- sanitized sample data structures
- Tableau calculation notes
- SQL reporting examples
- architecture documentation
- recruiter-friendly project positioning

## What is intentionally excluded

The production SETA engine is not included here. Private or proprietary components remain outside this public showcase, including:

- production ingestion pipelines
- API integrations and credentials
- orchestration logic
- proprietary weighting methodology
- live database connections
- private deployment configuration
- raw production data
- monetization or member-only infrastructure

This repository is the showroom, not the machine.

## Public safety and use policy

This project is educational and analytical. It is not financial advice, does not provide personalized recommendations, and avoids buy/sell language, guarantees, or trading instructions.

## Repository layout

```text
Sentiment-Analytics-Dashboard/
├── README.md
├── .gitignore
├── architecture/
│   └── public_portfolio_architecture.md
├── docs/
│   ├── dashboard_methodology.md
│   ├── data_dictionary_sanitized.md
│   ├── recruiter_talking_points.md
│   └── source_selection_log.md
├── sample_data/
│   ├── sample_asset_metrics.csv
│   └── sample_sentiment_scores.csv
├── sql_examples/
│   └── sentiment_dashboard_rollup_sample.sql
└── tableau_notes/
    └── calculated_fields.md
```

## Relationship to `sentiment-dash`

The existing `sentiment-dash` repository is the current public-facing working dashboard source. This portfolio repo is a cleaner, recruiter-facing companion repo. It selectively documents the dashboard concept, reporting model, sample data, and safe excerpts without copying over production-sensitive workflows.

## Suggested reviewer path

1. Start with `docs/recruiter_talking_points.md` for the professional summary.
2. Review `architecture/public_portfolio_architecture.md` for the system overview.
3. Open `docs/dashboard_methodology.md` for the analytical framework.
4. Inspect `sample_data/` and `sql_examples/` for sanitized reporting examples.
5. Review `tableau_notes/calculated_fields.md` for dashboard implementation logic.

## Core professional narrative

This project demonstrates the ability to combine accounting discipline, data engineering judgment, SQL reporting, dashboard design, and financial analytics into a clear decision-support system.

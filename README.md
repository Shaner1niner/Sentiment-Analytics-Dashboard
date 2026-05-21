# Sentiment Analytics Dashboard

A public portfolio showcase for a sentiment-driven financial analytics dashboard. This repository is designed for recruiters, hiring managers, and professional reviewers who want to understand the project at the product, analytics, reporting, and governance layer while keeping the private SETA engines protected.

## What this repository demonstrates

This repo highlights how social sentiment, engagement behavior, model validation concepts, and market-related data can be organized into clean dashboard-ready reporting assets using Tableau, SQL, Python, and PostgreSQL-style data modeling.

It is intentionally curated to show:

- dashboard design and analytical storytelling
- sentiment and engagement reporting concepts
- sanitized sample data structures
- Tableau calculation notes
- SQL reporting examples
- architecture documentation
- recruiter-friendly project positioning
- model validation and dashboard handoff concepts
- public/private engineering judgment

## What is intentionally excluded

The production SETA engines are not included here. Private or proprietary components remain outside this public showcase, including:

- production ingestion pipelines
- API integrations and credentials
- orchestration logic
- proprietary weighting methodology
- live database connections
- private deployment configuration
- raw production data
- model training code and artifacts
- ensemble selection logic
- monetization or member-only infrastructure

This repository is the showroom, not the machine.

## Public safety and use policy

This project is educational and analytical. It presents dashboard context and portfolio documentation only. It is not a personalized recommendation system.

## Repository layout

```text
Sentiment-Analytics-Dashboard/
├── README.md
├── .gitignore
├── architecture/
│   └── public_portfolio_architecture.md
├── docs/
│   ├── analytics_framework_glossary.md
│   ├── dashboard_handoff_contract_concept.md
│   ├── dashboard_methodology.md
│   ├── data_dictionary_sanitized.md
│   ├── model_validation_principles.md
│   ├── prediction_intelligence_public_summary.md
│   ├── private_engine_boundary.md
│   ├── public_safe_output_contract.md
│   ├── recruiter_talking_points.md
│   ├── seta_engine_public_summary.md
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

## Relationship to the private SETA engines

The private SETA engine is the analytics and data-quality layer behind the broader project. The private SETA Prediction Intelligence Engine is the model validation and dashboard-context layer. This public repository summarizes both at a conceptual level while keeping production code, source adapters, model internals, database details, and commercial infrastructure private.

Useful docs:

- `docs/seta_engine_public_summary.md`
- `docs/prediction_intelligence_public_summary.md`
- `docs/private_engine_boundary.md`
- `docs/model_validation_principles.md`
- `docs/dashboard_handoff_contract_concept.md`

## Suggested reviewer path

1. Start with `docs/recruiter_talking_points.md` for the professional summary.
2. Review `architecture/public_portfolio_architecture.md` for the system overview.
3. Open `docs/seta_engine_public_summary.md` for the private analytics-engine summary.
4. Open `docs/prediction_intelligence_public_summary.md` for the private modeling-layer summary.
5. Open `docs/private_engine_boundary.md` to understand what is intentionally protected.
6. Open `docs/dashboard_methodology.md` for the analytical framework.
7. Inspect `sample_data/` and `sql_examples/` for sanitized reporting examples.
8. Review `tableau_notes/calculated_fields.md` for dashboard implementation logic.

## Core professional narrative

This project demonstrates the ability to combine accounting discipline, data engineering judgment, SQL reporting, dashboard design, financial analytics, validation thinking, and public-safe communication into a clear decision-support system.

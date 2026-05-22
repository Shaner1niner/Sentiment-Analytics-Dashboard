# Public Architecture Diagram

## Purpose

This diagram explains the public/private architecture boundary for the Sentiment Analytics Dashboard portfolio.

The public repository is designed to show the reporting surface, methodology, sample data, and recruiter-safe documentation. The private repositories keep ingestion, scoring, orchestration, validation, and production infrastructure protected.

## High-level architecture

```mermaid
flowchart LR
    A[Public and market data sources] --> B[Private SETA Engine]
    B --> C[Private analytics and enrichment layer]
    C --> D[Dashboard-ready reporting outputs]
    D --> E[Sentiment Dash working dashboard]
    D --> F[Public portfolio repository]

    G[Private Prediction Intelligence Engine] --> D
    G --> H[Model validation and context outputs]
    H --> D

    F --> I[Recruiter-safe docs]
    F --> J[Sanitized sample data]
    F --> K[SQL examples]
    F --> L[Tableau notes]
    F --> M[Screenshots after review]
```

## Public/private boundary

```mermaid
flowchart TB
    subgraph Private_System[Private system - protected]
        A1[Ingestion logic]
        A2[Source adapters]
        A3[Database connections]
        A4[Scoring and weighting internals]
        A5[Model training and validation code]
        A6[Production orchestration]
    end

    subgraph Public_Portfolio[Public portfolio - recruiter safe]
        B1[Architecture summaries]
        B2[Methodology docs]
        B3[Sanitized sample CSVs]
        B4[SQL reporting examples]
        B5[Tableau calculated-field notes]
        B6[Reviewed screenshots]
    end

    Private_System --> C[Sanitized concepts and dashboard-ready examples]
    C --> Public_Portfolio
```

## Dashboard handoff concept

```mermaid
flowchart LR
    A[Private analytics engine] --> B[Clean output contract]
    B --> C[Dashboard context fields]
    C --> D[Public-safe visual layer]
    D --> E[Recruiter portfolio]

    B --> B1[asset]
    B --> B2[date]
    B --> B3[sentiment state]
    B --> B4[attention state]
    B --> B5[context label]
    B --> B6[review status]
```

## Design principle

> The private system can be complex. The public portfolio should be clear.

## Reviewer takeaway

This architecture demonstrates separation of concerns:

- private engines perform the complex work
- reporting outputs create stable dashboard handoffs
- public documentation explains the system safely
- recruiters can evaluate skill without seeing proprietary internals

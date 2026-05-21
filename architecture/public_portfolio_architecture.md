# Public Portfolio Architecture

## Purpose

This document describes the public-facing architecture of the Sentiment Analytics Dashboard portfolio. It is intentionally high-level and sanitized for public review.

## Architecture concept

```text
Public/social/news inputs
        ↓
Private ingestion and normalization layer
        ↓
Private sentiment and engagement processing
        ↓
Private reporting tables and dashboard extracts
        ↓
Public-safe sample data and documentation
        ↓
Tableau-style dashboards, scorecards, and narrative visuals
```

## Public vs private boundary

### Public showcase layer

This repository may include:

- dashboard screenshots
- sanitized sample CSVs
- data dictionary examples
- SQL reporting examples
- Tableau calculation notes
- architecture summaries
- recruiter-friendly methodology documentation

### Private production layer

The following remain private:

- raw ingestion scripts
- API connectors
- database credentials
- production orchestration
- proprietary weighting and scoring internals
- member-only or monetization logic
- raw production data
- deployment configuration

## Dashboard domains

The dashboard concept organizes information into several analytical layers:

1. **Asset context**: the selected ticker or asset being reviewed.
2. **Sentiment direction**: public tone across relevant sources.
3. **Attention and engagement**: whether participation is concentrated, expanding, or fading.
4. **Market context**: price, volume, and indicator context used for interpretation.
5. **Narrative framing**: public-safe explanatory copy that avoids trading recommendations.
6. **Dashboard controls**: time period, asset, sentiment source, and visual mode toggles.

## Design principle

The public repository should prove analytical maturity without exposing the production machine. It should show enough to demonstrate professional capability while preserving the defensible architecture of the private SETA engine.

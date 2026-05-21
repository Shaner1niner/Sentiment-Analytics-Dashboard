# Private Engine Boundary

## Purpose

This document defines the boundary between the public portfolio repository and the private SETA engine.

The goal is to show professional capability while protecting the parts of the system that represent proprietary methodology, production infrastructure, and future commercial value.

## Public repository principle

The public repository should show the following:

- what the system is designed to explain
- why the analysis matters
- how outputs can be interpreted safely
- what dashboard-ready data can look like
- how SQL and Tableau logic support reporting
- how a reviewer should understand the project professionally

The public repository should not expose the implementation details that make the system difficult to replicate.

## Safe public content

The following content is generally safe for this repo:

- dashboard screenshots after manual review
- sanitized sample CSVs
- high-level architecture diagrams
- public-safe methodology summaries
- recruiter-facing talking points
- simplified SQL examples
- Tableau calculated-field examples
- general glossary terms
- educational disclaimers

## Content requiring review

The following should be reviewed carefully before being added:

- generated dashboard payloads
- detailed schema descriptions
- excerpts from operational documentation
- output examples produced from live data
- model comparison notes
- source-specific performance analysis
- anything mentioning exact production cadence
- anything describing future paid features

## Content that should stay private

The following should not be copied into this public repo:

- API keys or credentials
- `.env` files
- database URLs
- raw source adapters
- ingestion scripts
- orchestration scripts
- scheduler configuration
- database migrations
- production schemas
- proprietary weighting formulas
- engagement scoring internals
- model tuning workflows
- private research automation
- member-only product logic
- monetization infrastructure
- unreleased roadmap details

## Practical rule

Use this decision rule when deciding whether to add something:

> Public repo gets the what and why. Private repo keeps the how.

## Examples

### Safe

> The system combines sentiment, attention, and market context into dashboard-ready summaries.

### Not safe

> The exact source-by-source weighting formula, production table joins, scheduler behavior, and fallback logic used to generate those summaries.

## Reviewer note

This boundary is intentional. A professional public portfolio should demonstrate capability without publishing the core production system.

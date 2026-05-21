# Source Selection Log

This document records the public/private selection logic for this portfolio repository.

## Source repo reviewed

The current public-facing dashboard source is `Shaner1niner/sentiment-dash`.

That repository contains a more operational dashboard baseline, including public and member dashboard shells, dashboard application logic, CSS, mode manifests, generated chart payloads, screener payloads, and smoke-test workflows.

## Selection principle

For this recruiter-facing portfolio repo, we are not copying production-sensitive files by default. Instead, we are using `sentiment-dash` as the conceptual starting point and creating a cleaner public portfolio layer.

## Safe to include here

- high-level architecture notes
- dashboard methodology
- recruiter-facing talking points
- sanitized sample data
- sanitized SQL examples
- Tableau calculation examples
- public-safe copy rules
- screenshots after manual review

## Do not include here without review

- live dashboard payloads
- member-mode assets
- generated chart stores
- local refresh scripts
- database export bridges
- API-dependent scripts
- production smoke-test internals
- local path references
- files containing environment variables

## Review checklist before adding future files

Before copying any file from another repo, check for:

- credentials or tokens
- local Windows paths
- database URLs
- private endpoint names
- proprietary weighting formulas
- member-only content
- production data
- hidden notebook outputs
- personal identifiers

## Current status

Initial public portfolio scaffold created. Future additions should prioritize reviewed screenshots and documentation over raw production code.

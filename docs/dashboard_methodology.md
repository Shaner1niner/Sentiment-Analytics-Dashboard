# Dashboard Methodology

## Overview

The Sentiment Analytics Dashboard is designed to explain market narrative behavior, not to provide trading instructions. The central question is:

> What is the public attention and sentiment structure around an asset, and how is that structure changing over time?

## Analytical dimensions

### Sentiment

Sentiment represents directional tone in public discussion. In a production system, sentiment may be derived from multiple sources and models. In this public repository, sample sentiment values are simplified and sanitized.

Typical fields:

- `asset`
- `date`
- `source`
- `sentiment_score`
- `sentiment_label`
- `mention_count`

### Attention

Attention measures participation and engagement. It is separate from sentiment. A strongly positive narrative with low attention may mean something different from a neutral narrative with unusually high engagement.

Typical fields:

- `engagement_score`
- `mention_count`
- `source_count`
- `attention_bucket`

### Market context

Market data provides context but does not automatically validate sentiment. The project treats price and volume as companion variables rather than direct proof that a narrative is correct.

Typical fields:

- `close_price`
- `volume`
- `return_1d`
- `volatility_bucket`

## Interpretation rules

- Sentiment is context, not a trading signal.
- Attention is not the same thing as validation.
- Positive tone with weak engagement may represent shallow optimism.
- Negative tone with rising attention may represent narrative stress.
- High attention with neutral sentiment may indicate uncertainty or unresolved debate.
- Human review remains important for public-facing summaries.

## Public-facing language rules

Dashboard copy should avoid:

- buy/sell language
- guaranteed outcomes
- personalized financial advice
- price targets
- certainty around predictions

Preferred language:

- "narrative pressure"
- "attention concentration"
- "sentiment context"
- "participation pattern"
- "public tone"
- "market narrative"

## Portfolio objective

For career and recruiter use, this repository demonstrates how to convert messy, unstructured behavioral data into a structured analytics product with clear reporting logic and public-safe communication.

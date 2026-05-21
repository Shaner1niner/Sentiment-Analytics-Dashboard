# Sanitized Data Dictionary

This data dictionary describes simplified, public-safe fields suitable for examples and documentation. It does not represent a production database schema.

## `sample_sentiment_scores.csv`

| Field | Description | Example |
| --- | --- | --- |
| `date` | Observation date | `2026-01-01` |
| `asset` | Asset or ticker symbol | `BTC` |
| `source` | Public discussion source category | `reddit` |
| `sentiment_score` | Simplified sentiment score from -1 to 1 | `0.42` |
| `sentiment_label` | Human-readable sentiment bucket | `positive` |
| `mention_count` | Sanitized count of source mentions | `185` |
| `engagement_score` | Sanitized engagement index | `74.3` |
| `attention_bucket` | Low, medium, or high attention label | `high` |

## `sample_asset_metrics.csv`

| Field | Description | Example |
| --- | --- | --- |
| `date` | Observation date | `2026-01-01` |
| `asset` | Asset or ticker symbol | `BTC` |
| `close_price` | Example closing price | `95000.00` |
| `volume_index` | Sanitized volume index | `1.18` |
| `return_1d` | One-day example return | `0.012` |
| `volatility_bucket` | Simplified volatility classification | `medium` |

## Notes

- Values are illustrative and sanitized.
- These files are intended for dashboard and reporting examples only.
- They should not be interpreted as production data or financial advice.

# Sanitized Data Dictionary

This data dictionary describes simplified, public-safe fields suitable for examples and documentation. It does not represent a production database schema.

## `sample_sentiment_scores.csv`

| Field | Description | Example |
| --- | --- | --- |
| `date` | Observation date | `2026-01-01` |
| `asset` | Asset or ticker symbol | `BTC` |
| `source` | Public discussion source category | `reddit` |
| `sentiment_score` | Simplified sentiment score from -1 to 1 | `0.42` |
| `sentiment_label` | Human-readable sentiment bucket such as `positive`, `neutral_positive`, `neutral`, `neutral_negative`, or `negative` | `positive` |
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

## `sql_examples/sentiment_dashboard_rollup_sample.sql`

The sample SQL joins the two public CSV-shaped tables into a dashboard-facing rollup. Output fields are illustrative and derived only from the sanitized examples above.

| Field | Description | Example |
| --- | --- | --- |
| `date` | Observation date used for the joined sentiment and asset context | `2026-01-01` |
| `asset` | Asset or ticker symbol | `BTC` |
| `avg_sentiment_score` | Average simplified sentiment score by asset/date | `0.4200` |
| `total_mentions` | Total sanitized mention count by asset/date | `185` |
| `avg_engagement_score` | Average sanitized engagement index by asset/date | `74.30` |
| `close_price` | Example closing price from the asset metrics sample | `95000.00` |
| `volume_index` | Sanitized volume index from the asset metrics sample | `1.18` |
| `return_1d` | One-day example return from the asset metrics sample | `0.012` |
| `volatility_bucket` | Simplified volatility classification | `medium` |
| `narrative_state` | Public-safe combined sentiment/attention bucket emitted by the sample SQL | `positive_high_attention` |

## Notes

- Values are illustrative and sanitized.
- These files are intended for dashboard and reporting examples only.
- They should not be interpreted as production data or financial advice.

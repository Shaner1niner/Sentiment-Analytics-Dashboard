-- Sentiment dashboard rollup sample
-- Public-safe illustrative SQL only. This is not a production schema.

WITH sentiment_daily AS (
    SELECT
        date,
        asset,
        AVG(sentiment_score) AS avg_sentiment_score,
        SUM(mention_count) AS total_mentions,
        AVG(engagement_score) AS avg_engagement_score
    FROM sample_sentiment_scores
    GROUP BY date, asset
),
asset_daily AS (
    SELECT
        date,
        asset,
        close_price,
        volume_index,
        return_1d,
        volatility_bucket
    FROM sample_asset_metrics
)
SELECT
    s.date,
    s.asset,
    ROUND(s.avg_sentiment_score, 4) AS avg_sentiment_score,
    s.total_mentions,
    ROUND(s.avg_engagement_score, 2) AS avg_engagement_score,
    a.close_price,
    a.volume_index,
    a.return_1d,
    a.volatility_bucket,
    CASE
        WHEN s.avg_sentiment_score >= 0.25 AND s.avg_engagement_score >= 60 THEN 'positive_high_attention'
        WHEN s.avg_sentiment_score <= -0.10 AND s.avg_engagement_score >= 60 THEN 'negative_high_attention'
        WHEN s.avg_engagement_score >= 60 THEN 'neutral_high_attention'
        ELSE 'normal_attention'
    END AS narrative_state
FROM sentiment_daily s
LEFT JOIN asset_daily a
    ON s.date = a.date
   AND s.asset = a.asset
ORDER BY s.date, s.asset;

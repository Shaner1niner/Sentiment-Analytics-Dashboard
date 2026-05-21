# Tableau Calculated Field Notes

These examples are public-safe dashboard implementation notes. They are written as conceptual Tableau logic rather than production workbook exports.

## Sentiment label

```text
IF [Avg Sentiment Score] >= 0.25 THEN "Positive"
ELSEIF [Avg Sentiment Score] <= -0.10 THEN "Negative"
ELSE "Neutral"
END
```

## Attention bucket

```text
IF [Avg Engagement Score] >= 70 THEN "High Attention"
ELSEIF [Avg Engagement Score] >= 45 THEN "Medium Attention"
ELSE "Low Attention"
END
```

## Narrative state

```text
IF [Avg Sentiment Score] >= 0.25 AND [Avg Engagement Score] >= 60 THEN "Positive / High Attention"
ELSEIF [Avg Sentiment Score] <= -0.10 AND [Avg Engagement Score] >= 60 THEN "Negative / High Attention"
ELSEIF [Avg Engagement Score] >= 60 THEN "Neutral / High Attention"
ELSE "Normal Attention"
END
```

## Dashboard title example

```text
"Sentiment and Attention Context for " + [Asset]
```

## Public-safe interpretation rule

Dashboard text should describe sentiment and attention conditions without implying a trade recommendation.

Preferred phrasing:

> Public discussion shows elevated attention and positive tone.

Avoid:

> This is a buy signal.

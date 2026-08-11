from news_agent.tools.sentiment import analyze_sentiment


def test_positive_sentiment():
    result = analyze_sentiment.invoke(
        {
            "text": (
                "The company reported excellent results "
                "and strong growth."
            )
        }
    )

    assert result["sentiment"] == "positive"


def test_negative_sentiment():
    result = analyze_sentiment.invoke(
        {
            "text": (
                "The company reported major losses and "
                "a significant decline in revenue."
            )
        }
    )

    assert result["sentiment"] == "negative"


def test_neutral_sentiment():
    result = analyze_sentiment.invoke(
        {
            "text": (
                "The meeting was held on Tuesday in "
                "the company's headquarters."
            )
        }
    )

    assert result["sentiment"] == "neutral"
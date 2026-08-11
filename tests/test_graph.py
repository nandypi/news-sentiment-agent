from news_agent.graph import graph


def test_news_graph():
    article = """
    The technology company announced record revenue this
    quarter. Executives said demand for its products remained
    strong and the company plans to expand its operations.
    """

    result = graph.invoke(
        {
            "input_text": article,
        }
    )

    assert result["article_text"] == article.strip()
    assert result["summary"]
    assert result["sentiment"] in {
        "positive",
        "negative",
        "neutral",
    }
    assert -1.0 <= result["sentiment_score"] <= 1.0
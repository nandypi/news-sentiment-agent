from ..state import NewsState
from ..tools.sentiment import analyze_sentiment


def analyze_article_sentiment(state: NewsState) -> dict:
    """Run sentiment analysis on the article."""

    result = analyze_sentiment.invoke(
        {
            "text": state["article_text"]
        }
    )

    return {
        "sentiment": result["sentiment"],
        "sentiment_score": result["score"],
    }
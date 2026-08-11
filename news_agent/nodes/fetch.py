from ..state import NewsState
from ..tools.news_fetcher import fetch_news


def fetch_article(state: NewsState) -> dict:
    """Fetch article content or use directly provided text."""

    input_text = state["input_text"].strip()

    if input_text.startswith(("http://", "https://")):
        article_text = fetch_news.invoke({"url": input_text})

        return {
            "source_url": input_text,
            "article_text": article_text,
        }

    if len(input_text) < 50:
        raise ValueError(
            "Article text is too short. Provide a valid URL "
            "or meaningful article text."
        )

    return {
        "article_text": input_text,
    }
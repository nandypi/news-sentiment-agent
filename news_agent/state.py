from typing import TypedDict


class NewsState(TypedDict, total=False):
    input_text: str
    source_url: str
    article_text: str
    summary: str
    sentiment: str
    sentiment_score: float
    error: str
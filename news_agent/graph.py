from langgraph.graph import StateGraph, START, END

from .state import NewsState
from .nodes.fetch import fetch_article
from .nodes.summarize import summarize_article
from .nodes.sentiment import analyze_article_sentiment


def build_graph():
    """Build and compile the news analysis LangGraph."""

    builder = StateGraph(NewsState)

    builder.add_node("fetch_article", fetch_article)
    builder.add_node("summarize", summarize_article)
    builder.add_node(
        "analyze_sentiment",
        analyze_article_sentiment,
    )

    builder.add_edge(START, "fetch_article")
    builder.add_edge("fetch_article", "summarize")
    builder.add_edge("summarize", "analyze_sentiment")
    builder.add_edge("analyze_sentiment", END)

    return builder.compile()


graph = build_graph()
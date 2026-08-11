from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from ..state import NewsState


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


def summarize_article(state: NewsState) -> dict:
    """Generate a concise factual summary using Gemini."""

    article = state["article_text"]

    prompt = f"""
You are a professional news summarization assistant.

Summarize the following news article.

Requirements:
- Keep the summary concise.
- Include the main event.
- Mention important people, organizations, numbers,
  or consequences when relevant.
- Preserve the facts from the article.
- Do not invent information.
- Do not express your own opinion.

NEWS ARTICLE:
{article}
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, str):
        summary = response.content
    else:
        summary = "".join(
            block.get("text", "")
            for block in response.content
            if isinstance(block, dict)
        )

    return {
        "summary": summary.strip(),
    }
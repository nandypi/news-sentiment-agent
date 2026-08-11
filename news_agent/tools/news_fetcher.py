import requests
from bs4 import BeautifulSoup
from langchain.tools import tool


@tool
def fetch_news(url: str) -> str:
    """Fetch readable text content from a news article URL."""

    response = requests.get(
        url,
        timeout=15,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
            )
        },
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup(
        ["script", "style", "nav", "footer", "header", "aside"]
    ):
        element.decompose()

    text = soup.get_text(" ", strip=True)

    if not text:
        raise ValueError("No readable content found at the URL.")

    return text
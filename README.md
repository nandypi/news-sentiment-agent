# 📰 LangGraph News Intelligence Agent

A LangGraph-based AI agent for news summarization and
sentiment analysis.

## Overview

Given a news article URL or raw article text, the agent:

1. Fetches and extracts the article content.
2. Generates a concise summary using Google's Gemini LLM.
3. Performs sentiment analysis using a dedicated sentiment tool.
4. Returns a structured analysis containing the summary,
   sentiment, and sentiment score.

## Architecture

![LangGraph Architecture](langgraph.png)

### Workflow

START
↓
Fetch Article
↓
Summarize with Gemini
↓
Analyze Sentiment
↓
END

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
| Agent orchestration | LangGraph |
| LLM framework | LangChain |
| LLM | Google Gemini |
| Web extraction | Requests + BeautifulSoup |
| Sentiment analysis | VADER |
| Data validation | Pydantic |
| Testing | Pytest |

## Features

- URL-based news extraction
- Raw article text support
- LLM-powered summarization
- Tool-based sentiment analysis
- Structured output
- Error handling
- Automated tests
- LangGraph workflow visualization

## Project Structure

```text
news-sentiment-agent/
├── src/
├── tests/
├── examples/
├── main.py
├── requirements.txt
└── README.md
```

## Example

### Input

```text
https://example.com/news-article
```

### Output

{
  "summary": "The CM of Andhra Pradesh is...",
  "sentiment": "positive",
  "sentiment_score": 0.72
}

## Testing

Run the test suite with:

```bash
python -m pytest
```

## Future Improvements

- Support additional news extraction strategies for
  JavaScript-rendered websites.
- Add article metadata extraction.
- Add confidence estimation.
- Add a web interface.
- Support multiple LLM providers.
- Add persistent analysis history.
- Add observability and tracing.

## Limitations

- Some news websites may block automated requests.
- JavaScript-rendered pages may not expose article content
  through a simple HTTP request.
- VADER is a lightweight lexicon-based sentiment analyzer
  and may not capture complex context or sarcasm.
- LLM-generated summaries depend on the quality and length
  of the extracted article content.
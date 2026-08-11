from news_agent.graph import graph


def main():
    print("=" * 60)
    print("       NEWS SUMMARIZATION & SENTIMENT AGENT")
    print("=" * 60)

    print("\nEnter a news article URL or paste article text.")
    print("For multi-line text, type END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    user_input = "\n".join(lines).strip()

    if not user_input:
        print("No input provided.")
        return

    try:
        print("\nAnalyzing article...")

        result = graph.invoke(
            {
                "input_text": user_input,
            }
        )

        print("\n" + "=" * 60)
        print("RESULT")
        print("=" * 60)

        if result.get("source_url"):
            print(f"\nSource: {result['source_url']}")

        print("\nSummary:")
        print(result["summary"])

        print(f"\nSentiment: {result['sentiment']}")
        print(f"Sentiment score: {result['sentiment_score']:.3f}")

        print("\n" + "=" * 60)

    except Exception as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()
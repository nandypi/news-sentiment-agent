from news_agent.graph import graph


png = graph.get_graph().draw_mermaid_png()

with open("langgraph.png", "wb") as file:
    file.write(png)

print("Graph saved to langgraph.png")
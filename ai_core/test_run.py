from ai_core.graph.research_graph import build_research_graph

graph = build_research_graph()

initial_state = {
    "query": "Explain diffusion models in machine learning",
}

final_state = graph.invoke(initial_state)

print("\n===== FINAL ANSWERS =====\n")
for subtask, answer in final_state["answers"].items():
    print(f"\n## {subtask}\n")
    print(answer)

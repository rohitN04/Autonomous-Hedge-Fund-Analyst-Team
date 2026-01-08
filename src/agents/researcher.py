from src.state import AgentState
from langgraph.graph import StateGraph, END
from src.tools.search_tool import SearchTool

searcher = SearchTool()

def search_node(state: AgentState):
    ticker = state['ticker']
    print(f"--- Processing: {ticker} ---")
    news = searcher.run_search(ticker)

    return {"news_data": [news]}

workflow = StateGraph(AgentState)

workflow.add_node("search_agent", search_node)

workflow.set_entry_point("search_agent")

workflow.add_edge("search_agent", END)

app = workflow.compile()

if __name__ == "__main__":
    initial_state = {"ticker": "MSFT", "news_data": [], "stock_data": {}, "final_report": ""}
    results = app.invoke(initial_state)

    print("\n\n################ RESULT ################")
    print(results['news_data'][0])


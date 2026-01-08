from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.tools.finance_tool import FinanceTool

finder = FinanceTool()

def finance_node(state: AgentState):
    ticker = state['ticker']

    stock_str = finder.stock_record_finder(ticker, '5d')

    return {"stock_data": {ticker:stock_str}}

workflow = StateGraph(AgentState)

workflow.add_node("analyse_agent", finance_node)

workflow.set_entry_point("analyse_agent")

workflow.add_edge("analyse_agent", END)

app = workflow.compile()

if __name__ == "__main__":
    initial_state = {"ticker": "MSFT", "news_data": [], "stock_data": {}, "final_report": ""}

    results = app.invoke(initial_state)

    print("\n\n################ RESULT ################")
    print(results['stock_data'][results['ticker']])

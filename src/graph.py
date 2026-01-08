from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.agents.researcher import search_node
from src.agents.analyst import finance_node
from src.agents.writer import stock_analysis

workflow = StateGraph(AgentState)

workflow.add_node("search_node", search_node)
workflow.add_node("finance_node", finance_node)
workflow.add_node("write_analysis", stock_analysis)

workflow.set_entry_point("search_node")
workflow.add_edge("search_node", "finance_node")
workflow.add_edge("finance_node", "write_analysis")
workflow.add_edge("write_analysis", END)

graph = workflow.compile()
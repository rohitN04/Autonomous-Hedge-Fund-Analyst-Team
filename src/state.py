from typing import TypedDict, Any

class AgentState(TypedDict):
    ticker: str
    news_data: list[str]
    stock_data: dict[str, Any]
    final_report: str
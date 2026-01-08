import os
from openai import OpenAI
from dotenv import load_dotenv
from src.state import AgentState
from src.agents.researcher import search_node
from src.agents.analyst import finance_node
from langgraph.graph import StateGraph, END

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def stock_analysis(state: AgentState):

    ticker = state['ticker']
    news = state['news_data'][0] if state['news_data'] else "No news found."
    stock_data = state['stock_data'].get(ticker, ['No data'])

    prompt = f"""
    You are a VP at a prestigious Hedge Fund. Write a professional investment analysis report for {ticker}.
    
    Use the following data:
    1. Recent News: {news}
    2. Stock Price Data: {stock_data}

    Strictly follow this format:
    ## 📊 Investment Report: {ticker}
    ### 📝 Executive Summary
    [Brief summary of the situation]
    
    ### 📉 Key Risks & Opportunities
    [Bullet points based on the news]
    
    ### 🚀 Recommendation
    [Buy/Sell/Hold with reasoning]
    """


    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial analyst. Write using professional Markdown formatting."},
            {"role": "user", "content": prompt}
        ]
    )

    return {"final_report" : response.choices[0].message.content}

workflow = StateGraph(AgentState)

workflow.add_node("search_node", search_node)
workflow.add_node("finance_node", finance_node)
workflow.add_node("write_analysis", stock_analysis)

workflow.set_entry_point("search_node")
workflow.add_edge("search_node", "finance_node")
workflow.add_edge("finance_node", "write_analysis")
workflow.add_edge("write_analysis", END)

app = workflow.compile()

if __name__ == "__main__":
    initial_state = {"ticker": "MSFT", "news_data": [], "stock_data": {}, "final_report": ""}
    results = app.invoke(initial_state)

    print(results['news_data'][0])

    print("\n\n" + "-"*30 + "stock data")
    print(results['stock_data'][results['ticker']])

    print("\n\n" + "#"*40)
    print("FINAL ANALYST REPORT")
    print("#"*40 + "\n")
    print(results['final_report'])


from src.graph import graph
import streamlit as st

st.set_page_config(page_title="Hedge Fund Analyst", page_icon="📈")
st.title("📈 Autonomous Hedge Fund Analyst Team")

with st.sidebar:
    ticker_input = st.text_input('Enter Stock Ticker (e.g., AAPL):", "MSFT"')
    run_btn = st.button("Run Analysis")

if run_btn:
    with st.spinner(f"🤖 Agents are researching {ticker_input}..."):
        try:
            initial_state = {
                "ticker": ticker_input, 
                "news_data": [], 
                "stock_data": {}, 
                "final_report": ""
            }

            results = graph.invoke(initial_state)
            
            st.markdown(results['final_report'])

            with st.expander("See Raw Data"):
                st.write(results['stock_data'])
                st.write(results['news_data'])
        
        except Exception as e:
            st.markdown("Enter a Valid Stock Ticker!!!")
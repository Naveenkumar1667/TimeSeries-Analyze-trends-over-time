import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

# --- Page Setup ---
st.set_page_config(page_title="CRPM Calculator", layout="wide")
st.title("CRPM Beta & Return Calculator")

# --- User Inputs ---
stocks_input = st.text_input("Enter stock tickers (comma separated)", "AAPL,AMZN,TSLA")
stocks = [s.strip().upper() for s in stocks_input.split(",")]
market_ticker = "^GSPC"
risk_free_rate = st.number_input("Risk-free rate (decimal, annual)", 0.01, 0.10, 0.04)
start_date = st.date_input("Start Date", pd.to_datetime("2024-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

if st.button("Calculate CRPM"):
    # --- Fetch market data ---
    market_data = yf.download(market_ticker, start=start_date, end=end_date)['Close']
    market_returns = market_data.pct_change().dropna()
    
    results = []

    for stock_ticker in stocks:
        # --- Fetch stock data ---
        stock_data = yf.download(stock_ticker, start=start_date, end=end_date)['Close']
        stock_returns = stock_data.pct_change().dropna()

        # --- Align dates ---
        combined = pd.concat([stock_returns, market_returns], axis=1).dropna()
        combined.columns = ['Stock', 'Market']

        # --- Calculate Beta ---
        cov_matrix = np.cov(combined['Stock'], combined['Market'])
        beta = cov_matrix[0,1] / cov_matrix[1,1]

        # --- Annualized market return ---
        annual_market_return = combined['Market'].mean() * 252

        # --- CRPM Expected Return ---
        crpm_return = risk_free_rate + beta * (annual_market_return - risk_free_rate)

        # --- Add notifications ---
        if beta > 1.5:
            st.warning(f"⚠️ {stock_ticker} has a high Beta ({beta:.2f}) - higher risk!")
        if crpm_return < risk_free_rate:
            st.warning(f"⚠️ {stock_ticker}'s CRPM Return ({crpm_return:.2%}) is below the risk-free rate ({risk_free_rate:.2%})!")

        results.append({
            'Stock': stock_ticker,
            'CRPM Beta': round(beta, 4),
            'CRPM Return': round(crpm_return, 4)
        })
    
    crpm_df = pd.DataFrame(results)

    # --- Highlight top-performing stock ---
    max_return_stock = crpm_df.loc[crpm_df['CRPM Return'].idxmax(), 'Stock']
    crpm_df['Highlight'] = crpm_df['Stock'].apply(lambda x: x == max_return_stock)

    # --- Display DataFrame with top stock highlighted ---
    st.write("### CRPM Beta & Expected Return")
    def highlight_top(s):
        return ['background-color: yellow' if v else '' for v in s]
    st.dataframe(crpm_df.style.apply(highlight_top, subset=['Highlight']))

    # --- Plot Beta vs CRPM Return ---
    crpm_df['Color'] = crpm_df['Highlight'].apply(lambda x: 'red' if x else 'blue')
    fig = px.scatter(
        crpm_df, x='CRPM Beta', y='CRPM Return', text='Stock',
        color='Color', color_discrete_map={'red':'red','blue':'blue'},
        size=crpm_df['CRPM Return']*100,  # scale marker size for visibility
        title=f"CRPM Beta vs Expected Return (Highest: {max_return_stock})"
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)

    # --- Download Button ---
    csv = crpm_df.drop(columns=['Highlight','Color']).to_csv(index=False)
    st.download_button(
        label="Download CRPM Data as CSV",
        data=csv,
        file_name='crpm_data.csv',
        mime='text/csv'
    )

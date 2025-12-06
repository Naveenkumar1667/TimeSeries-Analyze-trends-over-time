# Stock Analysis & Prediction Platform

## Project Overview

This project is a comprehensive web application designed to provide users with in-depth stock analysis, predictive insights, and financial modeling capabilities. Built using Python and Streamlit, it offers an intuitive interface for exploring historical stock data, visualizing trends with technical indicators, forecasting future prices, and understanding investment risk through the Capital Asset Pricing Model (CAPM).
## Dashboard Screenshot

![Dashboard Screenshot]()
---

## Features

This platform offers a suite of tools for both novice and experienced investors:
**Detailed Stock Information:**
    *   Access real-time company overview, including business summary, sector, number of employees, and official website.
    *   View key financial metrics such as Market Cap, Beta, EPS, PE Ratio, Quick Ratio, Revenue per Share, Profit Margins, Debt to Equity, and Return on Equity.
**Historical Data & Interactive Charts:**
    *   Display the latest 10 days of historical stock data in a clear table format.
    *   Visualize price movements using interactive Candlestick and Line charts.
    *   Filter data by various periods: 5 Days, 1 Month, 6 Months, Year-to-Date, 1 Year, 5 Years, and Max available history.
**Technical Indicators:**
    *   **Relative Strength Index (RSI):** Analyze momentum with overbought/oversold levels.
    *   **Moving Average Convergence Divergence (MACD):** Identify trend changes and momentum.
    *   **Simple Moving Average (SMA 50):** Track price trends over a 50-day period.
**Stock Price Prediction (ARIMA Model):**
    *   Forecast the next 30 days of closing prices based on historical data.
    *   Utilizes an ARIMA (AutoRegressive Integrated Moving Average) model for time series forecasting.
    *   Provides the Root Mean Squared Error (RMSE) score to evaluate model accuracy.
    *   Visualizes historical prices alongside the 30-day future price forecast.
**CAPM Beta & Expected Return Calculator:**
    *   Calculate the Capital Asset Pricing Model (CAPM) Beta for multiple stocks against a market index (S&P 500 by default).
    *   Determine the expected return for each stock based on the CAPM formula, considering a user-defined risk-free rate.
    *   Provides warnings for high Beta stocks or those with expected returns below the risk-free rate.
    *   Interactive scatter plot visualizing Beta vs. Expected Return, highlighting the top-performing stock.
    *   Option to download CAPM data as a CSV file.

## Technologies Used

**Python:** The core programming language for the application logic.
**Streamlit:** For building the interactive web application interface.
**yfinance:** To fetch historical and real-time stock data from Yahoo Finance.
**Pandas:** For data manipulation and analysis.
**Plotly:** For creating interactive and visually appealing charts and tables.
**statsmodels:** For implementing the ARIMA time series forecasting model.
**scikit-learn:** For data scaling (StandardScaler) and model evaluation (mean_squared_error).
**NumPy:** For numerical operations.
**ta (Technical Analysis Library):** For calculating various technical indicators.
**datetime & dateutil:** For date and time manipulations.

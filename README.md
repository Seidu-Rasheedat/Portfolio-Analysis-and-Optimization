# Portfolio Analysis and Optimization

A comprehensive quantitative finance project that applies **Modern Portfolio Theory (MPT)** to analyse, optimise, and visualise an equity portfolio using Python. The project combines financial data analysis, portfolio optimisation, risk analytics, and an interactive Streamlit dashboard to demonstrate practical portfolio management techniques.

---

## Live Dashboard

> **Streamlit App:** *https://portfolio-analysis-optimization-app.streamlit.app/*

---

## Project Report

The complete technical report can be downloaded directly from the Streamlit dashboard or viewed in this repository.

---

# Project Overview

This project analyses a diversified portfolio of U.S. equities using historical market data and evaluates its performance through return and risk metrics. Monte Carlo simulation is then used to generate thousands of random portfolios to identify allocations that maximise risk-adjusted performance while illustrating the Efficient Frontier.

The project demonstrates the complete quantitative investment workflow from raw financial data to portfolio optimisation and interactive visualisation.

---

# Features

- Historical stock price analysis
- Daily return analysis
- Cumulative portfolio performance
- Equal-weighted portfolio construction
- Monte Carlo portfolio optimisation (10,000 simulations)
- Maximum Sharpe Ratio portfolio
- Minimum Volatility portfolio
- Maximum Drawdown analysis
- Rolling 30-Day Annualised Volatility
- Portfolio allocation visualisation
- Performance comparison tables
- Interactive Streamlit dashboard
- Professional Portfolio Analysis report

---

# Dashboard Pages

- Executive Summary
- Performance Analytics
- Risk Analytics
- Portfolio Optimization
- Portfolio Allocation
- Research Report
- About Project

---

# Methodology

The analysis follows a structured quantitative investment process:

1. Historical market data collection
2. Data preprocessing
3. Return computation
4. Portfolio construction
5. Risk measurement
6. Monte Carlo portfolio optimisation
7. Efficient Frontier visualisation
8. Interactive dashboard development

---

# Risk Metrics

The project evaluates portfolio performance using:

- Expected Annual Return
- Annual Volatility
- Sharpe Ratio
- Rolling 30-Day Volatility
- Maximum Drawdown

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- yfinance
- Matplotlib
- Seaborn

---

# Repository Structure

```text
Portfolio-Analysis-and-Optimization/
│
├── Portfolio_dashboard.py
├── Portfolio_Analysis_and_Optimization.ipynb
├── portfolio_data.pkl
├── Portfolio_Analysis_Report.pdf
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# Key Results

- Generated and evaluated **10,000 Monte Carlo portfolios**
- Identified the **Maximum Sharpe Portfolio**
- Identified the **Minimum Volatility Portfolio**
- Demonstrated the improvement achievable through strategic asset allocation
- Developed a fully interactive portfolio analytics dashboard

---

# Portfolio Performance Comparison

The portfolio optimisation process was evaluated by comparing the original equally weighted portfolio against the optimal portfolio identified through **10,000 Monte Carlo simulations**. While the equally weighted portfolio allocates identical weights to every asset, the optimised portfolio strategically reallocates capital to maximise the portfolio's **Sharpe Ratio**, producing superior risk-adjusted performance.

| Metric | Equal-Weighted Portfolio | Optimised Portfolio |
|--------|-------------------------:|--------------------:|
| Expected Annual Return | **23.78%** | **29.53%** |
| Annual Volatility | **21.40%** | **22.60%** |
| Sharpe Ratio | **0.92** | **1.13** |

## Interpretation
The optimisation process increased the portfolio's expected annual return from 23.78% to 29.53%, representing a substantial improvement in potential performance. Although annual volatility increased slightly from 21.40% to 22.60%, the increase in expected return more than compensated for the additional risk.

Most importantly, the portfolio's Sharpe Ratio improved from 0.92 to 1.13, indicating that the optimised portfolio generates significantly more return for each unit of risk assumed. This demonstrates the effectiveness of Modern Portfolio Theory in constructing portfolios that maximise risk-adjusted performance rather than simply pursuing the highest returns.

Overall, the results illustrate how quantitative portfolio optimisation can produce a more efficient allocation of capital than a naïve equal-weighted strategy while maintaining a well-diversified investment portfolio.


---

# Installation

Clone the repository

```bash
git clone https://github.com/Seidu-Rasheedat/Portfolio-Analysis-and-Optimization.git
```

Navigate into the project

```bash
cd Portfolio-Analysis-and-Optimization
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run Portfolio_dashboard.py
```

---

# Future Improvements

- Black-Litterman Portfolio Optimisation
- CAPM Integration
- Value-at-Risk (VaR)
- Conditional Value-at-Risk (CVaR)
- Sector Allocation Analysis
- Real-time Portfolio Updates
- Multi-factor Portfolio Models

---

# Author

**Rasheedat Seidu**

B.Sc. Finance  
University of Lagos

**Quant Foundations Project 1**

---

# References
- Sharpe, W. F. (1966). *Mutual fund performance*
- Markowitz, H. (1952). *Portfolio Selection.*
- Streamlit Documentation
- Pandas Documentation
- NumPy Documentation

---

# Disclaimer

This project was developed solely for **educational, research, and portfolio demonstration purposes** as part of the author's Quant Foundations learning journey.

All portfolio analyses, optimisation results, visualisations, and performance metrics are based on historical market data and should **not** be interpreted as financial, investment, or trading advice. Past performance does not guarantee future results, and actual market conditions may differ significantly from those presented in this project.

The optimisation process employs **Modern Portfolio Theory (MPT)** and Monte Carlo simulation under a set of simplifying assumptions. Real-world portfolio management involves additional considerations such as transaction costs, taxes, liquidity constraints, market impact, and changing economic conditions, which are beyond the scope of this analysis.

Users should conduct their own independent research and, where appropriate, seek advice from qualified financial professionals before making investment decisions.

---

# License

This project is licensed under the MIT License.
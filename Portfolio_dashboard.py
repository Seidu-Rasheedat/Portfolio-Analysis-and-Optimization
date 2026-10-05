import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle


# Page Configuration

st.set_page_config(
    page_title="Portfolio Analysis & Optimization",
    layout="wide",
    initial_sidebar_state="expanded"
)





# Load Saved Portfolio Data

with open("portfolio_data.pkl", "rb") as Portfolio_data:
    data = pickle.load(Portfolio_data)

portfolio_returns = data["portfolio_returns"]
portfolio_cumulative = data["portfolio_cumulative"]

rolling_volatility = data["rolling_volatility"]
drawdown = data["drawdown"]

best_weights = data["best_weights"]
simulation_results = data["simulation_results"]

expected_return = data["expected_return"]
portfolio_volatility = data["portfolio_volatility"]
sharpe_ratio = data["sharpe_ratio"]
equal_weighted_portfolio = data["equal_weighted_portfolio"]
equal_return = equal_weighted_portfolio.loc[
    equal_weighted_portfolio["Metric"] == "Expected Annual Return",
    "Value"
].iloc[0]

equal_volatility = equal_weighted_portfolio.loc[
    equal_weighted_portfolio["Metric"] == "Annual Volatility",
    "Value"
].iloc[0]

equal_sharpe = equal_weighted_portfolio.loc[
    equal_weighted_portfolio["Metric"] == "Sharpe Ratio",
    "Value"
].iloc[0]

max_drawdown = data["max_drawdown"]

max_sharpe = data["max_sharpe"]
min_volatility = data["min_volatility"]
optimized_portfolio = data["optimized_portfolio"]
opt_return = optimized_portfolio.loc[
    optimized_portfolio["Metric"] == "Expected Annual Return",
    "Value"
].iloc[0]

opt_volatility = optimized_portfolio.loc[
    optimized_portfolio["Metric"] == "Annual Volatility",
    "Value"
].iloc[0]

opt_sharpe = optimized_portfolio.loc[
    optimized_portfolio["Metric"] == "Sharpe Ratio",
    "Value"
].iloc[0]


# Sidebar

st.sidebar.markdown(
    """
    ## PORTFOLIO ANALYSIS & OPTIMIZATION

    Historical quantitative portfolio analysis
    """
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Performance Analytics",
        "Risk Analytics",
        "Portfolio Optimization",
        "Investment Portfolio",
        "Research Report",
        "About the Project"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.caption("30 U.S. Equities  •  2020–2024")
st.sidebar.caption("Modern Portfolio Theory  •  Monte Carlo")
st.sidebar.caption("Python  •  Plotly  •  Streamlit")





# Overview

if page == "Overview":

    st.title("Portfolio Analysis & Optimization")

    st.caption(
    "This dashboard examines the historical performance, risk, and "
    "portfolio characteristics of 30 U.S. equities from 2020 to 2024. "
    "It combines portfolio analytics with Modern Portfolio Theory to "
    "evaluate how diversification and portfolio allocation influence "
    "the return-risk trade-off."
)

    st.divider()

    # Portfolio Snapshot

    st.subheader("Portfolio Snapshot")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Assets",
            "30",
            "U.S. equities"
        )

    with col2:
        st.metric(
            "Sectors",
            "7",
            "Diversified exposure"
        )

    with col3:
        st.metric(
            "Trading Days",
            "1,258",
            "Historical observations"
        )

    with col4:
        st.metric(
            "Study Period",
            "2020–2024",
            "5-year analysis"
        )

    st.divider()

    # Portfolio Performance

    st.subheader("Portfolio Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Annual Return",
            f"{expected_return:.2%}"
        )

    with col2:
        st.metric(
            "Annual Volatility",
            f"{portfolio_volatility:.2%}"
        )

    with col3:
        st.metric(
            "Sharpe Ratio",
            f"{sharpe_ratio:.2f}"
        )

    with col4:
        st.metric(
            "Maximum Drawdown",
            f"{max_drawdown:.2%}"
        )

    st.divider()

    # Portfolio Growth

    st.subheader("Portfolio Growth")

    fig = px.line(
        x=portfolio_cumulative.index,
        y=portfolio_cumulative.values,
        labels={
            "x": "Date",
            "y": "Growth of $1"
        }
    )

    fig.update_layout(
        title="Growth of $1 Invested",
        hovermode="x unified",
        xaxis=dict(
            dtick="M12",
            tickformat="%Y"
        ),
        yaxis=dict(
            showgrid=False
        ),
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # Analytical Framework

    st.header("Analytical Framework")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Portfolio Construction")

        st.write(
            """
            The portfolio begins with an equal-weight allocation across
            30 U.S. equities. Each constituent receives approximately
            3.33% of the portfolio.
            """
        )

    with col2:

        st.markdown("### Quantitative Analysis")

        st.write(
            """
            The analysis evaluates historical performance, volatility,
            drawdown and risk-adjusted returns before applying Monte Carlo
            simulation to identify more efficient portfolio allocations.
            """
        )

    st.divider()

    # Key Takeaway

    st.subheader("Key Takeaway")

    st.write(
        f"""
        The equal-weighted portfolio generated an annualised return of
        **{expected_return:.2%}** with **{portfolio_volatility:.2%}**
        annualised volatility and a **{sharpe_ratio:.2f} Sharpe Ratio**.
        The historical maximum drawdown was **{max_drawdown:.2%}**.

        The optimisation analysis extends this baseline by examining
        thousands of alternative allocations and evaluating how portfolio
        weighting affects the return-risk trade-off.
        """
    )





# Performance Analytics

if page == "Performance Analytics":

    st.title("Performance Analytics")

    st.caption(
        "This section evaluates how the portfolio performed over the study "
        "period, focusing on cumulative growth, annualised returns, and the "
        "contribution of individual equities to overall portfolio performance. "
        "The analysis provides a historical baseline for understanding the "
        "portfolio before assessing its risk and optimisation characteristics."
    )

    st.divider()

    performance_view = st.selectbox(

        "Select Performance View",

        [

            "Portfolio Growth",
            "Daily Portfolio Returns"

        ]

    )


    if performance_view == "Portfolio Growth":

        fig = px.line(

            x=portfolio_cumulative.index,
            y=portfolio_cumulative.values,

            labels={
                "x":"Date",
                "y":"Growth of $1"
            }

        )

        fig.update_layout(

            title="Cumulative Portfolio Growth",

            hovermode="x unified",

            template="plotly_white"
,
            xaxis=dict(dtick="M12", tickformat="%Y"),

            yaxis=dict(showgrid=False)
        )

        fig.update_traces(
            hovertemplate=
            "<b>%{x|%d %b %Y}</b><br>"
            "Growth of $1: $%{y:.2f}"
            "<extra></extra>"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        st.divider()

        st.subheader("Interpretation")

        st.write(
        """
The cumulative growth curve illustrates how a hypothetical one-dollar investment
would have evolved over the analysis period after accounting for the portfolio's
daily returns.

Periods of sustained upward movement indicate consistent portfolio appreciation,
while temporary declines correspond to periods of market stress, most notably
during the COVID-19 market disruption in early 2020.

Overall, the long-term upward trajectory demonstrates that despite experiencing
short-term volatility, the diversified portfolio generated positive cumulative
wealth over the five-year investment horizon.
"""
        )

    

    elif performance_view == "Daily Portfolio Returns":

        fig = px.line(

            x=portfolio_returns.index,
            y=portfolio_returns.values,

            labels={
                "x":"Date",
                "y":"Daily Return"
            }

        )

        fig.update_layout(

            title="Daily Portfolio Returns",

            hovermode="x unified",

            template="plotly_white",

            xaxis=dict(dtick="M12", tickformat="%Y"),

            yaxis=dict(showgrid=False)


        )

        fig.update_traces(
            hovertemplate=
            "<b>%{x|%d %b %Y}</b><br>"
            "Daily Return: %{y:.2%}"
            "<extra></extra>"
        )


        st.plotly_chart(

            fig,

            width="stretch"

        )

        st.divider()

        st.subheader("Interpretation")

        st.write(
        """
Daily portfolio returns fluctuate around zero, reflecting the normal day-to-day
movement of financial markets.

While most observations remain relatively small, several larger positive and
negative movements are visible during periods of heightened market uncertainty.
These fluctuations collectively determine the portfolio's long-term cumulative
performance and provide the foundation for subsequent risk measures such as
volatility, drawdown, and the Sharpe Ratio.
"""
        )


# Risk Analytics

if page == "Risk Analytics":

    st.title("Risk Analytics")

    st.caption(
    "This section examines the risk characteristics of the portfolio using "
    "volatility, drawdowns, and rolling risk measures. The objective is to "
    "understand not only how much the portfolio returned, but also the "
    "magnitude and behaviour of the risks taken to achieve those returns."
)

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "Rolling Volatility",
            "Maximum Drawdown"
        ]
    )

    
    # Rolling Volatility

    with tab1:

        fig = px.line(

            x=rolling_volatility.index,
            y=rolling_volatility.values,

            labels={
                "x":"Date",
                "y":"Annualised Volatility"
            }

        )

        fig.update_layout(

            template="plotly_white",

            hovermode="x unified",

            title="30-Day Rolling Portfolio Volatility",

            xaxis=dict(dtick="M12", tickformat="%Y"),

            yaxis=dict(showgrid=False)
        )

        fig.update_traces(
            line=dict(color="firebrick", width=2.5)
        )

        fig.update_traces(
            hovertemplate=
            "<b>%{x|%d %b %Y}</b><br>"
            "Annualised Volatility: %{y:.2%}"
            "<extra></extra>"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("---")
            col1.metric(
            "◉ Average",
            "18.10%"
            )
            st.markdown("---")
        with col2:
            st.markdown("---")
            col2.metric(
            "▲ Highest",
            "85.03%"
            )
            st.markdown("---")
        with col3:
            st.markdown("---")
            col3.metric(
            "▼ Lowest",
            "6.42%"
            )
            st.markdown("---")

        st.divider()
        st.subheader("Interpretation")

        st.write(
            """
            Rolling volatility measures how portfolio risk changes through time by
            calculating annualised volatility over a moving 30-day window.

            A 30-day window was intentionally selected because it provides sufficient
            detail to capture short-term market events while still smoothing out daily
            market noise. This makes it particularly effective for identifying periods
            of elevated uncertainty, including the COVID-19 market crash.

            The portfolio maintained an average annualised volatility of approximately
            18.10%, indicating relatively moderate long-term risk. During periods of
            market disruption, volatility increased dramatically, reaching a maximum
            of approximately 85.03%, reflecting the extreme uncertainty experienced
            during early 2020.

            Conversely, the minimum rolling volatility of approximately 6.42% occurred
            during periods of relatively stable market conditions when price movements
            became considerably less volatile.

            Overall, the chart demonstrates that portfolio risk was dynamic rather than
            constant, highlighting how external economic events can substantially alter
            market behaviour over relatively short periods.
            """
                    )

        st.info(
            "Key Insight: The largest spike in rolling volatility coincides with "
            "the COVID-19 market crash, illustrating how systemic events can "
            "temporarily increase portfolio risk far beyond its long-term average."
        )

   
    # Drawdown
    
    with tab2:

        fig = go.Figure()

        fig.add_trace(

            go.Scatter(

                x=drawdown.index,

                y=drawdown,

                fill="tozeroy",

                name="Drawdown"

            )

        )

        fig.update_layout(

            template="plotly_white",

            hovermode="x unified",

            title="Historical Portfolio Drawdown",

            xaxis=dict(dtick="M12", tickformat="%Y"),

            yaxis=dict(showgrid=False)

        )

        fig.update_traces(
            line=dict(color="firebrick", width=2.5),
            fill="tozeroy",
            fillcolor="rgba(178,34,34,0.20)"
        )

        fig.update_traces(
        hovertemplate=
            "<b>%{x|%d %b %Y}</b><br>"
            "Drawdown: %{y:.2%}"
            "<extra></extra>"
        )

        st.plotly_chart(

            fig,

            width="stretch"

        )
        st.divider()
        st.subheader("Interpretation")

        st.write(
        f"""
            Drawdown measures the percentage decline from the portfolio's previous peak
            value and represents one of the most widely used measures of downside risk
            within portfolio management.

            The portfolio experienced a maximum drawdown of **{max_drawdown:.2%}**,
            indicating that at its worst point the portfolio lost approximately one-third
            of its value relative to its previous peak before subsequently recovering.

            The deepest decline occurred during the COVID-19 market crisis, a period
            characterised by unprecedented uncertainty, widespread market sell-offs,
            and heightened investor risk aversion.

            Despite this substantial temporary decline, the portfolio gradually recovered
            as financial markets stabilised, demonstrating the resilience of a diversified
            portfolio over longer investment horizons.

            Unlike volatility, which measures fluctuations in returns, drawdown captures
            the actual magnitude of losses experienced by an investor, making it an
            important complement to traditional risk measures.
            """
        )

        st.warning(
            "Key Insight: Although the portfolio suffered a significant drawdown "
            "during the COVID-19 crisis, it successfully recovered over the "
            "remaining investment horizon, reinforcing the importance of "
            "maintaining a long-term investment perspective."
        )





# Portfolio Optimization

if page == "Portfolio Optimization":

    st.title("Portfolio Optimization")

    st.caption(
    "This section applies Modern Portfolio Theory through Monte Carlo "
    "simulation to evaluate 10,000 alternative portfolio allocations. "
    "The analysis explores the relationship between expected return and "
    "risk and identifies allocations that offer stronger risk-adjusted "
    "performance within the simulated portfolio set."
    )
    
    st.divider()


    
    # Monte Carlo Scatter Plot
    
    fig = px.scatter(

        simulation_results,

        x="Volatility",

        y="Return",

        color="Sharpe Ratio",

        color_continuous_scale="Blues",

        hover_data={
            "Return":":.2%",
            "Volatility":":.2%",
            "Sharpe Ratio":":.2f"
        }
    )

    # Maximum Sharpe

    fig.add_trace(

        go.Scatter(

            x=[max_sharpe["Volatility"]],

            y=[max_sharpe["Return"]],

            mode="markers",

            marker=dict(

                size=18,

                color="gold",

                symbol="star"

            ),

            name="Maximum Sharpe Portfolio",
            hovertemplate=
            "<b>Maximum Sharpe Portfolio</b><br>"
            "Annual Volatility: %{x:.2%}<br>"
            "Expected Return: %{y:.2%}<br>"
            f"Sharpe Ratio: {max_sharpe['Sharpe Ratio']:.2f}"
            "<extra></extra>"
            )

        )

    # Minimum Volatility

    fig.add_trace(

        go.Scatter(

            x=[min_volatility["Volatility"]],

            y=[min_volatility["Return"]],

            mode="markers",

            marker=dict(

                size=18,

                color="red",

                symbol="diamond"

            ),

            name="Minimum Volatility Portfolio",
            hovertemplate=
            "<b>Minimum Volatility Portfolio</b><br>"
            "Annual Volatility: %{x:.2%}<br>"
            "Expected Return: %{y:.2%}<br>"
            f"Sharpe Ratio: {min_volatility['Sharpe Ratio']:.2f}"
            "<extra></extra>"

        )

    )

    fig.update_layout(

    title="Efficient Frontier with Monte Carlo Portfolio Simulation",

    template="plotly_white",

    hovermode="closest",

    legend=dict(
    orientation="h",
    y=1.08,
    x=0.5,
    xanchor="center"
),
    xaxis=dict(showgrid=False),

    yaxis=dict(showgrid=False)

)

    fig.update_coloraxes(

    colorbar=dict(

        title="Sharpe Ratio",

        y=0.35,

        len=0.60

    )

)

    st.plotly_chart(

    fig,

    width="stretch"

)

    st.divider()

   
    # Portfolio Comparison
    
    st.subheader("Optimal Portfolio Comparison")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Maximum Sharpe Portfolio")
        st.markdown("---")
        c1,c2,c3 = st.columns(3)

        c1.metric(

            "↗ Expected Return",

            f"{max_sharpe['Return']:.2%}"

        )

        c2.metric(

            "⚠ Annual Volatility",

            f"{max_sharpe['Volatility']:.2%}"

        )

        c3.metric(

            "★ Sharpe ratio",

            f"{max_sharpe['Sharpe Ratio']:.2f}"

        )
        st.markdown("---")

    with col2:

        st.markdown("### Minimum Volatility Portfolio")
        st.markdown("---")
        c1,c2,c3 = st.columns(3)

        c1.metric(

            "↗ Expected Return",

            f"{min_volatility['Return']:.2%}"

        )

        c2.metric(

            "⚠ Annual Volatility",

            f"{min_volatility['Volatility']:.2%}"

        )

        c3.metric(

            "★ Sharpe ratio",

            f"{min_volatility['Sharpe Ratio']:.2f}"

        )
        st.markdown("---")

    st.divider()

    st.subheader("Portfolio Improvement Comparison")

    c1, c2, c3 = st.columns(3)

    c1.metric(
    "↗ Expected Return",
    f"{opt_return:.2%}",
    delta=f"{opt_return - equal_return:.2%}"
)

    c2.metric(
    "⚠ Annual Volatility",
    f"{opt_volatility:.2%}",
    delta=f"{opt_volatility - equal_volatility:.2%}",
    delta_color="inverse"
)

    c3.metric(
    "★ Sharpe Ratio",
    f"{opt_sharpe:.2f}",
    delta=f"{opt_sharpe - equal_sharpe:.2f}"
)
    comparison = pd.DataFrame({

        "Metric": [
            "Expected Annual Return",
            "Annual Volatility",
            "Sharpe Ratio"
        ],

        "Original Portfolio": [
            equal_return,
            equal_volatility,
            equal_sharpe
        ],

        "Optimised Portfolio": [
            opt_return,
            opt_volatility,
            opt_sharpe
        ],

        "Metric Change": [
            opt_return - equal_return,
            opt_volatility - equal_volatility,
            opt_sharpe - equal_sharpe
        ]

    })

    comparison["Original Portfolio"] = [
    f"{equal_return:.2%}",
    f"{equal_volatility:.2%}",
    f"{equal_sharpe:.2f}"
]

    comparison["Optimised Portfolio"] = [
    f"{opt_return:.2%}",
    f"{opt_volatility:.2%}",
    f"{opt_sharpe:.2f}"
]

    comparison["Metric Change"] = [
    f"{opt_return-equal_return:+.2%}",
    f"{opt_volatility-equal_volatility:+.2%}",
    f"{opt_sharpe-equal_sharpe:+.2f}"
]

    st.subheader("Portfolio Performance Comparison")

    st.dataframe(
    comparison,
    hide_index=True,
    width="stretch"
)
    st.divider()

    # Best Allocation Preview

    st.subheader("Top Portfolio Holdings")

    top10 = (
        best_weights
        .sort_values(ascending=False)
        .head(10)
        .rename("Portfolio Weight")
        .reset_index()
        )

    top10.columns = [
        "Ticker",
        "Portfolio Weight"
        ]

    st.dataframe(
        top10.style.format({
        "Portfolio Weight": "{:.2f}%"
            }),
        width="stretch",
        hide_index=True
        )

    st.divider()

    # Interpretation
    
    st.subheader("Interpretation")
    
    st.write(
            f"""
        The Monte Carlo simulation demonstrates how different portfolio weight
        allocations influence the relationship between expected return and
        investment risk.
    
        Among the **10,000 simulated portfolios**, the Maximum Sharpe portfolio
        achieved an expected annual return of **{max_sharpe['Return']:.2%}**
        with an annual volatility of **{max_sharpe['Volatility']:.2%}**,
        producing the highest Sharpe Ratio of **{max_sharpe['Sharpe Ratio']:.2f}**.
    
        Compared with the original equally weighted portfolio
        (Expected Return = **{expected_return:.2%}**,
        Volatility = **{portfolio_volatility:.2%}**,
        Sharpe Ratio = **{sharpe_ratio:.2f}**),
        the optimised portfolio generated both a higher expected return and
        superior risk-adjusted performance, illustrating the benefits of
        portfolio optimisation.
    
        The Minimum Volatility portfolio followed a different objective by
        minimising overall investment risk. Although this resulted in a lower
        expected return, it also substantially reduced portfolio volatility,
        making it a more conservative investment alternative.
    
        These findings demonstrate one of the central principles of Modern
        Portfolio Theory: portfolio construction is not solely about maximising
        returns, but about identifying the most efficient balance between
        return and risk.
        """
        )
    
    st.success(
            "Key Insight: Portfolio optimisation improved the portfolio's "
            "risk-adjusted performance beyond that of the original equally "
            "weighted allocation, demonstrating the value of strategic asset "
            "allocation."
    )





# Investment Portfolio

if page == "Investment Portfolio":

    st.title("Investment Portfolio")

    st.caption(
    "This section translates the portfolio's historical performance into "
    "an investment perspective. It shows how an initial investment would "
    "have changed over the study period and allows different starting "
    "amounts to be tested against the same historical portfolio returns."
    )

    st.divider()

    # Featured Investment Scenario

    st.subheader("Historical Investment Scenario")

    st.caption(
    "Illustrative historical outcome: how a $100,000 investment would "
    "have grown if invested at the beginning of the study period."
)

    featured_investment = 100000

    featured_values = featured_investment * portfolio_cumulative
    featured_ending_value = featured_values.iloc[-1]
    featured_gain = featured_ending_value - featured_investment
    featured_return = (featured_ending_value / featured_investment) - 1

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Initial Investment",
            f"${featured_investment:,.0f}"
        )

    with col2:
        st.metric(
            "Ending Value",
            f"${featured_ending_value:,.0f}"
        )

    with col3:
        st.metric(
            "Total Return",
            f"{featured_return:.2%}"
        )

    st.caption(
        f"Historical outcome over the study period, "
        f"1 January 2020 to 1 January 2025."
    )

    fig = px.line(
        x=featured_values.index,
        y=featured_values.values,
        labels={
            "x": "Date",
            "y": "Portfolio Value ($)"
        }
    )

    fig.update_layout(
        title="Historical Growth of $100,000",
        hovermode="x unified",
        xaxis=dict(
            dtick="M12",
            tickformat="%Y"
        ),
        yaxis=dict(
            tickprefix="$",
            tickformat=",.0f",
            showgrid=False
        ),
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # Investment Simulator

    st.header("Investment Simulator")

    st.write(
        "Enter an initial investment to see how the portfolio would "
        "have performed historically."
    )

    investment = st.number_input(
        "Initial Investment ($)",
        min_value=100.0,
        value=10000.0,
        step=1000.0
    )

    if st.button("Simulate Investment"):

        simulated_values = investment * portfolio_cumulative
        ending_value = simulated_values.iloc[-1]
        gain = ending_value - investment
        total_return = (ending_value / investment) - 1

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Initial Investment",
                f"${investment:,.0f}"
            )

        with col2:
            st.metric(
                "Ending Value",
                f"${ending_value:,.0f}"
            )

        with col3:
            st.metric(
                "Gain / Loss",
                f"${gain:,.0f}",
                f"{total_return:.2%}"
            )

        simulator_fig = px.line(
            x=simulated_values.index,
            y=simulated_values.values,
            labels={
                "x": "Date",
                "y": "Portfolio Value ($)"
            }
        )

        simulator_fig.update_layout(
            title=f"Historical Growth of ${investment:,.0f}",
            hovermode="x unified",
            xaxis=dict(
                dtick="M12",
                tickformat="%Y"
            ),
            yaxis=dict(
                tickprefix="$",
                tickformat=",.0f",
                showgrid=False
            ),
            height=420
        )

        st.plotly_chart(
            simulator_fig,
            use_container_width=True
        )
    st.divider()





# Research Report


if page == "Research Report":

    st.title("Portfolio Research Report")

    st.caption(
    "The accompanying research report documents the methodology and "
    "reasoning behind the portfolio analysis. It provides additional "
    "context for the data, portfolio construction, performance and risk "
    "measures, Monte Carlo optimisation, and the interpretation of the "
    "results presented throughout this dashboard."
    )

    st.divider()

    st.subheader("Report Contents")

    st.markdown("""

- Executive Summary

- Research Objectives

- Data Collection & Methodology

- Portfolio Construction

- Correlation Analysis

- Return Analysis

- Risk Analysis

- Portfolio Optimisation

- Results & Discussion

- Conclusions

- References

""")

    st.divider()

    st.subheader("Project Report")

    st.write(
    "Download the complete portfolio analysis report in PDF format."
    )

    with open("Portfolio_Analysis_Report.pdf", "rb") as pdf_file:
        st.download_button(
            label="Download Full Report (PDF)",
            data=pdf_file,
            file_name="Portfolio_Analysis_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )





# About Project

if page == "About the Project":

    st.title("About the Project")

    st.caption(
    "This project is an end-to-end quantitative portfolio analysis built "
    "to examine how a diversified portfolio of 30 U.S. equities performed "
    "over the 2020–2024 study period. The analysis begins with historical "
    "market data and an equal-weight portfolio, then evaluates portfolio "
    "returns, volatility, drawdowns, rolling risk, and risk-adjusted "
    "performance to understand the relationship between return and risk. "
    "The project then applies Modern Portfolio Theory and Monte Carlo "
    "simulation to generate and evaluate 10,000 alternative portfolio "
    "allocations, allowing the historical equal-weight portfolio to be "
    "compared with portfolios designed around different risk-return "
    "objectives. The dashboard brings these analyses together in an "
    "interactive format, while the accompanying research report provides "
    "the methodology, calculations, findings, and interpretation behind "
    "the results."
    )

   
    st.divider()

    st.subheader("Quantitative Approach")

    st.markdown("""

- Historical Return Analysis

- Correlation & Diversification Analysis

- Portfolio Performance Analysis

- Volatility & Rolling Risk Analysis

- Maximum Drawdown Analysis

- Risk-Adjusted Performance (Sharpe Ratio)

- Monte Carlo Portfolio Simulation

- Portfolio Optimization & Allocation

""")

    st.divider()

    st.subheader("Technology Stack")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""

**Programming**

- Python

- Jupyter Notebook

- Streamlit

""")

    with col2:

        st.markdown("""

**Libraries**

- pandas

- NumPy

- yfinance

- Plotly

- Matplotlib

""")
    
    st.divider()

    st.caption(
        "Developed by Rasheedat Seidu | University of Lagos | B.Sc. Finance"
    )



import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle


# Page Configuration


st.set_page_config(
    page_title="Portfolio Analytics Dashboard",
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

st.sidebar.title("Portfolio Analytics Dashboard")

st.sidebar.write(
"""
This dashboard presents an end-to-end quantitative portfolio analysis of
30 large-cap U.S. equities between **2020 and 2025**.

The project evaluates portfolio performance,
risk characteristics,
diversification,
and portfolio optimisation using Modern Portfolio Theory.
"""
)

st.sidebar.divider()

page = st.sidebar.radio(

    "Navigation",

    [

        "Executive Summary",

        "Performance Analytics",

        "Risk Analytics",

        "Portfolio Optimization",

        "Portfolio Allocation",

        "Research Report",

        "About Project"
    ],
    label_visibility="collapsed"

)

st.sidebar.divider()

st.sidebar.caption("Developed using Python, Plotly and Streamlit")


# Executive Summary

if page == "Executive Summary":

    st.title("Portfolio Analytics Dashboard")

    st.caption(
        "An end-to-end quantitative portfolio analysis of an equally weighted portfolio "
        "comprising 30 U.S. large-cap equities over the period 2020–2025."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("---")

        st.metric(
            label="↗ Expected Annual Return",
            value=f"{expected_return:.2%}"
)

        st.markdown("---")

    with col2:
        st.markdown("---")

        st.metric(
            label="⚠ Annual Volatility",
            value=f"{portfolio_volatility:.2%}"
        )

        st.markdown("---")

    with col3:
        st.markdown("---")

        st.metric(
            label="★ Sharpe Ratio",
            value=f"{sharpe_ratio:.2f}"
        )

        st.markdown("---")

    with col4:
        st.markdown("---")

        st.metric(
            label="↓ Maximum Drawdown",
            value=f"{max_drawdown:.2%}"
        )

        st.markdown("---")

    st.divider()

    st.subheader("Executive Summary")

    st.write(
        """
This dashboard presents the findings of a comprehensive portfolio analytics project
conducted on an equally weighted portfolio of thirty U.S. equities.

The analysis follows a complete quantitative investment workflow, beginning with
historical price collection before progressing through return estimation,
risk measurement, portfolio construction, optimisation using Monte Carlo
simulation, and performance evaluation.

Rather than serving as an investment recommendation, the project demonstrates how
financial data can be transformed into meaningful portfolio insights through
Python and Modern Portfolio Theory.
"""
    )

    st.divider()

    st.subheader("Key Findings")

    findings = [
        f"Historical annual return was estimated at **{expected_return:.2%}**.",
        f"The portfolio exhibited an annualised volatility of **{portfolio_volatility:.2%}**.",
        f"A Sharpe Ratio of **{sharpe_ratio:.2f}** suggests moderate risk-adjusted performance.",
        f"The maximum historical drawdown reached **{max_drawdown:.2%}**, largely driven by the COVID-19 market crash.",
        "Monte Carlo optimisation identified portfolios capable of improving the return-risk trade-off.",
        "Interactive visualisations throughout this dashboard allow further exploration of portfolio behaviour."
    ]

    for item in findings:
        st.success(item)

    st.divider()

    st.info(
        "Use the navigation panel on the left to explore portfolio performance, "
        "risk analysis, optimisation results, allocation decisions, and the "
        "underlying research methodology."
    )


# Performance Analytics


if page == "Performance Analytics":

    st.title("Performance Analytics")

    st.write(
        """
Explore how the portfolio evolved throughout the five-year investment period.
The visualisations below provide insight into cumulative portfolio growth and
daily portfolio return behaviour.
"""
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

    st.write(
        """
Understanding portfolio risk is just as important as measuring returns.
        The analyses below examine how portfolio risk evolved over time and
        quantify the magnitude of losses experienced during adverse market
        conditions.
        """
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

    st.write(
        """
        Monte Carlo simulation was used to generate 10,000 random portfolio allocations.
        Each simulated portfolio was evaluated based on its expected annual return,
        annual volatility and Sharpe Ratio, allowing the identification of optimal
        portfolios under different investment objectives.
        """
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


# Portfolio Allocation


if page == "Portfolio Allocation":

    st.title("Portfolio Allocation")

    st.write(
        """
Portfolio allocation represents the proportion of total capital invested
across individual securities.

The visualisations below present the optimal portfolio allocation obtained
from the Monte Carlo optimisation process, highlighting the largest holdings
and illustrating how capital is distributed across the portfolio.
"""
    )

    st.divider()

    allocation_view = st.radio(

    "Select Allocation View",

    [

        "Sunburst Chart",

        "Treemap",

        "Top 10 Holdings"

    ],

    horizontal=True

)


# Sunburst Chart


    if allocation_view == "Sunburst Chart":

        sunburst_df = (

        best_weights
        .sort_values(ascending=False)
        .reset_index()

    )

        sunburst_df.columns = [

        "Ticker",

        "Weight"

    ]

        sunburst_df["Portfolio"] = "Optimal Portfolio"

        fig = px.sunburst(

        sunburst_df,

        path=["Portfolio", "Ticker"],

        values=best_weights.values,

        color=best_weights.values,

        color_continuous_scale="Blues"

    )
        fig.update_traces(
        hovertemplate=
        "<b>Ticker:</b> %{label}<br>"
        "<b>Portfolio Weight:</b> %{value:.2f}%"
        "<extra></extra>"
    )

        fig.update_layout(

        template="plotly_white",

        title="Optimal Portfolio Allocation"
    )

        fig.update_coloraxes(
        
            colorbar=dict(
        
                title="Weight(%)",
        
                y=0.35,
        
                len=0.95
        
            )
        
        )
        

        st.plotly_chart(

        fig,

        width="stretch"

    )


    
    # Treemap
   
    elif allocation_view == "Treemap":

        fig = px.treemap(

            names=best_weights.index,

            parents=[""] * len(best_weights),

            values=best_weights.values,

            color=best_weights.values,

            color_continuous_scale="Blues"

        )

        fig.update_traces(
        hovertemplate=
        "<b>Ticker:</b> %{label}<br>"
        "<b>Portfolio Weight:</b> %{value:.2f}%"
        "<extra></extra>"

        )

        fig.update_layout(

            template="plotly_white"

        )

        fig.update_coloraxes(
        
            colorbar=dict(
        
                title="Weight(%)",
        
                y=0.35,
        
                len=0.95
        
            )
        
        )
        

        st.plotly_chart(

            fig,

            width="stretch"

        )

   
    # Bar Chart
   
    else:

        top10 = (

            best_weights

            .sort_values(ascending=False)

            .head(10)

            .reset_index()

        )

        top10.columns = [

            "Ticker",

            "Weight"

        ]

        fig = px.bar(

            top10,

            x="Weight",

            y="Ticker",

            orientation="h",

            text="Weight",

            color="Weight",

            color_continuous_scale="Blues"

        )

        fig.update_traces(
        texttemplate="%{text:.2f}%",
        hovertemplate=
        "<b>Ticker:</b> %{y}<br>"
        "<b>Portfolio Weight:</b> %{x:.2f}%"
        "<extra></extra>"
        )

        fig.update_layout(

            template="plotly_white",

            title="Top 10 Portfolio Holdings"

        )

        fig.update_coloraxes(
        
            colorbar=dict(
        
                title="Weight(%)",
        
                y=0.35,
        
                len=0.95
        
            )
        
        )
        

        st.plotly_chart(

            fig,

            width="stretch"

        )

    st.divider()

    # Portfolio Holdings
    
    st.subheader("Portfolio Holdings")

    holdings = (
    best_weights
    .sort_values(ascending=False)
    .rename("Portfolio Weight")
    .reset_index()
)

    holdings.columns = [
    "Ticker",
    "Portfolio Weight"
]

    st.dataframe(
    holdings.style.format({
        "Portfolio Weight": "{:.2f}%"
    }),
    width="stretch",
    hide_index=True
)
    

    st.divider()

    st.subheader("Interpretation")

    st.write(
        """
    The optimised portfolio demonstrates a diversified allocation across
    multiple sectors and industries rather than concentrating capital in a
    small number of securities.

    Although several companies receive relatively larger allocations,
    no single stock dominates the portfolio, helping to reduce
    concentration risk while allowing the optimisation process to allocate
    more capital to securities that improve the portfolio's overall
    risk-return profile.

    Interactive allocation visualisations make it easier to understand how
    capital has been distributed throughout the portfolio and identify the
    largest contributors to expected performance.

    Overall, the allocation reflects one of the central principles of Modern
    Portfolio Theory: diversification. Rather than attempting to maximise
    returns through a single investment, the optimisation process seeks the
    most efficient combination of assets capable of improving the portfolio's
    overall risk-adjusted performance.
    """
        )

    st.success(
            "Key Insight: The optimised portfolio remains well diversified despite "
            "favouring higher-performing securities, illustrating how effective "
            "asset allocation can improve portfolio efficiency without excessive "
            "concentration."
        )


# Research Report


if page == "Research Report":

    st.title("Portfolio Research Report")

    st.write(
        """
This dashboard accompanies a comprehensive portfolio research report
documenting the methodology, analytical techniques, findings, and
conclusions derived from this quantitative portfolio analysis.

The report will provide a detailed explanation of the complete workflow,
from data collection and preprocessing through portfolio optimisation,
risk analysis, and performance evaluation.
"""
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


if page == "About Project":

    st.title("About Project")

    st.write(
        """
This project presents an end-to-end quantitative portfolio analysis
conducted using Python and Modern Portfolio Theory.

The objective was to evaluate the performance, risk characteristics,
and diversification benefits of an equally weighted portfolio
consisting of thirty large-cap U.S. equities between 2020 and 2025.

Rather than serving as an investment recommendation,
the project demonstrates the practical application of financial
analytics, portfolio management techniques, statistical analysis,
and data visualisation using Python.
"""
    )

    st.divider()

    st.subheader("Project Objectives")

    st.markdown("""

- Collect and preprocess historical market data.

- Analyse historical asset returns.

- Measure portfolio performance.

- Evaluate portfolio risk using multiple metrics.

- Construct an equally weighted investment portfolio.

- Optimise portfolio allocation using Monte Carlo Simulation.

- Demonstrate Modern Portfolio Theory in practice.

- Present findings through an interactive Streamlit dashboard.

""")

    st.divider()

    st.subheader("Analytical Techniques")

    st.markdown("""

- Historical Return Analysis

- Correlation Matrix & Heatmap

- Portfolio Return Estimation

- Portfolio Volatility

- Rolling Volatility

- Maximum Drawdown

- Sharpe Ratio

- Monte Carlo Portfolio Simulation

- Efficient Portfolio Selection

- Portfolio Allocation Analysis

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

    st.subheader("Skills Demonstrated")

    st.markdown("""

- Quantitative Finance

- Financial Data Analysis

- Portfolio Management

- Risk Analytics

- Data Visualisation

- Statistical Analysis

- Python Programming

- Interactive Dashboard Development

""")

    st.divider()

    st.subheader("Project Summary")

    st.write(
        """
This project demonstrates an end-to-end quantitative portfolio analysis 
using Python and Modern Portfolio Theory. The accompanying Streamlit dashboard 
was developed as an interactive visualisation of the completed analysis rather 
than a portfolio management application. It enables users to explore the project's 
methodology, portfolio performance, risk metrics, optimisation outcomes, and asset 
allocation through an intuitive interface, making the findings more accessible than 
a traditional Jupyter Notebook. The dashboard complements the research report by presenting 
the analysis in a format that highlights both the financial insights and the technical implementation 
behind the project.
"""
    )

    st.divider()

    st.caption(
        "Developed by Rasheedat Seidu | University of Lagos | B.Sc. Finance"
    )



import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import time
from urllib.error import URLError
import requests

import datetime



###########  Header Start ############################

 

import streamlit as st
# Title Section and Dropdown Menu
st.markdown(
    """
   <style>
        /* Title Section Styling */
        .title-section {
            padding: 20px;
            background: linear-gradient(135deg, #b9d2ec, #bcd2e58c);
            color: white;
            border-radius: 25px;
            box-shadow: 0 12px 18px rgba(0, 0.44, 0.55, 0.55);
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;
        }

             .title-section h1:   {
            text-shadow: 0 0 5px rgba(255, 255, 255, 1),
                         0 0 10px rgba(0, 123, 255, 1),
                         0 0 15px rgba(0, 123, 255, 1);
            transform: scale(1.1);
        }

        

        .title-section h1 {
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.9),
                         0 0 20px rgba(0, 123, 255, 0.8),
                         0 0 30px rgba(0, 123, 255, 0.7);
            transition: all 0.3s ease-in-out;
        }

        .title-section h1:hover {
            text-shadow: 0 0 5px rgba(255, 255, 255, 1),
                         0 0 10px rgba(0, 123, 255, 1),
                         0 0 15px rgba(0, 123, 255, 1);
            transform: scale(1.1);
        }

        .title-section h2 {
            font-size: 2em;
            font-weight: semi-bold;
            margin-bottom: 15px;
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.8),
                         0 0 15px rgba(0, 123, 255, 0.7);
        }

        .title-section p {
            font-size: 1.2em;
            margin: 0;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.9);
        }

    

    
        /* Dropdown Button Styling */
        .dropdown-button {
            background-color: #b3cfed;
            color: white;
            font-size: 12px;
            font-weight: bold;
            padding: 10px 15px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0.44, 0.55);
            transition: all 0.3s ease-in-out;
            text-align: center;
        }

        .dropdown-button:hover {
            background-color: #0056b3;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.55);
        }

        /* Dropdown Menu Styling */
        .dropdown-container {
            position: absolute;
            top: 20px;
            right: 20px; /* Positioning the dropdown to the right-hand side */
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f8f9fa;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            margin-top: 10px;
            min-width: 220px; /* Slightly larger for better readability */
    right: 0; /* Align dropdown content to the right */
            z-index: 1;
            right: 0; /* Align the dropdown to the right */
        }

        .dropdown-content a {
            color: black;
            font-size: 14px;
            font-weight: 500;
            padding: 10px 20px;
            text-decoration: none;
            display: block;
            border-radius: 5px;
            transition: background-color 0.2s ease;
        }

        .dropdown-content a:hover {
            background-color: #cce4f7;
            color: #0056b3;
        }

        /* Show the dropdown content on hover */
        .dropdown-container:hover .dropdown-content {
            display: block;
        }

        /* Dropdown Arrow Styling */
        .dropdown-arrow {
            margin-left: 5px;
            font-size: 12px;
        }

  
  </style>



    <!-- Dropdown Menu -->
    <div class="dropdown-container">
        <button class="dropdown-button">
            Menu <span class="dropdown-arrow">▼</span>
        </button>
        <div class="dropdown-content">
            <a href="/?page=Home">Home</a>
            <a href="/?page=Calculators">Calculators</a>
            <a href="/?page=Business">Business</a>
            <a href="/?page=RealEstate">Real Estate</a>
            <a href="/?page=Investment">Investment</a>
            <a href="/?page=MarketAnalysis">Market Analysis</a>
            <a href="/?page=Trends">Trends</a>
            <a href="/?page=Contact">Contact</a>
        </div>
    </div>

    <!-- Title Section -->
    <div class="title-section">
        <h1>VillaTerras Ai</h1>
        <h2>Ai Real Estate Agent | Assistant</h2>
        <p><strong>VillaTerras Ai Real Estate Dashboard</strong>.</p>
        <p>All Real Estate Knowledge in One Place.</p>
        
 
 

  <p>Analyze, compare, and manage properties with advanced metrics and tools, all with VillaTerras.com</p>


 
    <p style="font-size:12px; color:lightgrey;">
      Written by Ekbalam.
    </p> 


    """,
    unsafe_allow_html=True
)


###########  Header End ############################



import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from urllib.error import URLError

# --- Utility functions ---
@st.cache_data
def load_data(filename):
    """Fetch data from a remote JSON file."""
    url = f"https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/{filename}"
    try:
        return pd.read_json(url)
    except ValueError:
        st.error(f"Error loading data from {url}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()

# --- Sidebar Configuration ---
def configure_sidebar():
    """Sets up the sidebar and returns the user inputs."""
    st.sidebar.header("Filters")

    # Location Details
    st.sidebar.subheader("Location Details")
    location_details = {
        "address": st.sidebar.text_input("Address", value="", key="location_address"),
        "city": st.sidebar.text_input("City", value="", key="location_city"),
        "state": st.sidebar.text_input("State", value="", key="location_state"),
        "zip": st.sidebar.text_input("Zip Code", value="", key="location_zip"),
    }

    # Property Details
    st.sidebar.subheader("Property Details")
    property_details = {
        "price_range": st.sidebar.slider("Price Range ($)", 50000, 5000000, (100000, 1000000), step=50000, key="price_range"),
        "bedrooms": st.sidebar.slider("Bedrooms", 1, 10, (2, 4), key="bedrooms"),
        "bathrooms": st.sidebar.slider("Bathrooms", 1, 10, (1, 3), key="bathrooms"),
        "area_range": st.sidebar.slider("Living Area (sq ft)", 500, 10000, (1000, 5000), step=100, key="area_range"),
        "land_area": st.sidebar.slider("Land Area (sq ft)", 1000, 50000, (5000, 20000), step=500, key="land_area"),
    }

    # Financial Details
    st.sidebar.subheader("Financial Details")
    financial_details = {
        "property_price": st.sidebar.number_input("Property Price ($)", value=300000, step=10000, key="property_price"),
        "down_payment": st.sidebar.number_input("Down Payment ($)", value=60000, step=1000, key="down_payment"),
        "closing_costs": st.sidebar.number_input("Closing Costs ($)", value=5000, step=500, key="closing_costs"),
        "rehab_costs": st.sidebar.number_input("Rehabilitation Costs ($)", value=10000, step=500, key="rehab_costs"),
        "annual_property_taxes": st.sidebar.number_input("Annual Property Taxes ($)", value=5000, step=500, key="property_taxes"),
        "annual_insurance": st.sidebar.number_input("Annual Insurance ($)", value=1200, step=100, key="insurance"),
        "annual_utilities": st.sidebar.number_input("Annual Utilities ($)", value=3000, step=500, key="utilities"),
        "maintenance_perc": st.sidebar.number_input("Maintenance (% of Rent)", value=10, step=1, key="maintenance"),
        "capex_perc": st.sidebar.number_input("Capital Expenditure (% of Rent)", value=10, step=1, key="capex"),
        "mgmt_perc": st.sidebar.number_input("Property Management (% of Rent)", value=8, step=1, key="mgmt"),
        "vacancy_perc": st.sidebar.number_input("Vacancy Rate (%)", value=5, step=1, key="vacancy"),
        "hoa_fees": st.sidebar.number_input("HOA Fees (Monthly $)", value=0, step=50, key="hoa_fees"),
        "other_income": st.sidebar.number_input("Other Income (Monthly $)", value=0, step=50, key="other_income"),
        "appreciation_rate": st.sidebar.number_input("Appreciation Rate (%)", value=3.0, step=0.1, key="appreciation"),
        "interest_rate": st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1, key="interest_rate"),
        "loan_term": st.sidebar.number_input("Loan Term (Years)", value=30, step=1, key="loan_term"),
        "annual_rent_income": st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000, key="rent_income"),
        "inflation_rate": st.sidebar.number_input("Inflation Rate (%)", value=2.0, step=0.1, key="inflation"),
        "selling_costs_perc": st.sidebar.number_input("Selling Costs (% of Sale Price)", value=6.0, step=0.1, key="selling_costs"),
    }

    return location_details, property_details, financial_details

# --- Calculate Metrics ---
def calculate_metrics(financial_details):
    """Calculate key financial metrics for a real estate investment."""
    # Extract Inputs
    price = financial_details["property_price"]
    rent = financial_details["annual_rent_income"]
    down = financial_details["down_payment"]
    closing = financial_details["closing_costs"]
    rehab = financial_details["rehab_costs"]
    taxes = financial_details["annual_property_taxes"]
    insurance = financial_details["annual_insurance"]
    utilities = financial_details["annual_utilities"]
    hoa_fees = financial_details["hoa_fees"] * 12  # Monthly to Annual
    other_income = financial_details["other_income"] * 12
    rate = financial_details["interest_rate"]
    term = financial_details["loan_term"]

    # Calculations
    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    annual_debt_service = monthly_payment * 12
    maintenance_cost = rent * (financial_details["maintenance_perc"] / 100)
    capex_cost = rent * (financial_details["capex_perc"] / 100)
    mgmt_cost = rent * (financial_details["mgmt_perc"] / 100)
    operating_expenses = taxes + insurance + utilities + hoa_fees + maintenance_cost + capex_cost + mgmt_cost
    effective_gross_income = rent * (1 - financial_details["vacancy_perc"] / 100) + other_income
    noi = effective_gross_income - operating_expenses
    cash_flow = noi - annual_debt_service
    total_investment = down + closing + rehab
    cap_rate = (noi / price) * 100 if price > 0 else 0
    cash_on_cash = (cash_flow / total_investment) * 100 if total_investment > 0 else 0

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate (%)": cap_rate,
        "Cash-on-Cash ROI (%)": cash_on_cash,
    }








# --- Main Function ---
# Function to create bar chart
# Function to create a bar chart
def create_bar_chart(dataframe, title):
    """Creates a bar chart from a given dataframe."""
    return alt.Chart(dataframe).mark_bar().encode(
        x=alt.X("Metric", sort=None, title="Metric"),
        y=alt.Y("Value", title="Value ($)"),
        tooltip=["Metric", "Value"]
    ).properties(title=title).interactive()


def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with detailed metrics and sensitivity analysis.")

    # Sidebar Inputs
    _, _, financial_details = configure_sidebar()

    # Debugging: Display financial_details
    st.write("Debug: Financial Details:", financial_details)

    # Calculate Metrics
    try:
        metrics = calculate_metrics(financial_details)
        st.header("Investment Metrics")
        
        # Display metrics as a table
        metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
        st.table(metrics_df)

        # Visualization: Bar Chart for Key Metrics
        st.subheader("Investment Metrics Visualization")
        selected_metrics = st.multiselect(
            "Select Metrics to Visualize",
            options=["Monthly Payment", "Operating Expenses", "NOI", "Cash Flow", "Cap Rate (%)", "Cash-on-Cash ROI (%)"],
            default=["Monthly Payment", "Operating Expenses", "NOI", "Cash Flow"]
        )

        bar_chart_data = metrics_df[metrics_df["Metric"].isin(selected_metrics)]
        if bar_chart_data.empty:
            st.warning("No metrics selected for visualization.")
        else:
            bar_chart = create_bar_chart(bar_chart_data, title="Key Investment Metrics")
            st.altair_chart(bar_chart, use_container_width=True)

        # Visualization: Trend Analysis Line Chart
        st.subheader("Trend Analysis")
        trend_data = []
        price_range = np.linspace(
            financial_details["property_price"] * 0.8,
            financial_details["property_price"] * 1.2,
            20
        )
        for price in price_range:
            temp_details = financial_details.copy()
            temp_details["property_price"] = price
            trend_metrics = calculate_metrics(temp_details)
            trend_data.append({
                "Property Price ($)": price,
                "NOI ($)": trend_metrics["NOI"],
                "Cash Flow ($)": trend_metrics["Cash Flow"]
            })

        trend_df = pd.DataFrame(trend_data)
        line_chart = alt.Chart(trend_df).mark_line(point=True).encode(
            x=alt.X("Property Price ($):Q", title="Property Price ($)"),
            y=alt.Y("NOI ($):Q", title="Net Operating Income ($)"),
            color=alt.value("steelblue"),
            tooltip=["Property Price ($)", "NOI ($)", "Cash Flow ($)"]
        ).interactive()
        st.altair_chart(line_chart, use_container_width=True)

        # Sensitivity Analysis
        if st.checkbox("Perform Sensitivity Analysis"):
            st.subheader("Sensitivity Analysis Results")
            try:
                sensitivity_results = sensitivity_analysis(financial_details)
                st.write(sensitivity_results)

                # Visualization: Sensitivity Analysis Scatterplot
                scatter_chart = alt.Chart(sensitivity_results).mark_circle(size=60).encode(
                    x=alt.X("Rent Income ($):Q", title="Rent Income ($)"),
                    y=alt.Y("Property Price ($):Q", title="Property Price ($)"),
                    color=alt.Color("Cap Rate (%)", scale=alt.Scale(scheme="viridis"), title="Cap Rate (%)"),
                    tooltip=["Rent Income ($)", "Property Price ($)", "Cap Rate (%)", "Cash Flow ($)"]
                ).interactive()
                st.altair_chart(scatter_chart, use_container_width=True)

            except Exception as e:
                st.error(f"Error during sensitivity analysis: {e}")

    except ValueError as e:
        st.error(f"Error in calculating metrics: {e}. Please check your input values.")
    except Exception as e:
        st.error(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

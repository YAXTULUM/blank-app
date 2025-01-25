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

        /* Responsive Adjustments */
        @media screen and (max-width: 768px) {
            .dropdown-button {
                font-size: 10px;
                padding: 8px 12px;
            }

            .dropdown-content {
                min-width: 180px; /* Adjust dropdown width for smaller screens */
            }

            .dropdown-content a {
                font-size: 12px;
                padding: 8px 15px;
            }
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



# Utility function to load JSON data
import streamlit as st
import pandas as pd
import numpy as np
from urllib.error import URLError

# Utility function to load JSON data
@st.cache_data
def from_data_file(filename):
    """Fetch data from a remote JSON file."""
    url = f"https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/{filename}"
    try:
        return pd.read_json(url)
    except ValueError:
        st.error(f"Error loading data from {url}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()

# Sidebar configuration function
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- Not so DUMMY Data Loader ---


@st.cache_data
def load_data(filename):
    """Placeholder function to load JSON data."""
    try:
        return pd.read_json(filename)
    except ValueError:
        st.error(f"Error loading data from {filename}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()








def configure_sidebar():
    """Sets up the sidebar and returns the user inputs."""
    st.sidebar.header("Filters")

    # Location Details
    st.sidebar.subheader("Location Details")
    location_details = {
        "address": st.sidebar.text_input("Address", value="", key="location_address_sidebar_1"),
        "city": st.sidebar.text_input("City", value="", key="location_city_sidebar_1"),
        "state": st.sidebar.text_input("State", value="", key="location_state_sidebar_1"),
        "zip": st.sidebar.text_input("Zip Code", value="", key="location_zip_sidebar_1"),
    }

    # Property Details
    st.sidebar.subheader("Property Details")
    property_details = {
        "price_range": st.sidebar.slider(
            "Price Range ($)", 50000, 5000000, (100000, 1000000), step=50000, key="price_range_sidebar"
        ),
        "bedrooms": st.sidebar.slider("Bedrooms", 1, 10, (2, 4), key="bedrooms_sidebar"),
        "bathrooms": st.sidebar.slider("Bathrooms", 1, 10, (1, 3), key="bathrooms_sidebar"),
        "area_range": st.sidebar.slider(
            "Living Area (sq ft)", 500, 10000, (1000, 5000), step=100, key="area_range_sidebar"
        ),
        "land_area": st.sidebar.slider(
            "Land Area (sq ft)", 1000, 50000, (5000, 20000), step=500, key="land_area_sidebar"
        ),
    }

    # Financial Details
    st.sidebar.subheader("Financial Details")
    financial_details = {
        "property_price": st.sidebar.number_input("Property Price ($)", value=300000, step=10000, key="property_price_sidebar"),
        "down_payment": st.sidebar.number_input("Down Payment ($)", value=60000, step=1000, key="down_payment_sidebar"),
        "closing_costs": st.sidebar.number_input("Closing Costs ($)", value=5000, step=500, key="closing_costs_sidebar"),
        "rehab_costs": st.sidebar.number_input("Rehabilitation Costs ($)", value=10000, step=500, key="rehab_costs_sidebar"),
        "annual_property_taxes": st.sidebar.number_input(
            "Annual Property Taxes ($)", value=5000, step=500, key="annual_property_taxes_sidebar"
        ),
        "annual_insurance": st.sidebar.number_input("Annual Insurance ($)", value=1200, step=100, key="annual_insurance_sidebar"),
        "annual_utilities": st.sidebar.number_input("Annual Utilities ($)", value=3000, step=500, key="annual_utilities_sidebar"),
        "maintenance_perc": st.sidebar.number_input("Maintenance (% of Rent)", value=10, step=1, key="maintenance_perc_sidebar"),
        "capex_perc": st.sidebar.number_input("Capital Expenditure (% of Rent)", value=10, step=1, key="capex_perc_sidebar"),
        "mgmt_perc": st.sidebar.number_input("Property Management (% of Rent)", value=8, step=1, key="mgmt_perc_sidebar"),
        "vacancy_perc": st.sidebar.number_input("Vacancy Rate (%)", value=5, step=1, key="vacancy_perc_sidebar"),
        "hoa_fees": st.sidebar.number_input("HOA Fees (Monthly $)", value=0, step=50, key="hoa_fees_sidebar"),
        "other_income": st.sidebar.number_input("Other Income (Monthly $)", value=0, step=50, key="other_income_sidebar"),
        "interest_rate": st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1, key="interest_rate_sidebar"),
        "loan_term": st.sidebar.number_input("Loan Term (Years)", value=30, step=1, key="loan_term_sidebar"),
        "annual_rent_income": st.sidebar.number_input(
            "Annual Rent Income ($)", value=30000, step=1000, key="annual_rent_income_sidebar"
        ),
        "appreciation_rate": st.sidebar.number_input("Appreciation Rate (%)", value=3.0, step=0.1, key="appreciation_rate_sidebar"),
        "inflation_rate": st.sidebar.number_input("Inflation Rate (%)", value=2.0, step=0.1, key="inflation_rate_sidebar"),
        "selling_costs_perc": st.sidebar.number_input("Selling Costs (% of Sale Price)", value=6.0, step=0.1, key="selling_costs_sidebar"),
    }

    return location_details, property_details, financial_details






# Calculation Function
def calculate_metrics(financial_details):
    """Calculate key financial metrics for a real estate investment."""
    # Input Validation
    if financial_details["property_price"] <= 0:
        raise ValueError("Property price must be greater than zero.")
    if financial_details["loan_term"] <= 0:
        raise ValueError("Loan term must be greater than zero.")
    if financial_details["interest_rate"] < 0:
        raise ValueError("Interest rate cannot be negative.")

    # Extract Inputs
    price = financial_details["property_price"]
    rent = financial_details["annual_rent_income"]
    down = financial_details["down_payment"]
    closing = financial_details["closing_costs"]
    rehab = financial_details["rehab_costs"]
    taxes = financial_details["annual_property_taxes"]
    insurance = financial_details["annual_insurance"]
    utilities = financial_details["annual_utilities"]
    hoa_fees = financial_details["hoa_fees"] * 12
    other_income = financial_details["other_income"] * 12
    rate = financial_details["interest_rate"]
    term = financial_details["loan_term"]

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

    # Additional Metrics
    dcr = noi / annual_debt_service if annual_debt_service > 0 else float('inf')
    break_even_rent = (operating_expenses + annual_debt_service) / (1 - financial_details["vacancy_perc"] / 100)

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate (%)": cap_rate,
        "Cash-on-Cash ROI (%)": cash_on_cash,
        "Debt Coverage Ratio": dcr,
        "Break-Even Rent": break_even_rent,
    }

def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with detailed metrics and sensitivity analysis.")

    # Sidebar Inputs
    _, _, financial_details = configure_sidebar()

    # Calculate Metrics
    try:
        metrics = calculate_metrics(financial_details)
        st.header("Investment Metrics")
        
        # Display metrics as a table
        metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
        st.table(metrics_df)

        # Visualization 1: Bar Chart for Key Metrics
        st.subheader("Investment Metrics Visualization")
        bar_chart_data = metrics_df[
            metrics_df["Metric"].isin(
                ["Monthly Payment", "Operating Expenses", "NOI", "Cash Flow"]
            )
        ]
        bar_chart = alt.Chart(bar_chart_data).mark_bar().encode(
            x=alt.X("Metric", sort=None, title="Metric"),
            y=alt.Y("Value", title="Value ($)"),
            tooltip=["Metric", "Value"]
        ).interactive()
        st.altair_chart(bar_chart, use_container_width=True)

        # Visualization 2: Pie Chart for Expense Breakdown
        st.subheader("Expense Breakdown")
        expense_data = pd.DataFrame({
            "Category": ["Taxes", "Insurance", "Utilities", "HOA Fees"],
            "Amount": [
                financial_details["annual_property_taxes"],
                financial_details["annual_insurance"],
                financial_details["annual_utilities"],
                financial_details["hoa_fees"] * 12,  # Convert monthly to annual
            ]
        })
        pie_chart = alt.Chart(expense_data).mark_arc().encode(
            theta=alt.Theta("Amount", title="Expense Amount"),
            color=alt.Color("Category", title="Expense Category"),
            tooltip=["Category", "Amount"]
        )
        st.altair_chart(pie_chart, use_container_width=True)

    except ValueError as e:
        st.error(f"Input Error: {e}")
        return




 


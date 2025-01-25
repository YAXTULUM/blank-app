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

@media screen and (max-width: 768px) {
    .dropdown-container {
        top: 10px;
        right: 10px; /* Adjust for mobile spacing */
    }

    .dropdown-button {
        font-size: 14px;
        padding: 8px 12px; /* Smaller padding for mobile */
    }

    .dropdown-content {
        min-width: 180px; /* Smaller dropdown width */
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


@st.cache_data
def from_data_file(filename):
    """Retrieve data from an online file and load it as a DataFrame."""
    url = f"https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/{filename}"
    try:
        return pd.read_json(url)
    except ValueError:
        st.error(f"Error loading data from {url}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()


# Sidebar configuration for filters
st.sidebar.header("Filters")

# Location details inputs
st.sidebar.subheader("Location Details")
location_address = st.sidebar.text_input("Address", value="")
location_city = st.sidebar.text_input("City", value="")
location_state = st.sidebar.text_input("State", value="")
location_zip = st.sidebar.text_input("Zip Code", value="")

# Property details inputs
st.sidebar.subheader("Property Details")
price_range = st.sidebar.slider("Price Range ($)", 50000, 5000000, (100000, 1000000), step=50000)
bedrooms = st.sidebar.slider("Bedrooms", 1, 10, (2, 4))
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, (1, 3))
area_range = st.sidebar.slider("Living Area (sq ft)", 500, 10000, (1000, 5000), step=100)
land_area = st.sidebar.slider("Land Area (sq ft)", 1000, 50000, (5000, 20000), step=500)

# Financial details inputs
st.sidebar.header("Financial Details")
property_price = st.sidebar.number_input("Property Price ($)", value=300000, step=10000)
down_payment = st.sidebar.number_input("Down Payment ($)", value=60000, step=1000)
closing_costs = st.sidebar.number_input("Closing Costs ($)", value=5000, step=500)
rehab_costs = st.sidebar.number_input("Rehabilitation Costs ($)", value=10000, step=500)
annual_property_taxes = st.sidebar.number_input("Annual Property Taxes ($)", value=5000, step=500)
annual_insurance = st.sidebar.number_input("Annual Insurance ($)", value=1200, step=100)
annual_utilities = st.sidebar.number_input("Annual Utilities ($)", value=3000, step=500)
maintenance_perc = st.sidebar.number_input("Maintenance (% of Rent)", value=10, step=1)
capex_perc = st.sidebar.number_input("Capital Expenditure (% of Rent)", value=10, step=1)
mgmt_perc = st.sidebar.number_input("Property Management (% of Rent)", value=8, step=1)
vacancy_perc = st.sidebar.number_input("Vacancy Rate (%)", value=5, step=1)
interest_rate = st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1)
loan_term = st.sidebar.number_input("Loan Term (Years)", value=30, step=1)
annual_rent_income = st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000)

# Calculate annual expenses
annual_expenses = (
    annual_property_taxes +
    annual_insurance +
    annual_utilities +
    (annual_rent_income * (maintenance_perc / 100)) +
    (annual_rent_income * (capex_perc / 100)) +
    (annual_rent_income * (mgmt_perc / 100)) +
    (annual_rent_income * (vacancy_perc / 100))
)


# Define the core calculation function
def calculate_metrics(price, rent, down, closing, rehab, taxes, insurance, utilities,
                      maintenance_perc, capex_perc, mgmt_perc, vacancy_perc, rate, term):
    """Calculate financial metrics for a property investment."""
    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12

    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    annual_debt_service = monthly_payment * 12

    operating_expenses = taxes + insurance + utilities + (rent * (maintenance_perc + capex_perc + mgmt_perc) / 100)
    effective_gross_income = rent * (1 - vacancy_perc / 100)
    noi = effective_gross_income - operating_expenses

    cash_flow = noi - annual_debt_service
    total_investment = down + closing + rehab

    cap_rate = (noi / price) * 100
    cash_on_cash = (cash_flow / total_investment) * 100

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate": cap_rate,
        "Cash on Cash": cash_on_cash
    }


# Perform calculations
metrics = calculate_metrics(
    property_price, annual_rent_income, down_payment, closing_costs, rehab_costs,
    annual_property_taxes, annual_insurance, annual_utilities, maintenance_perc,
    capex_perc, mgmt_perc, vacancy_perc, interest_rate, loan_term
)

# Display results
st.header("Investment Metrics")
st.write(f"**Monthly Mortgage Payment:** ${metrics['Monthly Payment']:.2f}")
st.write(f"**Annual Debt Service:** ${metrics['Annual Debt Service']:.2f}")
st.write(f"**Operating Expenses:** ${metrics['Operating Expenses']:.2f}")
st.write(f"**Effective Gross Income:** ${metrics['Effective Gross Income']:.2f}")
st.write(f"**Net Operating Income (NOI):** ${metrics['NOI']:.2f}")
st.write(f"**Cash Flow:** ${metrics['Cash Flow']:.2f}")
st.write(f"**Cap Rate:** {metrics['Cap Rate']:.2f}%")
st.write(f"**Cash-on-Cash Return:** {metrics['Cash on Cash']:.2f}%")


# Sensitivity Analysis
def sensitivity_analysis(rent_income, property_price, down_payment, closing_costs, rehab_costs,
                         taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc, rate, term):
    """Perform sensitivity analysis on key variables like rent income and property price."""
    rent_range = np.linspace(rent_income * 0.8, rent_income * 1.2, 20)
    price_range = np.linspace(property_price * 0.8, property_price * 1.2, 20)

    results = []
    for rent in rent_range:
        for price in price_range:
            metrics = calculate_metrics(
                price, rent, down_payment, closing_costs, rehab_costs,
                taxes, insurance, utilities, maintenance, capex,
                mgmt_perc, vacancy_perc, rate, term
            )
            results.append({
                "Rent Income ($)": rent,
                "Property Price ($)": price,
                "Cap Rate (%)": metrics["Cap Rate"],
                "Cash Flow ($)": metrics["Cash Flow"]
            })

    return pd.DataFrame(results)


# Perform and display sensitivity analysis
sensitivity_df = sensitivity_analysis(
    annual_rent_income, property_price, down_payment, closing_costs, rehab_costs,
    annual_property_taxes, annual_insurance, annual_utilities, maintenance_perc,
    capex_perc, mgmt_perc, vacancy_perc, interest_rate, loan_term
)
cap_rate_pivot = sensitivity_df.pivot(index="Rent Income ($)", columns="Property Price ($)", values="Cap Rate (%)")
st.write("Sensitivity Heatmap (Cap Rate)")
st.dataframe(cap_rate_pivot)


# Map Integration
st.subheader("Investment Heatmap")
city_data = pd.DataFrame({
    "City": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "San Jose"],
    "Latitude": [34.0522, 37.7749, 32.7157, 38.5816, 37.3382],
    "Longitude": [-118.2437, -122.4194, -117.1611, -121.4944, -121.8863],
    "Value": [75, 85, 70, 65, 80]
})
city_data.rename(columns={"Latitude": "lat", "Longitude": "lon"}, inplace=True)
st.map(city_data)


# Downloadable Report
def generate_report(data):
    """Generate a downloadable CSV report."""
    return data.to_csv(index=False).encode("utf-8")


download_csv = generate_report(city_data)
st.download_button(
    label="Download Investment Report",
    data=download_csv,
    file_name="investment_report.csv",
    mime="text/csv"




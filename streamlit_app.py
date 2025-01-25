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


# Sidebar configuration function
def configure_sidebar():
    """Sets up the sidebar and returns the user inputs."""
    st.sidebar.header("Filters")

    # Location Details
    st.sidebar.subheader("Location Details")
    location_details = {
        "address": st.sidebar.text_input("Address", value="", key="location_address_sidebar"),
        "city": st.sidebar.text_input("City", value="", key="location_city_sidebar"),
        "state": st.sidebar.text_input("State", value="", key="location_state_sidebar"),
        "zip": st.sidebar.text_input("Zip Code", value="", key="location_zip_sidebar"),
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




# Calculation function
def calculate_metrics(financial_details):
    """Calculate key financial metrics."""
    price = financial_details["property_price"]
    rent = financial_details["annual_rent_income"]
    down = financial_details["down_payment"]
    closing = financial_details["closing_costs"]
    rehab = financial_details["rehab_costs"]
    taxes = financial_details["annual_property_taxes"]
    insurance = financial_details["annual_insurance"]
    utilities = financial_details["annual_utilities"]
    maintenance_perc = financial_details["maintenance_perc"]
    capex_perc = financial_details["capex_perc"]
    mgmt_perc = financial_details["mgmt_perc"]
    vacancy_perc = financial_details["vacancy_perc"]
    rate = financial_details["interest_rate"]
    term = financial_details["loan_term"]
    hoa_fees = financial_details["hoa_fees"] * 12  # Annualized
    other_income = financial_details["other_income"] * 12  # Annualized

    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12

    try:
        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    except ZeroDivisionError:
        monthly_payment = 0

    annual_debt_service = monthly_payment * 12
    operating_expenses = taxes + insurance + utilities + hoa_fees + (rent * (maintenance_perc + capex_perc + mgmt_perc) / 100)
    effective_gross_income = rent * (1 - vacancy_perc / 100) + other_income
    noi = effective_gross_income - operating_expenses

    cash_flow = noi - annual_debt_service
    total_investment = down + closing + rehab
    cap_rate = (noi / price) * 100 if price > 0 else 0
    cash_on_cash = (cash_flow / total_investment) * 100 if total_investment > 0 else 0
    break_even_rent = (operating_expenses + annual_debt_service) / (1 - vacancy_perc / 100)

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate": cap_rate,
        "Cash on Cash": cash_on_cash,
        "Break-Even Rent": break_even_rent,
    }


# Main function

def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with detailed metrics.")

    # Sidebar Inputs
    location_details, property_details, financial_details = configure_sidebar()

    # Calculate Metrics
    metrics = calculate_metrics(financial_details)

    # Display Metrics
    st.header("Investment Metrics")
    for key, value in metrics.items():
        st.write(f"**{key}:** ${value:,.2f}" if "($)" in key or "Payment" in key else f"**{key}:** {value:.2f}%")

    st.write("Use the sidebar to adjust variables and see real-time analysis.")


# Run the app
if __name__ == "__main__":
    main()






#  SECTION  #

import streamlit as st
import pandas as pd
import numpy as np

# Sensitivity Analysis Function
def sensitivity_analysis(rent_income, property_price, down_payment, closing_costs, rehab_costs,
                         taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
                         hoa_fees, other_income, rate, term, appreciation_rate=0.0, inflation_rate=0.0):
    """
    Perform sensitivity analysis on rent and price, considering additional variables.
    """
    rent_range = np.linspace(rent_income * 0.8, rent_income * 1.2, 20)
    price_range = np.linspace(property_price * 0.8, property_price * 1.2, 20)
    return perform_sensitivity_analysis(rent_range, price_range, down_payment, closing_costs, rehab_costs,
                                        taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
                                        hoa_fees, other_income, rate, term, appreciation_rate, inflation_rate)

# Perform Sensitivity Analysis Function
def perform_sensitivity_analysis(rent_range, price_range, down_payment, closing_costs, rehab_costs,
                                 taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
                                 hoa_fees, other_income, rate, term, appreciation_rate, inflation_rate):
    """
    Perform sensitivity analysis for a range of rent and price combinations.
    """
    results = []

    for rent in rent_range:
        for price in price_range:
            # Prepare financial details for the current combination
            financial_details = {
                "property_price": price,
                "annual_rent_income": rent,
                "down_payment": down_payment,
                "closing_costs": closing_costs,
                "rehab_costs": rehab_costs,
                "annual_property_taxes": taxes,
                "annual_insurance": insurance,
                "annual_utilities": utilities,
                "maintenance_perc": maintenance,
                "capex_perc": capex,
                "mgmt_perc": mgmt_perc,
                "vacancy_perc": vacancy_perc,
                "hoa_fees": hoa_fees,
                "other_income": other_income,
                "interest_rate": rate,
                "loan_term": term,
                "appreciation_rate": appreciation_rate,
                "inflation_rate": inflation_rate,
            }

            # Calculate metrics for the current combination
            metrics = calculate_metrics(financial_details)

            # Append results for this combination
            results.append({
                "Rent Income ($)": rent,
                "Property Price ($)": price,
                "Cap Rate (%)": metrics.get("Cap Rate", 0),  # Default to 0 if not found
                "Cash Flow ($)": metrics.get("Cash Flow", 0),  # Default to 0 if not found
                "Break-Even Rent ($)": metrics.get("Break-Even Rent", None),  # Include new metrics if calculated
                "ROI (%)": metrics.get("ROI", None),  # Include ROI if calculated
            })

    return pd.DataFrame(results)

# Metrics Calculation Function
def calculate_metrics(financial_details):
    """
    Calculate key financial metrics based on provided financial details.
    """
    price = financial_details["property_price"]
    rent = financial_details["annual_rent_income"]
    down = financial_details["down_payment"]
    closing = financial_details["closing_costs"]
    rehab = financial_details["rehab_costs"]
    taxes = financial_details["annual_property_taxes"]
    insurance = financial_details["annual_insurance"]
    utilities = financial_details["annual_utilities"]
    maintenance_perc = financial_details["maintenance_perc"]
    capex_perc = financial_details["capex_perc"]
    mgmt_perc = financial_details["mgmt_perc"]
    vacancy_perc = financial_details["vacancy_perc"]
    hoa_fees = financial_details["hoa_fees"]
    other_income = financial_details["other_income"]
    rate = financial_details["interest_rate"]
    term = financial_details["loan_term"]

    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12

    try:
        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    except ZeroDivisionError:
        monthly_payment = 0

    annual_debt_service = monthly_payment * 12
    operating_expenses = taxes + insurance + utilities + (rent * (maintenance_perc + capex_perc + mgmt_perc) / 100) + hoa_fees
    effective_gross_income = rent * (1 - vacancy_perc / 100) + other_income
    noi = effective_gross_income - operating_expenses

    cash_flow = noi - annual_debt_service
    total_investment = down + closing + rehab

    cap_rate = (noi / price) * 100 if price > 0 else 0
    cash_on_cash = (cash_flow / total_investment) * 100 if total_investment > 0 else 0
    break_even_rent = (operating_expenses + annual_debt_service) / (1 - vacancy_perc / 100)

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate": cap_rate,
        "Cash on Cash": cash_on_cash,
        "Break-Even Rent": break_even_rent,
    }

# Main Function
def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with advanced metrics and sensitivity analysis.")

    # Example inputs for sensitivity analysis
    rent_income = 30000
    property_price = 300000
    down_payment = 60000
    closing_costs = 5000
    rehab_costs = 10000
    taxes = 5000
    insurance = 1200
    utilities = 3000
    maintenance = 10
    capex = 10
    mgmt_perc = 8
    vacancy_perc = 5
    hoa_fees = 1000
    other_income = 500
    rate = 4.5
    term = 30

    # Perform sensitivity analysis
    st.subheader("Sensitivity Analysis Results")
    sensitivity_results = sensitivity_analysis(
        rent_income, property_price, down_payment, closing_costs, rehab_costs,
        taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
        hoa_fees, other_income, rate, term, appreciation_rate=3, inflation_rate=2
    )
    st.dataframe(sensitivity_results)


if __name__ == "__main__":
    main()



# Perform sensitivity analysis
# Example usage
rent_range = np.linspace(2000, 4000, 20)  # Example rent range
price_range = np.linspace(100000, 500000, 20)  # Example property price range

sensitivity_df = perform_sensitivity_analysis(
    rent_range=rent_range,
    price_range=price_range,
    down_payment=50000,
    closing_costs=5000,
    rehab_costs=10000,
    taxes=5000,
    insurance=2000,
    utilities=3000,
    maintenance=10,
    capex=10,
    mgmt_perc=8,
    vacancy_perc=5,
    hoa_fees=100,
    other_income=500,
    rate=4.5,
    term=30,
    appreciation_rate=3,
    inflation_rate=2
)

# Display sensitivity analysis
st.dataframe(sensitivity_df)







# Main function
def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with detailed metrics.")

    # Sidebar Inputs
    location_details, property_details, financial_details = configure_sidebar()

    # Calculate Metrics
    metrics = calculate_metrics(financial_details)

    # Display Metrics
    st.header("Investment Metrics")
    for metric, value in metrics.items():
        st.write(f"**{metric}:** ${value:,.2f}" if "($)" in metric or "Payment" in metric else f"**{metric}:** {value:.2f}%")

    # Perform Sensitivity Analysis
    st.header("Sensitivity Analysis")
    st.write("Explore how changes in rent and price affect key metrics.")
    sensitivity_df = sensitivity_analysis(
        rent_income=financial_details["annual_rent_income"],
        property_price=financial_details["property_price"],
        down_payment=financial_details["down_payment"],
        closing_costs=financial_details["closing_costs"],
        rehab_costs=financial_details["rehab_costs"],
        taxes=financial_details["annual_property_taxes"],
        insurance=financial_details["annual_insurance"],
        utilities=financial_details["annual_utilities"],
        maintenance=financial_details["maintenance_perc"],
        capex=financial_details["capex_perc"],
        mgmt_perc=financial_details["mgmt_perc"],
        vacancy_perc=financial_details["vacancy_perc"],
        hoa_fees=financial_details["hoa_fees"],
        other_income=financial_details["other_income"],
        rate=financial_details["interest_rate"],
        term=financial_details["loan_term"],
        appreciation_rate=financial_details.get("appreciation_rate", 0),
        inflation_rate=financial_details.get("inflation_rate", 0)
    )

    # Display Sensitivity DataFrame
    st.dataframe(sensitivity_df)

    # Plot the ROI Graph
    st.subheader("ROI Analysis")
    roi_chart = alt.Chart(sensitivity_df).mark_circle(size=60).encode(
        x=alt.X("Property Price ($):Q"),
        y=alt.Y("Rent Income ($):Q"),
        size=alt.Size("Cap Rate (%)", legend=None),
        color=alt.Color("Cash Flow ($):Q", scale=alt.Scale(scheme="blues")),
        tooltip=["Property Price ($)", "Rent Income ($)", "Cap Rate (%)", "Cash Flow ($)"]
    ).interactive()
    st.altair_chart(roi_chart, use_container_width=True)


if __name__ == "__main__":
    main()


 # Display Metrics
st.header("Investment Metrics")
for key, value in metrics.items():
    # Dynamically format based on type of metric
    if "($)" in key or "Payment" in key:
        st.write(f"**{key}:** ${value:,.2f}")
    elif "%" in key:
        st.write(f"**{key}:** {value:.2f}%")
    else:
        st.write(f"**{key}:** {value}")

# Perform Sensitivity Analysis
sensitivity_df = sensitivity_analysis(
    rent_income=financial_details["annual_rent_income"],
    property_price=financial_details["property_price"],
    down_payment=financial_details["down_payment"],
    closing_costs=financial_details["closing_costs"],
    rehab_costs=financial_details["rehab_costs"],
    taxes=financial_details["annual_property_taxes"],
    insurance=financial_details["annual_insurance"],
    utilities=financial_details["annual_utilities"],
    maintenance=financial_details["maintenance_perc"],
    capex=financial_details["capex_perc"],
    mgmt_perc=financial_details["mgmt_perc"],
    vacancy_perc=financial_details["vacancy_perc"],
    hoa_fees=financial_details.get("hoa_fees", 0),
    other_income=financial_details.get("other_income", 0),
    rate=financial_details["interest_rate"],
    term=financial_details["loan_term"],
    appreciation_rate=financial_details.get("appreciation_rate", 0),
    inflation_rate=financial_details.get("inflation_rate", 0)
)

# Enhanced Sensitivity Analysis Results
st.header("Sensitivity Analysis")
st.write("Explore how changes in rent and price affect key metrics.")
st.dataframe(sensitivity_df)

# Additional: ROI Visualization
st.subheader("ROI Visualization")
roi_chart = alt.Chart(sensitivity_df).mark_circle(size=60).encode(
    x=alt.X("Property Price ($):Q", title="Property Price ($)"),
    y=alt.Y("Rent Income ($):Q", title="Rent Income ($)"),
    size=alt.Size("Cap Rate (%)", legend=None, title="Cap Rate"),
    color=alt.Color("Cash Flow ($):Q", scale=alt.Scale(scheme="blues"), title="Cash Flow"),
    tooltip=[
        alt.Tooltip("Property Price ($):Q", title="Property Price ($)"),
        alt.Tooltip("Rent Income ($):Q", title="Rent Income ($)"),
        alt.Tooltip("Cap Rate (%)", title="Cap Rate (%)"),
        alt.Tooltip("Cash Flow ($):Q", title="Cash Flow ($)")
    ]
).interactive()
st.altair_chart(roi_chart, use_container_width=True)

# Run the App
if __name__ == "__main__":
    main()







# Enhanced Data Loading Function
@st.cache_data
def from_data_file(filename: str, base_url: str = "https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/"):
    """
    Load JSON data from a URL with error handling.
    """
    url = f"{base_url}{filename}"
    try:
        data = pd.read_json(url)
        st.success(f"Successfully loaded data from: {url}")
        return data
    except ValueError as ve:
        st.error(f"ValueError: Could not parse JSON data from {url}. Please check the file format.")
    except URLError as e:
        st.error(f"URLError: Unable to fetch data from {url}. Error: {e.reason}")
    return pd.DataFrame()  # Return an empty DataFrame on failure


# Sidebar Configuration for Map Settings
st.sidebar.header("Map Settings")
user_lat = st.sidebar.number_input("Starting Latitude", value=37.76, step=0.01)
user_lon = st.sidebar.number_input("Starting Longitude", value=-122.4, step=0.01)
hex_radius = st.sidebar.slider("Hexagon Radius (meters)", min_value=100, max_value=1000, value=200, step=50)

# Define Layers for Visualization
try:
    # Define all layers dynamically
    def create_layer(layer_type, filename, **kwargs):
        """
        Generic function to create layers dynamically.
        """
        data = from_data_file(filename)
        if data.empty:
            return None
        if layer_type == "HexagonLayer":
            return pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=kwargs.get("get_position", ["lon", "lat"]),
                radius=kwargs.get("radius", hex_radius),
                elevation_scale=kwargs.get("elevation_scale", 4),
                elevation_range=kwargs.get("elevation_range", [0, 1000]),
                extruded=kwargs.get("extruded", True),
            )
        elif layer_type == "HeatmapLayer":
            return pdk.Layer(
                "HeatmapLayer",
                data=data,
                get_position=kwargs.get("get_position", ["lon", "lat"]),
                get_weight=kwargs.get("get_weight", None),
                radius=kwargs.get("radius", 500),
            )
        elif layer_type == "ScatterplotLayer":
            return pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position=kwargs.get("get_position", ["lon", "lat"]),
                get_color=kwargs.get("get_color", [200, 30, 0, 160]),
                get_radius=kwargs.get("get_radius", 100),
                radius_scale=kwargs.get("radius_scale", 0.05),
            )
        elif layer_type == "TextLayer":
            return pdk.Layer(
                "TextLayer",
                data=data,
                get_position=kwargs.get("get_position", ["lon", "lat"]),
                get_text=kwargs.get("get_text", "name"),
                get_color=kwargs.get("get_color", [0, 0, 0, 200]),
                get_size=kwargs.get("get_size", 10),
                get_alignment_baseline=kwargs.get("get_alignment_baseline", "'bottom'"),
            )
        elif layer_type == "ArcLayer":
            return pdk.Layer(
                "ArcLayer",
                data=data,
                get_source_position=kwargs.get("get_source_position", ["lon", "lat"]),
                get_target_position=kwargs.get("get_target_position", ["lon2", "lat2"]),
                get_source_color=kwargs.get("get_source_color", [200, 30, 0, 160]),
                get_target_color=kwargs.get("get_target_color", [200, 30, 0, 160]),
                auto_highlight=kwargs.get("auto_highlight", True),
                width_scale=kwargs.get("width_scale", 0.0001),
                get_width=kwargs.get("get_width", 1),
                width_min_pixels=kwargs.get("width_min_pixels", 3),
                width_max_pixels=kwargs.get("width_max_pixels", 30),
            )
        return None

    # Define layers
    ALL_LAYERS = {
        "VillaZone": create_layer("HexagonLayer", "bike_rental_stats.json"),
        "Residential": create_layer("HexagonLayer", "bike_rental_stats.json"),
        "Multifamily": create_layer("HexagonLayer", "bike_rental_stats.json"),
        "Retail": create_layer("HexagonLayer", "bike_rental_stats.json"),
        "Industrial Parks": create_layer("HexagonLayer", "bike_rental_stats.json"),
        "Schools": create_layer("HexagonLayer", "bike_rental_stats.json"),
        "Heatmap": create_layer(
            "HeatmapLayer",
            "bike_rental_stats.json",
            get_weight="investment_potential" if "investment_potential" in from_data_file("bike_rental_stats.json").columns else None,
        ),
        "Bart Stop Exits": create_layer(
            "ScatterplotLayer",
            "bart_stop_stats.json",
            get_radius="[exits]" if "exits" in from_data_file("bart_stop_stats.json").columns else 100,
        ),
        "Bart Stop Names": create_layer("TextLayer", "bart_stop_stats.json"),
        "Outbound Flow": create_layer(
            "ArcLayer",
            "bart_path_stats.json",
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
        ),
    }

    # Select layers to display
    st.sidebar.subheader("Layer Visibility")
    selected_layers = [
        layer for layer_name, layer in ALL_LAYERS.items() if layer and st.sidebar.checkbox(layer_name, True)
    ]

    # Render the map with selected layers
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/streets-v11",
                initial_view_state={
                    "latitude": user_lat,
                    "longitude": user_lon,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
                tooltip={"html": "<b>Location:</b> {name}<br><b>Value:</b> {value}", "style": {"color": "white"}},
            )
        )
    else:
        st.warning("Please choose at least one layer to display.")

except URLError as e:
    st.error(f"Connection error: {e.reason}. Please ensure you have internet access.")











# Bar Chart for Key Metrics
def display_key_metrics_bar_chart(dataframe):
    """
    Displays a bar chart for key metrics.
    
    Args:
        dataframe (pd.DataFrame): A DataFrame containing metrics to display.
    """
    if dataframe.empty:
        st.warning("The data for the bar chart is empty. Please provide valid data.")
        return
    
    try:
        # Generate the Altair Bar Chart
        chart = (
            alt.Chart(dataframe)
            .mark_bar()
            .encode(
                x=alt.X("Metric:O", sort=None, title="Metric"),
                y=alt.Y("Value:Q", title="Value"),
                color=alt.Color("Metric:N", legend=None),  # Optional: Color by Metric
                tooltip=[
                    alt.Tooltip("Metric:O", title="Metric"),
                    alt.Tooltip("Value:Q", title="Value", format=",.2f"),  # Format with commas and decimals
                ],
            )
            .properties(
                title="Key Metrics Overview",  # Add a chart title
                width="container",  # Make the chart responsive
                height=400,
            )
            .interactive()
        )
        
        # Display the chart
        st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred while generating the chart: {str(e)}")

# Example usage
# Assuming `comparison_df` is a DataFrame with "Metric" and "Value" columns
if "Metric" in comparison_df.columns and "Value" in comparison_df.columns:
    display_key_metrics_bar_chart(comparison_df)
else:
    st.error("The required columns ('Metric' and 'Value') are missing in the data.")









# Sensitivity Analysis Section
st.subheader("Sensitivity Analysis")
st.write("Explore how changes in key variables affect property performance.")

# Enhanced Sensitivity Analysis Data Generation
try:
    # Define ranges for sensitivity analysis
    interest_rate_range = np.arange(2.5, 5.5, 0.5)  # Interest rates from 2.5% to 5.0%
    
    # Generate the sensitivity data
    sensitivity_data = {
        "Interest Rate (%)": [],
        "Monthly Payment ($)": []
    }
    
    for rate in interest_rate_range:
        metrics = calculate_metrics({
            "property_price": property_price,
            "annual_rent_income": annual_rent_income,
            "down_payment": down_payment,
            "closing_costs": 0,  # Optional or default
            "rehab_costs": 0,  # Optional or default
            "annual_property_taxes": annual_expenses.get("taxes", 0),
            "annual_insurance": annual_expenses.get("insurance", 0),
            "annual_utilities": annual_expenses.get("utilities", 0),
            "maintenance_perc": annual_expenses.get("maintenance_perc", 0),
            "capex_perc": annual_expenses.get("capex_perc", 0),
            "mgmt_perc": annual_expenses.get("mgmt_perc", 0),
            "vacancy_perc": annual_expenses.get("vacancy_perc", 0),
            "hoa_fees": annual_expenses.get("hoa_fees", 0),
            "interest_rate": rate,
            "loan_term": loan_term
        })
        sensitivity_data["Interest Rate (%)"].append(rate)
        sensitivity_data["Monthly Payment ($)"].append(metrics["Monthly Payment"])

    sensitivity_df = pd.DataFrame(sensitivity_data)

    # Plot the Sensitivity Analysis Chart
    st.line_chart(sensitivity_df.set_index("Interest Rate (%)"))

except Exception as e:
    st.error(f"Error generating sensitivity analysis: {str(e)}")

# AI Predictions Section
st.subheader("AI-Powered Predictions")
st.write("Leverage AI to forecast future returns, property appreciation, and investment performance.")

# Mock AI Predictions (Replace with real AI integration later)
ai_predictions = {
    "Predicted 5-Year Appreciation": "12.5%",
    "Predicted Rental Growth Rate (Next 5 Years)": "4.2% per year",
    "Risk Assessment Score": "Low Risk (Score: 2.1/10)"
}

# Display AI Predictions
for prediction, value in ai_predictions.items():
    st.write(f"**{prediction}:** {value}")

# Generate Reports Section
st.subheader("Downloadable Reports")
if st.button("Generate Investment Report"):
    try:
        # Placeholder for PDF generation logic
        st.success("Investment report has been generated and is ready for download!")
        # Use this to enable report download if a file is generated
        # st.download_button(label="Download Report", data=report_file, file_name="Investment_Report.pdf")
    except Exception as e:
        st.error(f"Error generating report: {str(e)}")











import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from urllib.error import URLError



# Function to generate random price data for distribution
def display_price_distribution(price_range):
    """
    Display a bar chart for real estate price distribution.
    
    Args:
        price_range (tuple): Minimum and maximum price range.
    """
    st.subheader("Real Estate Price Distribution")
    if st.checkbox("Show Price Distribution"):
        price_data = pd.DataFrame({
            "Price ($)": np.random.randint(price_range[0], price_range[1], 100)  # Generate more data points
        })
        st.bar_chart(price_data)


# Function to fetch and process UN data
@st.cache_data
def fetch_un_data():
    """
    Fetch GDP data from a remote server and preprocess it.
    
    Returns:
        pd.DataFrame: Processed GDP data.
    """
    try:
        AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(f"{AWS_BUCKET_URL}/agri.csv.gz")
        return df.set_index("Region")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()


# Function to visualize GDP data for selected countries
def display_gdp_data():
    """
    Display GDP data and visualize trends using Altair.
    """
    st.subheader("Gross Real Estate GDP Data")
    df = fetch_un_data()
    
    if df.empty:
        st.error("Failed to load GDP data.")
        return

    # Allow users to select countries
    countries = st.multiselect("Choose countries", list(df.index), ["United States of America", "Mexico", "Canada"])
    
    if not countries:
        st.error("Please select at least two countries to visualize GDP trends.")
    else:
        # Filter and process data for selected countries
        data = df.loc[countries] / 1_000_000.0  # Convert values to trillions
        st.dataframe(data.sort_index())

        # Prepare data for Altair chart
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(columns={
            "index": "Year", 
            "value": "GDP ($T)"
        })

        # Create Altair chart
        chart = alt.Chart(data).mark_area(opacity=0.3).encode(
            x=alt.X("Year:T", title="Year"),
            y=alt.Y("GDP ($T):Q", stack=None, title="Gross Real Estate GDP (Trillions)"),
            color=alt.Color("Region:N", title="Country"),
            tooltip=["Year", "Region:N", "GDP ($T):Q"]
        ).properties(title="GDP Trends by Country")
        
        st.altair_chart(chart, use_container_width=True)


# Main function to integrate both features
def main():
    st.title("Real Estate Data Visualization")

    # Price Distribution
    st.sidebar.header("Price Distribution Settings")
    price_min = st.sidebar.number_input("Minimum Price ($)", value=100_000, step=10_000)
    price_max = st.sidebar.number_input("Maximum Price ($)", value=1_000_000, step=50_000)
    price_range = (price_min, price_max)

    display_price_distribution(price_range)

    # GDP Data Visualization
    st.sidebar.header("GDP Data")
    display_gdp_data()


# Entry point
if __name__ == "__main__":
    main()










# Dynamic Line Chart with Progress Bar
def dynamic_line_chart_with_progress(total_steps=100, update_interval=0.1):
    """
    Generate a dynamic line chart with a progress bar and real-time updates.
    
    Args:
        total_steps (int): Total number of updates for the progress bar.
        update_interval (float): Time interval (in seconds) between updates.
    """
    st.sidebar.subheader("Progress Tracker")
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)
    
    for i in range(1, total_steps + 1):
        # Simulate new data points
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        
        # Update chart and progress bar
        status_text.text(f"Progress: {i}% complete")
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        
        # Pause for the specified interval
        time.sleep(update_interval)
    
    # Clean up progress bar and status text
    progress_bar.empty()
    status_text.text("Task completed!")

# Main application
def main():
    st.title("Dynamic Line Chart with Progress")
    st.write("Watch the progress bar and line chart update in real-time.")

    # User customization options
    total_steps = st.sidebar.slider("Total Steps", min_value=50, max_value=200, value=100, step=10)
    update_interval = st.sidebar.slider("Update Interval (Seconds)", min_value=0.01, max_value=1.0, value=0.1, step=0.01)

    # Generate the dynamic line chart
    dynamic_line_chart_with_progress(total_steps=total_steps, update_interval=update_interval)

if __name__ == "__main__":
    main()

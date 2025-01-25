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




import streamlit as st

# Sidebar Filters
st.sidebar.header("Filters")

# Property Location
st.sidebar.subheader("Location Details")
location_address = st.sidebar.text_input("Address", value="")
location_city = st.sidebar.text_input("City", value="")
location_state = st.sidebar.text_input("State", value="")
location_zip = st.sidebar.text_input("Zip Code", value="")

# Property Details
st.sidebar.subheader("Property Details")
price_range = st.sidebar.slider("Price Range ($)", 50000, 5000000, (100000, 1000000), step=50000)
bedrooms = st.sidebar.slider("Bedrooms", 1, 10, (2, 4))
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, (1, 3))
area_range = st.sidebar.slider("Living Area (sq ft)", 500, 10000, (1000, 5000), step=100)
land_area = st.sidebar.slider("Land Area (sq ft)", 1000, 50000, (5000, 20000), step=500)

# Financial Inputs
st.sidebar.header("Financial Details")
property_price = st.sidebar.number_input("Property Price ($)", value=300000, step=10000)
down_payment = st.sidebar.number_input("Down Payment ($)", value=60000, step=1000)
closing_costs = st.sidebar.number_input("Closing Costs ($)", value=5000, step=500)
rehab_costs = st.sidebar.number_input("Rehabilitation Costs ($)", value=10000, step=500)
annual_property_taxes = st.sidebar.number_input("Annual Property Taxes ($)", value=5000, step=500)
annual_insurance = st.sidebar.number_input("Annual Insurance ($)", value=1200, step=100)
annual_utilities = st.sidebar.number_input("Annual Utilities ($)", value=3000, step=500)
maintenance_costs = st.sidebar.number_input("Maintenance Costs (% of Rent)", value=10, step=1)
capital_expenditures = st.sidebar.number_input("Capital Expenditures (% of Rent)", value=10, step=1)
property_management_fee = st.sidebar.number_input("Property Management Fee (% of Rent)", value=8.0, step=0.1)
vacancy_rate = st.sidebar.number_input("Vacancy Rate (%)", value=5.0, step=0.1)

# Income & Loan Inputs
st.sidebar.subheader("Income and Loan Details")
annual_rent_income = st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000)
interest_rate = st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1)
loan_term = st.sidebar.number_input("Loan Term (Years)", value=30, step=1)

# Calculations
def calculate_metrics(price, rent, down, closing, rehab, taxes, insurance, utilities,
                      maintenance_perc, capex_perc, mgmt_perc, vacancy_perc, rate, term):
    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12

    # Mortgage Payment
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    annual_debt_service = monthly_payment * 12

    # Operating Expenses
    operating_expenses = taxes + insurance + utilities + (rent * (maintenance_perc + capex_perc + mgmt_perc) / 100)
    effective_gross_income = rent * (1 - vacancy_perc / 100)
    noi = effective_gross_income - operating_expenses

    # Cash Flow and Returns
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
        "Cash on Cash": cash_on_cash,
    }

# Perform Calculations
metrics = calculate_metrics(
    property_price, annual_rent_income, down_payment, closing_costs, rehab_costs,
    annual_property_taxes, annual_insurance, annual_utilities, maintenance_costs,
    capital_expenditures, property_management_fee, vacancy_rate, interest_rate, loan_term
)

# Display Metrics
st.header("Investment Metrics")
st.write(f"**Monthly Mortgage Payment:** ${metrics['Monthly Payment']:.2f}")
st.write(f"**Annual Debt Service:** ${metrics['Annual Debt Service']:.2f}")
st.write(f"**Operating Expenses:** ${metrics['Operating Expenses']:.2f}")
st.write(f"**Effective Gross Income:** ${metrics['Effective Gross Income']:.2f}")
st.write(f"**Net Operating Income (NOI):** ${metrics['NOI']:.2f}")
st.write(f"**Cash Flow:** ${metrics['Cash Flow']:.2f}")
st.write(f"**Cap Rate:** {metrics['Cap Rate']:.2f}%")
st.write(f"**Cash-on-Cash Return:** {metrics['Cash on Cash']:.2f}%")

# Summary Section
st.sidebar.subheader("Summary")
st.sidebar.write(f"**Location:** {location_address}, {location_city}, {location_state}, {location_zip}")
st.sidebar.write(f"**Property Price:** ${property_price:,.2f}")
st.sidebar.write(f"**Loan Amount:** ${property_price - down_payment:,.2f}")
st.sidebar.write(f"**Annual Rent Income:** ${annual_rent_income:,.2f}")
st.sidebar.write(f"**Vacancy Rate:** {vacancy_rate:.1f}%")









# Sensitivity Analysis Function
def sensitivity_analysis(rent_income, property_price, taxes, insurance, utilities, maintenance, vacancy_rate, interest_rate, term):
    """Perform sensitivity analysis on key variables like rent income and property price."""
    # Define ranges for sensitivity
    rent_range = np.linspace(rent_income * 0.8, rent_income * 1.2, 10)
    price_range = np.linspace(property_price * 0.8, property_price * 1.2, 10)

    # Create an empty DataFrame to store results
    results = []

    # Loop through ranges to calculate sensitivity for each combination
    for rent in rent_range:
        for price in price_range:
            metrics = calculate_metrics(
                price, rent, down_payment, closing_costs, rehab_costs,
                taxes, insurance, utilities, maintenance, capital_expenditures,
                property_management_fee, vacancy_rate, interest_rate, term
            )
            results.append({
                "Rent Income ($)": rent,
                "Property Price ($)": price,
                "Cap Rate (%)": metrics["Cap Rate"],
                "Cash-on-Cash Return (%)": metrics["Cash on Cash"],
                "NOI ($)": metrics["NOI"],
                "Cash Flow ($)": metrics["Cash Flow"]
            })

    # Convert results to a DataFrame
    df = pd.DataFrame(results)
    return df

# Call Sensitivity Analysis
try:
    sensitivity_df = sensitivity_analysis(
        annual_rent_income, property_price, annual_property_taxes,
        annual_insurance, annual_utilities, maintenance_costs,
        vacancy_rate, interest_rate, loan_term
    )
    # Display Sensitivity Results
    st.header("Sensitivity Analysis")
    st.write("Explore the impact of varying Rent Income and Property Price on investment metrics:")
    st.dataframe(sensitivity_df)
except Exception as e:
    st.error(f"Error performing sensitivity analysis: {e}")






# Map Integration
st.subheader("Investment Heatmap")
city_data = pd.DataFrame({
    "City": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "San Jose"],
    "Latitude": [34.0522, 37.7749, 32.7157, 38.5816, 37.3382],
    "Longitude": [-118.2437, -122.4194, -117.1611, -121.4944, -121.8863],
    "Value": [75, 85, 70, 65, 80]
})

st.map(city_data)

# Downloadable Report
def generate_report(metrics):
    report_df = pd.DataFrame.from_dict(metrics, orient='index', columns=['Value'])
    return report_df.to_csv().encode('utf-8')

download_csv = generate_report(metrics)
st.download_button(
    label="Download Investment Report",
    data=download_csv,
    file_name="investment_report.csv",
    mime="text/csv"
)








# Display Metrics
st.header("Metrics")
st.write(f"**Capitalization Rate:** {cap_rate:.2f}%")
st.write(f"**Cash-on-Cash Return:** {cash_on_cash:.2f}%")
st.write(f"**Monthly Mortgage Payment:** ${monthly_payment:,.2f}")
st.write(f"**Net Operating Income (NOI):** ${noi:,.2f}")# Display Comprehensive Metrics
st.header("Comprehensive Metrics")

# Core Metrics
st.write(f"**Capitalization Rate (Cap Rate):** {cap_rate:.2f}%")
st.write(f"**Cash-on-Cash Return (CoC):** {cash_on_cash:.2f}%")
st.write(f"**Monthly Mortgage Payment:** ${monthly_payment:,.2f}")
st.write(f"**Net Operating Income (NOI):** ${noi:,.2f}")
st.write(f"**Effective Gross Income (EGI):** ${metrics['Effective Gross Income']:.2f}")
st.write(f"**Operating Expenses:** ${metrics['Operating Expenses']:.2f}")
st.write(f"**Annual Debt Service (Mortgage):** ${metrics['Annual Debt Service']:.2f}")
st.write(f"**Total Cash Flow:** ${metrics['Cash Flow']:.2f}")

# Equity & Leverage Metrics
ltv_ratio = ((property_price - down_payment) / property_price) * 100
st.write(f"**Loan-to-Value Ratio (LTV):** {ltv_ratio:.2f}%")
equity_build_up = down_payment + metrics['Cash Flow'] * loan_term
st.write(f"**Equity Build-Up Over Loan Term:** ${equity_build_up:,.2f}")

# Profitability Metrics
grm = property_price / annual_rent_income
st.write(f"**Gross Rent Multiplier (GRM):** {grm:.2f}")
cash_flow_margin = (metrics['Cash Flow'] / metrics['Effective Gross Income']) * 100
st.write(f"**Cash Flow Margin:** {cash_flow_margin:.2f}%")

# Risk & Break-Even Analysis
ber = ((metrics['Operating Expenses'] + metrics['Annual Debt Service']) / metrics['Effective Gross Income']) * 100
st.write(f"**Break-Even Ratio (BER):** {ber:.2f}%")
break_even_rent = (metrics['Operating Expenses'] + metrics['Annual Debt Service']) / (1 - vacancy_rate / 100)
st.write(f"**Break-Even Rent Per Year:** ${break_even_rent:,.2f}")
st.write(f"**Break-Even Rent Per Month:** ${(break_even_rent / 12):,.2f}")

# Advanced Metrics
debt_coverage_ratio = metrics['NOI'] / metrics['Annual Debt Service']
st.write(f"**Debt Coverage Ratio (DCR):** {debt_coverage_ratio:.2f}")
total_investment = down_payment + closing_costs + rehab_costs
st.write(f"**Total Investment:** ${total_investment:,.2f}")

# Return Metrics
irr = metrics["Internal Rate of Return"]
npv = metrics["Net Present Value"]
st.write(f"**Internal Rate of Return (IRR):** {irr:.2f}%")
st.write(f"**Net Present Value (NPV):** ${npv:,.2f}")

# Visualizations
st.subheader("Metric Comparisons")

# Metrics DataFrame for Visualization
comparison_df = pd.DataFrame({
    "Metric": [
        "Cap Rate (%)", "CoC Return (%)", "Cash Flow ($)", 
        "NOI ($)", "Break-Even Rent ($)", "LTV (%)", 
        "Debt Coverage Ratio", "GRM"
    ],
    "Value": [
        cap_rate, cash_on_cash, metrics['Cash Flow'], 
        metrics['NOI'], break_even_rent, ltv_ratio, 
        debt_coverage_ratio, grm
    ]
})

# Bar Chart for Key Metrics
chart = alt.Chart(comparison_df).mark_bar().encode(
    x=alt.X("Metric", sort=None, title="Metric"),
    y=alt.Y("Value", title="Value"),
    tooltip=["Metric", "Value"]
).interactive()
st.altair_chart(chart, use_container_width=True)

# Sensitivity Analysis
st.subheader("Sensitivity Analysis")
st.write("Explore how changes in key variables affect property performance.")

# Sensitivity Analysis Example Data
sensitivity_df = pd.DataFrame({
    "Interest Rate (%)": [2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
    "Monthly Payment ($)": [
        calculate_metrics(property_price, annual_rent_income, annual_expenses, down_payment, rate, loan_term)[2]
        for rate in [2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    ]
})
st.line_chart(sensitivity_df.set_index("Interest Rate (%)"))

# AI Predictions
st.subheader("AI-Powered Predictions")
st.write("Leverage AI to forecast future returns, property appreciation, and investment performance.")

# Placeholder for AI Model Integration
st.write("**Predicted 5-Year Appreciation:** 12.5%")
st.write("**Predicted Rental Growth Rate (Next 5 Years):** 4.2% per year")
st.write("**Risk Assessment Score:** Low Risk (Score: 2.1/10)")

# Generate Reports
st.subheader("Downloadable Reports")
if st.button("Generate Investment Report"):
    # Placeholder for PDF generation function
    st.success("Investment report has been generated and is ready for download!")
    # st.download_button(label="Download Report", data=report_file, file_name="Investment_Report.pdf")







# Visualization: Real Estate Price Distribution
if st.checkbox("Show Price Distribution"):
    price_data = pd.DataFrame({"Price ($)": np.random.randint(price_range[0], price_range[1], 50)})
    st.bar_chart(price_data)

# Data: Gross Real Estate GDP 
@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

try:
    df = get_UN_data()
    countries = st.multiselect("Choose countries", list(df.index), ["United States of America", "Mexico", "Canada",])
    if not countries:
        st.error("Please select at least Two countries.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.subheader("Gross Real Estate GDP ($T)")
        st.dataframe(data.sort_index())

        # Altair chart
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(columns={"index": "year", "value": "Gross Agricultural Production ($B)"})
        chart = alt.Chart(data).mark_area(opacity=0.3).encode(
            x="year:T",
            y=alt.Y("Gross Agricultural Production ($B):Q", stack=None),
            color="Region:N",
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(f"This demo requires internet access. Connection error: {e.reason}")



# Dynamic Line Chart with Progress Bar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()





# Mapping
## 









@st.cache_data
def from_data_file(filename):
    url = (
        "https://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)

try:
    ALL_LAYERS = {
"VillaZone": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
"Residential": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
"Multifamily": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
"Retail": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
 "Industrial Parks": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
 "Schools": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Bike rentals": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Bart stop exits": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        "Bart stop names": pdk.Layer(
            "TextLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_text="name",
            get_color=[0, 0, 0, 200],
            get_size=10,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[200, 30, 0, 160],
            get_target_color=[200, 30, 0, 160],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound",
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }
    st.sidebar.subheader("Map layers")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style=None,
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
    else:
        st.error("Please choose at least one layer above.")
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )





 

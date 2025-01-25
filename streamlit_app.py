import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import time
from urllib.error import URLError


###########  Header Start ############################

import streamlit as st

st.markdown(
    """
    <style>
        /* Dropdown Button Styling */
        .dropdown-button {
            background-color: #007BFF;
            color: white;
            font-size: 12px;
            font-weight: bold;
            padding: 10px 15px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.22);
            transition: all 0.3s ease-in-out;
            text-align: center;
        }

        .dropdown-button:hover {
            background-color: #0056b3;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }

        /* Dropdown Menu Styling */
        .dropdown-container {
            position: absolute;
            top: 20px;
            right: 20px; /* Aligns the dropdown container to the right-hand side */
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f8f9fa;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            margin-top: 10px;
            min-width: 220px;
            z-index: 1;
            right: 0; /* Aligns the dropdown content to the right edge of the button */
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
    """,
    unsafe_allow_html=True
)

###########  Header End ############################






# Sidebar Filters
st.sidebar.header("Filters")
price_range = st.sidebar.slider("Price Range ($)", 50000, 5000000, (100000, 1000000), step=50000)
bedrooms = st.sidebar.slider("Bedrooms", 1, 10, (2, 4))
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, (1, 3))
area_range = st.sidebar.slider("Area (sq ft)", 500, 10000, (1000, 5000), step=100)

# Financial Inputs
st.sidebar.header("Financial Details")
property_price = st.sidebar.number_input("Property Price ($)", value=300000, step=10000)
annual_rent_income = st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000)
annual_expenses = st.sidebar.number_input("Annual Expenses ($)", value=5000, step=1000)
down_payment = st.sidebar.number_input("Down Payment ($)", value=60000, step=1000)
interest_rate = st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1)
loan_term = st.sidebar.number_input("Loan Term (Years)", value=30, step=1)

# Calculations
def calculate_metrics(price, rent, expenses, down, rate, term):
    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    noi = rent - expenses
    cap_rate = (noi / price) * 100
    cash_on_cash = (noi / down) * 100
    return cap_rate, cash_on_cash, monthly_payment, noi

cap_rate, cash_on_cash, monthly_payment, noi = calculate_metrics(
    property_price, annual_rent_income, annual_expenses, down_payment, interest_rate, loan_term
)

# Display Metrics
st.header("Metrics")
st.write(f"**Capitalization Rate:** {cap_rate:.2f}%")
st.write(f"**Cash-on-Cash Return:** {cash_on_cash:.2f}%")
st.write(f"**Monthly Mortgage Payment:** ${monthly_payment:,.2f}")
st.write(f"**Net Operating Income (NOI):** ${noi:,.2f}")

# Visualization: Price Distribution
if st.checkbox("Show Price Distribution"):
    price_data = pd.DataFrame({"Price ($)": np.random.randint(price_range[0], price_range[1], 50)})
    st.bar_chart(price_data)

# Data: Gross Agricultural Production
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
@st.cache_data
def from_data_file(filename):
    url = "https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/%s" % filename
    return pd.read_json(url)

try:
    ALL_LAYERS = {
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
    }
    st.sidebar.subheader("Map layers")
    selected_layers = [
        layer for layer_name, layer in ALL_LAYERS.items() if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style=None,
                initial_view_state={"latitude": 37.76, "longitude": -122.4, "zoom": 11, "pitch": 50},
                layers=selected_layers,
            )
        )
    else:
        st.error("Please choose at least one layer above.")
except URLError as e:
    st.error(f"Connection error: {e.reason}")

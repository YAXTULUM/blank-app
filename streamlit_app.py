import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import time
from urllib.error import URLError


###########  Header Start ############################

# App Configuration
st.set_page_config(page_title="VillaTerras Ai Real Estate Dashboard", layout="wide")

# Header Section
def render_header():
    st.markdown(
        """
        <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #f8f9fa;
            border-bottom: 2px solid #ddd;
        }
        .logo-container img {
            height: 150px;
            width: auto;
        }
        .menu-container a {
            margin-left: 20px;
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
            font-size: 16px;
        }
        .menu-container a:hover {
            color: #0056b3;
            text-decoration: underline;
        }
        </style>
        <div class="header-container">
            <div class="logo-container">
                <a href="/"><img src="https://i0.wp.com/villaterras.com/wp-content/uploads/2024/11/cropped-VillaTerra-Logo.png?resize=264%2C264&ssl=1" alt="VillaTerras Logo"></a>
            </div>
            <div class="menu-container">
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

# Call the header rendering function
render_header()

# Title and Description
st.title("VillaTerras Ai Real Estate Dashboard")
st.markdown(
    """
    Welcome to the **VillaTerras Ai Real Estate Dashboard**.  
    All Real Estate Knowledge in One Place.  
    Analyze, compare, and manage properties with advanced metrics and tools.
    """
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

# Data: Real Estate GDP
@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

try:
    df = get_UN_data()
    countries = st.multiselect("Choose countries", list(df.index), ["United States of America" "Mexico", "Canada",])
    if not countries:
        st.error("Please select at least Two countries.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.subheader("Real Estate GDP ($T)")
        st.dataframe(data.sort_index())

        # Altair chart
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(columns={"index": "year", "value": "Real Estate GDP ($T)"})
        chart = alt.Chart(data).mark_area(opacity=0.3).encode(
            x="year:T",
            y=alt.Y("Gross Real Estate GDP ($T):Q", stack=None),
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

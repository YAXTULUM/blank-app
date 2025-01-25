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





# Function to generate mock data for California's growing cities
@st.cache_data
def california_investment_data():
    data = pd.DataFrame({
        "city": [
            "San Francisco", "Los Angeles", "San Diego", "San Jose", "Fresno",
            "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim",
            "Santa Ana", "Riverside", "Stockton", "Irvine", "Chula Vista",
            "Fremont", "San Bernardino", "Modesto", "Fontana", "Oxnard",
            "Moreno Valley", "Glendale", "Huntington Beach", "Santa Clarita", "Garden Grove"
        ],
        "lat": [
            37.7749, 34.0522, 32.7157, 37.3382, 36.7378,
            38.5816, 33.7701, 37.8044, 35.3733, 33.8366,
            33.7455, 33.9806, 37.9577, 33.6846, 32.6401,
            37.5485, 34.1083, 37.6391, 34.0922, 34.1975,
            33.9425, 34.1425, 33.6595, 34.3917, 33.7743
        ],
        "lon": [
            -122.4194, -118.2437, -117.1611, -121.8863, -119.7871,
            -121.4944, -118.1937, -122.2711, -119.0187, -117.9145,
            -117.8677, -117.3755, -121.2908, -117.8265, -117.0842,
            -121.9886, -117.2898, -120.9969, -117.4350, -119.1771,
            -117.2297, -118.2551, -117.9988, -118.5426, -117.9379
        ],
        "investment_value": [
            80, 95, 85, 88, 75,
            82, 78, 81, 74, 89,
            83, 80, 76, 90, 79,
            84, 77, 73, 76, 72,
            70, 69, 86, 88, 68
        ],
    })
    return data

# Load the California investment data
california_data = california_investment_data()

# Display the raw data
st.subheader("California Investment Data")
st.dataframe(california_data)

# Heat Map Layer
heatmap_layer = pdk.Layer(
    "HeatmapLayer",
    data=california_data,
    get_position=["lon", "lat"],
    get_weight="investment_value",
    radius=200,
    opacity=0.8,
    aggregation="MEAN",
)

# Scatterplot Layer (Optional for city markers)
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=california_data,
    get_position=["lon", "lat"],
    get_radius=500,
    get_color="[200, 30, 0, 160]",
    pickable=True,
)

# Set the view state
view_state = pdk.ViewState(
    latitude=36.7783,  # Center latitude of California
    longitude=-119.4179,  # Center longitude of California
    zoom=6,
    pitch=50,
)

# Render the map
st.header("California Investment Heat Map")
st.pydeck_chart(
    pdk.Deck(
        layers=[heatmap_layer, scatter_layer],
        initial_view_state=view_state,
        tooltip={
            "html": "<b>City:</b> {city}<br><b>Investment Value:</b> {investment_value}",
            "style": {"color": "white"}
        },
    )
)

# Highlight Best Cities to Invest
st.subheader("Top 5 Cities to Invest")
top_cities = california_data.nlargest(5, "investment_value")[["city", "investment_value"]]
st.table(top_cities)

















import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

# Mock advanced data for 25 cities in California
@st.cache_data
def get_advanced_data():
    return pd.DataFrame({
        "City": [
            "Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno",
            "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim",
            "Stockton", "Riverside", "Irvine", "Santa Ana", "Chula Vista",
            "Fremont", "Santa Clarita", "San Bernardino", "Modesto", "Fontana",
            "Oxnard", "Moreno Valley", "Glendale", "Huntington Beach", "Ontario"
        ],
        "Latitude": [
            34.0522, 32.7157, 37.3382, 37.7749, 36.7378,
            38.5816, 33.7701, 37.8044, 35.3733, 33.8366,
            37.9577, 33.9806, 33.6846, 33.7455, 32.6401,
            37.5485, 34.3917, 34.1083, 37.6391, 34.0922,
            34.1975, 33.9425, 34.1425, 33.6595, 34.0633
        ],
        "Longitude": [
            -118.2437, -117.1611, -121.8863, -122.4194, -119.7871,
            -121.4944, -118.1937, -122.2711, -119.0187, -117.9145,
            -121.2908, -117.3755, -117.8265, -117.8677, -117.0842,
            -121.9886, -118.5426, -117.2898, -120.9969, -117.4350,
            -119.1771, -117.2297, -118.2551, -117.9988, -117.6509
        ],
        "Population Growth (%)": np.random.uniform(0.5, 3.5, 25),
        "Median Home Price ($)": np.random.randint(300000, 1500000, 25),
        "Average Rental Yield (%)": np.random.uniform(2.5, 6.0, 25),
        "Employment Rate (%)": np.random.uniform(80, 95, 25)
    })

# Load data
data = get_advanced_data()

# Sidebar filters
st.sidebar.header("Filters")
growth_filter = st.sidebar.slider("Population Growth (%)", 0.5, 3.5, (1.0, 3.0))
rental_yield_filter = st.sidebar.slider("Rental Yield (%)", 2.5, 6.0, (3.0, 5.0))
price_filter = st.sidebar.slider("Median Home Price ($)", 300000, 1500000, (500000, 1000000))

# Apply filters
filtered_data = data[
    (data["Population Growth (%)"].between(*growth_filter)) &
    (data["Average Rental Yield (%)"].between(*rental_yield_filter)) &
    (data["Median Home Price ($)"].between(*price_filter))
]

# Heatmap Layer
heatmap_layer = pdk.Layer(
    "HeatmapLayer",
    data=filtered_data,
    get_position=["Longitude", "Latitude"],
    get_weight="Population Growth (%)",
    radius=300,
    opacity=0.7,
    aggregation="MEAN"
)

# Scatterplot Layer
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_data,
    get_position=["Longitude", "Latitude"],
    get_radius=500,
    get_color="[200, 30, 0, 160]",
    pickable=True
)

# View State
view_state = pdk.ViewState(
    latitude=36.7783,
    longitude=-119.4179,
    zoom=6,
    pitch=40
)

# Render Map
st.header("California Advanced Real Estate Heatmap")
st.pydeck_chart(pdk.Deck(
    layers=[heatmap_layer, scatter_layer],
    initial_view_state=view_state,
    tooltip={
        "html": "<b>City:</b> {City}<br>"
                "<b>Population Growth:</b> {Population Growth (%)},<br>"
                "<b>Median Price:</b> {Median Home Price ($)}",
        "style": {"color": "white"}
    }
))

# Show Filtered Table
st.subheader("Filtered Data")
st.dataframe(filtered_data)





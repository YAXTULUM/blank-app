# Enhanced Debug: Financial Details
st.subheader("📊 Debug: Financial Details")
st.markdown(
    """
    <style>
        .details-container {
            background: linear-gradient(135deg, #ffffff, #e8f1f7);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .details-header {
            font-size: 1.5em;
            font-weight: bold;
            text-align: center;
            color: #0056b3;
            margin-bottom: 15px;
        }
        .details-table {
            width: 100%;
            border-collapse: collapse;
        }
        .details-table th, .details-table td {
            text-align: left;
            padding: 12px 15px;
            border: 1px solid #dde5ed;
        }
        .details-table th {
            background: #0056b3;
            color: white;
            font-weight: bold;
        }
        .details-table tr:nth-child(even) {
            background: #f9f9f9;
        }
        .details-table tr:hover {
            background: #f1f7fc;
        }
        .details-value {
            font-weight: bold;
            color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Convert financial details dictionary to a DataFrame for a clean display
details_df = pd.DataFrame(list(financial_details.items()), columns=["Detail", "Value"])

# Display the financial details in a custom-styled container
st.markdown('<div class="details-container">', unsafe_allow_html=True)
st.markdown('<div class="details-header">Financial Details Overview</div>', unsafe_allow_html=True)
st.markdown(details_df.to_html(index=False, classes="details-table"), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


###########  Header End ############################

# --- Sidebar Configuration ---
def configure_sidebar():
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


# --- Main Function ---
def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with detailed metrics and sensitivity analysis.")

    location_details, property_details, financial_details = configure_sidebar()

    st.subheader("Debug: Financial Details")
    st.json(financial_details)

if __name__ == "__main__":
    main()

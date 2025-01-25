import streamlit as st
import pandas as pd
from backend import calculate_metrics, ai_assistant


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
        "interest_rate": st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1, key="interest_rate"),
        "loan_term": st.sidebar.number_input("Loan Term (Years)", value=30, step=1, key="loan_term"),
        "annual_rent_income": st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000, key="rent_income"),
    }

    return location_details, property_details, financial_details


def main():
    st.title("Real Estate Investment Calculator with AI")
    st.markdown("Analyze, compare, and manage your real estate investments.")

    # Sidebar Configuration
    location_details, property_details, financial_details = configure_sidebar()

    # Metrics Calculation
    try:
        metrics = calculate_metrics(financial_details)
        st.subheader("Investment Metrics")
        metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
        st.table(metrics_df)
    except Exception as e:
        st.error(f"Error calculating metrics: {e}")

    # AI Assistant
    st.subheader("🤖 Ask the AI Assistant")
    user_question = st.text_input("Ask any real estate-related question:")
    if user_question:
        with st.spinner("Generating AI response..."):
            ai_response = ai_assistant(user_question)
        st.markdown(f"**AI Response:** {ai_response}")


if __name__ == "__main__":
    main()

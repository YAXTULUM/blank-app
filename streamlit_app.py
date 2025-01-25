import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- Styling Section ---
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .title-section {
            background: linear-gradient(135deg, #4c88d2, #5ba2f7);
            color: white;
            text-align: center;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        .details-container {
            background: linear-gradient(135deg, #ffffff, #e8f1f7);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
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
            padding: 12px 15px;
            border: 1px solid #dde5ed;
            text-align: left;
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
    </style>
    """,
    unsafe_allow_html=True,
)

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
        "interest_rate": st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1, key="interest_rate"),
        "loan_term": st.sidebar.number_input("Loan Term (Years)", value=30, step=1, key="loan_term"),
        "annual_rent_income": st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000, key="rent_income"),
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
    hoa_fees = financial_details["hoa_fees"] * 12
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
def main():
    st.markdown('<div class="title-section"><h1>Real Estate Investment Calculator</h1></div>', unsafe_allow_html=True)

    location_details, property_details, financial_details = configure_sidebar()

    st.subheader("📊 Debug: Financial Details")
    st.json(financial_details)

    metrics = calculate_metrics(financial_details)
    st.subheader("Investment Metrics")
    st.table(pd.DataFrame(metrics.items(), columns=["Metric", "Value"]))

if __name__ == "__main__":
    main()

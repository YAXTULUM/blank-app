import openai
import numpy as np
import pandas as pd

 

def calculate_metrics(financial_details):
    """Calculate key financial metrics for a real estate investment."""
    try:
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
    except Exception as e:
        return {"error": str(e)}


def ai_assistant(prompt):
    """Connects to OpenAI API to generate AI responses for real estate questions."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

import streamlit as st

from app_functions import convert

st.title("Convertisseur de devises")

rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130
}

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", rates.keys())
to_currency = st.selectbox("Vers :", rates.keys())

if st.button("Convertir"):
    result = convert(amount, from_currency, to_currency, rates)
    if result is None:
        st.error("Le montant doit être strictement supérieur à 0.")
    else:
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
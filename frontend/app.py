import streamlit as st
from backend.app_functions import rates, convert

st.title("Convertisseur de devises")

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", rates.keys())
to_currency = st.selectbox("Vers :", rates.keys())

if st.button("Convertir"):
    result = amount * rates[to_currency] / rates[from_currency]
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
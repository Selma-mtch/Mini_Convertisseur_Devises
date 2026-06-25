import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.app_functions import rates, convert

st.title("Convertisseur de devises")

currencies = list(rates.keys())

if "from_currency" not in st.session_state:
    st.session_state.from_currency = "EUR"

if "to_currency" not in st.session_state:
    st.session_state.to_currency = "USD"

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")

if st.button("Inverser"):
    st.session_state.from_currency, st.session_state.to_currency = (
        st.session_state.to_currency,
        st.session_state.from_currency
    )

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "De :",
        currencies,
        index=currencies.index(st.session_state.from_currency),
        key="from_currency"
    )

with col2:
    to_currency = st.selectbox(
        "Vers :",
        currencies,
        index=currencies.index(st.session_state.to_currency),
        key="to_currency"
    )

if st.button("Convertir"):
    result = convert(amount, from_currency, to_currency)
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
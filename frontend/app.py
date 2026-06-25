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
from backend.app_functions import rates, convert, format_history

st.title("Convertisseur de devises")

if "history" not in st.session_state:
    st.session_state.history = []

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
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    try:
        result = convert(amount, from_currency, to_currency, rates)
    except ValueError:
        st.warning(f"Devises identiques ({from_currency}) : choisissez deux devises différentes.")
    else:
        if result is None:
            st.error(f"Montant invalide ({amount:.2f}) : il doit être strictement supérieur à 0.")
        else:
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            st.session_state.history.append(
                format_history(amount, from_currency, to_currency, result)
            )

if st.session_state.history:
    st.subheader("Historique")
    for line in reversed(st.session_state.history):
        st.write(line)

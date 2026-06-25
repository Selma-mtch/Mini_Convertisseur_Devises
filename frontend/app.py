import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.app_functions import get_rates, convert, format_history

st.title("Convertisseur de devises")


@st.cache_data(ttl=3600)
def load_rates():
    return get_rates()


rates = load_rates()
currencies = [c for c in ["EUR", "USD", "JPY", "GBP", "CAD"] if c in rates]

if "from_currency" not in st.session_state:
    st.session_state.from_currency = "EUR"

if "to_currency" not in st.session_state:
    st.session_state.to_currency = "USD"

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
    from_currency = st.selectbox("De :", currencies, key="from_currency")

with col2:
    to_currency = st.selectbox("Vers :", currencies, key="to_currency")

if st.button("Convertir"):
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

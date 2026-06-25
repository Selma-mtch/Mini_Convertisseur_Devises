import streamlit as st
from backend.app_functions import rates, convert, format_history

st.title("Convertisseur de devises")

if "history" not in st.session_state:
    st.session_state.history = []

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", rates.keys())
to_currency = st.selectbox("Vers :", rates.keys())

if st.button("Convertir"):
    try:
        result = convert(amount, from_currency, to_currency, rates)
    except ValueError as e:
        st.error(str(e))
    else:
        if result is None:
            st.error("Le montant doit être strictement supérieur à 0.")
        else:
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            st.session_state.history.append(
                format_history(amount, from_currency, to_currency, result)
            )

if st.session_state.history:
    st.subheader("Historique")
    for line in reversed(st.session_state.history):
        st.write(line)
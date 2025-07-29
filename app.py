import streamlit as st
import pandas as pd

# Load the CSV from the local file uploaded in Streamlit Cloud
@st.cache_data
def load_wallet_data():
    df = pd.read_csv("wallet_region.csv")
    # Optionally, clean up columns (strip spaces, etc.)
    df.columns = df.columns.str.strip()
    return df

df = load_wallet_data()

st.title("Wallet Region Lookup")

wallet = st.text_input("Enter your wallet address:")

if wallet:
    match = df[df['wallet'].str.lower() == wallet.strip().lower()]
    if not match.empty:
        region = match['region'].values[0]
        st.success(f"Region: {region}")
    else:
        st.warning("Wallet not found.")

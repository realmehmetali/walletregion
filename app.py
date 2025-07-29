import streamlit as st
from google.oauth2 import service_account
import pandas as pd
from pandas_gbq import read_gbq
import json

service_account_info = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(dict(service_account_info))

# Your query
query = """
SELECT 1
FROM `pi-home-1718508233284.112233.walletregion`
"""

@st.cache_data
def load_wallet_data():
    df = read_gbq(query, project_id='pi-home-1718508233284', credentials=credentials)
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

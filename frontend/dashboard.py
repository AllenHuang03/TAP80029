import streamlit as st
import requests
import plotly.io as pio

st.title("Astronomical Data Dashboard")

# Fetch JSON data from API
response = requests.get("http://127.0.0.1:5000/plot")
fig_json = response.json()

# Convert JSON to Plotly figure
fig = pio.from_json(fig_json)

# Display in Streamlit
st.plotly_chart(fig)

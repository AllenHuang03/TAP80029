from flask import Flask, render_template, redirect, url_for
import plotly.express as px
import plotly.io as pio
import os
import pandas as pd
from updater import download_latest_data

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('plot'))  # Redirect to the plot page

@app.route('/plot')
def plot():
    # Run update before serving the page
    download_latest_data()

    # Path to dataset
    data_path = "data/observations/exoplanets.csv"

    # Check if the dataset exists
    if os.path.exists(data_path):
        try:
            df = pd.read_csv(data_path, comment="#")  # Skip commented lines in CSV
            if 'pl_name' in df.columns and 'pl_orbper' in df.columns:
                df = df[['pl_name', 'pl_orbper']].dropna()
                df = df.sort_values(by='pl_orbper')
                fig = px.scatter(df, x='pl_name', y='pl_orbper', title="Exoplanet Orbital Periods")
            else:
                raise ValueError("Missing required columns")
        except Exception as e:
            print(f"⚠️ Error loading dataset: {e}")
            df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 15, 30]})  # Default sample data
            fig = px.line(df, x='x', y='y', title="Sample Data (Error Loading File)")
    else:
        print("⚠️ No dataset found. Using sample data.")
        df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 15, 30]})
        fig = px.line(df, x='x', y='y', title="Sample Data")

    # Convert figure to JSON for Plotly
    graph_json = pio.to_json(fig)

    return render_template("plot.html", graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, jsonify
import plotly.express as px
import pandas as pd

viz = Blueprint("viz", __name__)

@viz.route("/plot")
def get_plot():
    time = range(100)
    flux = [x**0.5 for x in time]
    df = pd.DataFrame({"Time": time, "Flux": flux})

    fig = px.line(df, x="Time", y="Flux", title="Live Pulsar Data")
    return jsonify(fig.to_json())

from flask import Flask, jsonify, render_template
from app.data_ingestion import load_csv, preprocess_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def get_data():
    df = load_csv("data/processed/processed_observations.csv")
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

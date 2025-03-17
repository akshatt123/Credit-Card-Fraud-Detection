from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import joblib  # To load the trained model
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("fraud_model.pkl")  # Ensure the trained model is saved as fraud_model.pkl
scaler = joblib.load("scaler.pkl")  # Ensure the scaler is saved as scaler.pkl

# Home route - Render the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API - Accepts JSON input
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Preprocess the input
        df_scaled = scaler.transform(df)

        # Make prediction
        prediction = model.predict(df_scaled)

        # Return result as JSON
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Initialize Flask app
app = Flask(__name__)

# Load dataset
crop = pd.read_csv("Crop_recommendation.csv")

# Encoding Crop Labels
crop_dict = {
    'rice': 1, 'maize': 2, 'jute': 3, 'cotton': 4, 'coconut': 5,
    'papaya': 6, 'orange': 7, 'apple': 8, 'muskmelon': 9, 'watermelon': 10,
    'grapes': 11, 'mango': 12, 'banana': 13, 'pomegranate': 14, 'lentil': 15,
    'blackgram': 16, 'mungbean': 17, 'mothbeans': 18, 'pigeonpeas': 19, 
    'kidneybeans': 20, 'chickpea': 21, 'coffee': 22
}
crop['label'] = crop['label'].map(crop_dict)

# Splitting Data
X = crop.drop('label', axis=1)
y = crop['label']

# Standard Scaling
sc = StandardScaler()
X_scaled = sc.fit_transform(X)

# Train RandomForest Model
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_scaled, y)

# Save Model and Scaler
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(sc, open("scaler.pkl", "wb"))

# Load Model & Scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Reverse Mapping for Crop Names
reverse_crop_dict = {v: k for k, v in crop_dict.items()}

@app.route('/')
def home():
    return render_template("index.html")  # Load frontend

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from frontend
        data = [float(request.form.get(i)) for i in ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
        print("Input Data:", data)  # Debugging Line

        # Scale the data
        data_scaled = scaler.transform([data])
        print("Scaled Data:", data_scaled)  # Debugging Line

        # Predict the crop
        prediction = model.predict(data_scaled)
        print("Raw Prediction Output:", prediction)  # Debugging Line

        # Get crop name from encoded value
        crop_name = reverse_crop_dict[prediction[0]]
        print("Final Predicted Crop:", crop_name)  # Debugging Line

        return render_template("index.html", prediction_text=f"Recommended Crop: {crop_name}")
    
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)

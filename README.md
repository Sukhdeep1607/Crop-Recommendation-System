🌱 Crop Recommendation System
Python
Flask
Scikit-Learn
Render

The Crop Recommendation System is a machine learning-based web application that recommends the best crop to grow based on soil and environmental conditions. It uses a RandomForestClassifier trained on agricultural data to provide accurate predictions.

🚀 Features
User-Friendly Interface: Simple and intuitive web interface for inputting soil and environmental parameters.

Accurate Predictions: Machine learning model trained on real-world agricultural data.

Fast & Scalable: Built with Flask and deployed on Render for high performance.

Input Validation: Ensures valid input ranges for accurate predictions.

🛠️ Tech Stack
Frontend: HTML, CSS

Backend: Flask (Python)

Machine Learning: Scikit-Learn, RandomForestClassifier

Deployment: Render

Data Processing: Pandas, NumPy

🖥️ How to Use
1. Live Demo
You can access the live deployment of the project here:
https://crop-recommender-poe1.onrender.com/

2. Run Locally
To run the project on your local machine:

Clone the repository:

bash
Copy
git clone https://github.com/Sukhdeep1607/Crop-Recommendation-System.git
Install dependencies:

bash
Copy
pip install -r requirements.txt
Run the Flask app:

bash
Copy
python app.py
Open your browser:
Visit http://127.0.0.1:5000 to access the application.

📊 Input Parameters
The system takes the following inputs:

Parameter	Description	Range
Nitrogen (N)	Nitrogen content in soil	0 - 140
Phosphorus (P)	Phosphorus content in soil	5 - 145
Potassium (K)	Potassium content in soil	5 - 205
Temperature	Temperature in °C	8.8 - 43.7
Humidity	Relative humidity in %	14.3 - 99.9
pH	Soil pH level	3.5 - 9.9
Rainfall	Rainfall in mm	20.2 - 298.6
🤖 Machine Learning Model
Algorithm: RandomForestClassifier

Features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, Rainfall

Target: Crop label (22 unique crops)

Accuracy: >99% (on the training dataset)

🚀 Deployment
This project is deployed on Render. To deploy your own instance:

Fork this repository.

Create a new Web Service on Render and connect your GitHub repository.

Use the following settings:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Deploy!

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Dataset: Crop Recommendation Dataset

Flask Documentation: Flask

Scikit-Learn Documentation: Scikit-Learn

📧 Contact
For questions or feedback, feel free to reach out:

Your Name

Email: ssingh6_be21@thapar.edu

GitHub: Sukhdeep1607

Enjoy using the Crop Recommendation System! 🌾
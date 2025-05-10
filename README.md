<p align="center">
  <img src="https://img.shields.io/badge/Smart--Web-House%20Price%20Prediction-blueviolet?style=for-the-badge&logo=homeadvisor&logoColor=white" alt="Smart-Web Logo"/>
</p><h1 align="center">Smart-Web</h1>
<h3 align="center">Intelligent House Price Prediction for King County, Seattle</h3><p align="center">
  <img src="https://img.shields.io/badge/Django-Backend-green?style=flat-square&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/XGBoost-ML-orange?style=flat-square&logo=githubactions&logoColor=white">
  <img src="https://img.shields.io/badge/Leaflet-Map-00C851?style=flat-square&logo=leaflet&logoColor=white">
  <img src="https://img.shields.io/badge/Accuracy-90%25-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square">
</p>
---

🚀 Overview

Smart-Web is a powerful web application designed to predict house prices with high accuracy (~90%) in King County, Seattle.
Built with Django, powered by XGBoost ML model, and integrated with Leaflet.js for map visualization.


---

✨ Features

Accurate Prediction (~90%)

Interactive Form to input house features (bedrooms, bathrooms, sqft, year built, etc.)

Live Map with Leaflet.js to visualize geographic coordinates

User Authentication System:

Signup / Login / Logout

Password Reset


Responsive and Mobile-Friendly UI



---

🧩 System Flow

flowchart TD
    A[User Submits House Details] --> B[Backend Processes Form]
    B --> C[XGBoost Model Predicts Price]
    C --> D[Price Displayed to User]
    B --> E[Plot Location on Leaflet Map]

(Rendered using mermaid.js syntax, GitHub will render this automatically)


---

⚙️ Installation

1. Clone the repository:

git clone https://github.com/amirhosssein0/Smart-Web.git
cd Smart-Web


2. Create a virtual environment:

python -m venv env
source env/bin/activate   # (Windows: env\Scripts\activate)


3. Install dependencies:

pip install -r requirements.txt


4. Apply migrations:

python manage.py migrate


5. Run the server:

python manage.py runserver


6. Open your browser:

http://127.0.0.1:8000/




---

📚 Project Structure

Smart-Web/
├── accounts/          # User authentication (Signup, Login, Password Reset)
├── home_prediction/   # House price prediction app
├── static/            # Static files (CSS, JS, Images)
├── templates/         # HTML templates
├── Smart_Web/         # Project settings and configurations
├── requirements.txt   # Python dependencies
└── README.md          # This file


---

🤖 About the ML Model

Trained on King County house sales dataset

XGBoost Regressor is used for its efficiency and high accuracy

Important features include:

Number of bedrooms

Living area (sqft)

Lot size

Year built

Condition and location (lat/lon)




---

🤝 Contribution

Contributions, issues, and feature requests are welcome!
Please feel free to fork the repository and submit a pull request.


---

📜 License

Distributed under the MIT License. See LICENSE for more information.


---

> Made with ❤️ by Amirhossein

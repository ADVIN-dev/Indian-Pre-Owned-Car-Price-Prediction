# 🚗 Indian Pre-Owned Car Price Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

A Machine Learning web application that predicts the estimated selling price of Indian pre-owned cars based on various vehicle specifications. The project combines data preprocessing, feature engineering, a trained regression model, and an interactive Streamlit interface to provide real-time price predictions.

---

## 📌 Table of Contents

- Project Overview
- Key Features
- Technologies Used
- Application Preview
- Machine Learning Workflow
- Dataset
- Model Information
- Project Structure
- Installation
- Usage
- Future Enhancements
- Acknowledgements
- Author
- License

---

## 📖 Project Overview

The value of a pre-owned car depends on several factors such as its manufacturer, model, age, mileage, engine specifications, ownership history, transmission type, fuel type, and overall condition.

This project predicts the estimated selling price of Indian pre-owned cars using a Machine Learning regression model trained on historical vehicle data. Users can enter the specifications of a car through an interactive Streamlit application and instantly receive its predicted market value.

The project demonstrates a complete end-to-end Machine Learning workflow, including:

- Data preprocessing
- Feature engineering
- Categorical feature encoding
- Model training
- Model serialization
- Streamlit deployment

---

## ✨ Key Features

| Feature | Description |
|----------|-------------|
| 🚗 Car Price Prediction | Predicts the estimated selling price of used cars |
| 🌐 Streamlit Application | Interactive and user-friendly web interface |
| ⚡ Real-Time Prediction | Generates instant price estimates |
| 📊 Data Preprocessing | Handles numerical and categorical features |
| 🔤 Label Encoding | Encodes categorical variables before prediction |
| 🤖 Machine Learning | Uses a trained regression model |
| 💾 Model Deployment | Loads the trained model using Joblib |

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

### Machine Learning Concepts

- Regression
- Feature Engineering
- Label Encoding
- Model Serialization

### Development Tools

- VS Code
- Git
- GitHub

---

## 🖥️ Application Preview

### Home Page

<img width="959" height="538" alt="1 Home (2)" src="https://github.com/user-attachments/assets/b65db092-f2af-485c-bbdb-5a8b27f71482" />


### Input Form

<img width="959" height="537" alt="2 Input_form" src="https://github.com/user-attachments/assets/4154ca9a-37ee-4f08-80c0-ec5b04e6144c" />


### Prediction Result

<img width="959" height="536" alt="3 Prediction_result" src="https://github.com/user-attachments/assets/dc339813-82f2-4621-8e3e-17677b35ca77" />


---

## 🔄 Machine Learning Workflow

```text
                    Dataset
                       │
                       ▼
             Data Preprocessing
                       │
                       ▼
            Feature Engineering
                       │
                       ▼
              Label Encoding
                       │
                       ▼
          Machine Learning Model
                       │
                       ▼
             Model Serialization
                  (Joblib)
                       │
                       ▼
             Streamlit Web App
                       │
                       ▼
           Estimated Car Price
```

---

## 📂 Dataset

The dataset contains detailed information about Indian pre-owned vehicles, including:

- Maker
- Model
- Location
- Distance Travelled
- Owner Type
- Manufacture Year
- Age of Car
- Engine Displacement
- Engine Power
- Body Type
- Vroom Audit Rating
- Transmission
- Door Count
- Seat Count
- Fuel Type

**Target Variable**

- Selling Price

---

## 🧠 Model Information

The prediction model was trained using historical data of Indian pre-owned cars.

The model learns the relationship between vehicle specifications and selling price to estimate the market value of unseen vehicles.

The deployment pipeline includes:

- Data preprocessing
- Label encoding
- Model prediction
- Streamlit interface

The trained model and label encoders are stored using **Joblib**, enabling fast and efficient predictions without retraining the model.

---

## 📁 Project Structure

```text
Indian-Pre-Owned-Car-Price-Prediction/

├── dataset/
│   ├── Cap_Training_Data_2025.csv
│   └── Cap_Test_Data_2025.csv
│
├── model/
│   ├── car_price_model.pkl
│   └── label_encoders.pkl
│
├── notebook/
│   └── Car_Price_Prediction.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── input_form.png
│   └── prediction_result.png
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ADVIN-dev/Indian-Pre-Owned-Car-Price-Prediction.git
```

### Navigate to the project directory

```bash
cd Indian-Pre-Owned-Car-Price-Prediction
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🚀 Usage

1. Launch the Streamlit application.
2. Enter the required vehicle specifications.
3. Click **Predict Price**.
4. View the estimated selling price.

---

## 🔮 Future Enhancements

- Deploy the application on Streamlit Cloud
- Improve prediction accuracy using XGBoost or CatBoost
- Add image-based car analysis
- Integrate real-time automobile market data
- Provide price trend analysis
- Add prediction history for users
- Develop a REST API for external integration

---

## 🙏 Acknowledgements

This project was developed as part of my **B.Tech Major Project**.

I would like to express my sincere gratitude to **Unlox Academy** and my project mentor **Sruthi Tarimana** for their continuous guidance, valuable suggestions, and support throughout the development of this project.

---

## 👨‍💻 Author

**Aditya Raj**

B.Tech Computer Science Student

Aspiring Machine Learning Engineer

**GitHub:** https://github.com/ADVIN-dev

**LinkedIn:** www.linkedin.com/in/aditya-raj-903b52349

---

⭐ If you found this project useful, consider giving it a star!

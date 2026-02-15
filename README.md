#💳 Credit Card Fraud Detection Using Machine Learning
##📌 Project Overview

This project aims to detect fraudulent credit card transactions using Machine Learning techniques. The model analyzes transaction patterns and classifies transactions as valid or fraudulent.

The system is deployed using Streamlit, providing an interactive web interface for real-time prediction.

##🎯 Objectives

Detect fraudulent transactions from transaction data

Handle highly imbalanced dataset

Compare multiple machine learning models

Deploy model using a web interface

Provide real-time prediction

##📊 Dataset

The dataset used is the Credit Card Fraud Detection dataset from Kaggle.

Total transactions: 284,807

Fraud cases: 492

Features: PCA transformed (V1–V28), Amount, Time, Class

##🤖 Machine Learning Models Used

Logistic Regression

Random Forest

Gradient Boosting

##🏆 Best Model

Random Forest achieved the highest accuracy (~99.9%) and was selected as the final model.

##🧠 Methodology

-Data Collection

-Data Preprocessing

-Exploratory Data Analysis

-Feature Scaling

-Train-Test Split

-Model Training

-Model Evaluation

-Model Comparison

-Deployment using Streamlit

##🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Streamlit

##🧰 Tools Used

Jupyter Notebook

VS Code

GitHub

##🌐 Web Application Features

Login Interface

Payment Form

Fraud Prediction Result

Interactive UI

Real-time detection

##🚀 How to Run the Project
1️⃣ Clone repository
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection

2️⃣ Install dependencies
pip install -r requirements.txt


OR

pip install streamlit pandas numpy scikit-learn joblib

3️⃣ Run the app
streamlit run app.py

4️⃣ Open browser

Go to:

http://localhost:8501

##📂 Project Structure
credit-card-fraud-detection/
│
├── app.py
├── fraud_model.ipynb
├── creditcard_fraud.png
├── screenshots/
├── README.md
├── requirements.txt

##📈 Results
Model	Accuracy
Logistic Regression	~98–99%
Gradient Boosting	~99.8%
Random Forest	~99.9%

##🏗️ System Architecture

User Input → Preprocessing → ML Model → Prediction → Result Display

##🔮 Future Improvements

Use SMOTE for imbalance handling

Add deep learning models

Deploy on cloud platform

Real-time API integration

Add fraud probability score

Use XGBoost

##📚 References

Kaggle Credit Card Fraud Dataset

Scikit-learn Documentation

Research papers on Fraud Detection

Streamlit Documentation

##👩‍💻 Author

Mrudula Sonawane

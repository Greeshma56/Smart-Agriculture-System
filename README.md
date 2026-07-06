# 🌱 Smart Agriculture System

An AI-powered Crop Recommendation System built using Machine Learning and Streamlit.

## 📌 Project Overview

This application recommends the most suitable crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

The system uses a Random Forest Classifier trained on agricultural data to provide accurate crop recommendations.

---

## 🚀 Features

- Crop Recommendation using Machine Learning
- Random Forest Classification Model
- Interactive Streamlit Web Application
- User-Friendly Interface
- Real-Time Predictions
- 99.32% Model Accuracy

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Streamlit

---

## 📂 Project Structure

```text
Smart-Agriculture-System
│
├── Crop_recommendation.csv
│
├── crop_model.pkl
│
├── day1_analysis.py
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
```

## 📊 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Model Accuracy:

- 99.32%

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/Smart-Agriculture-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🌾 Sample Prediction

Input:

- Nitrogen = 90
- Phosphorus = 42
- Potassium = 43
- Temperature = 20.87
- Humidity = 82
- pH = 6.5
- Rainfall = 202.93

Output:

```text
Recommended Crop: Rice
```

---

## 🎯 Future Enhancements

- Weather API Integration
- Fertilizer Recommendation System
- Crop Yield Prediction
- Soil Report Upload
- Multi-Language Support

---

## 👩‍💻 Author

Greeshma

Machine Learning Project developed using Python, Scikit-Learn, and Streamlit.

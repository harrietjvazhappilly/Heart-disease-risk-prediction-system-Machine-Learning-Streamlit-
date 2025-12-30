### Heart Disease Risk Prediction System (Machine Learning + Streamlit)

An end-to-end Heart Disease Risk Prediction System built using *Python, Machine Learning*, and *Streamlit* to analyze patient health data and predict the likelihood of heart disease.
This project automates medical risk assessment, reduces manual diagnosis effort, and demonstrates a complete ML deployment workflow.

---

### Features

 - Automated Risk Prediction using a tuned Random Forest model

 - Interactive Web Application built with Streamlit

 - Supports Single Patient Analysis – enter values and get instant prediction

 - Model Comparison – Logistic Regression, Random Forest, SVM

 - Hyperparameter Tuning using RandomizedSearchCV

 - Model Persistence using .pkl files

 - End-to-End Pipeline – Data → Training → Evaluation → Deployment

---

### Tech Stack

 - Programming Language: Python

 - Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn

 - Web Framework: Streamlit

 - Model Storage: Pickle

---

### Dataset

Dataset: Heart Disease Dataset (UCI / Kaggle)

Target Column: HeartDisease

0 → Low Risk

1 → High Risk

---

### Getting Started
Prerequisites

 - Python 3.x

 - Required Python packages listed in requirements.txt

---

### Installation

Clone the repository:

`git clone https://github.com/harrietjvazhappilly/heart-disease-predictor.git
cd heart-disease-predictor`


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

---

### Example – Low Risk Input

| Feature              | Value             |
|----------------------|-------------------|
| Age                  | 30                |
| Sex                  | Female            |
| Chest Pain Type      | Non-Anginal Pain  |
| Resting BP           | 110               |
| Cholesterol          | 170               |
| Fasting Blood Sugar  | 0                 |
| ECG                  | Normal            |
| Max Heart Rate       | 190               |
| Exercise Angina      | No                |
| Oldpeak              | 0                 |
| ST Slope             | Up                |


---

### Model Performance

The final tuned Random Forest model achieved approximately 86–88% accuracy with reduced false-negative predictions, making it suitable for healthcare-related risk assessment tasks.

---

### Conclusion

This project demonstrates:

Complete Machine Learning lifecycle

Model evaluation & tuning

Real-world deployment using Streamlit

Practical healthcare prediction system

---
### Author

Harriet J. Vazhappilly

GitHub: https://github.com/harrietjvazhappilly

LinkedIn: https://www.linkedin.com/in/harriet-j-vazhappilly-5aaa92329/

Email: 24ct245@mgits.ac.in 
       harrietjvazhappilly@gmail.com

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

```bash
git clone https://github.com/harrietjvazhappilly/Heart-disease-risk-prediction-system-Machine-Learning-Streamlit-.git
cd Heart-disease-risk-prediction-system-Machine-Learning-Streamlit-
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app locally:

```bash
streamlit run app.py
```

---

### Deployment

This app is ready to be deployed on Streamlit Community Cloud.

1. Push the project to GitHub.
2. Open Streamlit Cloud.
3. Click New app.
4. Select the repository and branch.
5. Set the main file path to `app.py`.
6. Click Deploy.

Required files for deployment:

- `app.py`
- `requirements.txt`
- `heart_disease_model.pkl`
- `model_columns.pkl`
- `.streamlit/config.toml`

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

### Example – High Risk Input

| Feature              | Value             |
|----------------------|-------------------|
| Age                  | 62                |
| Sex                  | Male              |
| Chest Pain Type      | Typical Angina    |
| Resting BP           | 140               |
| Cholesterol          | 260               |
| Fasting Blood Sugar  | 1                 |
| ECG                  | ST                |
| Max Heart Rate       | 125               |
| Exercise Angina      | Yes               |
| Oldpeak              | 3.5               |
| ST Slope             | Flat              |

---

### Model Performance

The final tuned Random Forest model achieved approximately 86–88% accuracy with reduced false-negative predictions, making it suitable for healthcare-related risk assessment tasks.

---

### Conclusion

This project demonstrates:

 - Complete Machine Learning lifecycle

 - Model evaluation & tuning

 - Real-world deployment using Streamlit

 - Practical healthcare prediction system

---
### Author

Harriet J Vazhappilly

GitHub: https://github.com/harrietjvazhappilly

LinkedIn: https://www.linkedin.com/in/harriet-j-vazhappilly-5aaa92329/

Email: 24ct245@mgits.ac.in 
       harrietjvazhappilly@gmail.com

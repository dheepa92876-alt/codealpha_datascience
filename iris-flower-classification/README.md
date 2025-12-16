# 🌸 Iris Flower Classification

## 📌 Overview
This project implements a professional **machine learning classification system** to predict the species of Iris flowers using flower measurements.  
It demonstrates an **end-to-end ML workflow** suitable for academic use and industry portfolios.

## 🧠 Problem Statement
Given measurements of an Iris flower:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Predict the species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn

## 📂 Project Structure
```
iris-flower-classification/
│
├── data/
│   └── Iris.csv
├── src/
│   └── iris_classifier.py
├── README.md
└── requirements.txt
```

## ⚙️ Model Used
- Support Vector Machine (SVM)
- Feature scaling using StandardScaler
- ML Pipeline for clean preprocessing & training

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the model:
   ```bash
   python src/iris_classifier.py
   ```

## 📊 Evaluation Metrics
- Accuracy Score
- Precision
- Recall
- F1-Score

## 💼 Resume Highlight
Built a scalable Iris Flower Classification system using Scikit-learn pipelines and SVM, achieving high accuracy and clean modular code structure suitable for production environments.

## 🔮 Future Enhancements
- Model comparison (Logistic Regression, Random Forest)
- Confusion Matrix visualization
- Web app using Streamlit
- Model deployment using Flask/FastAPI

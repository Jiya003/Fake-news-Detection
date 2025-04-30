# 📰 Fake News Detection with Flask

This project uses a machine learning model (XGBoost) to detect whether a given news article is **fake** or **real**. The model is trained using text data and deployed via a Flask web application.

---

## 🔍 Features

- Input news text and get prediction
- Shows **probability score** for both fake and real
- Flask-powered web interface
- XGBoost-based classifier
- Preprocessing: stemming, tokenizing, length features
- SMOTE for balancing dataset

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
pip install -r requirements.txt
```

---

## Run the app
```bash
python app.py
```

Navigate to http://127.0.0.1:5000 in your browser.

## MACHINE LEARNING MODEL DETAILS

- Algorithm: XGBoost Classifier
- Accuracy: ~63%
- Class 0: Fake News
- Class 1: Real News
- Text Features: Cleaned, tokenized, stemmed, and vectorized text
- SMOTE: Used to balance class distribution

---

## REQUIREMENTS

- Flask
- scikit-learn
- pandas
- xgboost
- nltk
- imblearn (for SMOTE)

--- 

## 📜 License

MIT License

--- 

## 👩‍💻 Author

Divyanshi Maurya – LinkedIn | GitHub

⭐ If you like this project, give it a star!


Let me know if you'd like the `requirements.txt` as well!


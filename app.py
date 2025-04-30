import joblib
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#Initializing the Flask app
app=Flask(__name__)

#Loading the saved model and vectorizer
xgb_model=joblib.load('xgb_model_final.pkl') 
vectorizer=joblib.load('tfidf_vectorizer.pkl') 

#Defining the home route
@app.route('/')
def home():
    return render_template('index.html') #Rendering the HTML page

#Defining the predict route
@app.route('/predict',methods=['POST'])
def predict():
    #Getting the news content from the form
    news_content=request.form['news_content']

    #Vectorizing the input text using the same vectorizer used in training
    news_vectorized=vectorizer.transform([news_content])

    #Predictting probabilities
    proba=xgb_model.predict_proba(news_vectorized)[0]  # [0] gives the single row

    #Get predicted label (0 or 1)
    prediction=xgb_model.predict(news_vectorized)[0]

    #Class labels
    labels={0: "Fake News", 1: "Real News"}
    
    #Confidence score
    confidence=round(proba[prediction] * 100, 2)

    #Final result
    result=f"The news is predicted to be {labels[prediction]} with {confidence}% confidence."

    return render_template('index.html',prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

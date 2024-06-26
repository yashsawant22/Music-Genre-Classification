# -*- coding: utf-8 -*-
"""genre predict APP_building.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GU_vQpLlFkOx3qdChg54mBHDWok9ACP0

#APP BUILDING:
"""

from pyngrok import ngrok

import nltk
nltk.download('stopwords')

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.utils import shuffle
from nltk.corpus import stopwords


stop = list(set(stopwords.words('english'))) # stopwords
wnl = WordNetLemmatizer() # lemmatizer

def tokenizer(x): # custom tokenizer
    return (
        wnl.lemmatize(w)
        for w in word_tokenize(x)
        if len(w) > 2 and w.isalnum() # only words that are > 2 characters
    )

import pickle

lr_model = open('/content/sample_data/genrepredict.pkl','rb')
classifier = pickle.load(lr_model)

#Commented out IPython magic to ensure Python compatibility.
#%%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from swachhdata.text import *
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.utils import shuffle
from nltk.corpus import stopwords

stop = list(set(stopwords.words('english'))) # stopwords
wnl = WordNetLemmatizer() # lemmatizer

def tokenizer(x): # custom tokenizer
     return (
        wnl.lemmatize(w)
        for w in word_tokenize(x)
        if len(w) > 2 and w.isalnum() # only words that are > 2 characters
      )

lr_model = open('genrepredict.pkl','rb')
classifier = pickle.load(lr_model)


PAGE_CONFIG = {"page_title":"Song Genre Prediction from Lyrics","page_icon":"🎸","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():

    st.title("Genre Classifier Using Song Lyrics")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">This app uses NLP to predict the genre of a song just by reading the lyrics</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    text = st.text_input("Enter Lyrics")

    result=""
    if st.button("Predict"):

        result=classifier.predict([text])
        st.write(result)

if __name__=='__main__':
    main()

import pandas as pd
import numpy as np
import hazm
import re
import string
import mapply
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2

from .parameter_finder import classification_parameter_finder
from .parameter.models import  get_details_models

mapply.init(
    n_workers=-1,
    chunk_size=100,
    max_chunks_per_worker=10,
    progressbar=False
)

def train_models(df : pd.DataFrame, PreProcess) -> pd.DataFrame:
    model_PreProcess = PreProcess()
    y = df["label"]
    df["PreProcess_comment"] = df["comment"].mapply(lambda text : model_PreProcess.pipeline(text))
    X = [" ".join(tokens) for tokens in df["PreProcess_comment"]]
    tfidf_vectorizer = TfidfVectorizer()
    X = tfidf_vectorizer.fit_transform(X)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    transformer = SelectKBest(chi2, k = 200).fit(X_train, y_train)
    X_train = transformer.transform(X_train)
    X_test = transformer.transform(X_test)
    X_train = X_train.toarray()
    X_test = X_test.toarray()
    parameter_models = get_details_models()
    result = []
    
    for model_info in parameter_models[:]:
        model, parameter = model_info
        result.append(classification_parameter_finder(model, parameter, X_train, y_train, X_test, y_test))
        print(f"{model} done")
    
    return pd.concat(result)

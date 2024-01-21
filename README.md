# Machine Learning News Classification

This repository contains a machine learning project for classifying news articles into different categories. The project includes data preprocessing, feature extraction using various methods, and the application of different machine learning models.
**this reposetery made with elham ghasemi , golshid ranjbaran and alireza parvaresh**
## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Data](#data)
- [Preprocessing](#preprocessing)
- [Feature Extraction](#feature-extraction)
- [Machine Learning Models](#machine-learning-models)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to classify news articles into different categories such as sports, politics, social, economy, and culture-media. It involves the use of various natural language processing techniques and machine learning models to achieve accurate classification.

## Dependencies

- Google Colab (for Jupyter notebook)
- Python 3.x
- pandas
- matplotlib
- string
- re
- hazm
- numpy
- torch
- transformers
- sentence-transformers
- accelerate
- scikit-learn
- datasets
- huggingface-hub
- kaggle

## Data

The dataset used in this project is stored in the CSV file `farsnews_fainal.csv`. It contains news articles with corresponding labels.

## Preprocessing

The preprocessing steps involve cleaning and normalizing the text data. This includes removing unnecessary spaces, crash data, punctuation, diacritics, and normalizing Persian characters. Additionally, the dataset is balanced to ensure equal representation of each category.
Certainly! If you want to include word frequency as part of the feature extraction section, you can modify the "Feature Extraction" section in the README as follows:

## Feature Extraction

Four different methods are used for feature extraction:

1. **TF-IDF Vectorization**: Converts the text data into numerical vectors using the TF-IDF method.
2. **Word Frequency**: Analyzes the frequency of each word in the corpus and represents the text data based on word occurrences.
3. **BERT Vectorization**: Uses the pre-trained BERT model for encoding the text data into numerical vectors.
4. **LaBSE Vectorization**: Utilizes the LaBSE (Language-agnostic BERT Sentence Embedding) model for encoding text data.


## Machine Learning Models

Various machine learning models are trained and evaluated on the feature-extracted data. The models include:

- Logistic Regression
- K-Nearest Neighbors
- Weighted K-Nearest Neighbors
- Naive Bayes
- Decision Tree
- Support Vector Machine (SVM)
- Gradient Boosting

The models are evaluated based on accuracy scores and confusion matrices.

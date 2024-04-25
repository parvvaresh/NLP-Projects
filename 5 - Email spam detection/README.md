# Email Persian Spam Detection using Machine Learning Algorithms

## Overview
This project focuses on detecting Persian spam emails using machine learning algorithms. The goal is to develop an effective spam detection system using various word embedding techniques and classification algorithms. The project utilizes three word embedding algorithms: TF-IDF, Frequency of Words, and Bag of Words. Additionally, six classification algorithms are employed: K-Nearest Neighbors (KNN), Logistic Regression, Decision Tree, Random Forest, Naive Bayes, and Support Vector Machine (SVM).

## Word Embedding Algorithms

### 1. TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. It is widely used for information retrieval and text mining.

### 2. Frequency of Words
This approach represents each word by its frequency of occurrence in the document. It provides a simple and intuitive representation of the document.

### 3. Bag of Words
The Bag of Words model represents a document as an unordered set of words, disregarding grammar and word order but keeping track of word frequency.

## Classification Algorithms

### 1. K-Nearest Neighbors (KNN)
KNN is a simple and effective algorithm for classification. It classifies a data point based on the majority class of its k-nearest neighbors.

### 2. Logistic Regression
Logistic Regression is a linear model used for binary classification. It models the probability of an instance belonging to a particular class.

### 3. Decision Tree
A Decision Tree is a flowchart-like structure where each internal node represents a decision based on the value of a feature. It is widely used for classification tasks.

### 4. Random Forest
Random Forest is an ensemble learning method that constructs a multitude of decision trees during training and outputs the class that is the mode of the classes.

### 5. Naive Bayes
Naive Bayes is a probabilistic algorithm based on Bayes' theorem. It assumes that the presence of a particular feature is unrelated to the presence of any other feature.

### 6. Support Vector Machine (SVM)
Support Vector Machine is a powerful supervised learning algorithm used for classification and regression tasks. It finds a hyperplane that best separates the classes in the feature space.

## Preprocessing

The project uses Hazm, a comprehensive natural language processing library for Persian, for text preprocessing. This includes tasks such as stemming, tokenization, and stop word removal.

## Results

The accuracy of each algorithm with different word embedding techniques is presented in both a plot and a table:

### Accuracy Plot
![image](https://github.com/parvvaresh/email-spam-detection/assets/89921883/05dd3baa-2b16-4f63-870d-e15b35a0da62)

### Accuracy Table

| Algorithm             | Accuracy with TF-IDF | Accuracy with Frequency of Words |  Accuracy with Bag Of Word|
|-----------------------|----------------------|----------------------------------|---------------------------|
| Logistic Regression   | 49.0%                | 97.0%                            | 93.5%
| Decision Tree         | 94.0%                | 93.5%                            | 93.5%
| Random Forest         | 93.0%                | 95.0%                            | 90.5%
| Naive Bayes           | 51.5%                | 77.0%                            | 51.5%
| KNN                   | 92.5%                | 98.5%                            | 82.0%

## Conclusion

The project demonstrates the effectiveness of different word embedding techniques and classification algorithms for Persian email spam detection. Further optimizations and parameter tuning can potentially enhance the performance of the models. This readme provides a brief overview, and the project repository may contain additional details, code, and documentation for interested users.

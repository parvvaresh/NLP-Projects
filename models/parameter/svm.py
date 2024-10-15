from sklearn.svm import SVC

def get_svm():
    param_svm = {
        'C': [0.1, 1, 10, 100, 1000],
        'kernel': ['rbf'],
        'gamma': [0.001, 0.01, 0.1, 1],
    }

    return SVC(), param_svm
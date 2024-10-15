from sklearn.naive_bayes import GaussianNB
def get_nb():

    param_naive_bayes = {
        'var_smoothing': [1e-9, 1e-8, 1e-7, 1e-6, 1e-5]
    }

    return GaussianNB(), param_naive_bayes
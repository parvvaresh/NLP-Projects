from .decision_tree import get_dt
from .knn import get_knn
from .logstic_regression import get_lr
from .naive_bayes import get_nb
from .perceptron import get_pr
from .random_forest import get_rf
from .svm import get_svm
from .NearestCentroid import get_nc

def get_details_models():
    return [
        get_nc(),
        get_knn(),
        get_dt(),
        get_lr(),
        get_nb(),
        get_pr(),
        get_svm(),
        get_rf(),

    ]
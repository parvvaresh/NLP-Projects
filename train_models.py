import pandas as pd
import numpy as np
import hazm
import re
import string
import mapply


mapply.init(
    n_workers=-1,
    chunk_size=100,
    max_chunks_per_worker=10,
    progressbar=False
)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2

output.clear()


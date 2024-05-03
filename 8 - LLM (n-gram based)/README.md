# N-grams Sentence Autocomplete Model

## Description
This Python class implements an n-grams language model for sentence autocomplete. It utilizes the concept of n-grams to predict the next word in a sentence given a prefix. The model can be trained on a corpus of text data and used to generate autocomplete suggestions for incomplete sentences.

## Installation
1. Install the required Python packages:
    ```
    pip install tqdm
    ```

## Usage
1. Import the `n_grams_model` class into your Python script.
2. Create an instance of the `n_grams_model` class with the desired value of `n` (the size of n-grams).
3. Train the model using the `train` method by providing a list of sentences as input.
4. Predict autocomplete suggestions for a given prefix using the `predict` method.

### Example Usage:
```python
from n_grams_model import n_grams_model

# Initialize the model with n=3 (trigrams)
model = n_grams_model(n=3)

# Train the model on a corpus of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The quick brown fox jumps over the lazy cat",
    "The lazy cat is sleeping"
]
model.train(sentences)

# Predict autocomplete suggestions for a prefix
prefix = "The quick"
suggestions = model.predict(prefix)
print("Autocomplete Suggestions for '{}':".format(prefix))
for suggestion in suggestions:
    print(suggestion)
```

## Class Methods
- `train(sentences: list)`: Train the model on a list of sentences.
- `predict(prefix: str, k: int = 3) -> list`: Predict autocomplete suggestions for a given prefix. Returns a list of suggested words.

## Author
[Alireza Parvaresh](http://parvaresh.github.io)

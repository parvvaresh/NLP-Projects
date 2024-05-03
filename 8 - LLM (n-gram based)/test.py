from model.model import n_grams_model

corpus = [
    "the quick brown fox jumps over the lazy dog",
    "the quick brown fox jumps over the lazy cat",
    "the lazy cat is sleeping"
]

n = 3  # Change to adjust the n-gram size
model = n_grams_model(n)
model.train(corpus)

prefix = "the quick brown fox jumps, over the lazy..... "
suggestions = model.predict(prefix)
print("Autocomplete Suggestions for '{}':".format(prefix))
for suggestion in suggestions:
    print(suggestion)
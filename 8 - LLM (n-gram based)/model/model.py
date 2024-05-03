from collections import defaultdict
from tqdm import tqdm
import re

class n_grams_model:
    def __init__(self,
                 n : int) -> None:
        self.n = n
        self.n_grams = defaultdict(int)
    
    
    def train(self,
              sentences : list) -> None:
        print("training ...")
        for sentence in tqdm(sentences):
            tokens = self._preprocess(sentence)
            for index in range(len(tokens) - self.n + 1):
                ngram = ' '.join(tokens[index : index + self.n])
                self.n_grams[ngram] += 1
                
    
    
    def predict(self, 
                prefix : str,
                k = 3) -> list:
        tokens = self._preprocess(prefix)
        context = ' '.join(tokens[- (self.n - 1) : ]  )  
        predictions = [(ngram, count)
            for ngram , count in self.n_grams.items() 
                if ngram.startswith(context)
        ]  
        
        predictions.sort(key=lambda item : item[1], reverse=True)
        suggestions = [ngram.split()[-1] for ngram, _ in predictions[ : k]]      
        return suggestions
    
    def _preprocess(self,
                   text : str) -> list:
        text = text.lower()
        text = re.sub(r'[^\w\s]', '' , text)
        tokens = text.split()
        return tokens
        
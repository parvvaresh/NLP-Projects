from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

with open('./final_models/tokenizer.json', 'r', encoding='utf-8') as f:
    tokenizer_json = f.read()
tokenizer = tokenizer_from_json(tokenizer_json)

model = tf.keras.models.load_model('./final_models/lstm_model.h5')

def pipeline_predict(text: str) -> str:
    sequences = tokenizer.texts_to_sequences([text])  
    padded_sequences = pad_sequences(sequences, maxlen=100, padding='post')
    prediction = model.predict(padded_sequences)
    sentiment_score = prediction[0][0]
    
    print(f'Sentiment Score: {sentiment_score}')
    lable = 'SAD' if sentiment_score > 0.5 else 'HAPPY'
    return lable

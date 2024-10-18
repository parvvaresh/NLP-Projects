import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split

def train_dl_model(df : pd.DataFrame):
    comments = df['comment']
    labels = df['label_id']

    tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
    tokenizer.fit_on_texts(comments)

    sequences = tokenizer.texts_to_sequences(comments)

    max_length = 100
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

    X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

    train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train)).shuffle(10000).batch(64)
    test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(64)
    model = keras.Sequential([
        keras.layers.Embedding(input_dim=10000, output_dim=64, input_length=max_length),
        keras.layers.Bidirectional(keras.layers.LSTM(64, return_sequences=True)),
        keras.layers.Bidirectional(keras.layers.LSTM(32)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(1, activation='sigmoid')  # Assuming binary classification
    ])

    model.compile(
        loss='binary_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    NUM_EPOCHS = 5
    history = model.fit(
        train_dataset,
        epochs=NUM_EPOCHS,
        validation_data=test_dataset
    )

    test_loss, test_acc = model.evaluate(test_dataset)
    print(f'Test Loss: {test_loss}')
    print(f'Test Accuracy: {test_acc}')
    return model , tokenizer

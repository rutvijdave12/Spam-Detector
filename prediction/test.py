import os

from utils import get_model, int2label, label2int
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import pickle
import numpy as np

SEQUENCE_LENGTH = 100

# get the tokenizer
tokenizer = pickle.load(open("results/tokenizer.pickle", "rb"))

model = get_model(tokenizer, 128)
model.load_weights("results/spam_classifier_0.08")

def get_predictions(text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = pad_sequences(sequence, maxlen=SEQUENCE_LENGTH)
    prediction = model.predict(sequence)[0]
    return int2label[np.argmax(prediction)]

if __name__ == "__main__":
    while True:
        text = input("Enter the mail:")
        print(get_predictions(text))
else:
    def send_text():
        df = pd.read_csv('my_emails_unfiltered.csv')
        for ind in df.index:
            text = str(df['Subject'][ind]) +" "+ str(df['Body'][ind])
            spam = get_predictions(text)
            df['Spam'][ind] = spam
        df.to_csv('my_emails_filtered.csv')

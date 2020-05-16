from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import keras_metrics
import numpy as np

SEQUENCE_LENGTH = 100 # the length of all sequences (number of words per sample)
tokenizer = Tokenizer()
int2label = {0: "ham", 1: "spam"}
def get_predictions(text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = pad_sequences(sequence, maxlen=SEQUENCE_LENGTH)
    model = load_model('Spam-model-compiled.h5',custom_objects={'binary_precision':keras_metrics.binary_precision(),'binary_recall':keras_metrics.binary_recall()})
    prediction = model.predict(sequence)[0]
    return int2label[np.argmax(prediction)]


text = "Congratulations! you have won 100,000$ this week, click here to claim fast"
print(get_predictions(text))



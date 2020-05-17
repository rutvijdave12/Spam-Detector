import tqdm
import numpy as np
import keras_metrics 
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, LSTM, Dropout, Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.model_selection import train_test_split
import time
import pandas as pd
import pickle
from keras.backend import manual_variable_initialization
manual_variable_initialization(True)






SEQUENCE_LENGTH = 100 
EMBEDDING_SIZE = 100  
TEST_SIZE = 0.25


BATCH_SIZE = 100
EPOCHS = 60


label2int = {"ham": 0, "spam": 1}
int2label = {0: "ham", 1: "spam"}


# def load_data():
#     df = pd.read_csv('emails.csv')

#     text,label = [],[]

#     for ind in df.index:
#         text.append(df['text'][ind])
#         label.append(df['spam'][ind])

#     return text,label

def load_data():

    texts, labels = [], []
    with open("data/SMSSpamCollection") as f:
        for line in f:
            split = line.split()
            labels.append(split[0].strip())
            texts.append(' '.join(split[1:]).strip())
    return texts, labels

    # print(label)
    # print(text)

#load_data()


X, y = load_data()


tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)

X = tokenizer.texts_to_sequences(X)



X = np.array(X)
y = np.array(y)


X = pad_sequences(X, maxlen=SEQUENCE_LENGTH)
# print(y)
y = [ label2int[label] for label in y ]
y = to_categorical(y)

# print(y)
# split and shuffle
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=7)

def get_embedding_vectors(tokenizer, dim=100):
    embedding_index = {}
    with open(f"data/glove.6B.{dim}d.txt", encoding='utf8') as f:
        for line in tqdm.tqdm(f, "Reading GloVe"):
            values = line.split()
            word = values[0]
            vectors = np.asarray(values[1:], dtype='float32')
            embedding_index[word] = vectors

    word_index = tokenizer.word_index
    embedding_matrix = np.zeros((len(word_index)+1, dim))
    for word, i in word_index.items():
        embedding_vector = embedding_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
            
    return embedding_matrix   



def get_model(tokenizer, lstm_units):

    embedding_matrix = get_embedding_vectors(tokenizer)
    model = Sequential()
    model.add(Embedding(len(tokenizer.word_index)+1,
              EMBEDDING_SIZE,
              weights=[embedding_matrix],
              trainable=False,
              input_length=SEQUENCE_LENGTH))

    model.add(LSTM(lstm_units, recurrent_dropout=0.2))
    model.add(Dropout(0.3))
    model.add(Dense(2, activation="softmax"))

    model.compile(optimizer="rmsprop", loss="categorical_crossentropy",
                  metrics=["accuracy", keras_metrics.precision(), keras_metrics.recall()])
    model.summary()
    return model


model = get_model(tokenizer=tokenizer, lstm_units=128)

model_checkpoint = ModelCheckpoint(f"results/spam_classifier",monitor='val_loss', save_best_only=True,
                                    verbose=1,save_weights_only=False)
print(1)
tensorboard = TensorBoard(f"logs/spam_classifier_{time.time()}")
# print our data shapes
print("X_train.shape:", X_train.shape)
print("X_test.shape:", X_test.shape)
print("y_train.shape:", y_train.shape)
print("y_test.shape:", y_test.shape)
# train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test),
          batch_size=BATCH_SIZE, epochs=EPOCHS,
          callbacks=[tensorboard, model_checkpoint],
          verbose=1,)





#loss and metrics
result = model.evaluate(X_test, y_test)

loss = result[0]
accuracy = result[1]
precision = result[2]
recall = result[3]

print(f"[+] Accuracy: {accuracy*100:.2f}%")
print(f"[+] Precision:   {precision*100:.2f}%")
print(f"[+] Recall:   {recall*100:.2f}%")


model.save("Spam-model-compiled.h5")


def get_predictions(text):
    sequence = tokenizer.texts_to_sequences([text])
    # pad the sequence
    sequence = pad_sequences(sequence, maxlen=SEQUENCE_LENGTH)
    # get the prediction
    prediction = model.predict(sequence)[0]
    # one-hot encoded vector, revert using np.argmax
    return int2label[np.argmax(prediction)]



if __name__ == "__main__":
    text = "Buy Health Insurance with Cashless Claim Benefit & Tax saving u/s 80D"
    print(get_predictions(text))

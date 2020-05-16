import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("//home/rutvij/Documents/spam2/Spam-Detector/prediction/emails.csv")
my_df = pd.read_csv("my_emails.csv")
# print(my_df.head())
my_df = my_df[['Subject','Spam']]
print(my_df.head())
my_df.dropna(inplace=True)


#First five rows
print(df.head(5))

#print(df.shape)
df.dropna(axis=1,inplace =True)
#print(df.shape)
#print(df.columns)

#Removing duplicates
df.drop_duplicates(inplace = True)

#print(df.shape)


#print(df.isnull().sum())



def clean_text(text):
    #Remove punctuation
    #Remove stopwords
    #Return a list of clean text words

    #1
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = "".join(nopunc)

    #2
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

    return clean_words


#print(df['text'].head().apply(clean_text))



#convert a collection of test into a matrix of text
messages_bow = CountVectorizer(analyzer=clean_text).fit_transform(df['text'])
print(messages_bow)
my_message_bow = CountVectorizer(analyzer=clean_text).fit_transform(my_df['Subject'])
print(my_message_bow)
#splitting the data
x_train,x_test,y_train,y_test = train_test_split(messages_bow,df['spam'], test_size = 0.2, random_state = 0)
_,data_test,__,Spam_test = train_test_split(my_message_bow,my_df['Spam'], test_size = 1, random_state = 0)

# data = my_message_bow
# print(x_train)
# print(x_test)


#shape
# print(messages_bow.shape)

#create and train the naive bayes classifier

classifier = MultinomialNB().fit(x_train,y_train)

print(classifier.predict(x_train))

# print(y_train.values)

#Evaluating
pred = classifier.predict(x_train)
# print(classification_report(y_train, pred))


print('Accuracy: ', accuracy_score(y_train,pred))


# print(classifier.predict(x_test))
# print(y_test.values)

pred = classifier.predict(x_test)
# print(classification_report(y_test, pred))

print('Accuracy: ', accuracy_score(y_test,pred))

print("Prediction")
pred = classifier.predict(data_test)
print(pred)





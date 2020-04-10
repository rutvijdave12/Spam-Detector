import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re


stop_words = set(stopwords.words('english'))
words = set(nltk.corpus.words.words())

# def tokenizer(string):
#     word_tokens = word_tokenize(string)
#     #print(word_tokens)
#     return word_tokens


def filter(content):
    content = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', content)
    no_punc = [char for char in content if char not in string.punctuation]
    #print(nopunc)
    no_punc = ''.join(no_punc)
    #print(nopunc)

    filtered = [word for word in no_punc.split() if word.lower() in words or not word.isalpha()]
    #print(filtered)
    filtered_list = list(set([word for word in filtered if word.lower() not in stop_words]))
    #print(filtered_list)
    filtered_list = [word for word in filtered_list if (word.isalpha() or word.isdigit())]
    
    return filtered_list



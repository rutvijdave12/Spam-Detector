#dataset 2.0.


This folder contains some python scripts which are present in readex(read and extract) and a new python module called reduce along with
two csv files showing how the dataset looks before and after some specific cleaning of the text.

Reduce.py:

1.It removes punctuations,links and stopwords present in the text.
         
2.It also removes some random combination of words and numbers (for eg. gjwj459q1vjr9eewf0wSDjjt93) which are irrelevant 
in determining if a mail is spam or ham, however some words such as 1st,2nd are also lost in this process.Losing such words
shouldn't be affecting the main motive of determining spam or ham however it would be appreciated if you find some way to retain those words.
           

Changes:
1.utf-8 decoding in login.py has been modified and an extra argument errors='ignore' has been added to decoding of bytes.
**********The result will be a csv file named 'emails' containing Sender's address,Subject and Body.***********

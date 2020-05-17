Readex:
1.Getting access to an inidividuals mail box using imap library in python.
2.extracting relevant email contents such as Sender email id, Subject, Body.
3.Cleaning the Subject and Body containing HTML tags with the help of beautiful soup (bs4 library), regex and
  some basic string operations.
  
Dataset:
1.Creating a dataset of emails containing Sender's id,Subject,Body and a spam column (containing 0s-ham by default) inside
  a csv file named "main-emails-a.csv"
2.Tokenization of Body and subject is done using the nltk library.
3.A login GUI has been added to achieve security.It asks user his/her email credentials to login when driver.py file is run 
  instead of creating a separate python script to keep user credentials which was the case previously in the readex folder
  (see config.py).

Prediction:
1.A rough model was created using Naive Bayes in scikit-learn module to see the accuracy which came out to be 0.992 approx.
2.The model created above is named trial.py is only used to test the dataset, live mails cannot be labelled as spam or ham
  using this script.
3.A working model is created using Keras which can distinguish between spam and legitimate emails.
4.Our original dataset contained only 1700 emails so we had to add some more emails which we found online in our dataset.
5.The new dataset created is used to train the model.The model created is a LSTM(Long Short Term Memory) Network
  (Part of Deep learning).
6.The first layer is a pre-trained embedding layer that maps each word to a N-dimensional vector of real numbers(See image).
  Two words that have similar meaning tend to have very close vectors.
7.The second layer is a recurrent neural network with LSTM units. Finally, the output layer is 2 neurons each corresponds
  to "spam" or "ham" with a softmax activation function(See image).
8.Then the model is trained and after that evaluation of model is done(see image for results).
9.Now predictions can be done by putting some texts after saving and loading the model.


Final Working:
1.Run driver.py file a login GUI will pop up.Enter your email credentials and then answer to the prompt asking 
  "How many emails do you want to read:".
2.Pass a number and the wait for it to process.
3.A "my_emails_unfiltered.csv" is created containing your email contents and a spam column with 0s.
4.After that further process of loading an already created model happens after which all the mails from "my_emails_unfiltered.csv"
  are passed into that model one at a time and the result(whether spam or ham) are stored in "my_emails_filtered.csv"
  which contains a spam column with "spam" or "ham" written into it accordingly.
  
  
  
  

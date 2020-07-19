# -*- coding: utf-8 -*-
"""nltk=1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ABsW48qcLVsvK8T4QXzf3B_IrrSAVNev
"""

!pip install nltk

import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

#tokenizing - word / sentences
#lexicon - dictionary (words and meanings )
#corporas - body of text

eg_text = "Hi, Ms. Tooshoes. I am great. What about you ? Will you care for a cup of tea or, do you want some coke"
print(sent_tokenize(eg_text))
print(word_tokenize(eg_text))


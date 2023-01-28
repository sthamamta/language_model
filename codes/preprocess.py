
import sys,io,os,glob,nltk, re, string
from nltk.corpus import stopwords
from timeit import default_timer as timer
from datetime import timedelta
import time
import random
     
def removeStopwords(line):
    nonstopword = []
    stop_words = set(stopwords.words('english'))
    for word in line:
        if word not in stop_words:
            nonstopword.append(word)
    return nonstopword
  
def removeNonAlpha(line):
    for word in line:
        if word.isalpha()==False:
            line = line.replace(word, " ")
    line = nltk.tokenize.word_tokenize(line)
    return line
        
def remove_short_form(line):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    line = re.sub(r"what's", "what is ", line)
    line = re.sub(r"\'s", " ", line)
    line = re.sub(r"\'ve", " have ", line)
    line = re.sub(r"can't", "cannot ", line)
    line = re.sub(r"n't", " not ", line)
    line = re.sub(r"i'm", "i am ", line)
    line = re.sub(r"\'re", " are ", line)
    line = re.sub(r"\'d", " would ", line)
    line = re.sub(r"\'ll", " will ", line)
    line = re.sub(r" e g ", " eg ", line)
    line = re.sub(r" b g ", " bg ", line)
    line = re.sub(r" u s ", " american ", line)
    line = re.sub(r"\0s", "0", line)
    line = re.sub(r"e - mail", "email", line)
    line = re.sub(r'[^\w\s]','',line)
    
    return line

def preprocess(line):
    line  = remove_short_form(line)
    line  = removeNonAlpha(line)
    # line  = removeStopwords(line)
    return line


from preprocess import *
from prob_sentence import read_bigrams, read_unigrams
import random

def get_next_word(word, bigrams):
    word = preprocess(word)
    next_words = {}
    for key in bigrams:
        if key.split()[0]== word[0]:
            next_words[key.split()[1]]= bigrams[key]
           
    sorted_words= sorted(next_words.items(), key=lambda x:x[1], reverse=True)

    # filter the words that have no bigram entry and return None while calculating next word
    sorted_words_with_bigram_entry=[]
    bigrams_key_0 =  [key.split()[0] for key in bigrams.keys()]
    for idx,(word,value) in enumerate(sorted_words):
        if word in bigrams_key_0:
            sorted_words_with_bigram_entry.append(sorted_words[idx])

    # check if there are more than five element in the next words list
    if len(sorted_words_with_bigram_entry)>5:
        sorted_words_with_bigram_entry= sorted_words_with_bigram_entry[:5] # only choose top five element from the list of next word

    # randomly shuffling the list of next words
    random.shuffle(sorted_words_with_bigram_entry)

    # check if list of next word is empty, if it is empty then return None as the next word else return the word at zero index
    if (len(sorted_words_with_bigram_entry)<=0):
        return None
    else:
        return sorted_words_with_bigram_entry[0][0]



def get_next_word_using_laplace_smoothing(word, bigrams, unigrams):
    word = preprocess(word)
    next_words = {}
    for key in bigrams:
        if key.split()[0]== word[0]:
            next_words[key.split()[1]]= bigrams[key]
           
    sorted_words= sorted(next_words.items(), key=lambda x:x[1], reverse=True)

    # filter the words that have no bigram entry and return None while calculating next word
    sorted_words_with_bigram_entry=[]
    bigrams_key_0 =  [key.split()[0] for key in bigrams.keys()]
    for idx,(word,value) in enumerate(sorted_words):
        if word in bigrams_key_0:
            sorted_words_with_bigram_entry.append(sorted_words[idx])

    # check if there are more than five element in the next words list
    if len(sorted_words_with_bigram_entry)>5:
        sorted_words_with_bigram_entry= sorted_words_with_bigram_entry[:5] # only choose top five element from the list of next word

    # randomly shuffling the list of next words
    random.shuffle(sorted_words_with_bigram_entry)

    # check if list of next word is empty, if it is empty then return random token from the list  as the next word else return the word at zero index
    if (len(sorted_words_with_bigram_entry)<=0):
        keys = list(unigrams.keys())
        random.shuffle(keys)
        return keys[0]
    else:
        return sorted_words_with_bigram_entry[0][0]
        

def generate_sentence(start_word, length=8, laplace_smoothing= False):
    sentence = [start_word]
    bigrams = read_bigrams()
    unigrams= read_unigrams()
    for i in range(length-1):
        if laplace_smoothing == True:
            next_word = get_next_word_using_laplace_smoothing(start_word,bigrams, unigrams)
        else:
            next_word = get_next_word(start_word,bigrams)
        if next_word is None: # if next word is empty then break out of loop
            break;
        sentence.append(next_word)
        start_word = next_word
    
    print (' '.join(sentence)) # print the sentence


if __name__== "__main__":
    laplace_smoothing = input('Do you want to use laplace smoothing? (y/n): ').lower().strip() == 'y'
    start_word = input("Enter a start word:")
    print("You entered",start_word)
    generate_sentence(start_word=start_word,length= 8, laplace_smoothing= laplace_smoothing)


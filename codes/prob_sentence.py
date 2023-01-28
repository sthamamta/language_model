from preprocess import *
import numpy as np

def get_total_tokens(file_path):
    with open(file_path) as f:
        try:
            lines = f.readlines()
            total_token = len(lines)
        except IOError:
            print("Cannot read input file "+file_path)
    return total_token

def read_bigrams():
    bigrams_dict = {}
    bigrams_path = 'outputs/bigrams_normalized.txt'
    with open(bigrams_path) as f:
        try:
            lines = f.readlines()
            for i,line in enumerate(lines):
                temp = []
                words = line.split( )
                temp.append(words[0])
                temp.append(words[1])
                key=' '.join(temp)
                bigrams_dict[key]= float(words[2])
        except IOError:
            print("Cannot read input file "+input_file)
    return bigrams_dict

def read_unigrams():
    unigram_dict = {}
    unigram_path = 'outputs/unigrams.txt'
    with open(unigram_path) as f:
        try:
            lines = f.readlines()
            for i,line in enumerate(lines):
                temp = []
                words = line.split( )
                unigram_dict[words[0]]= float(words[1])
        except IOError:
            print("Cannot read input file "+input_file)
    return unigram_dict

def calculate_probability(input_sentence, laplace_smoothing=False):
    prob = 0
    preprocessed = preprocess(input_sentence)
    bigrams_dict = read_bigrams()
    if laplace_smoothing== True:
        unigram_dict = read_unigrams()
    total_number_of_tokens =  get_total_tokens('outputs/unigrams.txt')
    for idx,element in enumerate(preprocessed):
        if idx < (len(preprocessed)-1):
            key = preprocessed[idx]+' '+ preprocessed[idx+1]
            if laplace_smoothing == True:
                token_count = (unigram_dict[element] if element in unigram_dict.keys() else 0)
                prob = prob + np.log( bigrams_dict[key] if key in bigrams_dict.keys() else (1/(token_count+total_number_of_tokens))) 
            else:
                prob = prob + np.log( ( bigrams_dict[key] if key in bigrams_dict.keys() else 1) )
    return prob

if __name__== "__main__":
    laplace_smoothing = input('Do you want to use laplace smoothing? (y/n): ').lower().strip() == 'y'
    input_sentence = input("Enter a sentence:")
    print("You entered :",input_sentence)
    probability = calculate_probability(input_sentence, laplace_smoothing)
    print("The probability of sentence is %0.4f. " % probability)


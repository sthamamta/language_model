import os
import time
from hash_table import HashTable
from preprocess import *


def save_to_file( count_hash, path):
    try:
        with open(path, 'w+') as output_file:
            for idx,item in enumerate(count_hash.getBgs(1000)):
                output_file.write((str(item[0])+ ' '+ str(item[1]))+'\n')

    except IOError:
        print("Cannot write output file "+output_file)


def count_bigrams_and_unigrams(input_dir, output_dir):
    bi_capacity=1000
    uni_capacity = 1000
    with open(input_dir) as f:
        try:
            print("Parsing file: "+input_dir)
            temp = []
            bhash = HashTable(bi_capacity)
            uhash = HashTable(uni_capacity)
            lines = f.readlines()
            
            #striping newlines
            striped_lines = []
            for readline in lines: 
                line_strip = readline.strip()
                striped_lines.append(line_strip)

            for line in striped_lines:
                line = preprocess(line)
                line = [elem.lower() for elem in line]
                size = len(line)
                for i in range(size-1):
                    temp.append(line[i])
                    temp.append(line[i+1])
                    bhash.find_and_update(key=' '.join(temp))
                    uhash.find_and_update(key=line[i])
                    if i==size-2:
                        uhash.find_and_update(key=line[i+1]) 
                    temp = []

        except IOError:
            print("Cannot read input file "+self.inputFile)



    path = os.path.join(output_dir, 'unigrams.txt')
    save_to_file(uhash,path)
    print("Unigrams Saved")


    path = os.path.join(output_dir,'bigrams.txt')
    save_to_file(bhash,path)
    print("Bigrams Saved")

    path = os.path.join(output_dir,'bigrams_normalized.txt')
    try:
        with open(path, 'w+') as output_file:
            for (key, elem_value) in bhash.getBgs(1000):
                item1 = key.split()[0]
                value = uhash.find(item1)
                value = bhash.update_value(key,value)
                output_file.write((str(key)+ ' '+ str(value))+'\n')
    except IOError:
        print("Cannot write output file "+output_file)
    print("normalized bigrams saved")

if __name__ == "__main__":
    startAll = timer()

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(output_dir):
        print("Creating an output directory: ",output_dir)
        os.makedirs(output_dir)
    count_bigrams_and_unigrams(input_dir, output_dir)
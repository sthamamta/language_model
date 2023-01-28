# language_model
This repository contains the code to generate Shakespearean-sounding text and calculate the probability of the given sentence.


### Usage
1. Clone the repository to your local machine.
   ```sh
   git clone https://github.com/sthamamta/language_model.git
   ```
2. Ensure that you have Python 3 and the necessary dependencies installed. These include numpy and nltk.
3. Go to codes directory
4. To run the code, specify the shell script by running:
```sh
  ./run.sh
   ```
This script will first calculate bigrams, unigrams, and normalized bigrams and store them in a text file inside the outputs directory by running the count_bigrams.py script.

Next, the prob_sentence.py script will run to calculate the probability of the input sentence with or without laplace smoothing based on user input. This script takes two inputs from the user:

The input sentence for which the probability is to be calculated
A "y" or "n" indicating whether to use laplace smoothing
Finally, the generate_sentence.py script will be run which generates a sentence based on the given input word with or without using laplace smoothing.



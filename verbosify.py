# Verbosify is a program that makes your sentences more verbose (by replacing each word with its longest synonym).

import nltk
# nltk.download('wordnet')      # you might need to uncomment this line the first time you run the program
from nltk.corpus import wordnet
import string

'''
given a word, returns it's longest synonym
'''
def get_verbose_word(word):
    # get the synonyms of the word
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    synonyms.append(word)   # in case there are no synonyms, or the current word is longer than any synonyms

    # return longest synonym
    return max(synonyms, key=len)


'''
takes in a sentence, replaces each word with it's longest synonym
'''
def verbosify(sentence):
    word_list = sentence.split(" ")
    verbose_list = []
    for word in word_list:
        word = word.strip(string.punctuation)
        verbose_word = get_verbose_word(word)
        # some verbose_words are actually multiple words, connected by underscores. Replace underscores w/ spaces here
        if '_' in verbose_word:
            verbose_word_parts = verbose_word.split('_')
            verbose_word = " ".join(verbose_word_parts)
        verbose_list.append(verbose_word)
    verbose_sentence = " ".join(verbose_list)
    return verbose_sentence


def main():
    sentence = input("Please enter a sentence to verbosify: ")
    verbose_sentence = verbosify(sentence)
    print(f"Better sentence: {verbose_sentence}")


if __name__ == "__main__":
    main()

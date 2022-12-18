from colorama import Fore, Back, Style      # used for coloring the letters on each guess
import random
import readline     # allows player to press up arrow to access their previous guesses

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
VALID_LENGTHS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 28, 45}
MIN_NUM_GUESSES = 5

'''
This function reads the words in from a file (must contain a single word on each line)

Parameters: 
- wordlist_path (string): The file path to the file we want to read words from

Returns:
- list: The list of all words in the file
'''
def read_wordlist(wordlist_path):
    wordlist = []
    with open(wordlist_path) as f:
        for word in f:
            word = word.strip().lower()
            wordlist.append(word)
    return wordlist


'''
This function gets a users requested word length for the Wordle. Will continue to ask the user to input a new guess if their
previous word length is not valid.

Returns:
- int: The user's requested word length
'''
def get_user_wordlen():
    while True:
        n = int(input(f"How many letters should today's Wordle have? "))
        if n in VALID_LENGTHS:
            return n
        print(f"Invalid word length. Valid lengths are: {VALID_LENGTHS}")


'''
This function gets all the words of length n from the provided list of words

Parameters:
- wordlist (list): A list of words
- n (int): The length of the words we want to get from our wordlist

Returns:
- list: The list of all n-letter words from wordlist
'''
def get_n_letter_words(wordlist, n):
    n_letter_words = []
    for word in wordlist:
        if len(word) == n:
            n_letter_words.append(word)
    return n_letter_words


'''
This function gets a users guess for the Wordle. Will continue to ask the user to input a new guess if their
previous guess was not a valid, n-letter word.

Parameters;
- n_letter_words (set): The set of all valid, n-letter words
- n (int): The length of a valid guess
- guesses_remaining (int): The remaining number of guesses the player has before losing

Returns:
- string: The user's valid guess
'''
def get_user_guess(n_letter_words, n, num_guesses):
    while True:
        guess = input(f"{num_guesses} guesses remaining. Guess a {n} letter word: ")
        if guess in n_letter_words:
            return guess
        print(f"Guess is not a valid word / not {n} letters")


'''
This function runs a single game of Wordle

Parameters:
- wordlist (list): list of valid words (typically all words from the english dictionary)
'''
def wordle(wordlist):
    n = get_user_wordlen()
    num_guesses = max(MIN_NUM_GUESSES, n + 1)

    n_letter_words = get_n_letter_words(wordlist, n)
    n_letter_words_set = set(n_letter_words)
    todays_word = n_letter_words[random.randint(0, len(n_letter_words) - 1)]
    print(f"Here's a hint: {todays_word}")

    # Make letter dictionary (map each letter to the indices it appears at in today's word)
    letter_to_indices = {}
    for ch in ALPHABET:
        letter_to_indices[ch] = set()
    for i in range(n):
        letter = todays_word[i]
        letter_to_indices[letter].add(i)

    while True:
        # If the player runs out of guesses, player loses
        if num_guesses <= 0:
            print(f"YOU LOSE! The word was: {todays_word}")
            return

        guess = get_user_guess(n_letter_words_set, n,  num_guesses)
        num_guesses -= 1

        # If the word is correct, player wins
        if guess == todays_word:
            print(Fore.GREEN + guess + Style.RESET_ALL)
            print("YOU WIN!")
            return

        # Color the letters in the player's guess
        temp_list = []
        for i in range(n):
            guess_letter = guess[i]
            indices = letter_to_indices[guess_letter]
            if i in indices:
                temp_list.append(Fore.GREEN + guess_letter)
            elif guess_letter in todays_word:
                temp_list.append(Fore.LIGHTYELLOW_EX + guess_letter)
            else:
                temp_list.append(Fore.RED + guess_letter)
        temp_list.append(Style.RESET_ALL)
        colored_guess = "".join(temp_list)

        print(colored_guess)


def main():
    wordlist = read_wordlist("wordlist.txt")
    wordle(wordlist)


if __name__ == "__main__":
    main()

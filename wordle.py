# ----------------------------------------------------------------------
# Name:      wordle
# Purpose:   implement the wordle game
# Author(s): Hrishikesh and Paul
# Date:
# ----------------------------------------------------------------------
"""
Enter your docstring with a one-line overview here
and a more detailed description here.
"""
import string
import random
# Constant assignments
RED = '\033[91m'     # to print text in red: print(RED + text)
GREEN = '\033[92m'   # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)
def choose_wordle(filename):
    """
    Read the file specified and choose a random 5-letter word.
    :param filename: (string) name of the file to choose the wordle from
    :return: (string) the mystery word in uppercase
    """
    random_word = ''
    with open(filename) as wordle_file:
        words = wordle_file.read().split()
        words_filter = [word for word in words if
                        word.isalpha() and len(
                            word) == 5]
        random_word = random.choice(words_filter)

    return random_word.upper()
def check(wordle, guess):
    """
    Check the player's guess against the wordle and return a string
    representing the color coded feedback for the specified guess.
    Red indicates that the guessed letter is NOT in the word.
    Yellow indicates that the letter is in the word but not in the
    correct spot.
    Green indicates that the letter is in the word in the correct spot.
    :param wordle: (string) the mystery word in upper case
    :param guess: (string) the user's guess in upper case
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # enter your code below and take out the pass statement
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string
    working_list = list(wordle)
    output_list = ['']*len(wordle)
    # going over the green letters and adding them to their
    # corresponding position
    for i in range(len(wordle)-1):
        if wordle[i] == guess[i]:
            output_list[i] = GREEN + wordle[i]
            working_list.remove(wordle[i])
    # iterating through the guess and adding the yellow letters
    # to corresponding position in output list
    for i in range(len(guess)-1):
        if guess[i] in working_list:
            output_list[i] = YELLOW + guess[i]
    # iterating and adding red letters to output
    # list
    for i in range(len(guess)-1):
        if guess[i] not in output_list and guess[i] not in working_list:
            output_list[i] = RED + guess[i]
    feedback_string = ''.join(output_list)
    return feedback_string
def feedback(attempt):
    """
    Print the feedback corresponding to the number of attempts
    it took to guess the wordle.
    :param attempt: (integer) number of attempts needed to guess
    :return: None
    """
    match attempt:
        case 1:
            print('Genius!')
        case 2:
            print('Magnificent!')
        case 3:
            print('Impressive!')
        case 4:
            print('Splendid!')
        case 5:
            print('Great!')
        case 6:
            print('Phew!')
        case other:
            print(None)




def prompt_guess():
    """
    Prompt the user repeatedly for a valid 5 letter guess that contains
    only letters.  Guess may be in lower or upper case.
    :return: (string) the user's valid guess in upper case
    """
    guess = input("Please enter your 5 letter guess: ")
    while len(guess) != 5 or not guess.isalpha():
        guess = input("Please enter your 5 letter guess: ")
    return guess.upper()
def play(wordle):
    """
    Implement the wordle game with all 6 attempts.
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts
             False otherwise
    """
    # enter your code below and take out the pass statement
    # call the prompt_guess function to prompt the user for each attempt
    # call the check function to build the colored feedback string
    # call the feedback function to print the final feedback if the user
    # guesses within 6 attempts
    attempts = 1
    while attempts <= 6:
        print(f'Attempt {attempts}')
        guess = prompt_guess()
        check(wordle, guess)
        attempts += 1

def main():
    # enter your code following the outline below and take out the
    # pass statement.
    # 1. prompt the player for a filename
    # 2. call choose_wordle and get a random mystery word in uppercase
    #    from the file specified
    # 3. call play to give the user 6 tries
    # 4. if the user has not guessed the wordle, print the correct
    #    answer
    filename = input('Please enter the filename: ')
    random_word = choose_wordle(filename)
    play(random_word)
    if not play(random_word):
        print(random_word)

if __name__ == '__main__':
    main()
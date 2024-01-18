# ----------------------------------------------------------------------
# Name:      songstats
# Purpose:   illustrate the use of sets & dictionaries
# Author(s): Hrishikesh Joshi and Paul Chon
# Date: 23 February 2023
# ----------------------------------------------------------------------
"""
This project will help users understand word-use statistics of songs.

The program will read the text files of lyrics of two songs provided by
the users. Then, it will return to the user important statistics such as
the eight most common words in each song in descending order, the total
number of distinct words in each song, and the four-letter words that
are appearing in both song's lyrics.
"""
import string
def tally(words):
    """
    Count the words in the word list specified
    :param words: (list of strings) list of lowercase words
    :return: a tally dictionary with items of the form word: count
    """
    word_dict = dict()
    for w in words:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict

def most_common(word_count):
    """
    Print the 8 most common words in the dictionary in descending order
    of frequency, with the number of times they appear.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    copy_word_count = sorted(word_count.items(), key = lambda
        x:x[1], reverse=True)
    for i in range(8):
        print(i+1,".",copy_word_count[i])
def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    print(sorted((item for item in word_count.items() if len(item[0])>=4 and item[1]>3)))

    pass
def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    with open(filename, 'r') as f:
        file_content = f.read()
        words_lowercase = file_content.lower()
        words_split = words_lowercase.split()
        words = map(lambda w: w.strip(string.punctuation), words_split)
        return list(words)



def get_stats(words):
    """
    Print the statistics corresponding to the list of words specified.
    :param words: (list of strings) list of lowercase words
    :return: None
    """
    # Call the tally function to build the word count dictionary
    # Then call the appropriate functions and print:
    # 1. The eight most common words in the song in descending order of
    #    frequency, with the number of times they appear.
    # 2. The total number of words in the song.
    # 3. The number of distinct words in the song.
    # 4. The words that are 4-letter or longer and that appear more
    #    than 3 times sorted alphabetically.
    # 5. The longest word.

    common_words(tally(words))
    print(len(words))
    print(len(set(words)))
    repeats(tally(words))
    print(max(words, key=len))


def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    words_one = set(word for word in words1 if len(word)>=4)
    words_two = set(word for word in words2 if len(word)>=4)
    print(words_one&words_two)
    # Enter your code below and take out the pass statement
    pass
def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    # and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.
    # Enter your code below and take out the pass statement
    song_one = input("Enter the first song text file: ")
    song_two = input("Enter the second song text file: ")
    s1 = get_words(song_one)
    s2 = get_words(song_two)
    common_words(s1, s2)



if __name__ == '__main__':
    main()
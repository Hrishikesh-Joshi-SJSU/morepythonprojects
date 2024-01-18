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
    copy_word_count = sorted(word_count.items(), key=lambda x: x[1],
                             reverse=True)
    for i in range(8):
        word, count = copy_word_count[i]
        print('    ' + word + ': appears ' + str(count) + ' times.')


def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    word_repeat = sorted((item for item in word_count.items() if
                          len(item[0]) >= 4 and item[1] > 3))
    for word, count in word_repeat:
        print('    ' + word)


def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    with open(filename, 'r') as songFile:
        file_content = songFile.read()
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

    word_count = tally(words)
    print('The 8 most common words are: ')
    most_common(word_count)
    print('There are ' + str(len(words)) + ' words in total in the song.')
    print('There are ' + str(len(set(words))) + ' distinct words in the song.')
    print('The following (4-letter or longer) words appear more than 3 times:')
    repeats(word_count)
    print('The longest word in the song is: ' + str(max(words, key=len)))
    print('-------------------------------------------------------------------'
          + '-------------')


def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    words_one = set(word for word in words1 if len(word) >= 4)
    words_two = set(word for word in words2 if len(word) >= 4)
    common_words_list = sorted(words_one & words_two)
    print('The words (4-letter or longer) that appear in both songs:')
    for common_word in common_words_list:
        print(common_word)


def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    # and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.
    # Enter your code below and take out the pass statement
    song_list = []
    word_list = []

    for i in range(2):
        file_name = input('Please enter the filename containing song ' +
                          str(i + 1) + ': ')
        song_list.append(file_name)
        word_list.append(get_words(file_name))

    for i in range(2):
        print('Song Statistics: ' + song_list[i])
        get_stats(word_list[i])

    common_words(word_list[0], word_list[1])


if __name__ == '__main__':
    main()
# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): Hrishikesh Joshi and Paul Chon
# ----------------------------------------------------------------------
"""
This project implements a basic chatbot.



"""
import random
import string
# Enter your constant assignments below
SPECIAL_TOPICS = {"family", "friends", "friend", "mom", "dad", "brother",
"sister", "girlfriend", "boyfriend", "children",  "son", "daughter", "child",  "wife",
"husband",  "home", "dog", "cat",  "pet"}
SET_FOR_CASE9 = {"give", "tell", "say"}
SET_FOR_CASE7 = {"need", "think", "have", "want"}
SET_FOR_CASE3 = {"would", "will", "can", "do"}
# Enter the function definition & docstring for the change_person
# function below
# Enter function definitions & docstrings for any other helper functions
def chat_with(name):
    """
    Enter your docstring
    :param name: string
    :return: Boolean
    """
    response = input('Talk to me please>').strip(".")
    modified_response = response.lower().split()# .strip(".")
    number = helper(modified_response)
    match number:
        case 1:
            print("Bye {name}.")
            print("Have a great day!")
        case 2:
            print("Tell me more about {")
        case 3:

        case 4:
            print("Why not?")
        case 5:
            possible_answers = ["{name}, why do you ask?", """{name}, how 
                                would an answer to that help you?""" ]
            print(random.choice(possible_answers))
        case 6:
            possible_answers = ["What do you think {name}?", """Why is 
             that important {name}?"""]
            print(random.choice(possible_answers))
        case 7:

        case 8:
            print(response,"too")
        case 10:
            possible_response = ["I have no clue", "Maybe"]
            print(random.choice(possible_response))
        case 11:
            print("Is that the real reason?")
        case 12:
            possible_response = ["That's interesting", "That's nice",
                                 "Can you elaborate on that?"]
            print(random.choice(possible_response))
def helper(response):
    """
    This function is a helper function for determining which case number
    applies to the response.

    :param response:
    :return: the word that is contained in the SPECIAL_TOPICS and
    response
    """
    wordset = set(response)
    specialwordset = wordset&SPECIAL_TOPICS
    if "bye" in wordset:
        return 1
    elif specialwordset&SPECIAL_TOPICS:
        return 2
    elif response[0] in SET_FOR_CASE3 and response[1] == "you":
        return 3
    elif response[len(response)-1] == "?":
        if response[0]=="why":
            return 4
        elif response[0] == "how":
            return 5
        elif response[0] == "what":
            return 6
        else:
            return 10
    elif response[0] == "i":
        if wordset &SET_FOR_CASE7:
            return 7
        else:
            return 8
    elif SET_FOR_CASE9&wordset:
        return 9
    elif "because" in wordset:
        return 11
    else:
        return 12

def main():
    # Enter your code following the outline below and take out the
    # pass statement.
    # 1.Prompt the user for their name
    name = input("Hello, what is your name please?")
    chat_with(name)
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.
    pass
if __name__ == '__main__':
    main()
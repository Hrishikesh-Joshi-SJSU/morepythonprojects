# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): Hrishikesh Joshi and Paul Chon
# ----------------------------------------------------------------------
"""
This project implements a basic chatbot.

The chatbot is a very simple one that chats based on different cases.
"""
import random
import string

# Enter your constant assignments below
SPECIAL_TOPICS = {"family", "friends", "friend", "mom", "dad", "brother",
                  "sister", "girlfriend", "boyfriend", "children", "son",
                  "daughter", "child", "wife",
                  "husband", "home", "dog", "cat", "pet"}
PRONOUN_MAP = {'i': 'you', 'am': 'are', 'my': 'your', 'your': 'my',
               'me': 'you', 'you': 'me'}


def change_person(*words):
    """
    Helper function to change the pronouns.
    :param words: variable number of words
    :return: string of words put together and pronouns changed
    """
    changed_words = []
    for word in words:
        if word in PRONOUN_MAP:
            changed_words.append(PRONOUN_MAP.get(word))
        else:
            changed_words.append(word)

    return " ".join(changed_words)


def chat_with(name):
    """
    The chatbot's response according to different cases.
    :param name: string username
    :return: Boolean True if ending chatbot and False if not
    """
    response = input('Talk to me please>')
    modified_response = response.strip(string.punctuation).lower().split()
    match modified_response:
        case ['bye']:
            print(f"Bye {name}.")
            print("Have a great day!")
            return True
        case [*words] if set(words) & SPECIAL_TOPICS:
            special_topic = set()
            for word in words:
                if word in SPECIAL_TOPICS:
                    special_topic.add(word)
            print(f"Tell me more about your {special_topic.pop()}, {name}.")
        case [('do' | 'can' | 'will' | 'would') as verb, 'you', *words]:
            changed_words = change_person(*words)
            possible_answers = [f'No {name}, I {verb} not {changed_words}.',
                                f'Yes I {verb}.']
            print(random.choice(possible_answers))
        case ['why', *words]:
            print("Why not?")
        case ['how', *words]:
            possible_answers = [f"{name}, why do you ask?",
                                f"{name}, how would an answer to that help "
                                f"you?"]
            print(random.choice(possible_answers))
        case ['what', *words]:
            possible_answers = [f"What do you think {name}?",
                                f"Why is that important {name}?"]
            print(random.choice(possible_answers))
        case ['i', ('need' | 'think' | 'have' | 'want') as verb, *words]:
            changed_words = change_person(*words)
            print(f'Why do you {verb} {changed_words}?')
        case ['i', *words] if words[-1] != 'too':
            phrase = " ".join(words)
            print(f'I {phrase} too.')
        case [('tell' | 'give' | 'say') as verb, *words]:
            phrase = " ".join(words)
            print(f'You {verb} {phrase}.')
        case [*words] if response[-1] == '?':
            possible_response = ["I have no clue", "Maybe"]
            print(random.choice(possible_response))
        case [*words] if 'because' in words:
            print("Is that the real reason?")
        case _:
            possible_response = ["That's interesting", "That's nice",
                                 "Can you elaborate on that?"]
            print(random.choice(possible_response))
    return False


def main():
    # Enter your code following the outline below and take out the
    # pass statement.
    # 1.Prompt the user for their name
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.
    name = input("Hello, what is your name please?")
    quitting = chat_with(name)
    while not quitting:
        quitting = chat_with(name)


if __name__ == '__main__':
    main()

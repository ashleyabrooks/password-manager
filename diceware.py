import random
import json
from time import time


def roll_dice():
    """Roll 'dice' with Python's random library seeded with current time.
       Random library is re-seeded with current time before each roll to
       increase entropy."""

    random.seed(time())

    roll_result = []

    while len(roll_result) != 5:
        roll_result.append(str(random.randint(1,6)))

    return ''.join(roll_result)


def convert_text_to_dict():
    """Convert EFF's long wordlist text document to hash table for quick lookup."""

    word_list_dict = {}
    wordlist_file = open('eff_wordlist_dict.txt', 'w')

    with open('eff_large_wordlist.txt') as word_list:
        for line in word_list:
            key, value = line.split('\t')
            word_list_dict[key] = value

    wordlist_file.write(str(word_list_dict))
    wordlist_file.close()


def generate_diceware_pw(word_count):
    """Use roll_dice() to generate diceware password of length determined by user."""

    diceware_list = []

    with open('eff_wordlist_dict.txt') as wordlist_data:
        wordlist = json.load(wordlist_data)

    while len(diceware_list) != word_count:
        roll_result = roll_dice()
        word = wordlist[roll_result]

        diceware_list.append(word)

    return ''.join(diceware_list)

generate_diceware_pw(6)






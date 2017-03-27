import random
from time import time

def roll_dice():
    random.seed(time())

    roll_result = []

    while len(roll_result) != 5:
        roll_result.append(random.randint(1,6))

    return roll_result

def convert_text_to_dict():

    word_list_dict = {}
    wordlist_file = open('eff_wordlist_dict.txt', 'w')

    with open('eff_large_wordlist.txt') as word_list:
        for line in word_list:
            key, value = line.split('\t')
            word_list_dict[key] = value

    wordlist_file.write(str(word_list_dict))
    wordlist_file.close()

convert_text_to_dict()


import random
import string


def get_random_card_number():
    number = ''
    for i in range(4):
        number += ''.join(random.sample(string.digits, 4))

    return int(number)


def get_random_card_cvv():
    number = ''.join(random.sample(string.digits, 3))
    return int(number)
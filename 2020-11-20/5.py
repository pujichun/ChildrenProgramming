import random


def shuffle1(lst):
    length = len(lst)
    for i in range(length):
        num = random.randint(0, length-1)
        lst[i], lst[num] = lst[num], lst[i]
    print(lst)


lst = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
shuffle1(lst)


def shuffle2(lst):
    random.shuffle(lst)
    print(lst)

shuffle2(lst)
shuffle2(lst)
shuffle2(lst)
shuffle2(lst)
shuffle2(lst)

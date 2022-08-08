# import random

# k = random.randint(2,10)
# print(k)

from random import randint

def pick_random_word():
    word_list = ["about","above","act","add","age","ago","air"]
    selected_index = randint(0,len(word_list)-1)
    return word_list[selected_index]
print(pick_random_word())   
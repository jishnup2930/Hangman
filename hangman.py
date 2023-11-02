import random

def get_random_word(library="/usr/share/dict/words"):
    good_words = []
    with open(library) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower():
                continue
            if not word.isalpha():
                continue
            if len(word) <5:
                continue
            good_words.append(word)
    
        return random.choice(good_words)

def mask_word():
    masked_word =""
    for letter in word:
        masked_word +="_"
    return masked_word
get_random_word()
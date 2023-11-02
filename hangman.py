import random

def get_random_word(library="/usr/share/dict/words"):
    good_words = []
    with open(library) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower():
                continue
            good_words.append(word)
    
        return random.choice(good_words)

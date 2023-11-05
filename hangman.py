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

def get_mask_the_word(word,guesses):
    """Returns the provided word with all letters except the ones in guesses replaced by - """
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append("-")
    return "".join(ret)

def get_status(secret_word, turns_remaining, guesses):
    masked_word = get_mask_the_word(secret_word, guesses)
    guesses = "".join(guesses)
    return f"""Secret word : {masked_word}
Turns remaining : {turns_remaining}
Guesses so far : {guesses}
"""

# def main():
#     word = get_random_word()
#     masked = get_mask_the_word(word)
#     print(f"Masked word: {masked}")

# if __name__== "__main__":
#     main()




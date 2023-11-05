import os

import hangman

def test_random_word_lowercase():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
    for _ in range(100):
        assert hangman.get_random_word(fname) == "apple"

    os.unlink(fname)

def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "mango's\n", '"beryl"'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
    os.unlink(fname)
def test_random_word_min_length_5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "ape\n", 'dog\n', 'bear\n'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
        
    os.unlink(fname)



def test_random_word_no_repeated_words():
    words = {hangman.get_random_word() for _ in range(10)}
    assert len(words) == 10 

def test_mask_word_no_guesses():
    guesses=[]
    word="elephant"
    masked_word=hangman.get_mask_the_word(word,guesses)
    assert masked_word =="--------"
    
def test_mask_word_one_guess():
    guesses =['a']
    word = 'apple'
    masked_word=hangman.get_mask_the_word(word,guesses)
    assert masked_word =="a----"

def test_mask_word_two_guesses():
    guesses=['a','e']
    word='apple'
    masked_word=hangman.get_mask_the_word(word,guesses)
    assert masked_word=='a---e'

def test_mask_word_one_guesses_multiple_choice():
    guesses=['p']
    word='apple'
    masked_word=hangman.get_mask_the_word(word,guesses)
    assert masked_word=='-pp--'

def test_mask_word_wrong_guess():
    guesses=['j']
    word='apple'
    masked_word=hangman.get_mask_the_word(word,guesses)
    assert masked_word=='-----'


def test_get_status():
    secret_word = "apple"
    turns_remaining = 10
    guesses = ['a','l','e']
    status = hangman.get_status(secret_word,
                                 turns_remaining,
                                 guesses,
                                 )
    assert status ==  """Secret word : a--le
Turns remaining : 10
Guesses so far : ale
"""

def test_play_round_correct_guess():
    secret_word = "apple"
    guesses = []
    guess = "e"
    turns_remaining = 10
    guesses, turns_remaining, next_action = hangman.play_round(secret_word,
                                                               guesses,
                                                               guess,
                                                               turns_remaining)
    assert guesses == ['e']
    assert turns_remaining == 10
    assert next_action == "next"



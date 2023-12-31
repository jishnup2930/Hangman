import random
import rich


def get_random_word(library="/usr/share/dict/words"):
    good_words = []
    with open(library) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower():
                continue
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            good_words.append(word)

        return random.choice(good_words)


def get_mask_the_word(word, guesses):
    """Returns the provided word with all letters except the ones in guesses replaced by -"""
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


def play_round(secret_word, guesses, guess, turns_remaining):
    if guess in guesses:
        return guesses, turns_remaining, "next"
    guesses.append(guess)
    if "-" not in get_mask_the_word(secret_word, guesses):
        return guesses, turns_remaining, "game_won"

    if guess not in secret_word:
        turns_remaining -= 1
        if turns_remaining == 0:
            return guesses, turns_remaining, "game_over"
    return guesses, turns_remaining, "next"


def main():
    print("")
    rich.print("[blue]Welcome to Hangman![/blue]")
    print("-------------------\n\n")
    secret_word = get_random_word()
    print(secret_word)
    turns_remaining = 10
    guesses = []
    while True:
        status = get_status(secret_word, turns_remaining, guesses)
        print(status)
        guess = input("Enter your guess ")
        guesses, turns_remaining, next_action = play_round(
            secret_word, guesses, guess, turns_remaining
        )
        if next_action == "game_over":
            rich.print(f"[red]You lost. The word is {secret_word}")
            break
        if next_action == "game_won":
            rich.print(f"[green]You won. The word is {secret_word}[/green]")
            break


if __name__ == "__main__":
    main()

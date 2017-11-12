import random

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1
    return clue



def main():
    lives = 9
    words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', 'brush', 'horse', 'light']
    secret_word = random.choice(words)
    clue = list('?????')
    heart_symbol = u'\u2764'
    guessed_word_correctly = False

    while lives > 0:
        print(clue)
        print('Lives left: ' + (heart_symbol + ' ') * lives)
        guess = input('Guess a letter or the whole word: ')

        if len(guess) != 1 and len(guess) != len(secret_word):
            print('Please print one letter at a time, or you can guess the whole word at once!')
            continue

        if guess == secret_word:
            guessed_word_correctly = True
            break

        if guess in secret_word:
            clue = update_clue(guess, secret_word, clue)
            print("Correct, '" + guess + "' is in the secret word!")
        else:
            print('Incorrect. You lose a life.')
            lives -= 1
        
    if guessed_word_correctly:
        print('You won! The secret word was ' + secret_word)
    else:
        print('You lost! The secret word was ' + secret_word)

if __name__ == "__main__":
    main()
import random

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter.lower() == secret_word[index].lower():
            clue[index] = secret_word[index]
            unknown_letters -= 1
        index += 1
    return clue, unknown_letters

# 'pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', 'brush', 'horse', 'light', 

def main():
    lives = 9
    words = ['Mississippi']
    secret_word = random.choice(words)
    clue = []
    index = 0
    while index < len(secret_word):
        clue.append('?')
        index += 1
    heart_symbol = u'\u2764'
    guessed_word_correctly = False
    unknown_letters = len(secret_word)
    guessed_list = []
    
    difficulty_verification = False
    difficulty = 0
    while not difficulty_verification:
        mode = input('Welcome to NINE LIVES! Choose difficulty (type 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
        if mode == '1' or mode == '2' or mode == '3':
            difficulty += int(mode)
            difficulty_verification = True
    
    if difficulty == 1:
        lives = 12
        print("Easy difficulty it is. Let's play!")
    elif difficulty == 2:
        lives = 9
        print("Normal difficulty it is. Let's play!")
    else:
        lives = 6
        print("Hard difficulty it is. Let's play!")

    while lives > 0:
        print(clue)
        print('Lives left: ' + (heart_symbol + ' ') * lives)
        guess = input('Guess a letter or the whole word: ')

        if len(guess) != 1 and len(guess) != len(secret_word):
            print('Please print one letter at a time, or you can guess the whole word at once!')
            continue

        if guess.lower() == secret_word.lower():
            guessed_word_correctly = True
            break

        if len(guess) == len(secret_word) and guess.lower() != secret_word.lower():
            print("Incorrect. '" + guess + "' is not the secret word. You lose a life.")
            lives -= 1
            continue

        if guess.lower() in guessed_list:
            print("'" + guess + "' has already been guessed! Try a new letter.")
            continue
        else:
            guessed_list.append(guess)

        if guess.lower() in secret_word or guess.upper() in secret_word:
            clue, unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
            suffix = ''
            if unknown_letters != 1:
                suffix = 's'
            print("Correct, '" + guess + "' is in the secret word! You have " + str(unknown_letters) + " letter" + suffix + " left to guess.")
        else:
            print('Incorrect. You lose a life.')
            lives -= 1
        
        if unknown_letters == 0:
            guessed_word_correctly = True
            break
        
    if guessed_word_correctly:
        print("You won! The secret word was '" + secret_word + "'")
    else:
        print("You lost! The secret word was '" + secret_word + "'")

if __name__ == "__main__":
    main()
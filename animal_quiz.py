def check_guess(guess, answer, score):
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score += 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again.')
            attempt += 1
    if attempt == 3:
        print('The correct answer is ' + answer)
    return score

def main():
    score = 0
    print('Guess the Animal!')
    guess1 = input('Which bear lives at the North Pole?')
    score = check_guess(guess1, 'polar bear', score)
    guess2 = input('Which is the fastest land animal?')
    score = check_guess(guess2, 'cheetah', score)
    guess3 = input('Which is the largest animal?')
    score = check_guess(guess3, 'blue whale', score)
    guess4 = input("""Which one of these is a fish?\n
    A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n
    Type A, B, C, or D """)
    score = check_guess(guess4, 'C', score)
    guess5 = input('Mice are mammals. True or false?')
    score = check_guess(guess5, 'True', score)
    print('Your score is ' + str(score))

if __name__ == "__main__":
    main()
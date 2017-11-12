import random
import string

def main():
    print('Welcome to Password Picker!')
    adjectives = ['sleepy', 'slow', 'smelly',
                'wet', 'fat', 'fluffy', 'proud', 'brave', 
                'other', 'new', 'good', 'high', 'old', 
                'great', 'big', 'American', 'small', 'large',
                'national', 'young', 'different', 
                'long', 'little', 'important', 'political', 
                'bad', 'real', 'best', 'right', 'social', 
                'only', 'public', 'sure', 'low', 'early', 
                'able', 'human', 'local', 'late', 'hard']
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'black', 'white']
    nouns = ['apple', 'dinosaur', 'ball', 'toaster',
            'goat', 'dragon', 'hammer', 'duck', 'panda', 
            'telephone', 'banana', 'teacher', 'people', 
            'woman', 'child', 'world', 'school', 'family',
            'student', 'country', 'company', 'program', 'question',
            'number', 'home', 'water', 'room', 'mother', 
            'money', 'story', 'month', 'study', 'book']
    while True:
        for num in range(3):
            adjective = random.choice(adjectives)
            color = random.choice(colors)
            noun = random.choice(nouns)
            number = random.randrange(0, 100)
            special_char = random.choice(string.punctuation)

            password = adjective + color + noun + str(number) + special_char
            print('Your new password is %s' % password)

        response = input('Would you like more passwords? Type y or n:')
        if response == 'n':
            break

if __name__ == "__main__":
    main()
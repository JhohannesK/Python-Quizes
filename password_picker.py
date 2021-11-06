import string
from random import choice, randrange

print("Welcome to Password Picker!")

adjectives = ['sleepy', 'slow', 'smelly',
              'wet', 'fat', 'red',
              'blue', 'purple', 'fluffy',
              'orange', 'yellow', 'green',
              'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']

while True:
    adjective = choice(adjectives)
    noun = choice(nouns)
    number = randrange(0, 100)
    special_char = choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' %password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break
import random
import emoji

lives = 9
words = ['plane', 'mouse', 'phone', 'pizza', 'fairy', 'teeth', 'shirt']
secret_word = random.choice(words)
print(secret_word)
clue = list('?????')
heart_symbol = emoji.emojize(':red_heart:')


def Nine_lives(guessed_letter, clue, secret_word):
    index = 0
    while index < len(secret_word):
        if guessed_letter.lower() == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

guessed_letters_correctly = False
while lives > 0:
    print(clue)
    print('Lives left: ', heart_symbol * lives)
    guessed_letter = input('Guess a letter or word: ')

    if guessed_letter.lower() == secret_word:
        print('You guessed the word right!!')
        break

    if guessed_letter.lower() in secret_word:
        print("That's right")
        Nine_lives(guessed_letter, clue, secret_word)
        if ''.join(clue) == secret_word or ''.join(clue) == secret_word.upper():
            guessed_letters_correctly = True
            break
    else:
        print('Incorrect letter. you lose a life')
        lives -= 1

if guessed_letters_correctly:
    print(f"The word was {secret_word}")
else:
    print(f"The word was {secret_word.upper()}")
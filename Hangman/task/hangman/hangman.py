# Write your code here
import random as r

# hint = word[:3]+'-'*len(word[3:])
print('H A N G M A N')
while True:
    play = input('Type "play" to play the game, "exit"  to quit: ')
    if play == 'exit':
        break
    elif play != 'play':
        continue
    words = ['python', 'java', 'kotlin', 'javascript']
    word = r.choice(words)
    objective = ['-'] * len(word)
    num_guesses = 0
    guessed = set()
    while num_guesses < 8:
        print('\n'+''.join(objective))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should print a single letter.')
        elif not letter.islower():
            print('It is not an ASCII lowercase letter.')
        elif letter not in guessed:
            if letter in word:
                for i, x in enumerate(word):
                    if x == letter:
                        objective[i] = x
                guessed.add(letter)
                if '-' not in objective:
                    break
            else:
                print('No such letter in the word')
                guessed.add(letter)
                num_guesses += 1
        else:
            print('You already typed this letter')
            continue

    if ''.join(objective) != word:
        print('You are hanged!\n')
    else:
        print(f'You guessed the word {word}!')
        print('You survived!\n')

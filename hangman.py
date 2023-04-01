'''
Skapa en version av det klassiska spelet Hangman.
Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.
Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.
Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.
Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.
'''
import pandas as pd
import os
import time
import random

class WrongType():

    def __init__(self, letter, *args):
        super().__init__(args)
        self.letter = letter
        print(f'{letter} is sent to {__class__.__name__}')

    def __str__(self):
        return f"WARNING! The '{self.letter}' is not a letter"
        
class LengthError():

    def __init__(self, letter, *args):
        super().__init__(args)
        self.letter = letter
        print(f'{self.letter} is sent to {__class__.__name__}')

    def __str__(self):
        return f"WARNING! The '{self.letter}' you typed has too many letters"

class MaxAttempt(Exception):

    def __init__(self, max_nr_attempt, *args):
        super().__init__(args)
        self.max_nr_attempt = max_nr_attempt
        print(f'{self.letter} is sent to {__class__.__name__}')

    def __str__(self):
        return f"WARNING! You tried '{self.max_nr_attempt}' times and you failed to guess the correct word"
'''
Try to add a functioniality to give the user the chance of starting a new game without the need 
for thowing an exception and kill the process
'''
# Here we choose one word from a database that contains over 3,000,000 words
# from movie lines
def random_word():
    csv_url = "./db-1_wordle/wordle_random.csv"
    with open(csv_url, 'r') as csvfile:
        csv_text = csvfile.read().splitlines()
        chosen_row = csv_text[random.randint(0,len(csv_text)-1)].split(',')
        return chosen_row[0]

# Here we check if the feed is correct for one single input
# Return back the result to the calling method
def get_next():
    index = 0
    while True:
        index += 1
        letter = input('Enter a letter: ')
        if not letter.isalpha():
            print(f"WARNING! The '{letter}' is not a letter")
            return False
        elif not len(letter) == 1:
            print(f"WARNING! The '{letter}' you typed has too many letters")
            return False
        else:
            return letter
'''
 if a letter is entered repeatedly, warn the player of it and do not count 
towards MAX

inactivity for more than 1 minute should be warned and after a more minute
the game should be ended, and the current result shown
    '''        

# As long as the MAX number of attempts has not been reached, continue accepting
# letters, check correctness of the feed and handle the issues that may arise
def play_game():
    print(f'The word I have chosen for you is {len(chosen_word)} letters long')
    letter = ''
    guessed = ''
    found = ''
    MAX = 13
    index = 0
    # If something is wrong with the input, ignore, increase index and proceed
    # If not, match the letter with the letters in the word and let the player
    # know if the guess is qualified or not
    while True:
        result = get_next()
        index += 1
        if not result:
            pass
        else:
            if letter in guessed:
                guessed += letter
                print(f"You've already named '{letter}', and I told you it's not there")
            else:
                if letter in found:
                    print(f"Yes, there is also a '{letter}' in my word")
                    guessed_word = input("Would you like to gueess what the word is?")
                    # continue here ...
        if index > MAX:
            raise MaxAttempt(MAX)
        
'''
add antother function and input here to ask for the word after a letter was successfully
chosen by the player

in this new window, if a dash is entered, it means the player does not want to
continue. print the current results and stop the game
'''

#    print(type(numbers1),'    ',type(player_word)):
#    result = ''.join(list(map(lambda x, y: str(x) if x==y else '*', player_word, chosen_word)))
#    print(result)

if __name__ == '__main__':
    print('starting')
    global chosen_word
    chosen_word = random_word()
    try:
        error = play_game()
    except MaxAttempt as ma:
        print(ma)

import random 
from time import process_time_ns
import time

computer_guessed_number = random.randint(1, 100) #randint - izvelas random skaitli kas iekavas
continue_game = True
user_guesses = []
start_time = time.time()
 #type - parbauda klasi 

while(continue_game):
    user_guess = int(input('guess number between 1 and 100'))
    user_guesses.append(user_guess)

    if user_guess == computer_guessed_number:
        print('you win') 
        continue_game = False
    elif user_guess < computer_guessed_number:
        print('more')
    elif user_guess > computer_guessed_number:
        print('less')
    else:
        print('there is kluda')

sum_of_difference = 0

for n in user_guesses:
    sum_of_difference += abs(n - computer_guessed_number)
avarage_of_difference = sum_of_difference / len(user_guesses)
print(f'videja starpiba bija {avarage_of_difference}')

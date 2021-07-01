numbers = [1, 2, 3, 4]
print ("Numbers in the list = ", len(numbers))

str = "My name is Arishay"
print(str.split())

# Import date and day 
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Boolean coding
print(10 > 9)


import random
number = random.randint(1, 10)


# Enter player user name
player_name = input("Hello, What's your name? ")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))

import random

attempts = 0

while True:

    random_num = random.randint(1,9)

    user_num = int(input('Hello there! Guess a number between 1 - 9: '))

    if random_num == user_num :
        print('You alright!')
        attempts += 1
    elif user_num > random_num:
        print('You are high')
        attempts += 1
    elif user_num < random_num:
        print('You are low')
        attempts += 1

    choice = input('if you want to quit, enter (exit): ')

    if choice == 'exit':
        break

print('The number of guesses is: ' + str(attempts))

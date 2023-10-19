import random


def guess_number(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        if user_guess < random_number:
            print('Sorry, guess again. Too low.')
        elif user_guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_by_computer = random.randint(low, high)
        else:
            guess_by_computer = low  # could also be high b/c low = high
        feedback = input(f'Is {guess_by_computer} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess_by_computer - 1
        elif feedback == 'l':
            low = guess_by_computer + 1

    print(f'Yay! The computer guessed your number, {guess_by_computer}, correctly!')


guess_number(10)

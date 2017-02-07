import random

def main():

    secret = get_secret_number()

    while True:

        guess = get_guess()

        if guess < secret:
            print('too low!')
        elif guess > secret:
            print('too high!')
        else:
            break

    print('Correct!')

def get_guess():
    # todo validation
    return int(input('guess the number? '))

def get_secret_number():
    return random.randint(1, 10)


if __name__ == '__main__':
    main()

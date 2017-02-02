import random

# simple dice game. If you roll a 6, you win
# otherwise you lose.
def main():
    won = play()
    if won:
        print('you win!')
    else:
        print('you lose :(')

def play():
    ''' roll dice. return True if user wins. '''

    number_rolled = roll()
    print('You rolled a %d' % number_rolled)
    return number_rolled == 6

def roll():
    return random.randint(1, 6)

if __name__ == '__main__':
    main()

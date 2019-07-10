import numpy as np
from random import *

rows = 4
cols = 4
board = np.zeros((rows,cols,2))
characters = [u'\u0293',u'\u0278',u'\u03C0',u'\u03A9', u'\u03A8',u'\u03A3',u'\u0414',u'\u0411']

def make_board():
    for i in range(2):
        for charidx in range(len(characters)):
            r = randint(0,rows-1)
            c = randint(0,cols-1)
            while board[r,c,1] != 0.0:
                r = randint(0,rows-1)
                c = randint(0,cols-1)
            board[r,c,1] = charidx
            

def print_board():
    print("    1 2 3 4")
    print('  ---------')
    for r in range(rows):
        print('{} | '.format(r+1)+' '.join(characters[int(board[r,c,1])] if board[r,c,0] == 1.0 else u'\u2588' for c in range(cols)))

def get_choice(limit, pos, turn):
    while True:
        try:
            idx = int(input('Enter the {} of the {} card you would like to flip:  '.format(pos,turn)))-1
        except ValueError:
            print ('That is not a number. Please enter a number between 1 and {}.'.format(limit))
        else:
            if idx >= limit:
                print ('That {} is out of range. Please enter a number between 1 and {}.'.format(pos,limit))
            else:
                break
    return idx


def main():
    make_board()
    print_board()
    match_count = 0
    attempts = 0
    first_flip = True
    while match_count < len(characters):
        if first_flip:
            r1 = get_choice(rows, 'row','first')
            c1 = get_choice(cols,'column','first')
            if board[r1,c1,0] == 1.0:
                print('That card is already flipped.')
            else:
                first_flip = False
                board[r1,c1,0] = 1.0
                print_board()
        else:
            r2 = get_choice(rows,'row','second')
            c2 = get_choice(cols,'column','second')
            if board[r2,c2,0] == 1.0:
                print('That card is already flipped.')
            else:
                attempts += 1
                board[r2,c2,0] = 1.0
                first_flip = True
                print_board()
                if board[r1,c1,1] == board[r2,c2,1]:
                    print('You got a match!')
                    match_count += 1
                else:
                    print('No match! Better luck next time.')
                    board[r1,c1,0] = 0.0
                    board[r2,c2,0] = 0.0
                    print_board()
    print('You completed the game in {} attempts.'.format(attempts))
            
if __name__ == '__main__':
    main()

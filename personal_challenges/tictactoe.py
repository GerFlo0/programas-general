#tic-tac-toe
import os
import random
import numpy
import random

matrix = numpy.full((3, 3), ' ', dtype = str)

next_matrix = matrix

empty_positions = [
    (0,0),(0,1),(0,2),
    (1,0),(1,1),(1,2),
    (2,0),(2,1),(2,2)]

turn = 'X'

win = False

def draw_board ():
    os.system('cls')
    print('\n')
    print(f"  {matrix[2][0]}  |  {matrix[2][1]}  |  {matrix[2][2]}  3")
    print('-----|-----|-----')
    print(f"  {matrix[1][0]}  |  {matrix[1][1]}  |  {matrix[1][2]}  2")
    print('-----|-----|-----')
    print(f"  {matrix[0][0]}  |  {matrix[0][1]}  |  {matrix[0][2]}  1")
    print("  a     b     c")
    print('\n')

def is_valid_position(pos = tuple):
    return pos in empty_positions

def next_turn():
    if turn == 'X': return'O'
    else: return 'X'

def is_win():
    return False

def delete_empty_position(pos = tuple):
    empty_positions.remove(pos)

def bot_choose_position():
    return random.choice(empty_positions)

def is_valid_input(input = tuple):
    if len(input) != 2: return False
    if not str(input[0]).isalpha: return False
    if not str(input[1]).isdigit: return False
    return True

def input_to_position(input = str):
    return (int(input[1]) - 1, ord(input[0]) - 97)

while (not win and not len(empty_positions) == 0):
    draw_board()
    if turn == 'X':
        while(True):
            user_position = input_to_position(input('Choose a position: '))
            if (user_position in empty_positions):
                matrix[user_position]=turn
                empty_positions.remove(user_position)
                turn = next_turn()
                break
    else:
        pos = random.choice(empty_positions)
        matrix[pos] = turn
        empty_positions.remove(pos)
        turn = next_turn()

print("salida")
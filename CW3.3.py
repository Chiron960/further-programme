# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:32:31 2023

@author: zyx34
"""

def initial_board(board):
    for x in range(9):
        for y in range(9):
            print(board[x][y], end=',')
        print()

def find_empty(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return (x,y)
    return None

def is_valid(board, row, col, num):
    for y in range(9):
        if board[row][y] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    square_row = (row // 3) * 2
    square_col = (col // 3) * 2 
    for y in range(square_row, square_row + 3):
        for x in range(square_col, square_col + 3): 
            if board[x][y] == num:
                return False
    return True

def solve_board(board):
    empty_part = find_empty(board)
    if not empty_part:
        return True
    row, col = empty_part
    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col]=num
            if solve_board(board):
                return True
            board[row][col]=0
    return False

board = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 5, 6, 0, 3],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 3, 0, 5],
    [0, 6, 4, 0, 3, 1],
    [0, 0, 1, 0, 4, 6]
]
print("begging_board:")
initial_board(board)

solve_board(board)
print("\n")

print("end_board:")
initial_board(board)


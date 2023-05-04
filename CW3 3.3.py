# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:32:31 2023

@author: zyx34
"""
#Outputs an array of initial sudoku so the user can see the state of the sudoku
def initial_board(board):
    for x in range(9):
        for y in range(9):
            print(board[x][y], end=' ')
        print()

#Find the location of a space in a sudoku and return its coordinates        
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
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3 
    for x in range(square_row, square_row + 3):
        for y in range(square_col, square_col + 3): 
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
    [9, 0, 6, 0, 0, 1, 0, 4, 0],
    [7, 0, 1, 2, 9, 0, 0, 6, 0],
    [4, 0, 2, 8, 0, 6, 3, 0, 0],
    [0, 0, 0, 0, 2, 0, 9, 8, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 9, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 3, 7, 0, 8, 4, 0, 9],
    [0, 4, 0, 0, 1, 3, 7, 0, 6],
    [0, 6, 0, 9, 0, 0, 1, 0, 8]
    ]

print("begging_board:")
initial_board(board)

solve_board(board)
print("\n")

print("end_board:")
initial_board(board)

# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:28:30 2023

@author: zyx34
"""

#Outputs an array of initial sudoku so the user can see the state of the sudoku
def initial_board(board):
    for x in range(6):
        for y in range(6):
            print(board[x][y], end=',')
        print()

#Find the location of a space in a sudoku and return its coordinates     
def find_empty(board):
    for x in range(6):
        for y in range(6):
            if board[x][y] == 0:
                return (x,y)
    return None
#Finds the location of a space in Sudoku and returns its coordinates Checks if a given number has already occurred in a row, column, and house. The function will return True if the number is not repeated in any row, column or house
def is_valid(board, row, col, num):
    for y in range(6):
        if board[row][y] == num:
            return False
    for x in range(6):
        if board[x][col] == num:
            return False
    square_row = (row // 2) * 3
    square_col = (col // 3) * 2 
    for y in range(square_row, square_row + 2):
        for x in range(square_col, square_col + 3): 
            if board[x][y] == num:
                return False
    return True

def solve_board(board):
    for depth in range(1, 7):
        if solve_recursive(board, depth):
            return True
    return False

def solve_recursive(board, depth):
    empty_part = find_empty(board)
    if not empty_part:
        return True
    row, col = empty_part
#Returns True if a solution was found, and the original array is modified to display the answer.
    for num in range(1,7):
        if is_valid(board, row, col, num):
            board[row][col]=num
            if depth > 1 and not solve_recursive(board, depth - 1):
                board[row][col]=0
            else:
                return True
    return False

board = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 5, 6, 0, 3],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 3, 0, 5],
    [0, 6, 4, 0, 3, 1],
    [0, 0, 1, 0, 4, 6]
]

print("begging_sudoku:")
initial_board(board)

solve_board(board)
print("\n")

print("end_sudoku:")
initial_board(board)

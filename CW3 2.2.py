# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:51:44 2023

@author: zyx34
"""

#Outputs an array of initial sudoku so the user can see the state of the sudoku
def initial_board(board):
    for x in range(4):
        for y in range(4):
            print(board[x][y], end=' ')
        print()

#Find the location of a space in a sudoku and return its coordinates
def find_empty(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == 0:
                return (x,y)
    return None
#Finds the location of a space in Sudoku and returns its coordinates Checks if a given number has already occurred in a row, column, and house. The function will return True if the number is not repeated in any row, column or house
def is_valid(board, row, col, num):
    for y in range(4):
        if board[row][y] == num:
            return False
    for x in range(4):
        if board[x][col] == num:
            return False
    square_row = (row // 2) * 2
    square_col = (col // 2) * 2 
    for y in range(square_row, square_row + 2):
        for x in range(square_col, square_col + 2): 
            if board[x][y] == num:
                return False
    return True

#Sudoku solver. By recursively calling the function solve_board(), the function will try to fill in the blanks with numbers and check for collisions.
def solve_board(board):
    empty_part = find_empty(board)
    if not empty_part:
        return True
    row, col = empty_part
    for num in range(1,5):
        if is_valid(board, row, col, num):
            board[row][col]=num
#Returns True if a solution was found, and the original array is modified to display the answer.
            if solve_board(board):
                return True
            board[row][col]=0
    return False

board = [
    [0,2,0,4],
    [3,0,0,2],
    [4,1,2,0],
    [0,0,0,1]
    ]

print("begging_board:")
initial_board(board)

solve_board(board)
print("\n")

print("end_board:")
initial_board(board)

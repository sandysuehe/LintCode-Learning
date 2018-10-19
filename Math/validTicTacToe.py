#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 17:54:01
# File Name: validTicTacToe.py
# Description: Valid Tic-Tac-Toe State 验证井字棋状态 
# LintCode: https://www.lintcode.com/problem/valid-tic-tac-toe-state/
#########################################################################
def validTicTacToe(board):
    x_win = False
    o_win = False
    row = [0, 0, 0]
    col = [0, 0, 0]
    diag = 0
    anti_diag = 0
    turns = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                row[i] += 1
                col[j] += 1
                turns += 1
                if i == j:
                    diag += 1
                if i + j == 2:
                    anti_diag += 1
            elif board[i][j] == 'O':
                row[i] -= 1
                col[j] -= 1
                turns -= 1
                if i == j:
                    diag -= 1
                if i + j == 2:
                    anti_diag -= 1

    if row[0] == 3 or row[1] == 3 or row[2] == 3 or col[0] == 3 or col[1] == 3 or col[2] == 3 or diag == 3 or anti_diag == 3:
        x_win = True 

    if row[0] == -3 or row[1] == -3 or row[2] == -3 or col[0] == -3 or col[1] == -3 or col[2] == -3 or diag == -3 or anti_diag == -3:
        o_win = True 

    # x win但选择权还在o
    if x_win and turns == 0:
        return False

    # o win但选择权还在x
    if o_win and turns == 1:
        return False

    # turns要么是x，要么是o，并且x_win或者o_win
    return turns in (0, 1) and (not x_win or not o_win)

board = ["O  ", "   ", "   "]
print board, validTicTacToe(board)
board = ["XOX", " X ", "   "]
print board, validTicTacToe(board)
board = ["XXX", "   ", "OOO"]
print board, validTicTacToe(board)
board = ["XOX", "O O", "XOX"]
print board, validTicTacToe(board)
board = ["OOX"," XO","X  "]
print board, validTicTacToe(board)
board = ["XX "," O ","  O"]
print board, validTicTacToe(board)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

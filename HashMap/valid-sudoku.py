#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: valid-sudoku.py
# Description: 判断数独是否合法 Valid Sudoku 
# LintCode: https://www.lintcode.com/problem/valid-sudoku/
#########################################################################
# 思路:
# 验证一个方阵是否为数独矩阵，判断标准是看各行各列是否有重复数字，以及每个小的3x3的小方阵里面是否有重复数字,
# 如果都无重复，则当前矩阵是数独矩阵，但不代表待数独矩阵有解，只是单纯的判断当前未填完的矩阵是否是数独矩阵。
# 在遍历每个数字的时候，就看看包含当前位置的行和列以及3x3小方阵中是否已经出现该数字
#########################################################################
def isValidSudoku(board):
    m = len(board)
    n = len(board[0])

    if m == 0 or n == 0:
        return False

    rowFlag = [[False for i in range(n)] for j in range(m)] 
    colFlag = [[False for i in range(n)] for j in range(m)] 
    cellFlag = [[False for i in range(n)] for j in range(m)] 

    for i in range(m):
        for j in range(n):
            index = 3*(i/3)+j/3
            if board[i][j].isdigit():
                val = int(board[i][j]) - 1

                if rowFlag[i][val]:
                    return False
                else:
                    rowFlag[i][val] = True

                if colFlag[val][j]:
                    return False
                else:
                    colFlag[val][j] = True

                if cellFlag[index][val]:
                    return False
                else:
                    cellFlag[index][val] = True
    return True


board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print isValidSudoku(board)

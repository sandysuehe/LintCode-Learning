def addDigits(num):
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: addDigits.py
# Description: 各位相加
# LintCode: https://www.lintcode.com/problem/add-digits/
#########################################################################
    if num / 10 == 0:
        return num
    count = 0
    while num:
        count +=  num % 10
        num = num / 10
    return addDigits(count)
    
num = 38
num = 100 
print addDigits(num)


#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 16:48:48
# File Name: two-numbers-that-are-not-repeated.py
# Description: Two Numbers That Are Not Repeated
# LintCode: https://www.lintcode.com/problem/two-numbers-that-are-not-repeated/
#########################################################################
def theTwoNumbers(a):
    n = 0
    for i in a:      #Get the xor of all elements
        n = n ^ i

    count = 0
    while (n & (1 << count)) == 0:
        count += 1

    ans1 = 0
    ans2 = 0

    for i in a:
        if (i & (1<<count)) == 0:
            ans1 ^= i
        else:
            ans2 ^= i
    return [ans1, ans2]

a =[1,2,5,5,6,6]
print theTwoNumbers(a)
# a=[3,2,7,5,5,7]
# print theTwoNumbers(a)

#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 12:42:04
# File Name: integer-to-english-words.py
# Description:  Integer to English Words
# LintCode: https://www.lintcode.com/problem/integer-to-english-words/
#########################################################################
IN_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
IN_HUNDRED = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
OVER_THOUSAND = ["", "Thousand", "Million", "Billion"]

def numberToWords(num):
    if num == 0:
        return "Zero"

    res = ""
    i = 0
    while num > 0:
        pre = convertHundred(num % 1000)
        if pre != "":
            res = "{0} {1} {2}".format(pre, OVER_THOUSAND[i], res)
        num /= 1000
        i += 1

    return res.strip()


def convertHundred(num):
    res = ""
    if num < 20:
        res = IN_TWENTY[num]
    elif num < 100:
        res = "{0} {1}".format(IN_HUNDRED[num/10], IN_TWENTY[num%10]) 
    else:
        res = "{0} Hundred {1}".format(IN_TWENTY[num/100], convertHundred(num%100)) 
    return res

num = 680901192 
print numberToWords(num)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

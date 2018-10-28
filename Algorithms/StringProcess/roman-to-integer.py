#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
# LintCode: https://www.lintcode.com/problem/roman-to-integer
# Rule:
# 1、相同的数字连写，所表示的数等于这些数字相加得到的数，如：Ⅲ = 3；
# 2、小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数， 如：Ⅷ = 8；Ⅻ = 12；
# 3、小的数字，（限于Ⅰ、X 和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如：Ⅳ= 4；Ⅸ= 9；
# 4、正常使用时，连写的数字重复不得超过三次。（表盘上的四点钟“IIII”例外）
# 5、在一个数的上面画一条横线，表示这个数扩大1000倍。
# 6、基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
# 7、不能把基本数字V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
# 8、V 和X 左边的小数字只能用Ⅰ。
# 9、L 和C 左边的小数字只能用X。
# 10、D 和M 左边的小数字只能用C。

def romanToInt(s):
    # ROMAN基本字符对应阿拉伯数字
    ROMAN = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    n = len(s)
    res = 0

    if not s or n == 0:
        return 0

    for i in range(n):
        val = ROMAN[s[i]]
        if i == n-1:
            res += val
        elif ROMAN[s[i+1]] <= ROMAN[s[i]]:
            res += val
        else:
            res -= val
    return res

s = "IV"
print romanToInt(s)


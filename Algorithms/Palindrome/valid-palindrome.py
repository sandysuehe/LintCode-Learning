#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
# LintCode: https://www.lintcode.com/problem/valid-palindrome
#########################################################################
# 所谓回文，就是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。
# 题解：
# 只需要建立两个指针，left和right, 分别从字符的开头和结尾处开始遍历整个字符串;
# 如果遇到非字母数字的字符就跳过，继续往下找，直到找到下一个字母数字或者结束遍历;
# 如果遇到大写字母，就将其转为小写。
# 等左右指针都找到字母数字时，比较这两个字符，若相等，则继续比较下面两个分别找到的字母数字,
# 若不相等，直接返回false. 
#########################################################################
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not isAlphaNum(s[left]):
            left += 1
        while left < right and not isAlphaNum(s[right]):
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def isAlphaNum(char):
    if char >= "a" and char <= "z":
        return True
    if char >= "A" and char <= "Z":
        return True
    if char >= "0" and char <= "9":
        return True
    return False

s = "A man, a plan, a canal: Panama" 
print isPalindrome(s)
s = "race a car"
print isPalindrome(s)

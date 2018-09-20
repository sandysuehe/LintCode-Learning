#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-13 19:05:54
# File Name: fullJustify.py
# Description: 
#########################################################################
def fullJustify(words, maxWidth):
    res = []

    if not words or len(words) == 0:
        return res

    left = 0

    while left < len(words):
        right = left
        count = 0

        # count: 上一次计算的单词长度
        # len(words[right]): 当前尝试的单词长度
        # right - left：这一行单词间的间隔数
        # 确定每一行能放下的单词数：比较（n个单词的长度+n-1个空格的长度）和 maxWidth长度

        while right < len(words) and count + len(words[right]) + right - left <= maxWidth:
            count += len(words[right])
            right += 1

        output = ""
        # 这一行的空格总数
        space_num = maxWidth - count

        for i in range(left, right):
            # 加入单词
            output += words[i]
            # 加入空格
            if space_num > 0:
                interval = 0
                # 当遍历到最后一行时，如果是最后一个单词，不需要再加空格，否则加空格
                if right == len(words):
                    if right - i == 1:
                        interval = space_num
                    else:
                        interval = 1
                else:
                    # 当没有遍历到最后一个单词时
                    if right - i -1 > 0:
                        if space_num % (right - i -1) == 0:
                            interval = space_num / (right - i -1)
                        else:
                            interval = space_num / (right - i -1) + 1
                    else:
                        interval = space_num
                output += " " * interval
                space_num -= interval
        res.append(output)
        left = right
    return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print fullJustify(words, maxWidth)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

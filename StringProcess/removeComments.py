#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 16:44:34
# File Name: removeComments.py
# Description: 删除注释 
# LintCode: https://www.lintcode.com/problem/remove-comments/
#########################################################################
def removeComments1(source):
    if not source:
        return []

    ans = []
    out = ""
    iscomment = False

    for i in range(0, len(source)):
        j = 0
        while j < len(source[i]):
            if not iscomment and j+1 < len(source[i]) and source[i][j] == "/" and source[i][j+1] == "/":
                # 如果没有注释，并且遇到了//的话，那么s相当于没有内容
                break
            elif not iscomment and j+1 < len(source[i]) and source[i][j] == "/" and source[i][j+1] == "*":
                # 如果没有注释，并且遇到了/*就说明有注释，直到下一个*/为止 
                iscomment = True
                j += 1
            elif iscomment and j+1 < len(source[i]) and source[i][j] == "*" and source[i][j+1] == "/":
                # 如果还在注释的情况下，遇到*/，那么就说明结束注释 
                iscomment = False
                j += 1
            elif not iscomment:
                out = out + source[i][j]
            j += 1

        if not iscomment and len(out):
            ans.append(out)
            out = ""
    return ans


source = ["a/*comment", "line", "more_comment*/b"]
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print removeComments1(source)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 16:37:57
# File Name: tag-validator.py
# Description: 标签验证器
# LintCode: https://www.lintcode.com/problem/tag-validator/
#########################################################################
# 思路: 成对匹配的问题, 需要用栈stack的
#########################################################################
def isValid(code):
    stack = []
    i = 0
    while i < len(code):
        if i > 0 and len(stack) == 0: # 开头结尾不是标签的情况，以及没有标签的情况，和开头的标签在中间就闭合了情况等等
            return False

        if code[i:i+9] == "<![CDATA[": # 判断<![CDATA[和]]>的成对匹配
            j = i+9
            i = code.find("]]>", j)
            if i < 0:
                return False
            i += 2
        elif code[i:i+2] == "</":     # 判断</和>的成对匹配 
            j = i+2
            i = code.find(">", j)
            if i < 0:
                return False
            # tag = code[j: i-j+1]
            tag = code[j: i]
            if len(stack) == 0 or stack[-1] != tag:
                return False
            stack.pop()
        elif code[i: i+1] == "<":    # 判断<和>的成对匹配
            j = i+1
            i = code.find(">", j)
            if i < 0 or i==j or i-j>9:
                return False
            for k in range(j,i):
                if code[k] < 'A' or code[k] > 'Z':
                    return False
            tag = code[j: i]
            stack.append(tag)
        i += 1
    return len(stack) == 0

code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
#code = "<DIV><YFSYYS><UVBNIQ><XPMXUNT><WNGMV><OJJGQREMT><Z><GEJDP><LIQS><NCVYU><RAS><UYFKCJCDN><NA><POJVYT><Z><TDC><VUIZQC><BNANGX><TOF><MR>MK</MR></TOF></BNANGX></VUIZQC></TDC></Z></POJVYT></NA></UYFKCJCDN></RAS></NCVYU></LIQS></GEJDP></Z></OJJGQREMT></WNGMV></XPMXUNT></UVBNIQ></YFSYYS></DIV>"
print isValid(code)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

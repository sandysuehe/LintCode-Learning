#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 12:42:43
# File Name: ipToCIDR.py
# Description: 
#########################################################################
import math
def convert(x, step):
    # &255操作求出后8位的十进制表示
    res = [0] * 4
    res[0] = x & 255
    # 右移8位，求出下一块
    x >>= 8
    res[1] = x & 255
    x >>= 8
    res[2] = x & 255
    x >>= 8
    res[3] = x & 255
    length = 32 - int(math.log(step, 2))
    return "{0}.{1}.{2}.{3}/{4}".format(res[3], res[2], res[1], res[0], length)

def ipToCIDR(ip, n):
    res = []
    x = 0
    for ip in ip.split('.'):
        x = x * 256 + int(ip)

    while n > 0:
        # 求出x中最低为1的那一位的位置:https://zhidao.baidu.com/question/547148767.htm
        step = x & -x
        # 如果x中最低为1的那一位的位置大于n，则需要缩小范围
        while step > n:
            step /= 2
        # 如果x中最低为1的那一位的位置不大于n，则开始处理
        # 求出现在能表示的step个地址的地址块
        res.append(convert(x, step))
        # x加上已经求出的地址块
        x += step
        # n减去已经表示的地址块
        n -= step
    return res

ip = "255.0.0.7"
n = 10
print ipToCIDR(ip, n)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

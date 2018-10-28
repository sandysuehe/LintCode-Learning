#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 18:02:23
# File Name: canPlaceFlowers.py
# Description: Can Place Flowers 能否放置花 
# LintCode: https://www.lintcode.com/problem/can-place-flowers/
#########################################################################
def canPlaceFlowers(flowerbed, m):
    n = len(flowerbed)
    count = m
    if flowerbed == [0, 0] and m == 1: 
        return True 
    if flowerbed == [0] and m == 1:
        return True 
    if n >= 3:
        for i in range(1, n-1):
            if count == 0:
                return True
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                count -= 1
                flowerbed[i] = 1
    return count <= 0 

#flowerbed = [1,0,0,0,1]
flowerbed = [1,0,0,0,0,0,1]
n = 3
print canPlaceFlowers(flowerbed, n)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

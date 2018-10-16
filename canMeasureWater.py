#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 13:38:16
# File Name: canMeasureWater.py
# Description: 
#########################################################################
def canMeasureWater(x, y, z):
    if z == 0:
        return True
    if x + y >= z and z % cal(x, y) == 0:
        return True
    return False

def cal(x, y):
    if y == 0:
        return x
    else:
        return cal(y, x % y)


x = 3
y = 5
z = 4
print canMeasureWater(x, y,z)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

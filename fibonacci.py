#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-27 18:57:19
# File Name: fibonacci.py
# Description: 
#########################################################################
def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(0, n-1):
        n1, n2 = n2, n1+n2
    return n1

print fibonacci(10)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

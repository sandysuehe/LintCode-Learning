#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 16:48:48
# File Name: Vector2D.py
# Description: 
#########################################################################
class Vector2D(object):
    def __init__(self, vec2d):
        self.result = []
        for e in vec2d:
            self.result.extend(e)
        self.length = len(self.result)
        self.index = 0

    def next(self):
        elem = self.result[self.index]
        self.index += 1
        return elem

    def hasNext(self):
        return True if self.index < self.length else False

vec2d = [
  [1,2],
  [3],
  [4,5,6]
]
i = Vector2D(vec2d)
v = []
while i.hasNext(): v.append(i.next())
print v
# vim: set noexpandtab ts=4 sts=4 sw=4 :

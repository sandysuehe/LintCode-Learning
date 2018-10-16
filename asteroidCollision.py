#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 19:18:59
# File Name: asteroidCollision.py
# Description: 
#########################################################################
def asteroidCollision(asteroids):
    ans = asteroids
    while True:
        if len(ans) <= 1:
            return ans 

        temp = [ans[0]]

        for i in range(1, len(ans)):
            if len(temp) == 0 or ans[i] * temp[-1] > 0:
                temp.append(ans[i])
            elif ans[i] > 0 and temp[-1] < 0:
                temp.append(ans[i])
            elif ans[i] + temp[-1] == 0:
                temp.pop()
            elif ans[i] < 0 and ans[i] + temp[-1] < 0:
                temp[-1] = ans[i]
        if len(temp) == len(ans):
            break
        else:
            ans = temp
    return ans

#asteroids = [5, 10, -5]
asteroids = [10, 2, -5]
asteroids = [3,-69,-65,67,-76,34,10,96,55,77,85,56,99,-1,6,-37,-7,-70,75,-60,4,-73,35,-32,3,-7,72,83,-82,70,68,63,33,-68,-100,61,-96,27,89,81,-11,-63,69,49,-34,23,87,23,26,-67,67,-100,-84,-89,-76,-42,-86,-96,86,7,25,9,-17,7,-15,-35,-65,-82,-32,90,-27,39,30,-42,-3,-71,-46,24,20,-84,8,51,-84,24,53,66,87,-64,27,-5,-68,86,-49,-53,68,21,-88,58,21,-18]
print asteroidCollision(asteroids)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

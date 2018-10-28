#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 18:58:07
# File Name: predictPartyVictory.py
# Description: Dota2 Senate 刀塔二参议院 
# LintCode: https://www.lintcode.com/problem/dota2-senate/
#########################################################################
def predictPartyVictory(senate):
    n = len(senate)
    from Queue import Queue
    R_queue = Queue()
    D_queue = Queue()
    for i in range(0, n):
        if senate[i] == "R":
            R_queue.put(i)
        else:
            D_queue.put(i)

    while not R_queue.empty() and not D_queue.empty():
        r = R_queue.get()
        d = D_queue.get()
        if r < d:
            R_queue.put(r+n)
        else:
            D_queue.put(d+n)
    return "Radiant" if R_queue.qsize() > D_queue.qsize() else "Dire"

senate = "RD"
print predictPartyVictory(senate)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

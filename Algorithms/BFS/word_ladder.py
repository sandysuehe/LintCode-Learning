#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 16:27:29
# File Name: word_ladder.py
# Description: Word Ladder 词语阶梯 
# LintCode: https://www.lintcode.com/problem/word_ladder/
#########################################################################
def ladderLength(start, end, dict):
    ans = 0
    word_set = set(dict)
    word_set.add(end)
    
    visited = set()
    visited.add(start)
    
    import Queue
    queue = Queue.Queue()
    queue.put(start)
    
    while not queue.empty():
        ans += 1
        for _ in range(queue.qsize()):
            word = queue.get()
            if word == end:
                return ans
    
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if word[i] == char:
                        continue
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        queue.put(new_word)
                        visited.add(new_word)
    return ans

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
print ladderLength(start, end, dict)


#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-06 16:54:28
# File Name: high-five.py
# Description: High Five 
# LintCode: https://www.lintcode.com/problem/high-five/
#########################################################################
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Solution:
    def highFive(self, results):
        import heapq
        heap = []

        for result in results:
            heapq.heappush(heap, (result.id, -result.score))

        hash_map = {}
        sums = 0
        count = 0

        while heap:
            rid, score = heapq.heappop(heap)
            print "rid: {0}, score: {1}, hash_map: {2}".format(rid, score, hash_map)
            if rid not in hash_map:
                count += 1
                sums += -score
            if count == 5:
                hash_map[rid] = float(sums)/float(count)
                sums = 0
                count = 0
        return hash_map


results = [Record(1,91),Record(1,92), Record(2,93),Record(2,99),Record(2,98),Record(2,97),Record(1,60),Record(1,58),Record(2,100),Record(1,61)]
obj = Solution()
print obj.highFive(results)

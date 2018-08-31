#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-09 13:51:31
# File Name: pyramidTransition.py
# Description: 
#########################################################################
class Solution(object):
    def recursive(self, cur, above, hash_set):
        print cur, above
        if len(cur) == 2 and len(above) == 1:
            return True
        if len(above) == len(cur) - 1:
            return self.recursive(above, "", hash_set)
        pos = len(above)
        base = tuple(list(cur[pos: pos+2]))
        if base in hash_set:
            above_list = hash_set[base]
            for above_item in above_list:
                if self.recursive(cur, above+above_item, hash_set):
                    return True
        return False
    
    
    def pyramidTransition(self, bottom, allowed):
        hash_set = {}
        for item in allowed:
            if (item[0], item[1]) not in hash_set:
                hash_set[item[0], item[1]] = [item[2]]
            else:
                hash_set[item[0], item[1]].append(item[2])
        print hash_set
        return self.recursive(bottom, "", hash_set)

# bottom = "XYZ"
# allowed = ["XYD", "YZE", "DEA", "FFF"]
# bottom = "ABC"
# allowed = ["ABD","BCE","DEF","FFF"]
bottom = "AABA"
allowed = ["AAA","AAB","ABA","ABB","BAC"]
obj = Solution()
print obj.pyramidTransition(bottom, allowed)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 14:05:08
# File Name: lfu_cache.py
# Description: Design an LFU cache 
#########################################################################
# 思路:
# 实现最近不常用页面置换算法LFU (Least Frequently Used), LFU是先淘汰一定时间内被访问次数最少的页面。
# 由于需要删除最少次数的数字，那么要统计每一个key出现的次数，用一个哈希表m来记录当前数据{key, value}和其出现次数之间的映射 
# 需要把相同频率的key都放到一个list中，那么需要另一个哈希表freq来建立频率和一个里面所有key都是当前频率的list之间的映射。 
# 为了快速的定位freq中key的位置，我们再用一个哈希表iter来建立key和freq中key的位置之间的映射。
# 最后当然我们还需要两个变量cap和minFreq，分别来保存cache的大小，和当前最小的频率。
#########################################################################
class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.hash_map = {}
        self.freq_map = {}
        self.iter_map = {}

    def get(self, key):
        if key not in self.hash_map:
            return -1

        self.freq_map[self.hash_map[key][1]].remove(key)

        self.hash_map[key][1] += 1
        self.freq_map[self.hash_map[key][1]].append(key)
        self.iter_map[key] = self.freq_map[self.hash_map[key][1]]

        if len(self.freq_map[self.min_freq]) == 0:
            self.min_freq += 1

        return self.hash_map[key][0]

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.hash_map:
            self.hash_map[key][0] = value
            return

        if len(self.hash_map) >= self.capacity:
            del self.hash_map[self.freq_map[self.min_freq]]
            del self.iter_map[self.freq_map[self.min_freq]]
            self.freq_map[self.min_freq].pop(0)

        self.hash_map[key] = (value, 1)

        if 1 not in self.freq_map: 
            self.freq_map[1] = [key]
        else:
            self.freq_map[1].append(key)

        self.iter_map[key] = self.freq_map[1][-1]

        self.min_freq = 1



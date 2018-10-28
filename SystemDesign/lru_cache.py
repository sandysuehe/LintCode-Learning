#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 14:05:08
# File Name: lru_cache.py
# Description: Design an LRU cache 
#########################################################################
# 思路:
# 实现一个LRU缓存器，LRU是Least Recently Used的简写，就是最近最少使用的意思。
# 那么这个缓存器主要有两个成员函数，get和put，
# get函数是通过输入key来获得value，如果成功获得后，这对(key, value)升至缓存器中最常用的位置（顶部），如果key不存在，则返回-1。
# put函数是插入一对新的(key, value)，如果原缓存器中有该key，则需要先删除掉原有的，将新的插入到缓存器的顶部。如果不存在，则直接插入到顶部。若加入新的值后缓存器超过了容量，则需要删掉一个最不常用的值，也就是底部的值。
#########################################################################
# 定义三个私有变量，cap, l和m，
# cap是缓存器的容量大小，
# l是保存缓存器内容的列表，
# m是哈希表，保存关键值key和缓存器各项的迭代器之间映射，方便我们以O(1)的时间内找到目标项。
# get的实现: 在m中查找给定的key，如果存在则将此项移到顶部，并返回value，若不存在返回-1。
# put的实现：在m中查找给定的key，如果存在就删掉原有项，并在顶部插入新来项，然后判断是否溢出，若溢出则删掉底部项(最不常用项)
########################################################################
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.lists = []

    def get(self, key):
        if key not in self.hash_map:
            return -1
        key, value = self.hash_map[key]
        self.lists.remove((key, value))
        self.lists.insert(0, (key, value))
        return value

    def put(self, key, value):
        if key in self.hash_map:
            self.lists.remove((key, self.hash_map[key]))
        self.lists.insert(0, (key, value))
        self.hash_map[key] = (key, value)

        if len(self.hash_map) > self.capacity:
            remove_key, remove_value = self.lists[-1]
            self.lists.pop()
            del self.hash_map[remove_key]

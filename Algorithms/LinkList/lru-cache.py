#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 18:46:47
# File Name: lru-cache.py
# Description: LRU缓存策略 
# LintCode: https://www.lintcode.com/problem/lru-cache/
#########################################################################
# 思路: 这道题让我们实现一个LRU缓存器，LRU是Least Recently Used的简写，就是最近最少使用的意思。
# 那么这个缓存器主要有两个成员函数，get和put。
# get函数: 是通过输入key来获得value，如果成功获得后，这对(key, value)升至缓存器中最常用的位置（顶部），如果key不存在，则返回-1。
# get函数的实现：在m中查找给定的key，如果存在则将此项移到顶部，并返回value，若不存在返回-1。
# put函数: 是插入一对新的(key, value)，如果原缓存器中有该key，则需要先删除掉原有的，将新的插入到缓存器的顶部。如果不存在，则直接插入到顶部。若加入新的值后缓存器超过了容量，则需要删掉一个最不常用的值，也就是底部的值。
# put函数的实现: 在m中查找给定的key，如果存在就删掉原有项，并在顶部插入新来项，然后判断是否溢出，若溢出则删掉底部项(最不常用项)
# 具体实现时我们需要三个私有变量，cap, l和m。
# cap是缓存器的容量大小
# l是保存缓存器内容的列表
# m是哈希表，保存关键值key和缓存器各项的迭代器之间映射，方便我们以O(1)的时间内找到目标项。
#########################################################################
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.hash_map = {}
        self.list = []

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hash_map:
            return -1
        self.list.remove((key, self.hash_map[key])) 
        self.list.append((key, self.hash_map[key])) 
        return self.hash_map[key]

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.hash_map:
            self.list.remove((key, value)) 
        self.list.append((key, self.hash_map[key]))
        self.hash_map[key] = value
        if len(self.hash_map) > self.capacity:
            remove_key = self.list[0][0]
            self.list.pop(0) 
            self.hash_map.pop(remove_key)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

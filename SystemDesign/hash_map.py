#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 14:05:08
# File Name: hash_map.py
# Description: Design a hash map 
#########################################################################
class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value 

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)

        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))
            

    def get(self, key):
        hash_index = self._hash_function(key)

        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        return KeyError("Key not found")

    def remove(self, key):
        hash_index = self._hash_function(key)

        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        return KeyError("Key not found")

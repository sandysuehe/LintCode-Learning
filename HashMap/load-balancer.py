#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: load-balancer.py
# Description: 负载均衡器 Load Balancer 
# LintCode: https://www.lintcode.com/problem/load-balancer/
#########################################################################
# 思路:
# 要在o(1)的时间内插入删除，只能hash。那hash可以getRandom吗?
# 什么数据结构比较好getRandom? 数组
# 考虑hash与数组结合起来用，hash插入一个，数组也插入一个。
# 数组删除元素怎么办? – 与最后插入的一个元素交换
# 怎么o(1)时间在数组中找到要删除元素(要交换)的位置? – 用hash将元素的位置记下来
#########################################################################
# 算法:
# 插入:
# – 数组末尾加入这个元素
# – Hash这个元素存下数组中的下标
# 删除:
# – 通过hash找到这个元素在数组中的位置
# – 数数组中这个元素和数组的末尾元素交换，交换后删除
# – Hash中删除这个元素，更新数组原末尾元素现在在数组中的位置
# Pick:
# – 数组中random一个返回
#########################################################################
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.id_index_map = {}
        self.server_ids = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.id_index_map:
            return
        self.server_ids.append(server_id)
        self.id_index_map[server_id] = len(self.server_ids) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.id_index_map:
            return

        index = self.id_index_map[server_id]
        del self.id_index_map[server_id]

        last_server_id = self.server_ids[-1]
        self.id_index_map[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        import random
        index = random.randint(0, len(server_ids)-1)
        return self.server_ids[index]

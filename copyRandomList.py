#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: copyRandomList.py
# Description: 
#########################################################################
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        cur = head
        while cur:
            # 在原链表中的每个节点后面，拷贝出一个新的节点
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next

        cur = head
        while cur:
            # 依次给新的节点的随机指针赋值，cur.next.random = cur.random.next
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        res = head.next
        while cur:
            temp = cur.next
            cur.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            cur = cur.next
        return res
# vim: set noexpandtab ts=4 sts=4 sw=4 :

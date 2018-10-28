#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-06 16:54:28
# File Name: mergeKLists.py
# Description: Merge k Sorted Lists 合并k个有序链表 
# LintCode: https://www.lintcode.com/problem/merge-k-sorted-lists/
#########################################################################
import heapq
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next


if __name__=='__main__':
    lists = []
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(1)
    node4 = ListNode(None)
    node1.next = node2
    lists.append(node1)
    lists.append(node3)
    lists.append(node4)
    obj = Solution()
    obj.mergeKLists(lists)
# vim: set noexpandtab ts=4 sts=4 sw=4 :

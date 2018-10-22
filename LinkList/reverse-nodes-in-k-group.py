#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 18:12:41
# File Name: reverse-nodes-in-k-group.py
# Description: K组翻转链表 
# LintCode: https://www.lintcode.com/problem/reverse-nodes-in-k-group/
#########################################################################
# 思路:
# 以每k个为一组来翻转链表，实际上是把原链表分成若干小段，然后分别对其进行翻转，那么肯定总共需要两个函数，一个是用来分段的，一个是用来翻转的。
# 对于给定链表1->2->3->4->5，一般在处理链表问题时，我们大多时候都会在开头再加一个dummy node，因为翻转链表时头结点可能会变化，为了记录当前最新的头结点的位置而引入的dummy node，那么我们加入dummy node后的链表变为-1->1->2->3->4->5。
# 如果k为3的话，我们的目标是将1,2,3翻转一下，那么我们需要一些指针，pre和next分别指向要翻转的链表的前后的位置，然后翻转后pre的位置更新到新的位置, 以此类推，只要next走过k个节点，就可以调用翻转函数来进行局部翻转了。
#########################################################################
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # write your code here
        if not head or k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        i = 0
        while cur:
            i += 1
            if i % k == 0:
                pre = self.reverseOneGroup(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next    # 找到k倍的节点，然后进行翻转
        return dummy.next

    def reverseOneGroup(pre, post):
        last = pre.next
        cur = last.next
        while cur != post:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last

# vim: set noexpandtab ts=4 sts=4 sw=4 :

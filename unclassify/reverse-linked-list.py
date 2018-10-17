class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head

        p = None
        while head:
            temp = head.next
            head.next = p
            p = head
            head = temp

        return p 

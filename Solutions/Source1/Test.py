# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None

        while head not none:
            next = head.next
            head.next = newHead
            newHead = newHead
            head = next

        return newHead

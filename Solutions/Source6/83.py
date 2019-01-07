# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currNode = head

        while currNode != None and currNode.next != None:
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next

        return head
asds

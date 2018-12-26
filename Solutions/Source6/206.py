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
        stack = [] # store nodes
        dummyNode = ListNode(-1)
        currentNode = head

        while currentNode != None: # adding nodes to stack while we can
            stack.append(currentNode)
            currentNode = currentNode.next

        if len(stack) == 0:
            return None

        dummyNode = stack.pop() # creating new head
        head = dummyNode

        while len(stack) != 0: # putting together new linked list in reverse order
            dummyNode.next = stack.pop()
            dummyNode = dummyNode.next

        dummyNode.next = None

        return head

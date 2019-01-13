# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # dictionary to store nodes
        nodesVisited = {}

        # if there is a head, travese until the end of the linked list
        while head != None:

            if head in nodesVisited: # we have seen value before and we have a cycle
                return True
            else:
                nodesVisited[head] = 1 # add to dictionary

            head = head.next # move to next node

        # if we never saw a cycle
        return False
asd

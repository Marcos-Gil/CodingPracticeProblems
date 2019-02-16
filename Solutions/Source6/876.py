# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        origHead = head #  storing original head while we iterate, copies LinkedList which is not as efficient
        listLen = 0
        midVal = 0

        if head == None:
            return 0

        while head.next != None: # while we can iterate, iterate and track length
            head = head.next
            listLen += 1

        if listLen % 2 == 1: # If length is not even then do floor division and add 1 to get second node
            midVal = listLen // 2
            midVal+= 1
        else:
            midVal = listLen // 2

        for i in range(0, midVal): # iterate to get middle node once we know which one it is
            origHead = origHead.next

        return origHead

# We can do this in same time complexity but in O(1) space complexity by using a slow and fast pointer,
# where the fast pointer goes through two elements at a time while the slow pointer goes through one
# element at a time, when the fast pointer reaches the end of the list the slow pointer will be in the
# middle and we can return the node it is pointing to as the answer
#
# slow = fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
# return slow
asd

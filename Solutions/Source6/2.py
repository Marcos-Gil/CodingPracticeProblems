# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = [] # store values from each linked list
        num2 = []

        # iterate through both linked lists
        while l1 != None:
            num1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            num2.append(l2.val)
            l2 = l2.next

        # reverse integers since the actual value is stored backwards
        num1fwd = num1[::-1]
        num2fwd = num2[::-1]

        # helper function to take a list of integers and return the one value they represent ([1,2,3] -> 123)
        def listToNumber(numList):
            s = ''.join(map(str, numList))
            return int(s)

        # add both the numbers represented in the lists
        answer = listToNumber(num1fwd) + listToNumber(num2fwd)

        # turn answer back into a list (123 -> [1,2,3])
        returnValue = [int(num) for num in str(answer)]

        # preparing to return linked list
        dummy = ListNode(0)
        pointer = dummy

        # iterate through return value backwards and adding to linked list since they are stored that way
        for i in range(len(returnValue) - 1, -1, -1):
            pointer.next = ListNode(returnValue[i])
            pointer = pointer.next

        pointer = dummy.next # setting head to first value we added then returning it

        return pointer

# Iterate both at same time until you reach the end of both
# while True:
#     if l1 and l2:
#     elif l1 and not l2:
#     elif not l1 and l2:
#     else:
#         break

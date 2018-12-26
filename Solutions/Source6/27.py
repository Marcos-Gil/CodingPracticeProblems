class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indexToRemove = []
        length = len(nums)

        for i in range(0, len(nums)): # find indexes of value we need to delete
            if nums[i] == val:
                indexToRemove.append(i)

        for j in range(len(indexToRemove) - 1, -1, -1): # iterate backwards and delete to preserve index numbers
            del nums[indexToRemove[j]]

        return length - len(indexToRemove) # return original length - amount of numbers we removed

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        currentLen = len(nums) # will remove 1 from this for every duplicate
        indexToDelete = [] # storing indexes of the values we need to delete

        for i in range(0, len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
                indexToDelete.append(i)
                currentLen -= 1
            else:
                dict[nums[i]] = 1

        for j in range(len(indexToDelete) - 1, -1, -1): # delete from back to front so indexes remain accurate
            del nums[indexToDelete[j]]

        return currentLen

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: # empty list
            return 0

        if nums[len(nums)-1] < target: # greater than max element
            return len(nums)

        for i in range(0, len(nums)): # iterate through list, return i if we find target or element larger
            if nums[i] == target or nums[i] > target:
                return i

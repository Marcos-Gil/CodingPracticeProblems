class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # improved solution
        lastZeroIndex = 0
        for i in range(0, len(nums)): # iterate through list
            if nums[i] != 0: # if number is not a zero, we swap current element with the last zero we saw
                nums[lastZeroIndex], nums[i] = nums[i], nums[lastZeroIndex]
                lastZeroIndex += 1
                
# First solution, ended up being extremely inefficient
#
# zeroCount = 0
#
# for x in range(0, len(nums)): # count zeroes
#     if nums[x] == 0:
#         zeroCount += 1
#
# i = 0
#
# while i < len(nums) - 1: # loop until we reach end of list
#     if nums[i] == 0: # if we find a zero
#         for j in range(i, len(nums)-1): # shift all values from 0 to end of list down 1 index
#             nums[j] = nums[j + 1]
#         if nums[i + 1] == 0:
#             i += 1
#         else:
#             i -= 1
#     else:
#         i += 1
#
#
# for j in range(0, zeroCount): # replace values at end with 0
#     nums[len(nums) - 1 - j] = 0

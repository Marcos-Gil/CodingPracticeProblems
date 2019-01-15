class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numList = []

        if k == 0: # if no rotation nothing to do
            return

        for i in range(0, len(nums)): # copy array
            numList.append(nums[i])

        for i in range(0, len(nums)):
            if (i + k) >= (len(nums)): # if new current value moving past last valid index
                index = (i + k) % (len(nums)) # modulate with length to get where index where value will go
                nums[index] = numList[i]
            else:
                nums[i + k] = numList[i] # element at i goes to i + k


# In place switching, O(1) space
# class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         count = 0
#         start = 0 # start at 0, every index from here + k will eventually reach back this element
#
#         while count < len(nums):
#
#             current = start
#             prev = nums[start]
#             while True:
#                 nextt = (current + k) % len(nums)
#                 temp = nums[nextt]
#                 nums[nextt] = prev
#                 prev = temp
#                 current = nextt;
#                 count += 1
#
#                 if (start == current): # if we reached back to the start
#                     break
#
#             start += 1 # increment start to next index, so we can handle all index spaced k apart from here
asd

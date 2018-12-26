class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        d = deque()

        if len(nums) < 2 and len(nums) != 0:
            return [max(nums)]

        maxPerWindow = []

        for i in range(0, len(nums)):
            if i < k: # setting up window
                d.append(nums[i])

                if i == len(nums) - 1: # if we have 1 window equal to size of key
                    maxPerWindow.append(max(d))

                continue

            maxPerWindow.append(max(d)) # add max from current window to return object
            d.popleft() # remove left most element of window and add new one to the right
            d.append(nums[i])

            if i == len(nums) - 1: # if we are on last iteration, we get value of the last window position that we just setup above
                maxPerWindow.append(max(d))

        return maxPerWindow

# Without a deck
# if len(nums) < 2 and len(nums) != 0:
#     return [max(nums)]
#
# maxPerWindow = []
# window = []
# for i in range(0, len(nums)):
#     if i < k: # setting up window
#         window.append(nums[i])
#
#         if i == len(nums) - 1: # if we have 1 window equal to size of key
#             maxPerWindow.append(max(window))
#
#         continue
#
#     maxPerWindow.append(max(window)) # add max from current window to return object
#     window.remove(window[0]) # remove left most element of window and add new one to the right
#     window.append(nums[i])
#
#     if i == len(nums) - 1: # if we are on last iteration, we get value of the last window position that we just setup above
#         maxPerWindow.append(max(window))
#
# return maxPerWindow

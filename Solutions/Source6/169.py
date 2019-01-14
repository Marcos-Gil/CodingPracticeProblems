class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {} # dictionary that we will use to store values and number of occurences

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        majorityAmount = int(len(nums)/2) # majority element is floor division of length of list divided by 1

        if max(dict.values()) >= majorityAmount: # if largest value in dictionary is equal to or higher than majority amount
            return next(key for key, value in dict.items() if value >= max(dict.values())) # return the accompanying key for the max value

# This could also be solved using Boyer-Moore Voting Algortihm:
# class Solution:
#     def majorityElement(self, nums):
#         count = 0
#         candidate = None
#
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#
#         return candidate

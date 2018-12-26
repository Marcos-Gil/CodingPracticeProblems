class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Similar to previous answer but checking from back of list at same time and moving inwards from both ends
        answers = {}

        left = 0 # index of left
        right = len(nums) - 1 # index of right
        while right >= left: # while they haven't crossed each other
            complement1 = target - nums[left] # get complement of each one
            complement2 = target - nums[right]

            if complement1 in answers: # if complement of left in dictionary, we have answer
                return [answers[complement1], left]

            answers[nums[left]] = left # if not we store it in dictionary then check compliment of right and do the same

            if complement2 in answers:
                return [answers[complement2], right]

            answers[nums[right]] = right

            right -= 1 # bring in both pointers by 1 index
            left += 1


# First answer
#
# answers = {}
#
# for i in range(0, len(nums)):
#     complement = target - nums[i]
#     if complement in answers:
#         return [answers[complement], i]
#     answers[nums[i]] = i

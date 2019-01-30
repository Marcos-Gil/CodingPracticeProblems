class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # init values and dictionary
        biggest = -9999999999999
        secondBiggest = -9999999999999
        thirdBiggest = -9999999999999
        dict = {}

        for num in nums: # iterate through numbers
            if num in dict: # to know if we don't have 3 unique numbers
                dict[num] += 1
            else:
                dict[num] = 1
            if num > biggest: # if we find new biggest, we shift current values down one
                thirdBiggest = secondBiggest
                secondBiggest = biggest
                biggest = num
            elif num > secondBiggest: # if we find second biggest, we shift values down one unless this num value is same as current biggest
                if num == biggest:
                    continue
                thirdBiggest = secondBiggest
                secondBiggest = num
            elif num > thirdBiggest: # if we find third biggest, we set it thirdBiggest unless this num value is same as second biggest
                if num == secondBiggest:
                    continue
                thirdBiggest = num

        if len(dict) < 3: # if we did't have 3 unique numbers
            return biggest

        return thirdBiggest
# Similar solution, using none and including that in comparions, no dictionary required
#
# first, second, third = None, None, None
# for n in nums:
#     if n in [first, second, third]:
#         continue
#     if first is None or n > first:
#         first, second, third = n, first, second
#     elif second is None or n > second:
#         second, third = n, second
#     elif third is None or n > third:
#         third = n
# return first if third is None else third

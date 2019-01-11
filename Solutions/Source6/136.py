class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = {} # dictionary

        for num in nums: # iterate through numbers
            if num in pairs: # if number in dictonary, we know there is another element to pair with and we can take that element out since we found pair
                pairs.pop(num)
            else:
                pairs[num] = num # we add unpaired element to dictionary

        for key in pairs: # after going through all the numbers we should only have 1 element left
            return key
asd

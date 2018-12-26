class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # add together and sort list of integers
        allNum = nums1 + nums2
        allNum.sort()

        if len(allNum) % 2 == 0: # if list is even in length, get add both middle indices and divide result by 2
            return (allNum[int((len(allNum)/2) - 1)] + allNum[int((len(allNum))/2)]) / 2.0
        else: # return middle index
            return allNum[int(len(allNum)/2)]

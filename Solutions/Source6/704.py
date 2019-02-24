class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = None
        left = 0
        right = len(nums) - 1
        found = False

        while (right >= left):

            mid = left + (right - left) // 2

            if nums[mid] == target:
                found = True
                index = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if found:
            return index
        else:
            return -1
asd

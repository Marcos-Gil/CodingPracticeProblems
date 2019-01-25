# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        right = n
        left = 1

        # BST to find lowest bad version
        while right >= left:
            mid = left + (right - left) // 2
            if (isBadVersion(mid)):
                right = mid - 1
            else:
                left = mid + 1

        return left

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Using splice to reverse
        return str(x) == str(x)[::-1]
a

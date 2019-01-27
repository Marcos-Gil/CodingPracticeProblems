class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        newString = ""

        for i in range(len(s)-1, -1, -1):
            newString += s[i]

        return newString

# Could also just return s[::-1]

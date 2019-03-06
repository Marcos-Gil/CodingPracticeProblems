class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = s.split(" ")

        for i in range(0, len(string)):
            string[i] = string[i][::-1]

        string = " ".join(string)

        return string

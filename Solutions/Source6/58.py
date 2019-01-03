class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: # if s is empty
            return 0

        s = s.split(" ") # splitting on spaces

        index = len(s) - 1 # setting last index

        while s[index] == "": # work from end of string in, if there is an empty spot we lower index
            index -= 1
            if index == 0: # start of string reached
                break

        return len(s[index])
assa

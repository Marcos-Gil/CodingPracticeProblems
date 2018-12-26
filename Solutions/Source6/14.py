class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if empty list is provided
        if len(strs) == 0:
            return ""

        # common prefix we will return
        common = ""

        # iterate through all letters in the first word
        for i in range(0, len(strs[0])):
            flag = 0
            currentLetter = strs[0][i]
            for j in range(1, len(strs)): # iterate through rest of words checking i-th letter
                if (i >= len(strs[j]) or strs[j][i] != currentLetter): # if word is shorter than first worst or letters don't match
                    flag = 1
                    break
            if flag == 0: # iterated through every word without an issue
                common += currentLetter
            else:
                break

        return common

as

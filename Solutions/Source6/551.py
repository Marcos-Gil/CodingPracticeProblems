class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA = 0
        streakOfL = 0

        for i in range(0, len(s)): # iterate through record
            if s[i] == 'L': # if we find a L, we continue loop and check the streak if we need to return False, if not streak will be reset
                streakOfL += 1
                if streakOfL > 2:
                    return False
                continue

            elif s[i] == 'A': # if we find more then one A at any point we return false
                countA += 1
                if countA > 1:
                    return False
            streakOfL = 0

        return True
asd

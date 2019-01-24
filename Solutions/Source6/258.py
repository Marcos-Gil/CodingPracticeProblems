class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tempStr = str(num) # so we can iterate through digits
        tempInt = 0 # integer value we can add to

        if len(tempStr) < 2:
            return num

        while len(tempStr) != 1: # while result is not 1 digit
            for number in tempStr: # add digits in current number together
                tempInt += int(number)

            tempStr = str(tempInt) # set new string value of number
            tempInt = 0 # reset for next iteration

        return int(tempStr)

asd
# O(1) time and space complexity solution based on: https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
#
# return 1 + (num - 1) % 9;

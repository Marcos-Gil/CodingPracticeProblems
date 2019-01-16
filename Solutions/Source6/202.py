class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        happy = False
        num = n

        while not happy:
            if num in [2,3,4]:
                return False

            numString = str(num)
            numString = list(numString)

            for num in numString:
                result += int(num) ** 2

            if result == 1:
                return True
            else:
                num = result
                result = 0
                continue

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        final = [] # list we will return with answer
        list = [str(x) for x in digits] # turn integers into string values
        list = ''.join(list) # joining the string values together
        list = int(list) # turning value into an integer
        list += 1 # adding 1 to value
        list = str(list) # turning back into list so we can iterate through values

        for i in range(0, len(list)): # iterate through string values, and append integer version into final list and return
            final.append(int(list[i]))
        return final

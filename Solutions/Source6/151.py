class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        finalString = []
        returnString = []

        for word in s.split(" "): # removing all spaces, including multiple spaces such as 'hello       world'
            if word != '':
                finalString.append(word)

        for i in range(len(finalString) - 1, -1, -1): # iterate backwords from list of just words and add to new string
            returnString.append(finalString[i])

        returnString = " ".join(returnString) # re add spaces between words at return

        return returnString
asd

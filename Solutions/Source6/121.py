class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: # if list is empty
            return 0

        minimumPrice = prices[0] # set initial values
        highestProfit = 0

        for i in range(0, len(prices)): # iterate through list
            if prices[i] < minimumPrice: # if we reached a new minimum value
                minimumPrice = prices[i]
            elif prices[i] - minimumPrice > highestProfit: # if we don't reach a new minimum and current value - current minimum is greater than highest profit recorded
                highestProfit = prices[i] - minimumPrice
                print(highestProfit)

        return highestProfit
asd

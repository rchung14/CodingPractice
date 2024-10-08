class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1

        maxProfit = 0
        for i in range(len(prices)-1): 
            currProfit = prices[right] - prices[left]

            if prices[left] < prices[right]: 
                maxProfit = max(currProfit,maxProfit)
            
            else: 
                left = right 

            right += 1

        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        R:
        given prices
        prices[i] stock price on ith day

        buy on one day, sell on another
        return max profit, else 0

        E:
        if len(prices) == 1:
            return 0

        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4

        ??
        while prices[l] > prices[r]:
            inc r pointer

        A:

        7   6   4   3   1
        l   r

        7   1   5   3   6   4
        l   r
            l   r
                
        [7,2,5,1,6,4]


        """

        max_profit = 0
        n = len(prices)
        if n == 1:
            return 0

        l,r = 0,1
        while r < n:
            if prices[l] > prices[r]:
                l=r
                r=l+1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r+=1
            
        return max_profit
        
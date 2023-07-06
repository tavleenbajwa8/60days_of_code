##Question 
"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

##Solution 1 (Brute Force ##High Time Complexity)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_difference = 0
        buy = 0
        sell = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                difference = prices[j] - prices[i]
                if difference > max_difference:
                    max_difference = difference
        return max_difference
    
    ##Solution-2 (Using 2 pointers approach)
    def maxProfit2(self, prices: List[int]) -> int:
        left = 0 #buy (Points the starting index)
        right = 1 #sell (Points to corresponding pointer after left)
        max_diff = 0 #Initially keeping max_diff as 0
        while right < len(prices):   #We dont want the right point to exceed the len of prices,ensuring that we don't exceed the bounds of the list., therefore keeping in while loop
            diff = prices[right] - prices[left]  #Will calculate the difference between sell - buy
            if prices[left] < prices[right]:     ##If the sell price is more than buy which is diff then only it will  
                max_diff = max(diff, max_diff)  ##Max of current max_diff and diff will update the max_diff value
            else:
                """
                If the buy price is not less than the sell price, it means the current buy point is not optimal, and we 
                need to update the left index to point to the current right index. This allows us to consider a new 
                potential buy point.
                """
                left = right   ## If not the index of left will be updated to right 
            right = right + 1
        return max_diff
        
        

obj = Solution()
result1 = obj.maxProfit([7,1,5,3,6,4])
result2 = obj.maxProfit2([7,1,5,3,6,4])
print(result1, result2)

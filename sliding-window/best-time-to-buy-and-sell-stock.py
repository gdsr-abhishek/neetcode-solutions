from typing import List

# INSIGHT: Find the max profit at that specific day and compare it with current profit get the max and update the min value as we go
# WHY IT WORKS: we are trying to find the max profit by updating the min that we saw in the past to the realtive max and getting the max profit.
# COMPLEXITY: time O(N) because single loop / space O(1) because only two variables
# BREAKS WHEN: empty array — prices[0] throws IndexError
#              all prices decreasing — returns 0 (correct, no transaction = 0 profit)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price =prices[0]
        max_profit = 0
        i=1
        while i < len(prices):
            max_profit = max(max_profit , prices[i] - min_price)
            min_price = min(prices[i],min_price)
            i+=1
        return max_profit

        
# INSIGHT: binary search works on sorted arrays by halving the search space each step
# WHY IT WORKS: sorted order guarantees the target can only exist in one half — 
#               eliminating the other half is always safe
# COMPLEXITY: time O(log n) because search space halves each iteration — 
#             1024 elements needs only 10 steps / space O(1) no extra structure needed
# BREAKS WHEN: unsorted array, duplicate handling needed, or overflow on (low+high)//2 
#              at very large indices — fix with low + (high-low)//2
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low =  0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) //2
            if nums[mid] ==  target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
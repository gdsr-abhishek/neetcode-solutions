from typing import List
# INSIGHT: find the left max and right max at that particular height to calculate the water trapped
# WHY IT WORKS: we are trying to find how much water we can store w.r.t each height and doing a summation
# COMPLEXITY: time O(n) since we are iterating all the heights / space O(1) since we are using only 5 variables to persist  
# BREAKS WHEN: empty array — left=0, right=-1, while condition false immediately, returns 0 correctly
#              all same height — water = 0 correctly, no valleys
#              monotonically increasing or decreasing — no valleys, returns 0 correctly

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max =0
        right_max =0
        water = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left+=1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right-=1
        return water
        
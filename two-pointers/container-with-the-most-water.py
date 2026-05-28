from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # INSIGHT: two pointers from both ends find the area at all the instance and get the maximum area returned
        # WHY IT WORKS: height[i] <= height[j] shrink from left to find the better height and shrink from right if height[i]>height[j] until i<j condition holds
        # COMPLEXITY: time O(n) one pass / space O(1) max_area
        # BREAKS WHEN: nothing — single element returns 0 correctly, equal heights handled by <= case
        i=0
        j= len(height)-1
        max_area = 0
        while i<j:
            max_area = max(min(height[i],height[j])*(j-i),max_area)
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return max_area
        
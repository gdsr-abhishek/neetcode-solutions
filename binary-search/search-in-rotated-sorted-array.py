# INSIGHT: find target in rotated sorted array by identifying which half 
#          is normally sorted at each midpoint, then checking if target 
#          falls within that half
# WHY IT WORKS: exactly one half is always sorted at any midpoint — 
#               use range check to decide which half to search, 
#               eliminating half the space each step → O(log n)
# COMPLEXITY: time O(log n) / space O(1)
# BREAKS WHEN: duplicates — nums[low] == nums[mid] makes it impossible 
#              to determine which half is sorted. Fix: low += 1, 
#              but worst case degrades to O(n)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]: 
                    high = mid - 1
                else:                               
                    low = mid + 1
            else:                       
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:                              
                    high = mid - 1

        return -1
        
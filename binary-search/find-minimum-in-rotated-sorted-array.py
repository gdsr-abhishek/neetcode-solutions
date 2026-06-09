# INSIGHT: we are trying to find the disrupted array subspace and find the minimum
# WHY IT WORKS: we are continously trying to find the disrupted subspace within the array since when rotated the first index of the sorted array will move to either mid or end 
# COMPLEXITY: time O(logn) because / space O(1) because we are persisiting low and high only
# BREAKS WHEN: duplicate values — nums[mid] == nums[high] makes it impossible to 
# determine which half is disrupted. Fix: high -= 1, but worst case degrades to O(n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1      # minimum is in right half
            else:
                high = mid         # mid could be the minimum, don't exclude it
        
        return nums[low]           # low == high, converged on minimum
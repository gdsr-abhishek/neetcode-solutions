# INSIGHT: run two separate binary searches — one for left boundary, 
#          one for right boundary of target in sorted array
# WHY IT WORKS: when target found, left search goes left (high=mid) 
#               to find first occurrence, right search goes right (low=mid) 
#               to find last. +1 in right mid prevents infinite loop 
#               when low and high are adjacent.
# COMPLEXITY: time O(log n) — two binary searches / space O(1)
# BREAKS WHEN: empty array — handle with early return [-1,-1]. 
#              Unsorted array — binary search assumption breaks.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_pos = -1
        right_pos = -1
        low = 0 
        high =  len(nums) - 1
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        if low == high and nums[low] ==  target:
            left_pos = low
        low = 0 
        high = len(nums) -1
        while low < high:
            mid = (low + high + 1) //2
            if nums[mid] == target:
                low = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        if low == high and nums[high] ==  target:
            right_pos = high
        return [left_pos, right_pos]
        
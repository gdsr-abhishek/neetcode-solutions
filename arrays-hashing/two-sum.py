# INSIGHT: for each number, check if its complement (target - num) was already seen
# WHY IT WORKS: hash map gives O(1) lookup — transforms O(n²) pair search into one pass
# COMPLEXITY: time O(n) because one pass / space O(n) because map grows with input
# BREAKS WHEN: duplicate numbers with same value but need different indices — 
#storing index as value (not bool) handles this correctly
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in hashmap:
                return [hashmap[residual],i]
            hashmap[nums[i]] = i
        return -1
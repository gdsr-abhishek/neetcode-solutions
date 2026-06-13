# INSIGHT: for each index, answer is product of all elements to its left 
#          multiplied by product of all elements to its right
# WHY IT WORKS: prefix[i] stores product of everything left of i, 
#               suffix[i] stores product of everything right of i.
#               Built in two O(n) passes — no recomputation from scratch
# COMPLEXITY: time O(n) three passes / space O(n) prefix + suffix arrays
# BREAKS WHEN: empty array — index out of bounds on nums[0] and nums[-1].
#              Can be optimised to O(1) space by computing suffix on the fly
#              into the result array directly — worth knowing for follow-up questions
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cummulative_product = nums[0]
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        i=1
        while i < len(nums):
            prefix[i] = cummulative_product
            cummulative_product *=nums[i]
            i +=1
        cummulative_product = nums[-1]
        i= len(nums) - 2
        while i >= 0:
            suffix[i] = cummulative_product
            cummulative_product *= nums[i]
            i -=1
        result = list()
        i = 0
        while i< len(nums):
            result.append(prefix[i] * suffix[i])
            i +=1
        return result 

            
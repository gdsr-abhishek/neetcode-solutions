from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # INSIGHT: two pointers from both ends — sorted array lets you eliminate half on each step
        # WHY IT WORKS: sum too big → shrink from right, sum too small → grow from left, guaranteed to converge
        # COMPLEXITY: time O(n) one pass / space O(1) no extra structure needed
        # BREAKS WHEN: return -1 is wrong return type — problem guarantees solution exists so never hits
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum_now = numbers[i] + numbers[j]
            if sum_now == target:
                return [i+1, j+1]
            elif sum_now < target:
                i += 1
            else:
                j -= 1
        return -1
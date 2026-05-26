# INSIGHT: for each element, find the frequency sort the hashmap using the frequency and get the top k elements
# WHY IT WORKS: sorting by frequency keeps key-value pairs together — 
#               sorting values alone loses the element association
# COMPLEXITY: time O(n log n) because of the sort / space O(n) because map + sorted array both grow with input
# BREAKS WHEN: n is large and k is small — sorting all n items is wasteful. 
#              Heap gives O(n log k) — only tracks k items at a time.

from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topkDict = defaultdict(int)
        for i in nums:
            topkDict[i]+=1
        topkArray = sorted(topkDict.items(),key=lambda item:item[1],reverse=True)[:k]
        result = [item[0] for item in topkArray]
        return result

        
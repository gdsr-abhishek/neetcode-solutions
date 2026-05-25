# INSIGHT: Flag the duplicate and return true using hashmap to persist the count
# WHY IT WORKS: because we are esentially calculating the first duplicate which fits the criteria
# COMPLEXITY: time O(n) worst case which is no duplicates   / space O(n) worst case which has no duplicates which makes us store all the numbers in hashmap 
# BREAKS WHEN:input is empty — but it handles it correctly, returns False naturally. Nothing actually breaks here.
from collections import defaultdict
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in nums:
            str_i =str(i)
            hashmap[str_i] +=1
            if hashmap[str_i] > 1:
                return True
        return False

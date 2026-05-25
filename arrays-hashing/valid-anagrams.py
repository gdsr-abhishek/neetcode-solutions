# INSIGHT:  build a hashmap with the original string and now use this to remove the chars in anagram string
# WHY IT WORKS: we are finding out whether the anagram has all the characters 
# COMPLEXITY: time O(n) because we are doing 3 independant loops / space O(n) because the worst case is that all the items in the string are unique but even in that case it should be always O(26)
# BREAKS WHEN: would break if you only counted one string's chars — missing characters in the longer string wouldn't be caught. Current approach handles this correctly.
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] +=1
        for j in t:
            hashmap[j] -=1
        hash_length = len(hashmap)
        zero_arr = [0 for i in range(hash_length)]
        if list(hashmap.values()) == zero_arr:
            return True
        return False
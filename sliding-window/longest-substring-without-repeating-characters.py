# INSIGHT: finding if duplicate exists and shrink the window and if it doesn't then expand the window find the max and return it
# WHY IT WORKS: because we are using the duplicate condition to dynamically shrink or expand our substring this makes us find the substring .
# COMPLEXITY: time O(n) because we iterate the entire string / space O(1) because hashmap will only have 26 alphabets at maximum
# BREAKS WHEN: it will not break even empty string is handled
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        left = 0
        right = 0
        max_string = 0
        current = 0
        while left <= right and right < len(s):
            if hashMap[s[right]] == 0:
                hashMap[s[right]] +=1
                current +=1
                max_string = max(max_string,current)
                right +=1
            else:
                hashMap[s[left]] -=1
                left +=1
                current = right - left
        return max_string
        
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # INSIGHT: use sorted characters as a derived key — anagrams share the same sorted form
        # WHY IT WORKS: sorting normalizes all anagrams to the same key — groups form naturally
        # COMPLEXITY: time O(n * k log k) where k is max string length / space O(n) for the map
        # BREAKS WHEN: unicode chars outside ASCII — sorting may not group correctly across encodings
        grpdict = defaultdict(list)
        for i in strs:
            grpdict[tuple(sorted(i))].append(i)
        return [value for value in grpdict.values()]
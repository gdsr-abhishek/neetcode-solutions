class Solution:
    def isPalindrome(self, s: str) -> bool:
        # INSIGHT: strip non-alphanumeric chars, compare string to its reverse
        # WHY IT WORKS: reverse of a palindrome is itself — equality check is sufficient
        # COMPLEXITY: time O(n) two passes / space O(n) for the cleaned string
        # BREAKS WHEN: nothing — empty string returns True correctly
        palString = ''
        for i in s:
            if i.isalnum():
                palString += i.lower()
        return palString == palString[::-1]
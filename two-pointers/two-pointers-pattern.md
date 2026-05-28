# Two Pointers Pattern

> **The core idea: use two indices moving toward each other — eliminate half the search space on each step instead of scanning everything.**

---

## The mental model

Two pointers work when the array is sorted or has a structure you can exploit directionally.

```
Brute force:  check every pair → O(n²)
Two pointers: move inward based on comparison → O(n)
```

**The rule:**
> If the array is sorted and you need a pair — start from both ends and converge.

---

## The pattern in code

```python
i = 0
j = len(arr) - 1

while i < j:
    current = arr[i] + arr[j]

    if current == target:
        return [i, j]
    elif current < target:
        i += 1   # need bigger → move left pointer right
    else:
        j -= 1   # need smaller → move right pointer left
```

**Why does this work?**
Because the array is sorted — moving `i` right increases the sum, moving `j` left decreases it. Every step eliminates one element from consideration. Guaranteed to converge in O(n).

---

## Problems solved so far

### Valid Palindrome
**Problem:** given a string, return true if it reads the same forward and backward after removing non-alphanumeric characters

**Key flip:** instead of checking pairs explicitly, ask *"is the cleaned string equal to its reverse?"*

```python
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
```

> **The insight:** cleaning and reversing is simpler than managing two pointers manually here. The two pointer version exists but this is cleaner for this constraint set.

---

### Two Sum II
**Problem:** find two numbers in a sorted array that add to target, return 1-indexed positions

**Key flip:** instead of searching for a complement, ask *"can I eliminate one element each step using sort order?"*

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # INSIGHT: two pointers from both ends — sorted array lets you eliminate one element each step
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
```

> **The insight:** sorted order is the key. Hash map Two Sum works on unsorted arrays — two pointers Two Sum works on sorted arrays and uses O(1) space instead of O(n).
---
### Container With Most Water
**Problem:** find two lines that together with the x-axis forms a container that holds the most water

**Key flip:** instead of checking every pair, ask *"which pointer is limiting the water level — move that one"*

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # INSIGHT: two pointers from both ends, track max area at each step
        # WHY IT WORKS: shorter wall is always the bottleneck — moving it inward is the only chance to find bigger area
        # COMPLEXITY: time O(n) one pass / space O(1) only max_area tracked
        # BREAKS WHEN: nothing — single element returns 0 correctly, equal heights handled by <= case
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(min(height[i], height[j]) * (j - i), max_area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area
```

> **The insight:** width shrinks every step — so your only lever is height. Always move the shorter wall inward. Keeping it gains nothing; replacing it might gain everything.
---

## Two pointers vs hash map — when to use which

| Situation | Use |
|---|---|
| Array is sorted, need a pair | Two pointers |
| Array is unsorted, need a pair | Hash map |
| Need O(1) space | Two pointers |
| Need O(n) time on unsorted input | Hash map |

---

## Variants of the pattern

| Variant | Movement | Example |
|---|---|---|
| **Converging** | both ends toward middle | Two Sum II, Valid Palindrome |
| **Sliding window** | both move same direction | Week 2 — longest substring |
| **Fast/slow** | different speeds | Linked list cycle detection |

---

## Complexity

| | Time | Space |
|---|---|---|
| Converging two pointers | O(n) | O(1) |
| vs Hash map approach | O(n) | O(n) |

---

## Problems to add here

- [x] Valid Palindrome ✅
- [x] Two Sum II ✅
- [ ] 3Sum
- [ ] Container With Most Water
- [ ] Trapping Rain Water
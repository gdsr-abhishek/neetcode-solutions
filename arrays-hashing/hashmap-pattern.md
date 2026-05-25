# Hash Map Pattern

> **The core idea: trade space for time. Store what you've seen so you can look it up in O(1) instead of searching in O(n).**

---

## The mental model

A hash map is a memory. Instead of scanning the array again to find something, you ask: *"have I seen what I need before?"*

```
Brute force:  for every element, scan the rest → O(n²)
Hash map:     for every element, check the map  → O(n)
```

**The rule:**
> Whatever you're searching for — make that the key.

---

## The pattern in code

```python
hashmap = {}

for i, val in enumerate(nums):
    complement = something_derived_from(val)

    if complement in hashmap:
        return [hashmap[complement], i]  # found the pair

    hashmap[val] = i  # store current: value → index
```

**Why value → index (not index → value)?**
Because you're looking up by value. If you stored `index → value`, you'd have to scan every value to find the complement — back to O(n) per lookup.

---

## Problems solved so far

### Two Sum
**Problem:** find two indices where `nums[i] + nums[j] == target`

**Key flip:** instead of finding a pair, ask *"does the complement of this number exist?"*

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # INSIGHT: for each number, check if its complement (target - num) was already seen
        # WHY IT WORKS: hash map gives O(1) lookup — transforms O(n²) pair search into one pass
        # COMPLEXITY: time O(n) because one pass / space O(n) because map grows with input
        # BREAKS WHEN: duplicate numbers — storing index as value (not bool) handles this correctly
        hashmap = {}
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in hashmap:
                return [hashmap[residual], i]
            hashmap[nums[i]] = i
        return -1
```

>**The insight:** `residual = target - nums[i]` flips the question from *"find two numbers"* to *"for this number, does its partner already exist?"*

---
### Valid Anagram
**Problem:** given two strings `s` and `t`, return true if `t` is an anagram of `s`

**Key flip:** instead of comparing characters directly, ask *"do both strings have identical character frequencies?"*

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # INSIGHT: build a frequency map — +1 for every char in s, -1 for every char in t
        # WHY IT WORKS: anagrams have identical char counts — if they cancel to zero, it's an anagram
        # COMPLEXITY: time O(n) because 3 independent passes / space O(k) where k is alphabet size — O(26) for lowercase, effectively O(1)
        # BREAKS WHEN: would break if you only counted one string — missing chars in the longer string wouldn't be caught
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1
        for j in t:
            hashmap[j] -= 1
        if all(v == 0 for v in hashmap.values()):
            return True
        return False
```

>**The insight:** +1 and -1 into the same map. If they're anagrams, every key cancels to zero. One map, two passes, no comparison needed.
---
### Contains Duplicate
**Problem:** return true if any value appears at least twice in the array

**Key flip:** instead of comparing every pair, ask *"have I seen this number before in this pass?"*

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # INSIGHT: flag the duplicate as you build — return True the moment count exceeds 1
        # WHY IT WORKS: persisting the count lets you catch the first repeat in a single pass
        # COMPLEXITY: time O(n) worst case — no duplicates, full pass / space O(n) worst case — all unique, full map built
        # BREAKS WHEN: nothing breaks — empty input returns False correctly
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
            if hashmap[i] > 1:
                return True
        return False
```

>**The insight:** check *as you insert*, not after. You don't need to finish building the map — return the moment you find the answer.
---
## Variants of the pattern

| Variant | What you store | What you look up |
|---|---|---|
| **Complement search** (Two Sum) | value → index | `target - current` |
| **Frequency count** (Valid Anagram) | value → count | whether counts match |
| **Existence check** (Contains Duplicate) | value → True | whether value seen before |
| **Group by key** (Group Anagrams) | key → list of values | sorted word as key |

---

## Complexity

| | Time | Space |
|---|---|---|
| Build the map | O(n) | O(n) |
| Lookup | O(1) average | — |
| Full pass + lookup | O(n) | O(n) |

> **Warning**
> Hash map lookup is O(1) *average* — not worst case. Hash collisions degrade to O(n) in the worst case, but this almost never matters in practice.

---

## When hash map is the right tool

- You need to find a **pair or complement** in an array
- You need to **count frequencies** of elements
- You need to **check for duplicates**
- You need to **group elements** by some derived key
- Brute force is O(n²) and you need O(n)

## When it isn't

- You need sorted order — use a sorted array or heap
- You need range queries — use a prefix sum or segment tree
- Space is constrained to O(1) — use two pointers instead

---

## Problems to add here

- [ ] Two Sum ✅
- [ ] Valid Anagram ✅
- [ ] Contains Duplicate ✅
- [ ] Group Anagrams
- [ ] Top K Frequent Elements
- [ ] Product of Array Except Self
- [ ] Valid Sudoku
- [ ] Encode/Decode Strings
- [ ] Longest Consecutive Sequence
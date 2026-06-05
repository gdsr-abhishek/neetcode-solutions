

> **Interview target:** identify when to use sliding window, explain the invariant, implement from scratch.

|Field|Value|
|---|---|
|Topic|Sliding window pattern|
|Week covered|Week 2 — Jun 5, 2026|
|Problems solved|Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters|
|Status|✅ Can implement without notes|

---

## What is sliding window?

A dynamic window over a sequence that can shrink, expand, or stay fixed based on a condition — instead of recalculating from scratch each time, you slide the window and update incrementally.

```
Brute force: check every possible subarray → O(n²)
Sliding window: maintain a window, update as you move → O(n)
```

**The key question for every sliding window problem:**

> When do you shrink the window?

---

## Two variants

|Variant|Window size|When to use|
|---|---|---|
|Fixed window|Constant k|"Find max sum subarray of size k"|
|Dynamic window|Varies|"Find longest substring with condition"|

---

## Problem 1 — Best Time to Buy and Sell Stock

**Problem:** One buy + one sell. Maximise profit.

**Insight:** At every position — buy at the lowest price seen so far, sell at current price.

**Approach:** Track running minimum and maximum profit. Not a classic two-pointer — left pointer only updates when a new minimum is found.

```
min_price = prices[0]
max_profit = 0

for each price:
    max_profit = max(max_profit, price - min_price)
    min_price = min(price, min_price)
```

```python
# INSIGHT: buy at lowest seen so far, sell today — track running min and max profit
# WHY IT WORKS: left pointer (min) only moves when strictly lower price found
#               ensures buy always happens before sell
# COMPLEXITY: time O(n) single pass / space O(1) two variables
# BREAKS WHEN: empty array — handle prices[0] IndexError
#              all decreasing — returns 0 correctly (no transaction = 0 profit)
```

---

## Problem 2 — Longest Substring Without Repeating Characters

**Problem:** Find length of longest substring with all unique characters.

**Insight:** Maintain a window of unique characters. When duplicate found — shrink from left until window is valid again.

**Approach:** Dynamic two-pointer + hashmap tracking character counts.

```
left = 0, right = 0
hashmap = {}

while right < len(s):
    if s[right] not in window:
        add s[right], expand right
        update max length
    else:
        remove s[left], shrink left
```

```python
# INSIGHT: maintain window of unique chars — shrink when duplicate found
# WHY IT WORKS: duplicate condition dynamically shrinks window until valid
#               every character visited at most twice (once by right, once by left)
# COMPLEXITY: time O(n) / space O(1) — hashmap bounded by alphabet size (constant 26)
# BREAKS WHEN: empty string — handled, returns 0
#              all same char "aaaa" — window always size 1, returns 1 correctly
```

---

## Key difference between the two problems

|Problem|Left pointer behaviour|Window type|
|---|---|---|
|Buy and Sell Stock|Updates only when new minimum found — greedy running min|Not classic two-pointer|
|Longest Substring|Shrinks actively when constraint violated|Classic dynamic two-pointer|

---

## When to reach for sliding window

- "Longest / shortest subarray / substring with condition X"
- "Maximum / minimum sum of subarray of size k"
- "Find all substrings / subarrays satisfying condition"
- Any problem where recomputing from scratch is O(n²) but updating incrementally is O(1)

---

## The shrink condition pattern

```
expand right → check condition
if condition violated:
    shrink left until condition satisfied again
update answer
```

---

## Depth trap Q&A — answer cold

|Question|Answer|
|---|---|
|When do you shrink the window?|When the window violates the problem constraint|
|Why is sliding window O(n)?|Each element is visited at most twice — once by right pointer, once by left|
|Fixed vs dynamic window?|Fixed: window size is constant k. Dynamic: size varies based on condition.|
|Space complexity of substring problems?|O(1) — hashmap bounded by alphabet size, a constant|

---

## Connections

- → `two-pointers.md` — sliding window is a specialised two-pointer
- → `hashmap-pattern.md` — hashmap used for O(1) duplicate detection
- → Week 2 Saturday look-ahead: Binary search
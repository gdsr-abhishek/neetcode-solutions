# Binary Search

> **Interview target:** identify when to use binary search, explain the invariant, implement all three templates from scratch.

| Field | Value |
|---|---|
| Topic | Binary search pattern |
| Week covered | Week 2 Saturday — Jun 7, 2026 |
| Status | ✅ Intuition locked — implementation next week |

---

## What is binary search?

Eliminate half the search space at every step by halving the range — instead of scanning every element, use the sorted property to discard irrelevant halves.

```
Linear search: check every element → O(n)
Binary search: halve the range    → O(log n)
```

**Why O(log n)?**
```
1024 elements → 10 halvings → done
2048 elements → 11 halvings → done
n elements    → log₂(n) halvings → done
```

Each step eliminates half. You're not scanning — you're discarding.

---

## The one requirement

**Array must be sorted.**

Without sorted order — halving means nothing. You can't eliminate half the search space if you don't know which half contains the answer.

Sorted array guarantees:
```
everything left of mid  < arr[mid]
everything right of mid > arr[mid]
```

That guarantee is what makes elimination safe.

---

## The invariant

> At every step, the answer is guaranteed to be within `[low, high]`.

You never eliminate a position that could be the answer. Every move of `low` or `high` is safe because you've already checked and eliminated `mid`.

---

## Why `(low + high) // 2`?

- `//` = integer division → mid must be a valid array index, not a float
- Safer form: `low + (high - low) // 2` → avoids integer overflow for very large arrays
- Both work in Python — know the safer form for interviews

---

## Three templates

### Template 1 — Exact match
Find target, return index. Return -1 if not found.

```
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: low = mid + 1
    else: high = mid - 1
return -1
```

**When:** looking for an exact value in sorted array.
**Key:** `low <= high` — need to check when low and high converge on one element.

---

### Template 2 — Left boundary
First position where condition is true.

```
while low < high:
    mid = (low + high) // 2
    if condition(mid): high = mid
    else: low = mid + 1
```

**When:** "find first/leftmost X" problems.
**Key:** `low < high` — convergence point is the answer. `high = mid` not `mid - 1` because mid could be the answer.

---

### Template 3 — Right boundary
Last position where condition is true.

```
while low < high:
    mid = (low + high + 1) // 2
    if condition(mid): low = mid
    else: high = mid - 1
```

**When:** "find last/rightmost X" problems.
**Key:** `+1` in mid calculation prevents infinite loop when `low = mid`.

---

## `low = mid + 1` vs `low = mid`

| When | Why |
|---|---|
| `low = mid + 1` | mid already checked and eliminated — not the answer |
| `low = mid` | mid itself could be the answer — boundary search |

This is the entire difference between exact match and boundary search templates.

---

## When to reach for binary search

- Sorted array + find target → exact match
- "Find first/last position of X" → boundary search
- "Find minimum in rotated array" → modified binary search
- Search space can be halved based on a condition → binary search on answer
- Brute force is O(n), sorted property exists → binary search gives O(log n)

---

## Complexity

| | Time | Space |
|---|---|---|
| Binary search | O(log n) | O(1) |
| Linear search | O(n) | O(1) |

---

## Depth trap Q&A — answer cold

| Question | Answer |
|---|---|
| Why must array be sorted? | Sorted order lets you safely eliminate half — without it, you can't know which half contains the answer |
| Why O(log n)? | Each step halves the search space — 1024 elements needs only 10 steps |
| `low <= high` vs `low < high`? | Exact match uses `<=`. Boundary search uses `<` — convergence point is the answer |
| Why `mid + 1` not `mid`? | Mid already checked and eliminated. `mid` only when mid itself could be the answer. |
| Integer overflow in mid? | Use `low + (high - low) // 2` instead of `(low + high) // 2` for large arrays |

---

## Problems to solve — Week 3

- [x] Binary Search (LC 704) — exact match template ✅ solved 7 min, accepted
- [ ] Find Minimum in Rotated Sorted Array (LC 153) — modified binary search
- [ ] Search in Rotated Sorted Array (LC 33) — harder variant
- [ ] Find First and Last Position (LC 34) — boundary search both sides

---

## Connections

- → `sliding-window.md` — both are O(n) reducers but different tools
- → `two-pointers.md` — binary search is a specialised two-pointer on sorted arrays
- → Week 3 Monday — execute binary search problems with this intuition already locked
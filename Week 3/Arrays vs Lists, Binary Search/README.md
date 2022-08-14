# Arrays vs Lists, Binary Search

**Table of Contents**:

- [Sequence of Value](#sequence-of-value)
- [Arrays](#arrays)
- [Lists](#lists)
- [Operations](#operations)
- [Search Problem](#search-problem)
- [Search a sorted sequence](#search-a-sorted-sequence)
- [Binary Search](#binary-search)
- [Python Lists](#python-lists)

## Sequence of Value

Two basic ways of storing a sequence of values.

- Arrays
- Lists

What's the difference?

## Arrays

- Single block of memory. (All elements are contiguous, without any gaps)
- Elements of uniform type.
  - Typically size of sequence is fixed in advance.
- Indexing is fast.
  - Access `i`th element in constant time for any `i`.
  - Compute offset from the start of memory block.
- Inserting between `i` and `i+1` is expensive.
- Contraction is expensive.

## Lists

- Values are scattered in memory.
  - Each element points to the next - "linked" list.
  - Flexible size.
  - Each element can be of different types.
- Follows `i` links to access `i`th element.
  - Cost proportional to `i`.
- Inserting or deleting an element is easy.
  - Plumbing, new block in memory, removes a link from `i` and `i+1`, and attaches itself in the `i+1` location. Similarly for deletion as well.

## Operations

- Exchange `seq[i]` and `seq[j]`.
  - Constant time in array.
  - Linear time in lists.
- Delete `seq[i]` or insert `v` after `seq[i]`.
  - Constant time in lists.
  - Linear time in array.
- Algorithms on one data structure might work differently from on other. eg: Binary Search.

## Search Problem

- Is value `v` present in the collection `seq`?
- Does the structure of seq matter?
  - Array vs List
- Does the organization of the information matter?
  - Values are sorter or unsorted.

```py
# Search function for an unsorted sequence
# Not looking for position
def search(seq, v):
  for x in seq:
    if x == v:
      return(True)
  return(False)
```

- Need to scan entire sequence.
- Time proportional to the length of the sequence.
- Does not matter if `seq` is list or array.

## Search a sorted sequence

- What is seq is sorted?
  - Compare `v` with the midpoint of `seq`.
  - If the midpoint is `v`, the value is found.
  - If `v` < midpoint, search left half of `seq`.
  - If `v` > midpoint, search right half of `seq`.
- This is **Binary Search**!

## Binary Search

```py
# assuming seq is sorted
# and l < r
def bsearch(seq, v, l, r):
  if (r - l == 0):
    return(False)
  mid = (l + r) // 2
  if (v == seq[mid]):
    return (True)
  if (v < seq[mid]):
    return(bsearch(seq, v, l, mid))
  else:
    return(bsearch(seq, v, mid+1, r))
```

- How long does it take?
  - Each step halves the interval to search.
  - For interval of size 0, the answer is immediate.
- T(n): time to search in an array of size n.
  - T(0) = 1
  - T(n) = 1 + T(n/2). This is a recurrence anomaly.
- Unwind the occurrence.
  - T(n) = 1 + T(n/2) = 1 + 1 + T(n/2^2) = ...
      = 1 + 1 + ... + 1 + T(n/2^k)
      = 1 + 1 + ... + 1 + T(n/2^log n) =
  - O(log n)
  - n = 2^k then k = log2 n
- Works only for arrays. As positions are only defined for them. Jumping to the `i`th position in constant time.

## Python Lists

- Are built in lists in Python lists or arrays?
- Documentation says they are lists.
- However, positional indexing allows indexing allows us to treat them as arrays.
- Assume that they are arrays.

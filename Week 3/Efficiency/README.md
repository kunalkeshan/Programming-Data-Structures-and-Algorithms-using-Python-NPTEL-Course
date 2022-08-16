# Efficiency

**Table of Contents**:

- [O(n) notation](#o-notation)

- Measure time taken by an algorithm as a function `T(n)` with respect to input size `n`.
- Usually report *worst case* behavior.
  - Worst case for search in a sequence is when value is not found in the sequence.
  - Worst case is easier to calculate than "average" case or other more reasonable measures.

## O() notation

- Interested in broad relationship between input size and running time.
- Is `T(n)` proportional to log n, n, n log n, ..2^n?
- Write `T(n) = O(n)`, `T(n) = O(n log n)` to indicate this
  - Linear scan is O(n) for arrays and lists.
  - Binary search is O(log n).

> Python can do about 10^7 basic steps in one second.

- Theoretically `T(n) = O(n^k)` is considered efficient.
  - Polynomial time.
- In practice even `T(n) = O(n^2)` has very limited effective range.
  - Inputs larger than size 5000 take very long time compute.
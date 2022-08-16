# Selection Sort

**Table of Contents**:

- [Other advantages of sorting a sequence](#other-advantages-of-sorting-a-sequence)
- [Selection sorting](#selection-sorting)
- [Analysis of selection sort](#analysis-of-selection-sort)

## Other advantages of sorting a sequence

- Finding *median* value; midpoint of sorted list.
- Checking for duplicates.
- Building a frequency table of value.

## Selection Sorting

- Select the next element in sorted order.
- Move it into its correct place in the final sorted list.
- Avoid using a second list.
  - Swap minimum element with the value in the first position.
  - Swap second minimum element to the second position.
  - and so on...

## Analysis of Selection Sort

- Finding minimum in unsorted segment of length `k` requires one scan of `k` steps.
- In each iteration, segment of scanned reduces by 1.
- `T(n) = n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n^2)`.

# Merge Sort

**Table of Contents**:

- [O(n^2) sorting algorithms](#on2-sorting-algorithms)
- [A different strategy?](#a-different-strategy)
- [Combining sorted lists](#combining-sorted-lists)
- [Merge Sorting](#merge-sorting)
  - [Divide and Conquer](#divide-and-conquer)

## O(n^2) sorting algorithms

- Selection sort and insertion sort are both O(n^2).
- O(n^2) sorting is infeasible for `n` over 5000.

## A different strategy?

- Divide array in two equal parts.
- Separately sort left and right half.
- Combine the two sorted halves to get the full array sorted.

## Combining sorted lists

- Given tow sorted lists A and B, combine into a sorted list C.
  - Compare first element of A and B.
  - Move it into C.
  - Repeat until all elements in A and B are over.
- Merging A and B.

## Merge Sorting

- Sort A[0:n//2]
- Sort A[n//2:n]
- Merge sorted halves into B[0:n].
- Using recursion to sort the halves.

### Divide and Conquer

- Break up problem into disjoint parts.
- Solve each part separately.
- Combine the solutions efficiently.

## Merging Sorted Lists

Combine two sorted lists A and B into C.

- If A is empty, copy B into C.
- If B is empty, copy A into C.
- Otherwise, compare first element of A and B and move the smaller into C.
- Repeat until all elements in A and B have been moved.

Code: [mergesorting.py](./mergesorting.py)

## Merge sort lists

To sort A[0:n] into B[0:n]

- If n is 1, noting to be done.
- Otherwise,
  - Sort A[0:n//2] into L.
  - Sort A[n//2:n] into R.
  - Merge L and R into B.

Code: [mergesort.py](./mergesort.py)

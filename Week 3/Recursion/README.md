# Recursions

**Table of Contents**:

- [Inductive definitions](#inductive-definitions)
- [Recursive computation](#recursive-computation)
- [Inductive definitions for lists](#inductive-definitions-for-lists)
- [Recursive insertion sort](#recursive-insertion-sort)
- [Analyzing Recursive insertion sort](#analyzing-recursive-insertion-sort)
- [O(n^2) sorting algorithms](#on2-sorting-algorithms)
- [Recursion limit in python](#recursion-limit-in-python)

## Inductive definitions

- Many arithmetic functions are naturally defined inductively.
- **Factorial**
  - `0! = 1`.
  - `n! = n * (n-1)!`.
- **Multiplication**
  - `m * 1 = m`.
  - `m * (n+1) = m + (m * n)`.
- Define one or more base cases.
- Inductive step defines f(n) in terms of smaller arguments.

## Recursive computation

- Inductive definitions naturally give rise to recursive programs.
- Factorial

```py
def factorial(n):
    if n == 0:
        return (1)
    else: 
        return (n * factorial(n - 1))
```

- Multiply

```py
def multiply(m,n):
    if(n==1):
        return m
    else:
        return (m + multiply(m, n-1))
```

## Inductive definitions for lists

- Lists can be decomposed as
  - First (or last) element
  - Remaining list with one less element.
- Define list functions inductively.
  - Base case: empty list of list of size 1.
  - Inductive step: f(l) in terms of smaller sub lists of l.
- Length of a list.

```py
def length(l):
    if l == []:
        return 0
    else:
        return(1 + length(l[1:]))
```

- Sum of a list.

```py
def sumlist(l):
    if l == []: 
        return 0
    else:
        return (l[0] + sumlist(l[1:]))
```

## Recursive insertion sort

- Base case: if list has length 1 or 0, return the list.
- Inductive step:
  - Inductively sort slice `l[0:len(l)-1]`.
  - Insert `l[len(l)]` into this sorted list.
- Check Code: [insertionsort.py]

## Analyzing Recursive insertion sort

- `T(n)` time to run insertion sort on length n.
  - Time `T(n-1)` to sort slice `seq[0:n-1]`.
  - n-1 steps to insert `seq[n-1]` in sorted slice.
- Recurrence
  - `T(n) = n -1 + T(n-1)`
  - `T(1) = 1`
  - `T(n) = n - 1 + T(n-1) = n -1 + n - 2 + T(n-2) = ... = n-1 + n-2 + ... 1 = n(n-1)/2 = O(n^2)`.

## O(n^2) sorting algorithms

- Selection sort and insertion sort are both O(n^2)
- O(n^2) sorting is infeasible for n over 5000.
- Insertion sort is better than selection sort as insertion sort, stops searching the list once the position is found.

## Recursion limit in Python

- Python sets a recursion limit of about 1000.
- Can manually raise the limit.

```py
import sys
sys.setrecursionlimit(10000)
```
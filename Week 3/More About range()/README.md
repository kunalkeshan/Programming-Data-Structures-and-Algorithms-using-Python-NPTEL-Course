# More about `range()`

**Table of Contents**:

- [Introduction](#introduction)
- [General Rule for `range(i,j,k)`](#general-rule-for-rangeijk)
- [Why does `range(i,j)` stop at `j-1`](#why-does-rangei-j-stop-at-j-1)
- [`range()` and lists](#range-and-lists)

## Introduction

- `range(i, j)` produces the sequence i, i+1, ..., j-1.
- `range(j)` automatically starts from 0, 1, ..., j-1.
- `range(i, j, k)` increments by k; i, i+k,..., i+nk.
  - Stops with n such that i + nk < j <= i + (n+1)k.
- Count down? Make `k` negative.
  - `range(i, j, -k)`, i > j, produces, i, i-1, ..., j+1.

## General Rule for `range(i,j,k)`

- Sequence starts from `i` and gets as close to `j` as possible without crossing `j`.
- If `k` is positive, and `i` >= `j`, empty sequence.
  - Similarly if `k` is negative and `i` <= `j`.
- If `k` is negative, stop "before" `j`.
  range(12, 1, -3) produces 12, 9, 6, 3.

## Why does `range(i, j)` stop at `j-1`?

- Mainly to make it easier to process lists.
- List of length n has positions 0, 1, ..., n-1.
- `range(0, len(l))` produces correct range of valid indices.

## `range()` and lists

```py
    for i in [0,1,2,3,4]
    for i in range(0, 5)
```

Is `range(0,5) == [0,1,2,3,4]`?

- In Python2, yes
- In Python3, no

Convert a `range()` to a list using `list()`.

- `list(range(0,5)) == [0, 1, 2, 3, 4]`.

# Insertion Sort

**Table of Contents**:

- [Introduction](#introduction)
- [Analysis of Insertion Sort](#analysis-of-insertion-sort)

## Introduction

- Start building a sorted sequence with one element.
- Pick up next unsorted element and insert it into its correct place in the already sorted sequence.

## Analysis of Insertion Sort

- Inserting a new value in sorted segment of length `k` requires up to `k` steps in the worst case.
- In each iteration, sorted segment in which to insert is increased by 1.
- `T(n) = 1 + 2 + ... + n-1 = n(n-1)/2 = O(n^2)`.

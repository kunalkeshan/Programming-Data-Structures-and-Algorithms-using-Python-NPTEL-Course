# Lists

**Table of Contents**:

- [Introduction](#introduction)
- [Strings and Lists](#strings-and-list)
- [Nested Lists](#nested-lists)
- [Mutable vs Immutable](#mutable-vs-immutable)
- [Copying Values](#copying-values)
- [Digression on equality](#digression-on-equality)
- [Concatenation](#concatenation)

## Introduction

It's a sequence of values. A collection of same or different data types.

eg:

```python
names = ["Jaswin", "Kumar", "Surendar", "Jaya"]
marks = [68, 23, 59, 56];
mixed = [69, "Lucifer", False]
```

Values can be extracted by their position.

eg:

- `names[0] is "Jaswin"`.
- `marks[1:3] is [23, 59]`.


Length of a list can be taken by `len()`.

eg:

`len(names) is 4`.

## Strings and List

Let `str = "hello"`.

Then `str[0] is h == str[0:1] is also h` in the case of strings.

Let `nums = [4, 62, 639]`.

Then `nums[0] is 4 (a value) != nums[0:1] is [4] (a list)` in the case of lists.

## Nested Lists

```python
nested = ["Kunal", [1, 2, 3], [True, "Hello, World!"]]
nested[0] # "Kunal"
nested[1] # [1, 3, 3]
nested[2][1] # "Hello, World"
```

## Updating Lists

Positions of lists can be updated unlike a string.

```python
nums = [1, 34, 6456, 43]
nums[2] = 45
```

Lists are **Mutable**!

## Mutable vs Immutable

What happens when we assign names?

```python
x = 5
y = x
x = 7
```

The values of `y` does not change.
`y` just just copies the value of `x` and creates a new copy of it.

For _immutable_ values, we can assume that assignment makes fresh copy of a value. `int`, `float`, `bool`, `str` are immutable. Updating one value does not update the other.

For _mutable_ values, the assignment does not make a fresh copy. Lists are mutable. Updating one list, will update the value of other list that it was copied from.

## Copying Values

What if we don't want a copied list to be updated when the original list is updated.

We can use slice to crease new (sub)lists from an old one.

Making a _full slice_

`l[:] == l[0:len(l)]`. This creates a copy, or a new list and does not get updated when the original list is updated.

## Digression on equality

```python
list1 = [1, 3, 5, 7]
list2 = [1, 3, 5, 7]
list3 = list2
```

- `list1` and `list2` are two list, with the same value.
- `list2` and `list3` are two names for the same list.
- `x == y` checks if `x` and `y` have the same value.
- `x is y` checks if `x` and `y` refer to the same object. (does both x and y point to the same memory location)
- `list2 is list3` is True.
- `list1 is list2` is False.

## Concatenation

Can combine lists using the `+` operator. `+`  also produces a new list.

```python
list1 = [1,3, 5, 7]
list2 = [9]
list3 = list1 + list2
```

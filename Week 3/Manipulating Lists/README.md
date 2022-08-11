# Manipulating Lists

**Table of Contents**:

- [Introduction](#introduction)
- [Extending a list](#extending-a-list)
- [List Functions](#list-functions)
- [Notes](#notes)
- [Further List manipulation](#further-list-manipulation)
- [List Membership](#list-functions)
- [Other functions](#other-function)

## Introduction

- Lists are mutable objects. 
- A copy of the original list, will affect the copy as well.
- Using Slices to make lists, creates a new copy that points to a different object.
- So does concatenation. It produces a new list.

## Extending a list

- Adding an element to a list?
- Using `append` to add a new item to the end of the list. 
- The copy of the original also gets appended with the new value.

```py
list1 = [1,3,5]
list1.append(7) # [1,3,5,7] 
```

## List Functions

- `append` only adds only one value at a time.
- Use `extend` to add a list of elements to the main list.
- `remove(x)` removes first occurrence of x in the list.
  - Gives an error if x does not exist.
  - Only the first occurrence is removed.

## Notes

`list.append(x)`

- `list` is an object.
- `append()` is a function to update the object.
- `x` is an argument to the function.

## Further list manipulation

### Slice replacement

```py
list1 = [1,3,5]
list2 = list1
list1[1:] = [7,8]
```

`list1` and `list2` are both `[1,7,8]`.

- Can be used to expand or shrink the list.

## List membership

To check if a value exists in a list. Use `in`.

- `x in l` returns True if value `x` is found in list `l`.

## Other Function

- `l.reverse()` - Reverse the list.
- `l.sort()` - Sort in ascending order.
- `l.index(x)` - Index of `x` from the left most position. Gives an error if not found.
- `l.rindex(x)` - Index of `x` from the right most position. Gives an error if not found.
- Many more...

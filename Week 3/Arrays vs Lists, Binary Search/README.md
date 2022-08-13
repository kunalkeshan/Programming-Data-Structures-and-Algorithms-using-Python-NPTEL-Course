# Arrays vs Lists, Binary Search

**Table of Contents**:

- [Sequence of Value](#sequence-of-value)
- [Arrays](#arrays)
- [Lists](#lists)

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

# Strings

Manipulating Text. Need for Text processing is increasingly important.

**Table of Contents**:

- [Basics and Features](#basics-and-features)
- [Operation on String](#operations-on-strings)
- [Extracting Substrings](#extracting-substrings)
- [Modifying String](#modifying-strings)

## Basics and Features

For text, python uses type `str`.

- It's a sequence of characters
- A single character is a string of length 1.
- No `char` type.
- Can use single, double, even triple quotes.

eg:

```python
name = 'Kunal'
thing = "Kunal's laptop" # use of ' inside the "".
speech = '''Jaswin said, "He was sleeping"'''
```

- Each character has a position in a string.

eg:

```python
name = "Kumar"
```

|Position | 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - | - |
|String | K | u | m | a | r |
| Reverse | -5 | -4 | -3 | -2 | -1 |

- Position -1, -2 count backwards.

## Operations on Strings

- Combine two strings, (concatenations) using `+`.
- `len(s)` returns the length of string `s`.

## Extracting substrings

Taking a `slice`, which is a segment from a string.

eg:

```python
name = "Surendar"
```

- `name[0:4]` is "Sure".
- `name[i:j]` starts at `name[i]` and ends at `name[j-1]`.
- `name[:j]` starts at `name[0]`.
- `name[i:]` ends at `name[les(s)-1]`.

## Modifying strings

Strings are immutable, meaning specific positions of strings cannot be replaced.

Instead, use slices and concatenation for forming a new string.

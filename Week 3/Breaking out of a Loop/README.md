# Breaking out of a Loop

**Table of Contents**:

- [Loops Revisited](#loops-revisited)
- [Using `break`](#using-break)
- [Odd feature of python, Use `else` with loops](#odd-feature-of-python-use-else-with-loops)

## Loops Revisited

- `for i in l` - Repeat body for each item in list `l`.
- `while condition` - Repeat body till `condition` becomes `False`.
- In some situations, when a condition is met, we might want to exit the loop then and there.

eg:

### Searching for a value in a list

- Scan for the list.
- When value is found, stop scanning.
- Return the position of value, if not found then return -1.

## Using `break`

- `break` exists the loop when called.
- Skips looping elements after break is called.

## Odd feature of python, Use `else` with loops

- `else` can be attached for a `while` or even a `for`.

```py
for i in l:
    ...
else:
    ...

while Condition:
    ...
else:
    ...
```

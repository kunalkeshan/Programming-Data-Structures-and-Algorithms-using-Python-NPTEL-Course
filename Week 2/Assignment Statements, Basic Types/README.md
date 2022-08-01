# Assignment Statements, Basic Types - Int, Float and Bool

**Table of Contents**:

- [Assignment Statement](#assignment-statement)
- [Numeric Values](#numeric-values)
- [Operations on numbers](#operations-on-numbers)
  - [Normal Arithmetic Operations](#normal-arithmetic-operations)
  - [Other Operators](#other-operators)
- [Boolean Values](#boolean-values)
  - [Boolean Operators](#boolean-operators)
  - [Comparisons](#comparisons)

## Assignment Statement

```python
i = 3
j = 23 * i
j = j + 351
```

- Left Hand Side is the `name` of the variable.
- Right Hand Side is the `value` or `expression` assigned to the variable.
- The Operations depend on the `type` of value.

## Numeric Values

- `int` - Integers, 13, -3, 3432, etc. Have no decimal part. (Decimal point is fixed)
- `float` - Fractional Numbers 324.345, 420.69, etc. Have decimal part. (Floating Point - Decimal point is not fixed)

What's the difference? Both are numbers, but why are they of different types?

- Distinction is in the way the numbers are stored.
- Internally, every number is stored as a finite sequence of 1s and 0s.

If it's an `int`, then the number is stored in their binary notation.

If it's a `float`, the sequence is broken up into two parts, `mantissa` and `exponent`.

eg: 0.420 (mantissa) * 10^24 (exponent)

## Operations on numbers

### Normal Arithmetic Operations

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/`  Division

`/`  always produces a float.
eg: `7/3.5 is 2.0`, `7/2 is 3.5`.

- `//` Quotient, returns the quotient in a division
- `%` Modulus  returns the remainder in a divsion
- `**` Exponential Operators

### Other Operators

`log()`, `sqrt()`, `sin()`.

These are built in with python, but not available by default. Needs to imported from the `math` library, using,

```python
from math import *
```

## Boolean Values

`bool` - True (or) False

- Used in conditionals and control the execution of the program.

### Boolean Operators

- `not` - True is False, and False is True.
- `x and y` - True only when x and y is True.
- `x or y` - True if only at least x or y is true.

### Comparisons

- `==` - Both operands should be equal
- `!=` - Both Operands are not equal
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal to
- `>=` - Greater than or equal to

# Finding the Greatest Common Divisor of Two Numbers

**Table of Contents**:

- [Logic](#logic)
- [Algorithm](#algorithm)
- [A Programmatic Algorithm](#a-programmatic-algorithm)

## Logic

A Greatest Common Divisor of two number is the largest *common* number that divides both the given numbers.

Eg: Finding the GCD of 8 and 12.

Factors of 8 are 1, 2, 4, and 8.

Factors of 12 are 1, 2, 3, 4, 6, and 12.

The common numbers that divides both is 1, 2 and 4. 4 being the largest number is the GCD for both 8 and 12.

Notice that 1 is always a common divisor for any number. So any two numbers will by default have a GCD of 1.

## Algorithm

- List out all the factors of first number.
- List out all the factors of second number.
- Compare both the lists and return the greatest number from it.

How to list out all the factors of a number?

- List out all numbers from 1 to the number itself.
- If the number divides with the current number (1, 2, 3, ..., n) without any remainder, then add it to the list.

## A Programmatic Algorithm

- Take in the two number as input, `m` and `n`.
- Add `i` to `fm` (factors of m) by looping it through number from `i` to `m` if remainder of `m/i` is 0.
- Add `j` to `fn` (factors of n) by looping it through number from `j` to `n` if remainder of `n/j` is 0.
- If a factor `f` of `fm` is present in `fn`, then add it to list of common factors `cf`.
- Return the largest `cf` from the list.

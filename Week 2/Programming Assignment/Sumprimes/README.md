# Sumprimes

Write a function `sumprimes(l)` that takes as input a list of integers l and returns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

```python
sumprimes([3,3,1,13])
# 19
sumprimes([2,4,6,9,11])
# 13
sumprimes([-3,1,6])
# 0
```

## Algorithm

- Take in list of numbers.
- Initialize a `total` value of 0.
- Check if each number is a prime
- If number is a prime, then add it to the `total`.
- Return `total`, once loop is completely iterated.

# Euclid's Algorithm for GCD

- Assume `d` divides both `m` and `n`, and `m` > `n`.
- Then `m = ad` and `n = bd`.
- So `m - n = ad - bd = (a-b)d`.
- `d` divides `m-n` as well.
- Therefore, `gcd(m,n) = gcd(n, m-n)`.

## Even Better GCD

This Algorithm improves the efficiency of the code, instead of computing through all the digits, it computes only through the number of digits in the largest number.

- Assuming `n` does not divide `m`.
- Then `m = qn + r`, where `q` is the quotient, `r` is the remainder when `m` is divided by `n`.
- Again, assume `d` divides both `m` and `n`.
- Then `m = ad` and `n = bd`.
- Substituting in the above equation we get, `ad = q(bd) + r`.
- Then `r = cd`, and `d` divides `r` as well.
 
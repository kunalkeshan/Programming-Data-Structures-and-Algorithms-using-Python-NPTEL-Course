# Improved GCD

[First approach](../Greatest%20Common%20Divisor%20of%20Two%20Numbers) taken was a brute force method. We can incrementally improve the program in the following ways.

**Table of Contents**:

-   [Single Scan for list of Factors](#single-scan-for-list-of-factors)
-   [Without using Lists](#without-using-lists)
-   [Scanning Backwards](#scanning-backwards)
-   [End Note](#end-note)

## Single Scan for list of Factors

In the first approach, we're scanning for both the list of factors for `m` and `n`.

We know that the common list of factors for both `m` and `n` will always be less that the maximum of both `m` and `n`.

So we can refactor the code to scan for `i` between 1 to the `max(m,n)` and for number to both a common factor of both `m` and `n`, the remainder of `i` divided with both `m` and `n` should be 0.

Check Code here: [Single Scan for list of Factors](./gcd_single_scan.py)

## Without using Lists

We've seen before that gcd of any two numbers will always have 1 as one of their Common Factors. If there's a number > 1, then that number becomes the Greatest common Denominator for the two numbers.

Essentially, when a greater number is found, it replaces the previous number. We can apply the same logic to drop the use of lists altogether.

Now the Common factor, will always be a number that is the minimum of `m` and `n`. It cannot be more than that of the number less that the other.

For eg: Let's take 8 and 12, we know that the GCD of this is 4.

List of Common Factors for 8: 1,2,4,8

List of Common Factors for 12: 1,2,4,6,12

From the list the GCD is 4. You can see that the GCD will always be the minimum of the two. Since 8 < 12, the Common factor will also be less than 8.

So we scan `i` for the range from 1 to `min(m,n)`.

Check Code here: [Without using Lists](./gcd_without_lists.py)

## Scanning Backwards

Since we're looking for the Greatest Common Denominator, wouldn't it make sense to start the scan from the greatest number. In this case too, the gcd will be the minimum of the two numbers.

We can backwards in this case, for `i` between `min(m,n)` and 1.

If the conditions match that both numbers are divisible by i, then we return the number without any further computation, else we continue looping till we find what we're looking for.

Check Code here: [Scanning Backwards](./gcd_backwards_scan.py)

## End note

Principally, all the refactors mentioned above still follow the same pattern that we did before. The only difference being that the code is optimized and will still loop through all the numbers given that they all have a common factor of 1 by default.

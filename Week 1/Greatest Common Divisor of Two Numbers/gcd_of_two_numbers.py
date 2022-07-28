def gcd(m, n):
    # Listing out factors of m
    fm = []
    for i in range(1, m+1):
        if(m%i) == 0:
            fm.append(i)
    
    # Listing out factors m
    fn = []
    for j in range(1, n+1):
        if(n%j) == 0:
            fn.append(j)

    # Finding Common factors in fm and fn
    cf = []
    for f in fm:
        if(f in fn):
            cf.append(f)

    # Since cf is already sorted, returning the right most number
    # or the largest number in the list of common factors
    return cf[-1]

gcd_of_two_nums = gcd(8, 12);

print(gcd_of_two_nums); # 4
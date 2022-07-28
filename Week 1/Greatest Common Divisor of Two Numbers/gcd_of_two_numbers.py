def gcd(m, n):
    fm = []
    for i in range(1, m+1):
        if(m%i) == 0:
            fm.append(i)
    
    fn = []
    for j in range(1, n+1):
        if(n%j) == 0:
            fn.append(j)

    cf = []
    for f in fm:
        if(f in fn):
            cf.append(f)

    return cf[-1]

gcd_of_two_nums = gcd(8, 12);

print(gcd_of_two_nums);
def gcd(m,n):
    cf = []
    for i in range(1, max(m,n)):
        if(m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return cf[-1]

gcd_of_two_nums = gcd(9, 12)

print(gcd_of_two_nums)
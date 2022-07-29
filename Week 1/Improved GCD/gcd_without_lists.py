def gcd(m,n):
    for i in range(1, min(n,m)):
        if(m%i) == 0 and (n%i) == 0:
            cf = i
    return cf

gcd_of_two_nums = gcd(43, 89)

print(gcd_of_two_nums)
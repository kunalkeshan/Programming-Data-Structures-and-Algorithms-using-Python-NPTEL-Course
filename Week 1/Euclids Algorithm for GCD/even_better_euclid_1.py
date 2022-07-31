def gcd(m,n):
    # Assuming m > n
    if(m < n):
        (m,n) = (n,m)

    if(m%n) == 0:
        return (n)
    else:
        return gcd(n, m%n) # m%n will always be less than n, m%n = r, and r < n.

n_from_gcd = gcd(64, 932)

print(n_from_gcd)
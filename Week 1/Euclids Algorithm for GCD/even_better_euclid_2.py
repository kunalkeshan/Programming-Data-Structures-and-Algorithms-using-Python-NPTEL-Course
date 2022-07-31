def gcd(m,n):
    # Assuming m > n
    if(m < n):
        (m,n) = (n,m)

    while(m%n) != 0:
        # m%n will always be less than n, m%n = r, and r < n.
        (m,n) = (n, m%n) 
    return (n)

n_from_gcd = gcd(64, 932)

print(n_from_gcd)
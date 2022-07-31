def gcd(m,n):
    if(m < n): # Asuming m > n
        (m,n) = (n,m)

    while(m%n) != 0:
        diff = m - n
        (m,n) = (max(n,diff), min(n, diff))

    return (n)

n_from_gcd = gcd(64, 932)

print(n_from_gcd)
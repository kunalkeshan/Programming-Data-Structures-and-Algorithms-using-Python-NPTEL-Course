def gcd(m,n):
    # Assuming m > n
    if (m < n):
        (m,n) = (n,m)
        
    if(m%n) == 0:
        return (n)
    else: 
        diff = m - n
        # What if diff > n? Most certainly possible
        return gcd(max(n, diff), min(n, diff))

n_from_gcd = gcd(64, 932)

print(n_from_gcd)
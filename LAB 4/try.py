x = 1234
y = 5678

def karatsuba(x,y):
    n = len(str(x))
    if n == 1:
        return x*y 
    a = str(x)
    b = str(y)
    n1 = len(a)
    n2 = len(b)

    a1 = a[:n1//2]
    a2 = a[n1//2:]

    b1 = b[:n2//2]
    b2 = b[n2//2:]

    p = int(a1) + int(a2)
    q = int(b1) + int(b2)

    w = karatsuba(int(a1),int(b1))
    t = karatsuba(int(a2),int(b2))
    s = karatsuba(p,q)

    m = s - w - t

    result = (10**n)*(w) + (10**n/2)*(m) + t
    return result
    
ans = karatsuba(x,y)
print(ans)    
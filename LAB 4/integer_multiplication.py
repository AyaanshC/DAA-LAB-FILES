a = 1999
b = -9111

def integer_multiplication(a,b):
    c = str(a)[::-1]
    d = str(b)[::-1]
    n1 = len(c)
    n2 = len(d)

    if a<0:
        c = str(a)[::-1]
        n1  = n1 - 1
    if b<0:
        d = str(b)[::-1]
        n2 = n2 - 1

    l = []
    for i in range(min(n1,n2)):
        ans = 0
        for j in range(max(n1,n2)):
            ans = ans + int(c[i])*int(d[j])*(10**j)*(10**i) 
        l.append(ans)
    result = 0
    for k in range(len(l)):
        result += l[k]
    if (a<0) ^ (b<0):
        return -result
    return result

c = integer_multiplication(a,b)
print(c)


def karatsuba_multiplication(a,b):
    if a < 10 or b < 10:
        return a * b
    
    p = max(len(str(a)), len(str(b)))
    q = p // 2 

    a1 = a // 10**q
    a0 = a % 10**q
    b1 = b // 10**q
    b0 = b % 10**q

    c2 = karatsuba_multiplication(a1, b1)
    c0 = karatsuba_multiplication(a0, b0)
    c1 = karatsuba_multiplication(a1 + a0, b1 + b0) - c2 - c0

    return (c2 * 10**(2*q)) + (c1 * 10**q) + c0

result = karatsuba_multiplication(a, b)
print(f"Product of {a} and {b} using Karatsuba multiplication is: {result}")

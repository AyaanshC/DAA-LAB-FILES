x = 1234
y = 5678

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

print(p)
print(q)
''' 
// Algorithm to calculate SPI
// Input: Array of credits C[], array of grades G[] and the number of subjects n
// Output: SPI of the semester
while n!=0 do:
    result += (C[n] * G[n])
    deno += C[n]
    n -= 1
SPI  = result/deno
return SPI

// Algorithm to calculate CPI
// Input: Array of SPI[] and the number of semesters n
// Output: CPI 
while i!=n do:
    sum += SPI[i]
    i += 1
CPI = sum/n
return CPI

'''

def calculateCPI(SPI,n):
    i=0
    sum = 0
    if(n<=0):
        print("Invalid Input for the number of semesters")
        return
    while i!=n:
        if(SPI[i]<=0):
            print("Invalid Input for SPI")
            return 0
        sum += SPI[i]
        i += 1
    CPI = sum/n
    return CPI

# T1
t1 = [8.9,9.8,10]
n = 3
print(calculateCPI(t1,n))

# T2
t2 = [9.5,9.6,9.7,9.8]
n = 4
print(calculateCPI(t2,n))

# T3
t3 = [8.52,9.67]
n = -5
print(calculateCPI(t3,n))

# T4
t4 = [-1,8.5,9.2]
n = 3
print(calculateCPI(t4,n))

# T5
t5 = [9.32,9.44,9.77,9.56,8.99,9.8,9.11,9.23]
n = 8
print(calculateCPI(t5,n))

def calculateSPI(g,c,n):
    i=0
    num = 0
    deno = 0
    if(n<=0):
        print("Invalid input for the number of subjects!!!")
        return 
    for j in range(0,n):
        if(g[j]<=0 or c[j]<=0):
            print("Invalid Input intercepted!!!")
            return 
    while i!=n:
        num += c[i]*g[i]
        deno += c[i]
        i+=1
    SPI = num/deno
    return SPI

# T1
g = [9,8,10]
c = [3,3,2]
n = 3
print(calculateSPI(g,c,n))

# T2
g = [7,8,10,9,9]
c = [3,3,5,2,1]
n = 5
print(calculateSPI(g,c,n))

# T3
g = [-1,8,9]
c = [3,3,2]
n = 3
print(calculateSPI(g,c,n))

# T4
g = [9,8,7,10]
c = [3,5,2,1]
n = -5
print(calculateSPI(g,c,n))

# T5
g = [10,9,10,8]
c = [3,3,5,1]
n = 4
print(calculateSPI(g,c,n))

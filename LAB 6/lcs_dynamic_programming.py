def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    mm = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  
                mm[i][j] = mm[i - 1][j - 1] + 1
            else:
                mm[i][j] = max(mm[i - 1][j], mm[i][j - 1])

    return mm[m][n]

s1 = "AAABBBBCAB"
s2 = "AABCBBABAB"

m = len(s1)
n = len(s2)
print(lcs(s1, s2))
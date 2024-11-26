def lcs_print(x, y, m, n):
    if m == 0 or n == 0:
        return ""
    
    if x[m-1] == y[n-1]:
        return lcs_print(x, y, m-1, n-1) + x[m-1]
    
    else:
        lcs1 = lcs_print(x, y, m-1, n)
        lcs2 = lcs_print(x, y, m, n-1)
        
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

# Example usage
x = "AAABBBBCAB"
y = "AABCBBABAB"
m = len(x)
n = len(y)

result = lcs_print(x, y, m, n)
print("Longest Common Subsequence:", result)

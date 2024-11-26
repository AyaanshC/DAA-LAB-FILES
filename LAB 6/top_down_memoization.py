import sys
import numpy as np


def mat_chain_mult(arr, i, j, memo):
    
    if i+1 == j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    res = sys.maxsize
    
    for k in range(i+1, j):
        min_cost = mat_chain_mult(arr, i, k, memo) + mat_chain_mult(arr, k, j, memo) + arr[i]*arr[k]*arr[j]
        
    res = min(res, min_cost)
    
    memo[i][j] = res
    return res

arr = [10,20,30,40,50,60]
i = 0
j = len(arr) - 1
memo = np.zeros((j+1,j+1), dtype = int) -1

print(mat_chain_mult(arr, i, j, memo))    
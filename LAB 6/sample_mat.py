import sys

def mat_chain_multiply(arr, i, j):
    if j - i <= 1:
        return 0
    
    min_cost = sys.maxsize

    for k in range(i + 1, j):
        cost = (mat_chain_multiply(arr, i, k) +
                mat_chain_multiply(arr, k, j) +
                arr[i] * arr[k] * arr[j])
        
        min_cost = min(min_cost, cost)

    return min_cost


arr = [7,4,7,3,7,5,7,9]
i = 0
j = len(arr) - 1

print(mat_chain_multiply(arr, i, j))
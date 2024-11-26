import numpy as np

x = np.random.randint(1,6,100)

print(x)

# Counting Inversions (Brute Force Algorithm):
def count_inversions(x):
    count = 0
    for j in range(100):
        for i in range(j+1,100):
            if(x[j]>x[i]):
                count = count + 1
    return count

a = count_inversions(x)
print(a)

# Counting Inversions (Divide And Conquer Algorithm):
def merge_and_count(arr, new_arr, left, mid, right):
    i = left    
    j = mid + 1 
    k = left    
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            new_arr[k] = arr[i]
            i += 1
        else:
            new_arr[k] = arr[j]
            inv_count += (mid-i + 1)  
            j += 1
        k += 1

    while i <= mid:
        new_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        new_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = new_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

print(f"Number of inversions: {count_inversions(x)}")

def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i * i  
    return result

print(f"Sum of squares: {sum_of_squares(5)}")
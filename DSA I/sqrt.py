
def sqrt_binary_search(n, precision=1e-6):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")
    
    low, high = (0, n) if n >= 1 else (n, 1)
    while (high - low) > precision:
        mid = (low + high) / 2
        if mid * mid < n:
            low = mid
        else:
            high = mid
    
    return (low + high) / 2

# Example usage
number = 25
result = sqrt_binary_search(number)
print(f"The square root of {number} is approximately {result:.6f}")

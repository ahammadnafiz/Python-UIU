def max_crossing_sum(arr, left, mid, right):
    """
    Find maximum sum of subarray that crosses the midpoint.

    Args:
        arr: Input array
        left: Left boundary
        mid: Midpoint
        right: Right boundary

    Returns:
        Maximum sum crossing the midpoint
    """
    # Find maximum sum for left part (including mid)
    left_sum = float("-inf")  # FIXED: Initialize to -infinity
    curr_sum = 0

    # Start from mid and go leftward
    for i in range(mid, left - 1, -1):  # FIXED: Start from mid, not mid+1
        curr_sum += arr[i]
        left_sum = max(left_sum, curr_sum)

    # Find maximum sum for right part (excluding mid)
    right_sum = float("-inf")
    curr_sum = 0

    # Start from mid+1 and go rightward
    for j in range(mid + 1, right + 1):
        curr_sum += arr[j]
        right_sum = max(right_sum, curr_sum)  # FIXED: Update right_sum

    # Return combined sum
    return left_sum + right_sum


def max_subarray(arr, left, right):
    """
    Find maximum subarray sum using divide and conquer.

    Args:
        arr: Input array
        left: Left boundary
        right: Right boundary

    Returns:
        Maximum subarray sum
    """
    # Base case: single element
    if left == right:
        return arr[left]

    # Divide
    mid = (left + right) // 2

    # Conquer: find max in left half, right half, and crossing
    left_max = max_subarray(arr, left, mid)
    right_max = max_subarray(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    # Combine: return maximum of the three
    return max(left_max, right_max, cross_max)


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
print("Maximum Subarray Sum:", max_subarray(arr, 0, n - 1))

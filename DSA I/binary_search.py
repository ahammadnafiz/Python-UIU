def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the middle element is the target
        if arr[mid] == x:
            return mid

        # If the target is greater, ignore the left half
        elif arr[mid] < x:
            left = mid + 1

        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target not found
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")


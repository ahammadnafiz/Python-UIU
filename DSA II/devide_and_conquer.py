def find_maxmin(arr, i, j):
    # base case: only one element
    if i == j:
        return arr[i], arr[i]

    # Base case: Two elements
    elif j == i + 1:
        if arr[i] > arr[j]:
            return arr[i], arr[j]
        else:
            return arr[j], arr[i]

    # devide
    mid = (i + j) // 2

    # conquer
    mx1, mn1 = find_maxmin(arr, i, mid)
    mx2, mn2 = find_maxmin(arr, mid + 1, j)

    # combine
    fmax = mx1 if mx1 > mx2 else mx2
    fmin = mn1 if mn1 < mn2 else mn2

    return fmax, fmin


A = [5, 1, 9, 3, 7, 2, 8]
max_val, min_val = find_maxmin(A, 0, len(A) - 1)
print("Maximum:", max_val)
print("Minimum:", min_val)

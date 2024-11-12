def bubble_sort(arr):
    n = len(arr)
    for _ in range(1, n):
        for j in range(0, n-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [10, 5, 2, 8, 7]
print(bubble_sort(arr))

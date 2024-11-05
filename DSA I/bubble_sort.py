# bubble_sort.py

def bubble_sort(arr):
    for _ in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [5, 2, 4, 6, 1, 3]
print(bubble_sort(arr))

# bubble_sort.py
def even_odd(arr):
    even = []
    odd = []
    for i in arr:
        if i %2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


def bubble_sort(arr):
    for _ in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [5, 2, 4, 6, 1, 3]
even, odd = even_odd(arr)
print(bubble_sort(even))
print(bubble_sort(odd))

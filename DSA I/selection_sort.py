# selection sort

def selection_sort(arr):
    for i in range(len(arr) - 1):
        m = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j

        arr[i], arr[m] = arr[m], arr[i]

    return arr

arr = [5, 2, 4, 6, 1, 3]
print(selection_sort(arr))


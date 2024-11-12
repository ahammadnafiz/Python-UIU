def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)

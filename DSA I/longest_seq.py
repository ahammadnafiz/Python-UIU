'''
You are given an unsorted array of integers, and your task is to find the longest subsequence of consecutive numbers. 
Consecutive numbers are those where each number is exactly 1 greater than the previous one
    '''

def bubble_sort(arr):
    n = len(arr)
    for _ in range(1, n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    arr = [4, 1, 2, 7, 6, 5]
    sorted_arr = bubble_sort(arr)

    max_len = 1
    current_len = 1
    start_index = 0
    for i in range(1, len(sorted_arr)):
        if arr[i] == arr[i-1] + 1:
            current_len += 1
        elif arr[i] != arr[i-1]:
            current_len = 1
            start_index = i

        if current_len > max_len:
            max_len = current_len
            start_index = i-current_len + 1

    result = sorted_arr[start_index:start_index + max_len]
    print("Longest consecutive subsequence:", result)

main()

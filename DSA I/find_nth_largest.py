'''
Find the nth largest number from an unsorted array.
'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if arr[j]<arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]

    return arr

def find_nth_largest(arr):
    selection_sort(arr)
    print("Sorted Array:", arr)
    
    while True:
        position = int(input("Enter the position (-1 to quit): "))
        if position == -1:
            break
        if 1 <= position <= len(arr):
            print(f"{position}th largest number is: {arr[-position]}")
        else:
            print("Invalid position. Please try again.")

# Example usage
arr = [4, 1, 2, 7, 6, 5]
find_nth_largest(arr)

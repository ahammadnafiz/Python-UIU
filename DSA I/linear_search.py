def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [4, 2, 2, 8, 3, 3, 1]
target = int(input('Enter a number: '))
result = linear_search(arr,target)

if result != -1:
    print(f"Target {target} found in index {result}")
else:
    print("Number is not found in list")

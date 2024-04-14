my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

new_dict = {}

for v in my_list:
    if v % 2 != 0:
        new_dict[v] = v ** 2

print(new_dict)
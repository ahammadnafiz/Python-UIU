user_input = input().split()

my_dict = {}

for word in user_input:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

print(my_dict)
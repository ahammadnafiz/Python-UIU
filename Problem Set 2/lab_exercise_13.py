'''
Write a program that will take a list as input. Next, find out, separately, the sum of the
odd and even index numbers of the list. If the list has one value only, print “Cannot do
this”.
'''


user_list = list(map(int, input().split()))  # Prompt the user to input a space-separated list of integers and convert it to a list of integers

even_index_sum = []  # Initialize an empty list to store the elements at even indices
odd_index_sum = []  # Initialize an empty list to store the elements at odd indices

if len(user_list) > 1:  # Check if the length of the user_list is greater than 1

    for i in user_list:  # Iterate over each element in the user_list
        if user_list.index(i) % 2 == 0:  # Check if the index of the current element is even
            even_index_sum.append(i)  # If the index is even, append the element to the even_index_sum list
        else:
            odd_index_sum.append(i)  # If the index is odd, append the element to the odd_index_sum list

    print(f"Even index sum: {sum(even_index_sum)}\nOdd index sum: {sum(odd_index_sum)}")  # Print the sum of the elements at even indices and odd indices

else:
    print('Cannot do this')  # If the length of the user_list is 1 or less, print 'Cannot do this'
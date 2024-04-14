my_dict = {'Math':81, 'Physics':83,'Chemistry':87}
print(list(sorted(my_dict.items(), key=lambda v: v[1], reverse= True))) 


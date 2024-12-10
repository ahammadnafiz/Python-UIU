list_1 = ["Black", "Red", "Maroon", "Yellow"]
list_2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

my_dict = dict(zip(list_1, list_2))
items = my_dict.items()

new_list = []

for key, value in items:
    new_dict = {}
    new_dict['color_name'] = key
    new_dict['color_code'] = value
    new_list.append(new_dict)

print(new_list)

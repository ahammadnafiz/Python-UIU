my_list = [{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}]

new_dict = {}

for d in my_list:
    item = d['item']
    amount = d['amount']
    
    if item in new_dict:
        new_dict[item] += amount
    else:
        new_dict[item] = amount

print(new_dict)
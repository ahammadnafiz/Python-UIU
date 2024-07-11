with open('demo.txt', 'r') as data:
    content = data.readlines()
    my_dict = {}
    for c in content:
        country, citys = c.strip().split()
        citys = citys.strip("[]").replace(" ", "").split(',')
        my_dict[country] = citys
        
with open('demo_copy.txt', 'w') as file:
    for k, v in my_dict.items():
        for i in v:
            file.write(f"{k:<10}{i}\n")
        
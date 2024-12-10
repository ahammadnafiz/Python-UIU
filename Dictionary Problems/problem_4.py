sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}

keys = ["age", "salary"]

new_dict = {}

for k in keys:
    new_dict[k] = sample_dict[k]

print(new_dict)
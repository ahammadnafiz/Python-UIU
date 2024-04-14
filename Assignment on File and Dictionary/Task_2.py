data = {}

with open('data.txt', 'r') as file:
    name_list = []
    Id_list = []
    email_list = []
    content = file.readlines()
    for line in content:
        name, Id, email = line.strip().split(',')
        name_list.append(name)
        Id_list.append(Id)
        email_list.append(email)
    data['name'] = name_list
    data['id'] = Id_list
    data['email'] = email_list

user_input = input().lower()

if 'email' in user_input and 'id' in user_input:
    email = data.get('email', [])
    Id = data.get('id', [])
    print([dict(zip(email, Id))])

elif 'name' in user_input and 'email' in user_input:
    name = data.get('name', [])
    email = data.get('email', [])
    print([dict(zip(name, email))])

elif '*' in user_input:
    with open('data.txt', 'r') as file:
        for line in file:
            print(line.strip())

elif 'name' in user_input:
    for n in data.get('name', []):
        print(n.strip())

elif 'email' in user_input:
    for n in data.get('email', []):
        print(n.strip())

elif 'id' in user_input:
    for n in data.get('id', []):
        print(n.strip())

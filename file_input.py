with open('demo.txt', 'r') as file:
    lines = file.readlines()
d_l = []
for line in lines:
    d = {}
    content = line.strip()[1:-1].split(',')
    for c in content:
        key, value = c.split(':')
        d[key.strip()] = value.strip()
    d_l.append(d)

for k in d_l:
    print(k)
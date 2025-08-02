'''
Line Reader Generator
'''

def read_lines(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line

for line in read_lines('data.txt'):
    print(line)

'''
Word Count Generator
'''

def word_count(filename):
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            yield len(words)

for count in word_count('data.txt'):
    print(count)

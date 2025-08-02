'''
Unique Words Generator
'''

def unique_words(filename):
    unique_word_set = set()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word not in unique_word_set:
                    unique_word_set.add(word)
                    yield word

for word in unique_words('data.txt'):
    print(word)

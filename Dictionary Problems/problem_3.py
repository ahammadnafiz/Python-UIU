string = input()

word_dict = {}
for s in string:
    if s in word_dict:
        word_dict[s] += 1
    else:
        word_dict[s] = 1

print(word_dict)
def element_frequency(lst):
    count = {}
    for e in lst:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1
    return count

print(element_frequency([2, 4, 4, 1, 1, 3, 9]))

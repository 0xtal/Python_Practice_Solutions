first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

inter = first_set.intersection(second_set)
print('Intersection is', inter)

for i in inter :
    first_set.discard(i)

print('After removing intersection', first_set)
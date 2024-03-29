COLLECTION = {1,2,2,2,2,3,4,5}
print(type(COLLECTION))  # Output: <class 'set'>


empty_set = set()

print(type(empty_set))  # Output: <class 'set'>
empty_set.add(1)

empty_set.discard(1)

# we cannot pass a list or dictionary as an element of a set

COLLECTION.pop()



# union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
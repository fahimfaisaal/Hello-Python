sets = {1, 2, 3, 4, 4, 5, 4, 3, 1, 2}

lists = [2, 3, 3, 5, 4, -1]
list_to_set = set(lists)

print(sets)
list_to_set.add(1)
list_to_set.add(10)

list_to_set.remove(10)
print(list_to_set)

# union set
print(sets | list_to_set)

# intersection set
print(sets & list_to_set)

# difference set
print(list_to_set - sets)
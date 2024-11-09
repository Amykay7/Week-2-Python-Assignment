
my_list = []  #an empty list

# Add all elements 
my_list.extend([10, 20, 30, 40])

print(my_list)


# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

print(my_list)


# Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])

print(my_list)


# Remove the last element
my_list.pop()

print(my_list)


# Sort the list in ascending order
my_list.sort()

print(my_list)


# Find and print the index of the value 30
index_of_30 = my_list.index(30)

print(index_of_30)

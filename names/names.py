import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# O(n**2) - 6.50 seconds to complete
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# O(n logn) average - 0.125 seconds to complete
# two iterations that perform logn time n times
# bst = BinarySearchTree(names_1[0])
# for name in names_1[1:]:
#     bst.insert(name)

# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# O() - 1.45 seconds
# list comprehensions are typically faster than two nested loops
# duplicates = [name for name in names_1 if name in names_2]

# O() - 0.005 seconds to complete on avg
duplicates = list(set(names_1) & set(names_2))

# O() - 0.005 seconds to complete on avg
# duplicates = set(names_1).intersection(set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
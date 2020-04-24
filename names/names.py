import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# original solution is O(n**2)
# approx 6 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# takes under 1.3 seconds
# O(n**2)
# duplicates = [name for name in names_1 if name in names_2]


# algorithm for binary searching a name from names_1 in binary tree sorted names_2
# O(n log(n)) ~ 0.115 seconds
# duplicates = []

# bst = BinarySearchTree(names_2[0])
# for name in names_2[1:]:
#   bst.insert(name)

# for name_1 in names_1:
#   if bst.contains(name_1):
#     duplicates.append(name_1)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# takes less than 0.005 of a second
names_1 = set(names_1) # O(len(names_1))
names_2 = set(names_2) # O(len(names_1))

# O(len(names_1) + len(names_2)) could go up to O(n) worst case
duplicates = names_1.intersection(names_2) 


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names

# assigning set to names_2
# names_2 = set(f.read().split("\n"))  # List containing 10000 names

# iterating over names in names_2.text and inserting them into a Binary Search Tree
names_2 = None
for name in f.read().split("\n"):  # List containing 10000 names
    if names_2 is not None:
        names_2.insert(name)
    else:
        names_2 = BSTNode(name)
f.close()


duplicates = []  # Return the list of duplicates in this data structure

# finding duplicates but locating intersections between the set and the list
# duplicates = names_2.intersection(names_1)  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Iterating over names_1 list and using BSTNode method contains to confirm if name_1 in names_1 array is found in names_2 BST
# If found then name_1 is appended to duplicates. 
# runtime: 0.1146857738494873 seconds
for name_1 in names_1:
        if names_2.contains(name_1):
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


for name in names_1:
    if name in names_2:
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

'''Trying out different things for Stretch below'''

# class BSTNode:  
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         # check if the value is less than the current node's value
#         if value < self.value:
#             # does the current node have a left child?
#             if self.left:
#                 self.left.insert(value)
#             # otherwise, it doesn't have a left child
#             # we can park the new node here
#             else:
#                 self.left = BSTNode(value)
#         # otherwise the value is greater or equal  to the current node's value
#         else:
#             # does the current node have a right child?
#             if self.right:
#                 # if it does, call the right child's `insert` method to repeat the process
#                 self.right.insert(value)
#             # otherwise, it doesn't have a right child
#             # we can park the new node here
#             else:
#                 self.right = BSTNode(value)

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target): # can implement using recursion
#         # pass
#         # check if the target value is less than the current node's value 
#         # if it is, we also want to know if the left child exists
#         if target < self.value and self.left is not None:
#             # use recursion to restart the cycle and check if the left child contains the value 
#             return self.left.contains(target)
#         # check if value is equal to the current node's value
#         elif target == self.value:
#             return True
#         # otherwise value is greater than current node
#         # so we want to check if there is a right child
#         elif self.right is not None:
#             # restart the process with recursion to check if the right child contains the target
#             return self.right.contains(target)
#         # otherwise, BST does NOT contain target
#         else:
#             return False

# bst = BSTNode("")
# for name in names_1:
#     bst.insert(name)

# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)


# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
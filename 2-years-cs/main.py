# Computer Science Basics

# Print statements
print("Hello World")

# Variables
x = 5
y = 0.5
z = 'hey'
a = True

# If statements
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# For/While
for i in range(3):
    print(i)

i = 0
while i < 3:
    print(i)
    i += 1

# Functions
def mul(x, y):
    return x * y

# Recursion
def mul(x, y):
    if y == 0:
        return 0
    return x + mul(x, y - 1)

# Object Oriented Programming
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
# Data Structures

# Array (List in Python)
arr = [5, 0.5, 'hey', True]

# Linked List
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Binary Search Tree
class BST:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Hash Table (Dictionary in Python)
hash = {'a':1, 'b':2, 'c':3}

# Algorithms

# Big-O Notation: O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!)

# Sorting Algorithms, below is selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

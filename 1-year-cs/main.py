#Print statements
print("Hello World")

#Variables
x = 1
y = 2.5
z = 'hi'
a = True

#If statements
if x > 1:
    print("x greater than 1")
else:
    print("x less than or equal to 1")

#For/While
for i in range(3):
    print(i)

i = 0
while i < 3:
    print(i)
    i += 1

#Functions
def mul(x, y):
    return x * y

#Recursion
def mul(x, y):
    if y == 1:
        return x
    # return x * mul(x, y - 1)
    # initially in my video, I messed up the above line
    return x + mul(x, y - 1)

#OOP
class Number:
    def __init__(self, number):
        self.number = number

    def get_num(self):
        return self.number
    
#Data Structures

#Array (Lists in Python)
new_arr = [1, 2.5, 'hi', True]

#Linked List
class LinkedList:
    # In my video, I did not use __init__, which is suppose to be the correct way
    # The below is OK though
    def init(self, value, next=None):
        self.value = value
        self.next = next

#Binary Search Tree
class BST:
    def init(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Hash Table
hash = {'a':1, 'b':2, 'c':3}

#Algorithms

#Big-O Notation: O(1), O(log(n)), O(n), O(nlog(n)), O(n^2), O(2^n), O(n!)

#Sorting Algorithms, Example below is selection sort
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # array[i] = array[min_index]
        # array[min_index] = array[i]
        # initially in my video, I messed up the above 2 lines
        array[i], array[min_index] = array[min_index], array[i]

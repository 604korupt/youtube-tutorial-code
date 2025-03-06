# List (mutable: can be changed after creation)
my_list = [1, "two", 3.0, True, None]

# Add items
my_list.append(4)
my_list.insert(1, "new")
my_list.extend([5, 6, 7])

# Remove items
my_list.remove("two")
my_list.pop() # removes last item
my_list.pop(2) # removes item at index 2
del my_list[0]

# Access an element
print(my_list[0])
print(my_list[-1]) # last element

# Dictionary
my_dict = {"super":"idol", "hello":"world"}

# Add a key-value pair
my_dict["new"] = "entry"

# Remove a key-value pair
my_dict.pop("hello")

# Access a value
print(my_dict["super"])

# Set
my_set = {1, 2, 3, 4, 5}
my_set2 = set([4, 5, 6, 7, 8])

# Add an element
my_set.add(6)

# Remove an element
my_set.remove(6)

# Access by iteration
for item in my_set:
    print(item)

# Tuple (immutable: cannot be changed after creation)
my_tuple = (1, 2, 3, 4, 5)
my_tuple2 = (1, )

# Access an element
print(my_tuple[0])
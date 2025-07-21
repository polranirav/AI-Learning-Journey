# Time complexity of Python built-in data structures

my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}
my_set = {1, 2, 3}

# List operations
my_list.append(4)      # O(1)
print(2 in my_list)    # O(n) search

# Dict operations
print(my_dict["a"])    # O(1) lookup
my_dict["c"] = 3       # O(1) insert

# Set operations
my_set.add(4)          # O(1)
print(2 in my_set)     # O(1) search
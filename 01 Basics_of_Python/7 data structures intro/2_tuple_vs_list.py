# Differences between tuple and list

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Lists are mutable
my_list[0] = 10
print("Modified list:", my_list)

# Tuples are immutable (uncommenting below will raise error)
# my_tuple[0] = 10

print("Tuple remains unchanged:", my_tuple)
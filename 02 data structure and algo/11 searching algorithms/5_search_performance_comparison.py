# Compare search performance of list vs set vs dict
# 🔸 Set and dict use hash tables → O(1) search
# 🔸 List is O(n)

import time

size = 1000000
target = 999999

big_list = list(range(size))
big_set = set(big_list)
big_dict = {i: True for i in big_list}

def timer(func, name):
    start = time.time()
    func()
    print(f"{name} → {round(time.time() - start, 6)}s")

timer(lambda: target in big_list, "List search")
timer(lambda: target in big_set, "Set search")
timer(lambda: target in big_dict, "Dict search")
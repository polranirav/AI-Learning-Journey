from collections import deque

# Maintain a sliding window of size 3

stream = [5, 10, 15, 20, 25, 30]
window = deque(maxlen=3)

for val in stream:
    window.append(val)
    print("Current window:", list(window))
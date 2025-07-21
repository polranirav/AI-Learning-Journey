import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="2x")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot")
plt.legend()
plt.grid(True)
plt.show()
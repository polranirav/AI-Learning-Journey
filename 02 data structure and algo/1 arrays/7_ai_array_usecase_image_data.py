import numpy as np

# Simulate a grayscale image (2D array)
img = np.array([[0, 255, 128], [34, 200, 90]])

print("Image array:\n", img)

# Normalize pixel values between 0 and 1
img_norm = img / 255.0
print("Normalized:\n", img_norm)

# Access pixel
print("Pixel at (1,2):", img[1, 2])
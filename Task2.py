import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load image in grayscale
image = cv2.imread("E:\Academic 7th Sem\Image_Processing\Assignment_1\Image_Processing\Image.jpg", cv2.IMREAD_GRAYSCALE)


# Show image
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()


def apply_spatial_average(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

# Test with different sizes
for size in [3, 10, 20]:
    blurred = apply_spatial_average(image, size)
    cv2.imwrite(f"Results/Task2/blurred_{size}x{size}.png", blurred)

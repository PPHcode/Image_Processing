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


def block_average(image, block_size):
    h, w = image.shape
    output = image.copy()
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = image[y:y+block_size, x:x+block_size]
            avg = int(np.mean(block))
            output[y:y+block_size, x:x+block_size] = avg
    return output

for size in [3, 5, 7]:
    block_avg = block_average(image, size)
    cv2.imwrite(f"Results/Task4/block_avg_{size}x{size}.png", block_avg)

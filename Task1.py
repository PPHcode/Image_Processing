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


#Task1
def reduce_intensity_levels(image, n_levels):
    factor = 256 // n_levels
    return (image // factor) * factor

# Example: reduce to 4 levels
reduced = reduce_intensity_levels(image, 4)
cv2.imwrite("Results/intensity_reduced_4_levels.png", reduced)






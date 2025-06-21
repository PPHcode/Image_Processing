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

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

for angle in [45, 90]:
    rotated = rotate_image(image, angle)
    cv2.imwrite(f"Results/Task3/rotated_{angle}_deg.png", rotated)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:55:45 2022

@author: claregarberg
"""

from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import random
from scipy import ndimage

root = "/Users/claregarberg/Documents/Graduate School/Summer 2022/Image Analytics/Project/Images"

os.chdir(root)

# PIL images
pil_image_list = []
for dir, subdirs, files in os.walk("."):
    for i, f in enumerate(files):
        if f == ".DS_Store":
            continue
        else:
            location = str(root + "/" + dir +  "/" + f)
            im=Image.open(location)
            pil_image_list.append(im)


# converting to numpy arrays for opencv
cv2_image_list = []
for item in pil_image_list:
    pil_image = item.convert('RGB') 
    open_cv_image = np.array(pil_image) 
    cv2_image_list.append(open_cv_image)

# selecting a rendom image
ran_img = random.choice(cv2_image_list)

plt.imshow(ran_img)

ran_img2 = random.choice(cv2_image_list)

plt.imshow(ran_img2)

# preprocessing steps

# converting to grayscale
ran_img_gray = cv2.cvtColor(ran_img2, cv2.COLOR_RGB2GRAY)

plt.imshow(ran_img_gray, cmap = "gray")

# resizing
k = 2
width = int((ran_img_gray.shape[1])/k)
height = int((ran_img_gray.shape[0])/k)

ran_img_resize = cv2.resize(ran_img_gray, (width, height), interpolation=cv2.INTER_AREA)
print(ran_img_resize.shape)

plt.imshow(ran_img_resize, cmap = "gray")

# normalization
norm_image = (ran_img_resize - np.min(ran_img_resize)) / (np.max(ran_img_resize) - np.min(ran_img_resize))
plt.imshow(norm_image, cmap = "gray")

# brightness increase
ran_image_bright = cv2.convertScaleAbs(norm_image, alpha=1, beta=0)
plt.imshow(ran_image_bright, cmap = "gray")

# laplacian gaussian transform
ran_img_transform = cv2.GaussianBlur(ran_image_bright,(5,5),0)
plt.imshow(ran_img_transform, cmap = "gray")

# flipped and rotated image
ran_img_flip = cv2.rotate(ran_img_transform, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
ran_img_flip = cv2.flip(ran_img_flip, 1)


# plotting
f, axes = plt.subplots(nrows = 3, ncols = 2, figsize=(12, 12))
axes[0, 0].imshow(ran_img2)
axes[0, 0].set_title('1. Original')
axes[0, 1].imshow(ran_img_resize, cmap = "gray")
axes[0, 1].set_title('2. Grayscale/Resized Image')
axes[1, 0].imshow(norm_image, cmap = "gray")
axes[1, 0].set_title('3. Normalized Image')
axes[1, 1].imshow(ran_image_bright, cmap = "gray")
axes[1, 1].set_title('4. Normalized/Bright Image')
axes[2, 0].imshow(ran_img_transform, cmap = "gray")
axes[2, 0].set_title('5. Gaussian Transformed Image')
axes[2, 1].imshow(ran_img_flip, cmap = "gray")
axes[2, 1].set_title('6. Flipped/Rotated Image')





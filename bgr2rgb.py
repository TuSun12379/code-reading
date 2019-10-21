import numpy as np
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('paper.jpg', 1)
im = im[...,::-1] # 将BGR图像转换成RGB
plt.imshow(im, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 用于隐藏坐标
plt.show()
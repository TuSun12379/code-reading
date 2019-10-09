import numpy as np
from PIL import Image
from pylab import *
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = np.array(Image.open("image340.tif"))
# print(img)
img_filter = ndi.gaussian_filter(img, sigma=1)
# print(img_filter)
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.imshow(img)
ax2.imshow(img_filter)
plt.show()

from matplotlib import pyplot as plt
from matplotlib.image import imread

img = imread('images/lena-gray.png')

plt.imshow(img)
plt.show()
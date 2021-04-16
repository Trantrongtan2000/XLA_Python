import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

foo = Image.open("test.jpg")

#print(foo.size)

foo = foo.resize((480,240),Image.ANTIALIAS)
foo.save("image_scaled.jpg",optimize=True,quality=95)


im = imageio.imread('test.jpg')
im2 = imageio.imread('image_scaled.jpg')
fig, ax = plt.subplots(2, 1, figsize=(15, 10))

ax[0].imshow(im);
ax[1].imshow(im2);
plt.show()
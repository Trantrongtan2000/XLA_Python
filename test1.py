import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

foo = Image.open("test.jpg")


x, y = foo.size
x2, y2 = math.floor(x/4), math.floor(y/4)
#print(foo.size)

foo = foo.resize((x2,y2),Image.ANTIALIAS)
foo.save("image_scaled.jpg",optimize=True,quality=95)


im = imageio.imread('test.jpg')
im2 = imageio.imread('image_scaled.jpg')
fig, ax = plt.subplots(2, 1, figsize=(15, 10))

ax[0].imshow(im);
ax[0].set_title('Ảnh gốc')
#ax[0].axis('off');
ax[1].imshow(im2);
ax[1].set_title('Ảnh giảm kích thước')
#ax[1].axis('off');
plt.show()
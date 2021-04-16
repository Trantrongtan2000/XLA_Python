from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('test.jpg')

newsize = (200, 500)

im1 = im.resize(newsize,quality=95)

fig, ax = plt.subplots(1, 2, figsize=(15, 10))

ax[0].imshow(im);
ax[1].imshow(im1);
plt.show()
import imageio
import matplotlib.pyplot as plt
import numpy as np
im = imageio.imread('chest-221.dcm')


#plt.imshow(im, cmap='gray')
#plt.axis('off')
#plt.show()

fig, ax = plt.subplots(1, 3, figsize=(15, 10))
# Draw the image in grayscale
ax[0].imshow(im, cmap='gray');

# Draw the image with greater contrast
ax[1].imshow(im, cmap='gray', vmin=-200, vmax=200);

# Remove axis ticks and labels
ax[2].imshow(im, cmap='gray', vmin=-200, vmax=200);
ax[2].axis('off');
plt.show()
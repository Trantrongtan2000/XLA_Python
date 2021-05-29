import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

img = nib.load('ds107_sub001_highres.nii')
data = img.get_data()
plt.imshow(data[:, :, 0], cmap='gray')
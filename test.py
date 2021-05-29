import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import skimage
import nibabel as nib
import mcubes

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

img = nib.load('ds107_sub001_highres.nii')

#data = np.asanyarray(img.dataobj)
data= img.get_fdata()

#plt.imshow(data[:, :, 30], cmap='gray')

#data_1d = data.ravel()
#plt.hist(data_1d, bins=100)
#plt.show()

subvolume = data[90:-90, 90:-90, 10:130]
pct_99 = np.percentile(subvolume, 99)
binarized_subvolume = subvolume > pct_99

def binarized_surface(binary_array):
    verts, faces= mcubes.marching_cubes(binary_array, 0)
    fig = plt.figure(figsize=(10, 12))
    ax = fig.add_subplot(111, projection='3d')
    mesh = Poly3DCollection(verts[faces], linewidths=0, alpha=0.5)
    ax.add_collection3d(mesh)
    ax.set_xlim(0, binary_array.shape[0])
    ax.set_ylim(0, binary_array.shape[1])
    ax.set_zlim(0, binary_array.shape[2])
    
#plt.imshow(binarized_subvolume[:, :, 20], cmap='gray')
binarized_surface(binarized_subvolume)
plt.show()

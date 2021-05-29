import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

img = nib.load('ds107_sub001_highres.nii')
data= img.get_fdata()
while True:
    nhap=int(input('\nNhập lớp muốn xem: '))
    if nhap >= 0 and nhap <192:
        break
    else:
        print("\nMời nhập lại giá trị từ 0 tới 191") 

a=data[nhap, :, :]
b=data[:, nhap, :]
c=data[:, :, nhap]
fig, ax = plt.subplots(1, 3, figsize=(15, 10))

ax[0].imshow(a,cmap='gray');
ax[0].set_title('Mặt nhìn từ bên hông')
ax[1].imshow(b,cmap='gray');
ax[1].set_title('Mặt nhìn từ trước tới')
ax[2].imshow(c,cmap='gray');
ax[2].set_title('Mặt nhìn từ trên xuống')
plt.show()
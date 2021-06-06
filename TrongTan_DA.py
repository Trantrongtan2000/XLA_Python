import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math
 
img = Image.open("lung-cancer.png")
 
#print(img.size)
a=int(input("Nhập tỉ lệ muốn giảm:\n"))
 
x, y = img.size
x2, y2 = math.floor(x/a), math.floor(y/a)
 

img = img.resize((x2,y2),Image.ANTIALIAS)

img.save("image_scaled.png",optimize=True,quality=95)
  
im = imageio.imread('lung-cancer.png')
im2 = imageio.imread('image_scaled.png')
fig, ax = plt.subplots(2, 1, figsize=(15, 10))
 
ax[0].imshow(im);
ax[0].set_title('Ảnh gốc')
ax[1].imshow(im2);
ax[1].set_title('Ảnh giảm kích thước '+str(a)+" lần so với ảnh gốc")
plt.show()
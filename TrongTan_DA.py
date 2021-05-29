import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math
 
foo = Image.open("test.jpg")
 
#print(foo.size)
a=int(input("Nhập tỉ lệ muốn giảm:\n"))
 
x, y = foo.size
x2, y2 = math.floor(x*a), math.floor(y*a)
 
foo = foo.rpen cv shape
esize((x2,y2),Image.ANTIALIAS)
foo.save("image_scaled.jpg",optimize=True,quality=95)
  
im = imageio.imread('test.jpg')
im2 = imageio.imread('image_scaled.jpg')
fig, ax = plt.subplots(2, 1, figsize=(15, 10))
 
ax[0].imshow(im);
ax[0].set_title('Ảnh gốc')
ax[1].imshow(im2);
ax[1].set_title('Ảnh giảm kích thước '+str(a)+" lần so với ảnh gốc")
plt.show()
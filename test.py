from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('test.jpg')

plt.imshow(im)
plt.show()
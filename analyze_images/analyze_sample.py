import numpy as np
from PIL import Image


image = Image.open('../testcases/input/input08.jpg')
im_arr = np.sum(np.array(image), axis=-1) / (255*3)

print(im_arr)
print(np.histogram(im_arr, bins=10))
im_arr = (np.sign(im_arr - 0.3) + 1) / 2
print(im_arr)
im = Image.fromarray(np.uint8((im_arr)*255))
im.save('test.jpg')
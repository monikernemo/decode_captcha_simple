import numpy as np
from PIL import Image

class image_loader(object):
    def __init__(self):
        return

    def load_image(self, im_path):
        try:
            image_arr = np.array(Image.open(im_path))
            image_arr = np.sum(image_arr, axis = -1)/(255 * 3)
            return self.increase_contrast(image_arr)
        except :
            raise 'Unable to open image'

    def increase_contrast(self, image_arr, threshold = 0.5):
        return (np.sign(image_arr - 0.5) + 1) / 2
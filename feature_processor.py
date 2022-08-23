import image_loader
import numpy as np

class feature_processor(object):
    def __init__(self, num_letters = 5, height = 10, width = 8):
        self.num_letters = num_letters
        self.row_offset = 11
        self.column_offset = 5
        self.height = height
        self.width = width


    # segment letters
    def segment_letter(self, im_arr):
        return [[(self.row_offset, self.row_offset + self.height), \
                    (self.column_offset + i * (self.width + 1), self.column_offset + i * (self.width + 1) + self.width)] for i in range(self.num_letters)]
        




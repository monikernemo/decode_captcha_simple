from feature_processor import feature_processor
from image_loader import image_loader
from os import listdir, mkdir
from os.path import isfile, join
import pickle
import numpy as np
from PIL import Image

class knn_model(object):
    def __init__(self):
        self.fp = feature_processor()
        self.loader = image_loader()
        self.char_array_dict = {}

    def load_model(self, save_model_path = 'model_assets', fn = 'knn_dict', save_diagnostic_im = False):
        try:
            model_file = open(join(save_model_path, fn), 'rb')
            self.char_array_dict = pickle.load(model_file)
            model_file.close()
            if save_diagnostic_im:
                for c in self.char_array_dict:
                    im = Image.fromarray(np.uint8((self.char_array_dict[c])*255))
                    im.save(f'letter_{c}.jpg')
        except:
            raise 'unable to load model_file'

    def fit_model(self, train_data_path = 'testcases/input', output_path = 'testcases/output', save_im = False):
        train_images = sorted([join(train_data_path, f) for f in listdir(train_data_path) if '.jpg' in f])
        test_phrases = sorted([join(output_path, f) for f in listdir(output_path)])
        temp_char_arr_dict = {}
        for im, phrase in zip(train_images, test_phrases):
            im_arr = self.loader.load_image(im)
            f = open(phrase, 'r')
            captcha_phrase = f.read().strip('\n')
            f.close()
            coords = self.fp.segment_letter(im_arr)
            for c, coord in zip(captcha_phrase,coords):
                x1, x2 = coord[0][0], coord[0][1]
                y1, y2 = coord[1][0], coord[1][1]
                letter_arr = im_arr[x1:x2, y1:y2]
                if c in temp_char_arr_dict:
                    temp_char_arr_dict[c].append(letter_arr)
                else:
                    temp_char_arr_dict[c] = [letter_arr]
        
        for c, arrs in temp_char_arr_dict.items():
            self.char_array_dict[c] = np.array(arrs).mean(axis = 0)
            if save_im:
                im = Image.fromarray(np.uint8((self.char_array_dict[c])*255))
                im.save(f'letter_{c}.jpg')
    
    def infer_captcha(self, image_path):
        im_arr = self.loader.load_image(image_path)
        coords = self.fp.segment_letter(im_arr)
        solution = ''
        for coord in coords:
            x1, x2 = coord[0][0], coord[0][1]
            y1, y2 = coord[1][0], coord[1][1]
            letter_arr = im_arr[x1:x2, y1:y2]
            char = self.infer_char(letter_arr)
            solution += char
        return solution

    def infer_char(self, letter_arr):
        guess = None
        min_dist = -1
        for c, arr in self.char_array_dict.items():
            dist = np.max(np.abs(arr - letter_arr))
            if min_dist == -1 or dist < min_dist:
                guess = c 
                min_dist = dist
        return guess

    def save_model(self, save_model_path = 'model_assets', fn = 'knn_dict'):
        s = pickle.dumps(self.char_array_dict)
        model_file = open(join(save_model_path, fn), 'wb')
        pickle.dump(self.char_array_dict, model_file)
        model_file.close()

def main():
    model = knn_model()
    model.fit_model(save_im = False)
    model.save_model() 
    model1 = knn_model()
    model1.load_model(save_diagnostic_im = True)

    train_data_path = 'testcases/input'
    output_path = 'testcases/output'
    train_images = sorted([join(train_data_path, f) for f in listdir(train_data_path) if '.jpg' in f])
    test_phrases = sorted([join(output_path, f) for f in listdir(output_path)])
    incorrect_test_cases = []
    for im, phrase in zip(train_images, test_phrases):
        inferred = model1.infer_captcha(im)
        f = open(phrase, 'r')
        captcha_phrase = f.read().strip('\n')
        f.close()
        if inferred != captcha_phrase:
            incorrect_test_cases.append(im)
    print(f'number of incorrectly inferred test cases are {len(incorrect_test_cases)}')

if __name__ ==  "__main__":
    main()

            
            





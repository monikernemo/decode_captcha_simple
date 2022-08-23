from knn_model import knn_model

'''
Strategy: 
For ease of calculation we normalize 0-255 to floats 0-1. 
Remove noise by letting slightly pixels with sum > 0.5 go to 1 (sum up all RGB coordinates), otherwise set them to 0.

Since characters are evenly space, an easy data exploration reviews that each space is 1 pixel wide, 
each character is 7 pixel wide, characters starts from  5-th pixel from the left (if zero index).

Height-wise, characters start from 11-th pixel from the top; height of characters are 9 pixels tall, so 63 pixels per char.

Each captcha, first segment into characters, and compare to dictionary of characters we have for each character encountered in sample data.
Find closest match in terms of L1 - distance. (in theory should choose other metrics such as Frobenius norm so less sensitive to noise, 
but since data is not too complicated, we tentatively use L1 norm). 

After matching all characters, return captcha phrase by concatenating all characters.
'''
class Captcha(object):
    def __init__(self):
        self.model = knn_model()
        self.model.load_model()

    def __call__(self, im_path, save_path):
        '''
        Algo for inference
        args:
            im_path: .jpg image path to load and to infer
            save_path: output file path to save the one-line outcome
        '''
        inferred = self.model.infer_captcha(im_path)
        f = open(save_path, 'w')
        f.write(inferred)
        f.close()




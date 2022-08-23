from knn_model import knn_model

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




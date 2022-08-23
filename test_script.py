from captcha import Captcha

def main():
    c = Captcha()
    c('testcases/input/input100.jpg', 'testoutput.txt')

if __name__ == "__main__":
    main()
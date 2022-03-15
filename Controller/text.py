from PIL import Image
from pytesseract import pytesseract


class __EXTRACT__():
    def __init__(self, __PATHIMAGE__):
        self.__PATHIMAGE__ =  __PATHIMAGE__

    # pytesseract.tesseract_cmd = path_pytesseract
    def get_image(self, image):
        image_text = pytesseract.image_to_string(Image.open(f'{self.__PATHIMAGE__}{image}'))
        return image_text

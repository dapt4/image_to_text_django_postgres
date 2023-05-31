import pytesseract
from PIL import Image
from requests import get
from shutil import copyfileobj


def image_to_text(path):
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    return text


def get_img(url, file_name):
    res = get(url, stream=True)
    path = 'static/' + file_name
    if res.status_code == 200:
        with open(path, 'wb') as f:
            copyfileobj(res.raw, f)
            text = image_to_text(path)
            return text



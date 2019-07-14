import tesserocr
from PIL import Image

image = Image.open('D:\\pythonSpider\\captcha\\images\\image.png')
result = tesserocr.image_to_text(image)
image = image.convert('1')
image.show()
import tesserocr
from PIL import Image

image = Image.open('D:/pythonSpider/seleniumFrame/images/image1.png')
result = tesserocr.image_to_text(image)
print(result)
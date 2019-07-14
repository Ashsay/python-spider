#codding:utf-8
import tesserocr
from PIL import Image
image = Image.open('D:\\py-django\\resource\\img\\image.png')
print(tesserocr.image_to_text(image))

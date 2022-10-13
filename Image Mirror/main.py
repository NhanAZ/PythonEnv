from email.mime import image
from PIL import Image

Image.open('origin.png')

img = Image.open('origin.png')
mirrorImage = img.transpose(Image.FLIP_LEFT_RIGHT)
mirrorImage.save(r'mirroredImage.png')
Image.open('mirroredImage.png')
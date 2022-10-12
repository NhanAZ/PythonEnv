import pyqrcode

from pyqrcode import QRCode

string = input('Enter your string: ')

url = pyqrcode.create(string)

url.svg('QR.svg', scale=8)

url.png('QR.png', scale=6)

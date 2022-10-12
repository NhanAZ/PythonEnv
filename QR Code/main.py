import pyqrcode

from pyqrcode import QRCode

string = "https://github.com"

url = pyqrcode.create(string)

url.svg("myqr.svg", scale=8)

url.png("myqr.png", scale=6)

import pyqrcode

from pyqrcode import QRCode

string = "https://github.com"

url = pyqrcode.create(string)

url.svg("myQR.svg", scale=8)

url.png("myQR.png", scale=6)

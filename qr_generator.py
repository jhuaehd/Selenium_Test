import pyqrcode

qrcode = pyqrcode.create('https://www.qrcode-monkey.com/')

qrcode.svg('default-preview-qr.svg', scale = 7)
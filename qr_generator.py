import pyqrcode

qrcode = pyqrcode.create('https://www.qrcode-monkey.com/')

qrcode.svg('qrcode-monkey.svg', scale=7)
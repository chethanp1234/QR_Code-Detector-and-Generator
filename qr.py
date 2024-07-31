# initially install pyqrcode and pypng

import pyqrcode
import png
from pyqrcode import QRCode

link = "www.google.com"
url = pyqrcode.create(link)
url.png("google.png",scale=10)



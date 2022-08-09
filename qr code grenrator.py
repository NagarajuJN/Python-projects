from codecs import backslashreplace_errors
from dataclasses import dataclass
import qrcode


# data = "https://drive.google.com/file/d/1aDZsn4ByWjIOTqLWdFtWZk16yRLvJ-6t/view?usp=sharing"
data = " Hi Nagaraj ! How r u ?? "
data = "https://www.linkedin.com/in/nagaraju-j-n-719249208/"
# qr = qrcode.QRCode(version=1,box_size=20,border=5)

img = qrcode.make(data)

# qr.make(fit=True)

# img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save("C:/Users/KITS/Documents/python mini projects/qr code/myq rcode.png " )  
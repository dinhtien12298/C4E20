from gmail import *
from random import choice
import datetime

now = datetime.datetime.now()

html_content ="""
<p style="text-align: center;"><strong>Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</strong></p>
<p style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<p style="text-align: center;">&nbsp;</p>
<h1 style="text-align: center;"><span style="color: #000000;"><strong>ĐƠN XIN BỎ HỌC</strong></span></h1>
<p>&nbsp;</p>
<p style="text-align: left;">Hi broooo.</p>
<p style="text-align: left;">Em viết đơn n&agrave;y xin thầy cho bỏ học v&igrave; {{reason}}</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Thankkk nha ^^</p>
"""

reasons = [
    "ốm",
    "đau",
    "bệnh",
    "tật",
    "gái gú"
]

loop = True
count = now.day
while loop:

    reason = choice(reasons)
    gmail = GMail('tiennguyendinh.1998@gmail.com','neverhate')
    msg = Message('Đơn xin bỏ học',to='dinhtiennguyen.1202@gmail.com', html= html_content.replace("{{reason}}", reason))

    if now.hour > 7 and count == now.day:
        gmail.send(msg)
        count += 1
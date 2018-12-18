from gmail import *
from random import choice

# from gmail import GMail, Message

html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<h1 style="text-align: center;"><strong>ĐƠN XIN BỎ HỌC</strong></h1>
<p>Em ch&agrave;o thầy, t&ecirc;n em l&agrave; Nguyễn Đ&igrave;nh Tiến</p>
<p>H&ocirc;m nay em viết mail n&agrave;y để xin thầy nghỉ học vì {{sickness}} <img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>C&oacute; g&igrave; thầy gửi em phong b&igrave; sau cũng được ạ</p>
<p>&nbsp;</p>
<p>Em cảm ơn!</p>
<p>Đ&igrave;nh Tiến</p>
"""

reason = [
    'ốm',
    'yếu',
    'bệnh',
    'tật',
    'chán',
    'thua cá độ'
]
reason1 = choice(reason)
html_content1 = html_content.replace("{{sickness}}", reason1 )

gmail = GMail('tiennguyendinh.1998@gmail.com','neverhate')
msg = Message('Hello',to='20130075@student.hust.edu.vn',html=html_content1)
gmail.send(msg)

from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import pyexcel

# 1. Download web page
url = 'http://dantri.com.vn'
# 1.1 Create function
# conn = urlopen(url)
# 1.2 Read
# data = conn.read()
# 1.3 Decode
# html_content = data.decode('utf-8')
# print(html_content)
html_content = urlopen('http://dantri.com.vn/').read().decode('utf-8')
# 1.4 Save html to file  
# Way1 urllib.request.urlretrieve('http://dantri.com.vn', 'dantri.html')
# f = open('dantri.html','wb') # Way2
# f.write(html_content) # Way2
# f.close() # Way2


# 2. Extract ROI (Region Of Interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, 'html.parser')
# find by class
ul = soup.find('ul','ul1 ulnew')
# print(ul.prettify())

# 3. Extract date
li_list = ul.find_all('li')
data = []
for li in li_list:
    post = {}
    a = li.h4.a
    # print(a.string)
    # print(url + a['href'])
    # print('* '*30)
    post['title'] = a.string
    post['url'] = url + a['href']

    data.append(post)

pyexcel.save_as(records=data, dest_file_name="data_dantri.xls")



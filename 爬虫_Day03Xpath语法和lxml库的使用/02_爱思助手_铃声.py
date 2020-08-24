
import requests
from lxml import etree
as_url = 'https://www.i4.cn/ring_3_0_1.html'
data_html = requests.get(as_url)
data = data_html.text
# print(data)
data_all = etree.HTML(data)
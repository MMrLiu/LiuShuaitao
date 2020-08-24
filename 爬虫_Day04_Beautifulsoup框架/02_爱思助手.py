
# [1]导入第三方包
import requests
from bs4 import BeautifulSoup
# [2]目标网址
as_url = 'https://www.i4.cn/ring_3_0_1.html'
# [3]进行网络数据请求
reqs_01 = requests.get(as_url);
# [4]数据的读取
data = reqs_01.content
# data = reqs_01.text
# print("测试内容输出：",data.decode('utf-8'))
# ==============
# [1]创建soup对象
soup = BeautifulSoup(data,'html.parser')
# [2]分析网页结构 - 找到需要查询的数据特征
div_tag_list = soup.find_all("div",attrs={'class':"list ring_list"})
print("查询到的的数据：",len(div_tag_list))
print(div_tag_list)
# [3]通过遍历for循环形式进行查询
for i in range(0,len(div_tag_list)):
    print("第%d首音乐-----------------"%i)
    item_div_mp3 = div_tag_list[i]
    # 音乐名称：
    mp3_name = item_div_mp3.find('div',attrs={'class':"title"}).string
    print("音乐名称：",mp3_name)
    # 音乐时长
    mp3_time = item_div_mp3.find('div',attrs={'class':'longtime'}).string
    print("音乐时长：", mp3_time)
    # 音乐地址
    mp3_addurl = item_div_mp3.find('div',attrs={"class":'btn audio_play'})['data-mp3']
    print('音乐地址：',mp3_addurl)
    # 下载到本地：requests下载到本地
    pass
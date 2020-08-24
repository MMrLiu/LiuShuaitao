
# [1]导入数据解析的包 - beautifulsoup
from bs4 import BeautifulSoup
# [2]读取本地待测试的数据
file = open("./测试.html",'r',1)
data = file.read()
file.close()
print("数据为：",data)
# ======使用beautifulsoup的使用===================
# [3]创建一个soup对象
soup = BeautifulSoup(data,'html.parser')
print("soup对象类型：",type(soup))
# [3.1]根据标签名称获取对于数据
# 只能获取第一个符合条件的标签
"""
Tag , NavigableString , BeautifulSoup , Comment .
"""
img_tag = soup.img
print("img_tag对象类型：",type(img_tag))
print("[3.1==]",img_tag)
#[3.2]tag类型对象获取对于属性的值
img_url = img_tag['src']
print("[3.2==]",img_url)
# [3.3]获取所有img标签的内容 -并获取对应的图片
# find_all返回值是一个数组-
img_tags = soup.find_all('img')
print("[3.3]==",len(img_tags),img_tags)
print("第二个img标签为：",img_tags[1])
#[3.4]通过添加条件-进行数据筛选
# attrs表示一个字典结构 - 可以添加多个字典的筛选条件 同样find_all也可以添加筛选条件
# find的返回值是一个对象 -
img_g_tag = soup.find('img',attrs={'class':'g_01'})
print('[3.4]==',img_g_tag['src'])
# [3.5]==遍历 - 结构分析
# None 如果找不到的情况下返回值为None
ul_tag = soup.find("ul",attrs={'class':'info-present'})
print('[3.5]==',ul_tag)
# 在ul_tag中查询所有的li
li_tag_list = ul_tag.find_all('li')
print('li_tag = ',li_tag_list)
# [3.6]获取标签中的内容 :.string
for i in range(0,len(li_tag_list)):
    print("第%d条数据："%i,li_tag_list[i].string)
    # parser会把父节点中包含的任意阶段都进行输出
    print("当前标签的父节点:",li_tag_list[i].parent)
    pass
# find函数 也支持正则表达式的筛选条件
import re
a_tag = soup.find(re.compile(r'>.*<'))
# [3.7]find函数可以值添加keyword(条件形式)值进行筛选
div_tag = soup.find(id='01')
print('[3.7==]',div_tag)



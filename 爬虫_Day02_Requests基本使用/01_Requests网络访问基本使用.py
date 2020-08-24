""""""
#[1]下载requests
"""
pip install requests
# 临时使用豆瓣镜像安装
pip3 install -i https://pypi.doubanio.com/simple/ requests
"""
# [2]导入第三方包
import requests
# [3]目标网址
as_url = 'https://www.i4.cn/ring_3_0_1.html'
# [4]常规用法- get请求 -访问网络
resq_01 = requests.get(url=as_url)
# [5]获取网络状态码
print('当前GET请求状态码：',resq_01.status_code)
# [6]获取一下网络数据内容
# 返回值是bytes型 二进制形式的数据
data = resq_01.content
# print(data.decode('utf-8'))
# 返回值Unicode编码进行返回 - 文本类型
str_data = resq_01.text
# print(str_data)
# [7]获取cookies值
print("当前请求的cookies值：",resq_01.cookies)
# [8]Get请求的形式
# 使用一个测试网址
cs_get_url = 'http://httpbin.org/get?'
data_other = {"username":'liushuaitao','password':'123456'}
resq_02 = requests.get(url=cs_get_url,params=data_other)
# [9]查看请求的地址
print("当前Get请求地址：",resq_02.url)
# [10]获取get请求内容
print(resq_02.text)

# [11]POST请求
cs_post_url = 'http://httpbin.org/post?'
resq_03 = requests.post(url=cs_post_url,data=data_other)
# 当前post请求地址
print("POST请求地址：",resq_03.url)
# 获取数据
print(resq_03.text)






# [1]导入包
import requests
"""
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
"""
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
# [2]测试网址
as_url = 'https://www.i4.cn/ring_3_0_1.html'
# [3]网络访问
resq_01 = requests.get(url=as_url,headers=header);
print("网络访问的请求码：",resq_01.status_code)
# [4]使用代理IP进行网络请求
# 获取代理IP
# 183.166.97.51 9999  175.42.123.48 9999
# 创建一个字典
proxies = {'https://':'183.166.97.51:9999'}
resq_02 = requests.get(url=as_url,proxies=proxies,headers=header)
print("使用代理IP进行请求：",resq_02.status_code)



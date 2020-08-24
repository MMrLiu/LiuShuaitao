import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request,urllib.parse
# [1]模拟浏览器进行数据请求
"""
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
"""
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# [2]目标网址
as_url='https://www.i4.cn/wper_3_0_0_1.html'
# [3]参数请求配置
req = urllib.request.Request(url=as_url,headers=header,method='GET',data=None)
# [4]网络访问
resq = urllib.request.urlopen(req)
print("当前网址数据为：",resq.read().decode('utf-8'))
# [5]获取网址的请求状态码
print("当前网址的请求状态码：",resq.code,resq.status)
# [6]设置网址请求超时
resq = urllib.request.urlopen(req,timeout=0.1)
# [7]获取请求数据的应用头信息
print(resq.getheaders())
# 带cookie默认账号密码登录
# 包含多条信息的求情头
header = {'Cookie':'AGL_USER_ID=fdcd044b-7e62-499a-b8d2-228ee5ea06f4;',
          "host":'www.i4.cn',
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}





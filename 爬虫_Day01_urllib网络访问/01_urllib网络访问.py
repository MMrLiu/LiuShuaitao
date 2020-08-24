#conding=utf-8
# python2.X时候 需要导入 urllib,urllib3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# [1]urllib包的导入
import urllib.request
# [2]目标网址
as_url = 'https://www.i4.cn/wper_3_0_0_1.html'
# [3]网络访问
resp = urllib.request.urlopen(as_url)
# [4]读取网络信息
data = resp.read()
# [5]输出到控制台
print(data)
# [6]把二进制的数据转换为utf-8
print(data.decode('utf-8'))
# [7]把数据存储到本地
file = open('爱思助手-笔笔直爬取.html','wb',1)
file.write(data)
file.close()
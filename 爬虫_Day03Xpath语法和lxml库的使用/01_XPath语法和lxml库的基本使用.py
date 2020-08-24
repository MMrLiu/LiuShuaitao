"""
XPath 本身是一个xml路径语言 主要作用：查找xml格式文件中提取信息的一门语言
# 类似于针对xml的正则表达
"""
# [1]下载lxml
# 命令下载：pip3 install lxml
# [2]lxml引入
import lxml
# 使用xPath语法需要用到etree模块
from lxml import etree
# lxml.etree 也可以这么使用
# [3]读取本地文件 - 之前学过open方式打开一个文件
# 3.1读取文本变量xml格式数据
data_html = '''
<header class="header">
		<a href="https://www.i4.cn/" title="爱思助手" class="logo"><img src="https://d-image.i4.cn/i4web/static2017/img/head_logo.png" width="164" height="46" alt="爱思助手"/></a>
		<nav>
			<a href="https://www.i4.cn/" title="首页" id="nav_index">首页</a>
			<a href="https://www.i4.cn/pros.html" title="产品中心" id="nav_pros">产品中心</a>
			<a href="https://www.i4.cn/firmware.html" title="固件" id="nav_ipsw">固件</a>
			<a href="https://www.i4.cn/app_3_1_1_0_1.html" title="资源" id="nav_res">资源</a>
			<a href="https://www.i4.cn/news_3.html" title="教程" id="nav_tutorial">教程</a>
			<a href="https://www.i4.cn/news_1.html" title="新闻" id="nav_article">新闻</a>
			<a href="https://developer.i4.cn" target="_blank" title="千锋教育">开发者平台</a>
		</nav>
		<div class="search">
			<form method="get" action="https://www.i4.cn/index_search.action">
				<div class="selectdown" name="search_select">
					<div class="arrows"></div>
					<div class="title">教程</div>
					<div class="options">
						<div class="list" data-value="3">教程</div>
						<div class="list" data-value="4">资讯</div>
						<div class="list" data-value="1">应用</div>
					</div>
					<input type="hidden" name="type" value="3" />
				</div>
				<input type="hidden" name="model" value="1" />
				<input type="text" name="k" id="textfield">
				<a href="javascript:;" title="搜索">搜索</a>
			</form>
		</div>
	</header>
'''
# 开始读取文件使用xpath
data_all = etree.HTML(data_html)
# print(data)
# 3.2读取文件正文数据
# tostring方法：以bytes形式进行输出
# 遇到中文数据：需要tostring中添加 encoding编码
data_content = etree.tostring(data_all,encoding='utf-8')
print("读取数据内容：\n",data_content.decode('utf-8'))
# 注释
"""
1.一般爬虫需要从网页获取数据 - 得到一个变量用于存储文本数据
"""
# 3.3读取本地一个文件：
# etree.parse 可以把一个不规范的html文件数据进行自动修正
# parser=etree.HTMLParser()
data = etree.parse(source='练习.html',parser=etree.HTMLParser())
data_html = etree.tostring(data,encoding="utf-8")
print("读取本地文件数据：\n",data_html)
# ============开始Xpath语法学习=====================
print('============开始Xpath语法学习====================')
# [1] //从当前节点获取所有的节点
# 1.1创建一个xpath语法
all_xpath = '//*'
all_data = data_all.xpath(all_xpath)
# 得到一个数组的格式
print('[1]--',all_data)
# [2]根据节点名称（根据标签名称获取所有子节点）
a_data = data_all.xpath('//a')
print('[2]--',a_data)
print('[2]查询到到a标签：',len(a_data))
# [3]想要查看标签内容 tosring形式进行查看
# 解决单挑语句中文乱码问题
a_data = etree.tostring(a_data[1],encoding='utf-8',pretty_print=True, method="html")
print(a_data.decode('utf-8'))
# 创建方法 - 标签文件转数据控制台输出
def bq_sj_show(element_data): #data element标签
    data = etree.tostring(element_data, encoding='utf-8', pretty_print=True, method="html")
    return data.decode('utf-8')
    pass
# [4] / 从当前节点选区直接子节点
res_01 = data_all.xpath('//nav/a')
print('[4]--',res_01)
# 通过for循环形式进行输出
for i in range(0,len(res_01)):
    data = bq_sj_show(res_01[i])
    print('[4]--(%d)数据：'%i,data)
    pass
# [5]@ 选择属性
res_01 = data_all.xpath('//nav/a/@target')
print('[5]--',res_01)
# [6]根据@数据添加条件查询内容 @target="_blank"
res_01 = data_all.xpath('//nav/a[@target="_blank"]')
print('[6]--',res_01)
print('[6]==',bq_sj_show(res_01[0]))
# [7].. 选取当前节点的父节点 a标签的父节点nav
res_01 = data_all.xpath('//nav/a[@target="_blank"]/..')
print('[7]--',res_01)
# print('[7]==',bq_sj_show(res_01[0]))
# [8]在xpath语法中添加下标
res_01 = data_all.xpath('//nav/a[7]')
print('[8]--',res_01)
print('[8]==',bq_sj_show(res_01[0]))
# [9]获取标签中的文本信息text()
res_01 = data_all.xpath('//nav/a/text()')
print('[9]--',res_01)
res_01 = data_all.xpath('//nav/a[7]/text()')
print('[9]--',res_01)
res_01 = data_all.xpath('//nav/a[7]/@title')
print('[0]--',res_01)
# [10]根据运算符使用查询
res_01 = data_all.xpath('//nav/a[@title="教程" or @title="新闻"]')
print('[10]--',bq_sj_show(res_01[0]),bq_sj_show(res_01[1]))
# [11] 运算符号
res_01 = data_all.xpath('//nav/a[last()-2]')
print('[11]--',res_01)
print('[11]--',bq_sj_show(res_01[0]))
# [12]其他运算
res_01 = data_all.xpath('//nav/a[position()!=3]')
print('[12]--',len(res_01),res_01)
print('[12]--',bq_sj_show(res_01[0]))

# 通过方法形式获取对于xml数据
# [13]ancestor 获取当前标签的所有父节点 也可以添加条件
res_01 = data_all.xpath('//nav/a[7]//ancestor::body')
print('[13]--',len(res_01),res_01)
print('[13]--',bq_sj_show(res_01[0]))
# [14]attribute
# 选取当前节点的所有属性。 也可以添加条件
res_01 = data_all.xpath('//nav/a[7]//attribute::title')
print('[14]--',len(res_01),res_01)
# [15]child
# 选取当前节点的所有子元素。
res_01 = data_all.xpath('//nav/child::*')
print('[15]--',len(res_01),res_01)
# [16]parent
# 选取当前节点的所有子元素。
res_01 = data_all.xpath('//nav/a[7]/parent::*')
print('[15]--',len(res_01),res_01)









# 导入包
from selenium import webdriver
import time
# 设置当前谷歌浏览器不进行界面渲染
from selenium.webdriver.chrome.options import Options
# 创建一个配置
option = Options();
option.headless = True # 无界面
# [1]调用谷歌驱动 - 带界面 - 效率低
driver = webdriver.Chrome(options=option)
# [2]请求一个网站
driver.get('https://www.i4.cn/')

# # 通过其他属性获取元素-标签中name对象的名称
# input_01 = driver.find_element_by_name('k').send_keys("火影")
# #通过特定的文字获取对应
# t_01 = driver.find_element_by_link_text('搜索').click()
# # 通过标签名称
# title_01 = driver.find_element_by_tag_name('meta')
# print("通过标签名称",title_01.get_attribute('charset'))
# 通过类选择器
# a_t01= driver.find_element_by_css_selector('#logo')
# print(a_t01)
# 通过层次进行绝对路径选择
# 如果遇到相同的标签名称 - 下表索引从1开始
a_01 = driver.find_element_by_css_selector('body>div.header_wrap>header>nav>a:nth-child(7)')
print(a_01.text)
# 鼠标的操作
# 双击
# 滑动
# 鼠标的一些坐标定位
# 跟xpath向结合
# 如果针对与一些比较登录爬虫 - 可以使用selenium进行登录 -
# 也可以通过拷贝带有登录信息的cookies值进行数据访问
a_02 = driver.find_element_by_xpath('//a[@target="_blank"]').text
print(a_02)
driver.quit()















time.sleep(5)
# [4]关闭浏览器
driver.quit()


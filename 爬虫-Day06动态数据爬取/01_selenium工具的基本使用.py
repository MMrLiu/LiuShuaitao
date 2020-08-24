
# [1]导入包
from selenium import webdriver
import time
# [2]创建phantomjs对象 - 无界面浏览器
# driver = webdriver.PhantomJS();
# [警告]warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
# [7]使用谷歌驱动进行网页访问
# 前提 - 一定要把谷歌驱动放到电脑的系统变量中
# 调用本电脑上的浏览器 - 带界面渲染
driver = webdriver.Chrome()
# [3]尝试请求一个网站
driver.get('https://www.i4.cn/')
# [4]进行页面保存
driver.save_screenshot("aisi.png")
# [6] 预留一个时间
time.sleep(5)
# 获取登录状态后的值然后进行获取通过requests加入cookies进行访问

cook = driver.get_cookies()
file = open("cc.json",'w',1)
file.write(cook)
file.close()
# [5]退出驱动
driver.quit()

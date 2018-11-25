#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains 
from selenium.common.exceptions import TimeoutException, NoSuchElementException


########################### 基本使用 ############################################
browser = webdriver.Chrome()

try:
	browser.get("https://www.baidu.com")
	input = browser.find_element_by_id('kw')
	input.send_keys('Python')
	# from selenium.webdriver.common.keys import Keys
	input.send_keys(Keys.ENTER)
	
	# from selenium.webdriver.support.wait import WebDriverWait
	wait = WebDriverWait(browser, 10)
	# from selenium.webdriver.support import expected_conditions as EC
	# from selenium.webdriver.common.by import By
	wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

	print(r'========================================================')
	print(browser.current_url)
	print(r'========================================================')
	print(browser.get_cookies())
	print(r'========================================================')
	print(browser.page_source)
finally:
	browser.close()
############################ 声明浏览器对象###########################
browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()
############################## 访问页面 ##############################
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
print(browser.page_source)
browser.close()
############################ 查找元素 ####################################
# 单个元素
# find_element(By., '')
# find_element_by_name('')
# find_element_by_css_selector()
# find_element_by_xpath('')
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_tag_name()
# find_element_by_class_name()
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_fourth = browser.find_element(By.ID, 'q')
print(input_first)
print(input_second)
print(input_third)
print(input_fourth)
browser.close()

#========================================================
# 多个元素
# find_elements(By., '')
# find_elements_by_name()
# find_elements_by_css_selector()
# find_elements_by_xpath()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_tag_name()
# find_elements_by_class_name()
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
lis_first = browser.find_elements_by_css_selector('.service-bd li')
lis_second = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis_first)
print(lis_second)
browser.close()
############################## 元素交互操作##########################################
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(10)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
browser.close()

# 交互动作
browser = webdriver.Chrome()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
browser.close()
############################### 执行JavaScript ##########################
browser = webdriver.Chrome()
browser.get("http://zhihu.com/explore")
browser.execute_script('window.scroll(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
browser.close()
################################ 获取元素信息 #############################

browser = webdriver.Chrome()

# 获取属性
url = "https://www.zhihu.com/explore"
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

# 获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

# 获取ID，位置，标签名，大小
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

browser.close()
################################### Frame #################################
browser = webdriver.Chrome()

url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
source = browser.find_element_by_css_selector('#draggable')
print(source)

try:
	logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
	print('NO LOGO')

browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

browser.close()
####################################### 等待 #####################################
browser = webdriver.Chrome()

# 隐式等待
browser.implicitly_wait(10)
url = "https://www.zhihu.com/explore"
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)

# 显式等待
browser.get("https://www.taobao.com/")
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)



####################################### 前进后退 ###################################
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
browser.get("https://taobao.com/")
browser.get("https://zhihu.com/")
browser.back()
time.sleep(1)
browser.forward()
browser.close()

#################################### Cookies ###################################

browser = webdriver.Chrome()

browser.get("https://www.zhihu.com/explore")
print(browser.get_cookies())

browser.add_cookie({
	'name':'name',
	'domain':'www.zhihu.com',
	'value':'germey'
	})
print(browser.get_cookies())

browser.delete_all_cookies()
print(browser.get_cookies())

browser.close()


######################################## 选项卡管理 #####################################
browser = webdriver.Chrome()

browser.get("http://www.baidu.com")

browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.taobao.com")

time.sleep(1)

browser.switch_to_window(browser.window_handles[0])
browser.get("https://www.python.org")
######################################## 异常处理 ################################
browser = webdriver.Chrome()

browser.get("https://www.baidu.com")
browser.find_element_by_id('hello')

try:
	browser.get("http://www.baidu.com")
	browser.find_element_by_id('hello')
except TimeoutException:
	print('Time Out')
except NoSuchElementException:
	print('No Element')
finally:
	browser.close()
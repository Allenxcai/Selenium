from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time as t
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\Firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('selenium')
t.sleep(3)
driver.find_element_by_link_text(u'新闻').click()
driver.quit()
print(dir(list))
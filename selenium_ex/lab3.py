#!/usr/bin/env python
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(
#     executable_path='/Users/xpop/128G/xPy/network_pro_bootC/lab2/geckodriver')
# driver.get("https://192.168.2.245/")
# elem = driver.find_element_by_name("q")
# print(elem)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# now Firefox will run in a virtual display.
# you will not see the browser.
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities['acceptSslCerts'] = False
browser = webdriver.Firefox(
    executable_path='/Users/xpop/128G/xPy/network_pro_bootC/lab2/geckodriver', capabilities=capabilities)
browser.get('http://192.168.2.245/login')
#body = browser.find_element_by_tag_name('html').text

username = browser.find_element_by_name('username')
username.send_keys('admin')

password = browser.find_element_by_name('secretkey')
password.send_keys('1234')

browser.find_element_by_name("login_button").click()
time.sleep(2)

# print(body)
# print(browser.title)
# browser.quit()

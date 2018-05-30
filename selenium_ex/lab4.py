#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

host = "https://192.168.2.245"

# Optional argument, if not specified will search path.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

browser = webdriver.Chrome(
    '/Users/xpop/128G/xPy/network_pro_bootC/lab2/chromedriver', chrome_options=options)
browser.maximize_window()
wait = WebDriverWait(browser, 30)
browser.get('%s/login' % host)
# browser.implicitly_wait(30)


username = browser.find_element_by_name('username')
username.send_keys('admin')

password = browser.find_element_by_name('secretkey')
password.send_keys('1234')
browser.find_element_by_name("login_button").click()


for x in range(10):
    # browser.switch_to_default_content()
    browser.get('%s/ng/firewall/address' % host)
    # print(browser.current_url)

    # print(browser.page_source)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="navbar-view-section"]/div/f-address-list/div/div[1]/f-address-list-menu/div[1]/div[1]/button/div/span[1]')))
    browser.find_element_by_xpath(
        '//*[@id="navbar-view-section"]/div/f-address-list/div/div[1]/f-address-list-menu/div[1]/div[1]/button/div/span[1]').click()

    wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[8]/div[1]/button/div')))
    browser.find_element_by_xpath(
        '/html/body/div[8]/div[1]/button/div').click()
    browser.switch_to_default_content()
    wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, 'iframe')))
    browser.switch_to_frame(browser.find_element_by_tag_name(
        'iframe'))
    wait.until(EC.presence_of_element_located(
        (By.ID, 'name')))
    ip_name = browser.find_element_by_name('name')
    ip_name.send_keys('itg_%s' % x)

    ipmask = browser.find_element_by_name('ipmask')
    ipmask.send_keys('192.168.100.1%s/32' % x)
    browser.find_element_by_id('submit_ok').click()
    # browser.switch_to_default_content()
    time.sleep(2)


browser.switch_to_default_content()
# iframe

# <iframe name="embedded-iframe" ng-class="{'loading': embeddedIframe.loading}" class=""></iframe>
# f = open('test.html', 'w')
# f.write(browser.page_source)
# f.close
# name_data = browser.find_element_by_xpath('//*[@id="name"]').text


# //*[@id="name"]
# time.sleep(.5)

# browser
# time.sleep(5)  # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)  # Let the user actually see something!
browser.quit()

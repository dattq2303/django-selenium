import csv
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/accounts/login/')


# dang nhap
browser.find_element_by_id(
    "id_login-username").send_keys('nguyenhthieu@gmail.com')
# browser.find_element_by_id(
#     "id_login-password").send_keys('123456')
# browser.implicitly_wait(5)
# browser.find_element_by_name("login_submit").click()
# browser.implicitly_wait(5)

# # chon hang
# browser.find_element_by_xpath('//*[@title="submit"][2]').click()

# thanh toan

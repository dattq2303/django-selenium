import csv
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/catalogue/')

browser.implicitly_wait(5)

search = ["art", "code", "cherry"]
# dky tk moi
for x in search:
    browser.find_element_by_id(
        "id_q").send_keys(x)
    browser.implicitly_wait(5)
    browser.find_element_by_xpath("//input[@value='Search']").click()
    browser.find_element_by_id(
        "id_q").clear()

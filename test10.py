import csv
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/catalogue/')

browser.implicitly_wait(5)

# dky tk moi
browser.find_element_by_xpath('//*[@title="Hacking Exposed Wireless"]').click()

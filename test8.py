import csv
import time
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

passwordCol = 10
emailCol = 9

with open('us-500.csv') as csvDataFile:
    data = list(csv.reader(csvDataFile))
n = random.randint(1, 500)

print(n)
randomEmail = data[n][emailCol]
randomPassword = data[n][passwordCol]

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/accounts/')

try:
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "login_link")))
    browser.get('https://latest.oscarcommerce.com/en-gb/accounts/login/')
    # r day eo hieu sao k click dc cai nut' kia
    browser.find_element_by_id(
        "id_login-username").send_keys(randomEmail)
    browser.find_element_by_id(
        "id_login-password").send_keys(randomPassword)
    browser.find_element_by_xpath(
        "//button[contains(text(), 'Log In')]").click()
except Exception as e:
    print(str(e))

search = ["art", "code", "cherry"]
for x in search:
    browser.find_element_by_id(
        "id_q").send_keys(x)
    browser.implicitly_wait(5)
    browser.find_element_by_xpath("//input[@value='Search']").click()
    browser.find_element_by_id(
        "id_q").clear()

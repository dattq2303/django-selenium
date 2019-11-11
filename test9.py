import csv
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/accounts/login/')


# dang nhap
browser.find_element_by_id(
    "id_login-username").send_keys('dattq12@gmail.com')
browser.find_element_by_id(
    "id_login-password").send_keys('5654577qa')
browser.implicitly_wait(5)
browser.find_element_by_name("login_submit").click()
browser.implicitly_wait(5)

# chon hang


try:
    wait = WebDriverWait(browser, 60)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Add to basket')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Add to basket')]"[3]))).click()
except Exception as e:
    print(str(e))

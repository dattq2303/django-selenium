from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import csv
import time
import random
browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/accounts/login/')

emailCol = 9
passwordCol = 10

with open('us-500.csv') as csvDataFile:
    data = list(csv.reader(csvDataFile))
n = random.randint(1, 500)

print(n)
randomEmail = data[n][emailCol]
randomPassword = data[n][passwordCol]

# dky tk moi
i = browser.find_element_by_id("id_registration-email")
i.send_keys(randomEmail)
browser.find_element_by_id(
    "id_registration-password1").send_keys(randomPassword)

browser.find_element_by_id(
    "id_registration-password2").send_keys(randomPassword)
browser.find_element_by_name("registration_submit").click()

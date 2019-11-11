from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import csv
import time
browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/accounts/login/')

generated_email = "users{}@gmail.com".format(time.time())
generated_password = "5654577qa"

# dky tk moi
i = browser.find_element_by_id("id_registration-email")
i.send_keys(generated_email)
browser.find_element_by_id(
    "id_registration-password1").send_keys(generated_password)

browser.find_element_by_id(
    "id_registration-password2").send_keys(generated_password)
browser.find_element_by_name("registration_submit").click()

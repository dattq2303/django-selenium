import csv
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

vn_country = [
    "An Giang Province",
    "Ba Ria-Vung Tau Province",
    "Yen Bai Province"
]

first_name = [
    "Dat",
    "Hoang",
    "Hieu",
    "Duong",
    "Giang"
]

last_name = [
    "Nguyen Hoang",
    "Pham Viet",
    "Tran Thi"
]

first_line_address = [
    "9 Ton That Tung",
    "224 Tran Duy Hung",
    "78 Giai Phong"
]

second_line_address = [
    "Thanh Xuan",
    "Hoan Kiem"
]

city = [
    "Ha Noi",
    "TP HCM",
    "Da Nang"
]

postcode = [
    "117082",
    "154000",
    "115500"
]

phone_number = [
    "01786545768",
    "01698453783",
    "09187439575"
]

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
firstName = first_name[random.randrange(0, len(first_name))]
lastName = last_name[random.randrange(0, len(last_name))]
address1 = first_line_address[random.randrange(0, len(first_line_address))]
address2 = second_line_address[random.randrange(0, len(second_line_address))]
randomCity = city[random.randrange(0, len(city))]
randomPostCode = postcode[random.randrange(0, len(postcode))]

try:
    wait = WebDriverWait(browser, 60)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Add to basket')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Checkout now')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_first_name"))).send_keys(firstName)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_last_name"))).send_keys(lastName)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_line1"))).send_keys(address1)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_line2"))).send_keys(address2)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_line4"))).send_keys(randomCity)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_postcode"))).send_keys(randomPostCode)
    select = Select(browser.find_element_by_id("id_country"))
    select.select_by_visible_text('Viet Nam')
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Continue')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.ID, "view_preview"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Place order')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Continue shopping')]"))).click()
except Exception as e:
    print(str(e))

# thanh toan

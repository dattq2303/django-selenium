import csv
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

firstNameCol = 0
lastNameCol = 1
addressCol = 2
cityCol = 3
countyCol = 4
stateCol = 5
postcodeCol = 6
phoneCol = 7
emailCol = 9
passwordCol = 10

with open('us-500.csv') as csvDataFile:
    data = list(csv.reader(csvDataFile))
n = random.randint(1, 500)

print(n)
randomEmail = data[n][emailCol]
randomPassword = data[n][passwordCol]
randomFirstName = data[n][firstNameCol]
randomLastName = data[n][lastNameCol]
randomAddress = data[n][addressCol]
randomCity = data[n][cityCol]
randomCounty = data[n][countyCol]
randomState = data[n][stateCol]
randomPostCode = data[n][postcodeCol]
randomPhone = data[n][phoneCol]

print(randomFirstName, randomLastName)

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/accounts/login/')


# dang nhap
browser.find_element_by_id(
    "id_login-username").send_keys(randomEmail)
browser.find_element_by_id(
    "id_login-password").send_keys(randomPassword)
browser.implicitly_wait(5)
# browser.find_element_by_id(
#     "id_login-username").send_keys("dattq12@gmail.com")
# browser.find_element_by_id(
#     "id_login-password").send_keys("5654577qa")
# browser.implicitly_wait(5)
browser.find_element_by_name("login_submit").click()
browser.implicitly_wait(5)

# chon hang
try:
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Add to basket')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Checkout now')]"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_first_name"))).send_keys(randomFirstName)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_last_name"))).send_keys(randomLastName)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_line1"))).send_keys(randomAddress)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_line4"))).send_keys(randomCity)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_state"))).send_keys(randomState)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "id_postcode"))).send_keys(randomPostCode)
    select = Select(browser.find_element_by_id("id_country"))
    select.select_by_visible_text('United States')
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

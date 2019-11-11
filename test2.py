import csv
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://latest.oscarcommerce.com/en-gb/catalogue/')

browser.find_element_by_link_text("Login or register").click()
browser.implicitly_wait(2)

with open('users.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)
        browser.find_element_by_link_text("Login or register").click()
        browser.find_element_by_id(
            "id_login-username").send_keys(row[0])
        browser.implicitly_wait(5)
        browser.find_element_by_id(
            "id_login-password").send_keys(row[1])
        browser.implicitly_wait(5)
        browser.find_element_by_name("login_submit").click()
        browser.implicitly_wait(5)

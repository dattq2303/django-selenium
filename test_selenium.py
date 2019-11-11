import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.python.org")
driver.get("http://localhost:8000")
# self.assertIn("Python", driver.title)
with open('/home/nguyenhieu/Downloads/MOCK_DATA.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            driver.find_element_by_link_text("Login or register").click()
            driver.implicitly_wait(2)
            driver.find_element_by_id("id_registration-email").send_keys(row[0])
            driver.implicitly_wait(2)   
            driver.find_element_by_id ("id_registration-password1").send_keys(row[1])
            driver.implicitly_wait(2)
            driver.find_element_by_id ("id_registration-password2").send_keys(row[1])
            driver.implicitly_wait(2)
            # driver.find_element_by_name("login_submit").click()
            # driver.implicitly_wait(2)
            driver.find_element_by_name("registration_submit").click()
            driver.implicitly_wait(2)
            driver.find_element_by_link_text("Logout").click()
# driver.find_element_by_link_text("Login or register").click()
# driver.implicitly_wait(2)
# driver.find_element_by_id("id_login-username").send_keys("nguyenhthieu@gmail.com")
# driver.implicitly_wait(2)
# driver.find_element_by_id ("id_login-password").send_keys("123456")
# driver.implicitly_wait(2)
# driver.find_element_by_name("login_submit").click()
driver.close()

# if __name__ == "__main__":
#     unittest.main()
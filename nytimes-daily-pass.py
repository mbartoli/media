from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

user = sys.argv[1]
password = sys.argv[2]
driver = webdriver.Firefox()
driver.get("https://myaccount.nytimes.com/auth/login?URI=http://")
elem_user = driver.find_element_by_name("userid")
elem_user.send_keys(user)
elem_pass = driver.find_element_by_name("password")
elem_pass.send_keys(password)
elem_submit = driver.find_element_by_id("js-login-submit-button")
elem_submit.send_keys(Keys.RETURN)
time.sleep(2)
driver.get("http://www.nytimes.com/passes")
time.sleep(4)
driver.close()

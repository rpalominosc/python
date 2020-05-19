from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# If you want to open Firefox
driver = webdriver.Firefox()
search_url=f'http://www.bncatalogo.gob.cl/F/47N7BU53G7VL6926PPST6K2H7X6VSSMEP565CD3692B7LKUXSB-21587?func=file&file_name=login'
print (search_url)
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("YourUsername")
password.send_keys("YourPassword")
driver.find_element_by_id("submit_btn").click()

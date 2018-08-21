from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#surfacebook and work computer webdriver path
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
driver.set_window_size(1900, 1900)
driver.set_window_position(0, 0)
driver.get('https://mail.google.com/mail/u/0/#inbox')

time.sleep(5)
page_body = driver.find_element_by_tag_name('body')

loginField = driver.find_element_by_id('identifierId')
nextButton = driver.find_element_by_id('identifierNext')
loginField.send_keys('user name')
nextButton.click()
time.sleep(3)

passwordField = driver.find_element_by_name('password')
passwordField.send_keys('pass word')
nextButton = driver.find_element_by_id('passwordNext')
nextButton.click()

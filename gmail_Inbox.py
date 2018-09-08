#import schedule
import time
import datetime
import re
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from bs4 import BeautifulSoup as bs


#surfacebook and work computer webdriver path
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
driver.set_window_size(1900, 1900)
driver.set_window_position(0, 0)
driver.get('https://mail.google.com/mail/u/0/#inbox')

time.sleep(5)
page_body = driver.find_element_by_tag_name('body')

loginField = driver.find_element_by_id('identifierId')
nextButton = driver.find_element_by_id('identifierNext')
loginField.send_keys('eventhandler808')
nextButton.click()
time.sleep(3)

passwordField = driver.find_element_by_name('password')
passwordField.send_keys('Eventdriven2018!')
nextButton = driver.find_element_by_id('passwordNext')
nextButton.click()

idList = []

time.sleep(5)
html = driver.page_source

soup = bs(html, 'lxml')

table = soup.findAll('table')[3]
for row in table.findAll('tr'):
     idList.append(str(row.get('id')))

emailRow = driver.find_element_by_xpath('//*[@id="' + idList[0] + '"]')

emailRow.click()


#len(idList)



#tr = table.find('tr', attrs={'draggable':'true'})
#baft = driver.find_element_by_xpath('//*[@id=":35"]')
#time.sleep(3)

#tr.click()

#count all tr in table
#click tr



##for row in table.findAll('tr'):
##     for elem in row.findAll():
##          if elem.has_attr('email'):
##               print(elem)
##               elem.click()



##print all tr in table
##table = soup.findAll('table')[3]
##for row in table.findAll('tr'):
##     print(row)
##     print("\n")

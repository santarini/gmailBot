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
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : r'C:\Users\santa\Desktop\bana'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe', chrome_options=chrome_options)
driver.set_window_size(1900, 1900)
driver.set_window_position(0, 0)
driver.get('https://mail.google.com/mail/u/0/#inbox')


time.sleep(5)

#login to gmail

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

#identify email ids in inbox

idList = []

time.sleep(5)
html = driver.page_source

soup = bs(html, 'lxml')

table = soup.findAll('table')[3]
for row in table.findAll('tr'):
     idList.append(str(row.get('id')))

emailRow = driver.find_element_by_xpath('//*[@id="' + idList[0] + '"]')

emailRow.click()

time.sleep(1)

#identify email body

html = driver.page_source
page_body = driver.find_element_by_tag_name('body')
soup = bs(html, 'lxml')
emailContent = soup.findAll('table', {'role': 'presentation'})

#find sender
 
for row in emailContent:
     for line in row.findAll():
          if line.has_attr('email'):
               print(line)

#find subject

for row in emailContent:
     for line in row.findAll('h2'):
          print(line)




#download attachment
for row in soup.findAll():
     if row.has_attr('download_url'):
          attachment = row
          aTag = attachment.findAll('a')[0]
          driver.execute_script("window.open('"+ aTag.get('href') +"');")
          
##          aTag = attachment.findAll('a')[0]
##          print(aTag.get('href'))



#find label button
page_body = driver.find_element_by_tag_name('body')
##page_body.send_keys('v')
##
###navigate to pertinent
##pertinent = soup.findAll('div', {'title': 'Pertinent'})
##
###navigate to nonpertinent
##nonPertinent = soup.findAll('div', {'title': 'NonPertinent'})

#pertinent.click()
#nonPertinent.click()

          
#find email text
#emailText = soup.findAll('div', {'dir': 'ltr'})





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

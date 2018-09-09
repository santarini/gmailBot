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
actionChains = ActionChains(driver)
time.sleep(5)

#login to gmail

page_body = driver.find_element_by_tag_name('body')
loginField = driver.find_element_by_id('identifierId')
nextButton = driver.find_element_by_id('identifierNext')
loginField.send_keys('username')
nextButton.click()

time.sleep(3)

passwordField = driver.find_element_by_name('password')
passwordField.send_keys('password')
nextButton = driver.find_element_by_id('passwordNext')
nextButton.click()


def inboxScan(driver):
     #identify email ids in inbox
     idList = []
     time.sleep(5)
     html = driver.page_source
     soup = bs(html, 'lxml')
     table = soup.findAll('table')[3]
     for row in table.findAll('tr'):
          idList.append(str(row.get('id')))

     #perform scan for each email in inbox

     i = 0
     while i < len(idList):
          emailRow = driver.find_element_by_xpath('//*[@id="' + idList[i] + '"]')
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
                         if not(line.get('email') == "*******@gmail.com"):
                              sender = line

          #find subject
          for row in emailContent:
               for line in row.findAll('h2'):
                    subject = line

          #check if subject.text contains "Receipt" and if sender.get('email') is from "********@gmail.com"
          if "Receipt:" in subject.text and "****************@gmail.com" in sender.get('email'):

               #get file name from subject
               emailSubject = subject.text
               fileName = emailSubject.split(":")[1]
               fileName = fileName.strip()

               #download and name attachment to folder
               elementR = driver.find_element_by_xpath("//a[@role='link']")
               actionChains.move_to_element(elementR)
               actionChains.context_click(elementR).perform()
               pyautogui.typewrite(['down','down','down','down','enter'])
               time.sleep(5)
               pyautogui.typewrite(r"C:\Users\santa\Desktop\bana\{}.txt".format(fileName))
               pyautogui.typewrite(['enter'])
               time.sleep(2)
                         
               #label pertinent
               page_body = driver.find_element_by_tag_name('body')
               page_body.send_keys('v')
               time.sleep(1)
               driver.find_element_by_xpath("//div[@title='Pertinent']").click()
          else:
               #label nonpertinent
               page_body = driver.find_element_by_tag_name('body')
               page_body.send_keys('v')
               time.sleep(1)
               driver.find_element_by_xpath("//div[@title='NonPertinent']").click()
          time.sleep(2)
          i +=1

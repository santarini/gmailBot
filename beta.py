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
import os
import img2pdf
import schedule


#surfacebook and work computer webdriver path
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : r'C:\Users\m4k04\Desktop\gmailBot'}
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
loginField.send_keys('user')
nextButton.click()

time.sleep(3)

passwordField = driver.find_element_by_name('password')
passwordField.send_keys('pass')
nextButton = driver.find_element_by_id('passwordNext')
nextButton.click()

def inboxScan(driver):
     #refresh
     driver.refresh()
     
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
          time.sleep(2)
          
          #identify email body for bs4
          html = driver.page_source
          page_body = driver.find_element_by_tag_name('body')
          soup = bs(html, 'lxml')
          emailContent = soup.findAll('table', {'role': 'presentation'})

          #find sender
          for row in emailContent:
               for line in row.findAll():
                    if line.has_attr('email'):
                         if not(line.get('email') == "*****@gmail.com"):
                              sender = line

          #find subject
          for row in emailContent:
               for line in row.findAll('h2'):
                    subject = line

          #check if subject.text contains "Receipt" and if sender.get('email') is from "*****@gmail.com"
          validEmails = ["*****@gmail.com", "*****@mms.att.net", "*****@dawson8a.com"]
          if "Receipt:" in subject.text and any(x in sender.get('email') for x in validEmails):

               #get file name from subject
               emailSubject = subject.text
               fileName = emailSubject.split(":")[1]
               fileName = fileName.strip()

               #LOCATE  and download and name attachment to path
               time.sleep(1)
               page_body = driver.find_element_by_tag_name('body')
               page_body.send_keys(Keys.TAB)
               page_body.send_keys(Keys.TAB)
               page_body.send_keys(Keys.TAB)
               page_body.send_keys(Keys.TAB)
               page_body.send_keys(Keys.TAB)
               page_body.send_keys(Keys.TAB)
               page_body.send_keys(Keys.TAB)
               time.sleep(2)
               actionChains.send_keys(Keys.SHIFT + Keys.F10).perform()
               pyautogui.typewrite(['down','down','down','down', 'enter'])
               time.sleep(5)
               pyautogui.typewrite(r"C:\Users\m4k04\Desktop\gmailBot\{}.jpg".format(fileName))
               pyautogui.typewrite(['enter'])
               time.sleep(2)
                         
               #label pertinent
               page_body = driver.find_element_by_tag_name('body')
               time.sleep(1)
               page_body.send_keys('v')
               time.sleep(2)
               driver.find_element_by_xpath("//div[@title='Pertinent']").click()

          elif "Generate Report" in subject.text and any(x in sender.get('email') for x in validEmails):
               #generate report
               with open("report.pdf","wb") as f:
                   f.write(img2pdf.convert([i for i in os.listdir(r'C:/Users/m4k04/Desktop/gmailBot') if i.endswith(".jpg")]))

               #create reply
               page_body.send_keys('r')
               time.sleep(3)

               attachButton = driver.find_element_by_xpath('//*[@data-tooltip = "Attach files"]')
               attachButton.click()

               time.sleep(3)

               pyautogui.typewrite(r"C:\Users\m4k04\Desktop\gmailBot\report.pdf")
               pyautogui.typewrite(['enter'])

               time.sleep(3)

               sendButton = driver.find_element_by_xpath('//*[@data-tooltip="Send ‪(Ctrl-Enter)‬"]')
               sendButton.click()

               time.sleep(3)
               
               #label pertinent
               page_body = driver.find_element_by_tag_name('body')
               time.sleep(1)
               page_body.send_keys('v')
               time.sleep(2)
               driver.find_element_by_xpath("//div[@title='Pertinent']").click()

                              
          else:
               #label nonpertinent
               page_body = driver.find_element_by_tag_name('body')
               time.sleep(1)
               page_body.send_keys('v')
               time.sleep(2)
               driver.find_element_by_xpath("//div[@title='NonPertinent']").click()

          time.sleep(2)
          i +=1
     timeNow = datetime.datetime.now().strftime("%H:%M:%S")
     print("Gmail Scanned at: " + str(timeNow))

     

schedule.every(5).minutes.do(inboxScan, driver=driver)
#schedule.every().hour.do(inboxScan(driver))

#schedule.every().day.at("10:30").do(inboxScan(driver))


while True:
     schedule.run_pending()

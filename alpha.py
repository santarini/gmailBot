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

def initalizeGmailReceiptBot():
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
     loginField.send_keys('gmailuser')
     nextButton.click()

     time.sleep(3)

     passwordField = driver.find_element_by_name('password')
     passwordField.send_keys('gmailpassword!')
     nextButton = driver.find_element_by_id('passwordNext')
     nextButton.click()

def inboxScan():
     #identify email ids in inbox
     idList = []

     time.sleep(5)
     html = driver.page_source

     soup = bs(html, 'lxml')

     table = soup.findAll('table')[3]
     for row in table.findAll('tr'):
          idList.append(str(row.get('id')))

     i = 0
     while i < len(idList):
          time.sleep(3)
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
                         if not(line.get('email') == "******@gmail.com"):
                              sender = line

          #find subject

          for row in emailContent:
               for line in row.findAll('h2'):
                    subject = line

          #check if sender.get('email') is from "******@gmail.com"

          #check if subject.text contains "Receipt"
          if "Receipt" in subject.text and "*******@gmail.com" in sender.get('email'):
               #download attachment
               for row in soup.findAll():
                    if row.has_attr('download_url'):
                         attachment = row
                         aTag = attachment.findAll('a')[0]
                         driver.execute_script("window.open('"+ aTag.get('href') +"');")
                         time.sleep(2)
               #label pertinent
               page_body = driver.find_element_by_tag_name('body')
               page_body.send_keys('vPertinent' + Keys.ENTER)
     ##          html = driver.page_source
     ##          page_body = driver.find_element_by_tag_name('body')
     ##          soup = bs(html, 'lxml')
     ##          time.sleep(1)
     ##          labelMenu = soup.findAll('div', {'role': 'menu'})[4]
     ##          labelInput = labelMenu.find('input', {'type': 'text'})
     ##          labelInput.send_keys('Pertinent/n')
               #pertinent.click()
          else:
               #label nonpertinent
               page_body = driver.find_element_by_tag_name('body')
               page_body.send_keys('vNonPertinent' + Keys.ENTER)
     ##          page_body.send_keys('v')
     ##          html = driver.page_source
     ##          page_body = driver.find_element_by_tag_name('body')
     ##          soup = bs(html, 'lxml')
     ##          time.sleep(1)
     ##          labelMenu = soup.findAll('div', {'role': 'menu'})[4]
     ##          labelInput = labelMenu.find('input', {'type': 'text'})
     ##          labelInput.send_keys('Pertinent/n')
     ##          #nonPertinent.click()
          i +=1



          #pertinent = soup.find('div', {'title': 'Pertinent'})
          #nonPertinent = soup.find('div', {'title': 'NonPertinent'})


          
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

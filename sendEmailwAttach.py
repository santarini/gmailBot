from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

#create new message
page_body.send_keys('c')

#define the "recipient" field
time.sleep(3)
recipient = driver.find_element_by_name('to')
recipient.send_keys('recving email adrs')

#define the "subject line" field
subject = driver.find_element_by_name('subjectbox')
timenow = datetime.datetime.now().strftime("%I:%M:%S %p")
datenow = datetime.datetime.now().strftime("%Y-%m-%d")
subject.send_keys("Timecard Submitted" + Keys.TAB + timenow + " " + datenow + " for week of " + str(today) + ".")

time.sleep(2)

attachButton = driver.find_element_by_xpath('//*[@data-tooltip = "Attach files"]')
attachButton.click()

time.sleep(3)

##clipboard.copy("C:\\Users\\m4k04\\Desktop\\TimeCardConfirmation.png")
##time.sleep(3)
##clipboard.paste()

pyautogui.typewrite(r"C:\Users\m4k04\Desktop\TimeCardConfirmation.png")
pyautogui.typewrite(['enter'])

time.sleep(3)

sendButton = driver.find_element_by_xpath('//*[@data-tooltip="Send ‪(Ctrl-Enter)‬"]')
sendButton.click()

driver.quit()

print("Done.")

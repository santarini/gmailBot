from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create new message
page_body.send_keys('c')

#define the "recipient" field
time.sleep(3)
recipient = driver.find_element_by_name('to')
recipient.send_keys('reciving email adrs')

#define the "subject line" field
subject = driver.find_element_by_name('subjectbox')
timenow = datetime.datetime.now().strftime("%I:%M:%S %p")
datenow = datetime.datetime.now().strftime("%Y-%m-%d")
subject.send_keys("Timecard Submitted" + Keys.TAB + timenow + " " + datenow + " for week of " + str(today) + ".")

sendButton = driver.find_element_by_xpath('//*[@data-tooltip="Send ‪(Ctrl-Enter)‬"]')
sendButton.click()

driver.quit()

print("Done.")

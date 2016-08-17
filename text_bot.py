#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python   
from splinter import Browser     
import time

# Define the username and password
username = ''
password = '' + '\n'

# Choose the browser (default is Firefox)
browser = Browser('chrome')

# Fill in the url
browser.visit('https://www.textnow.com/')

browser.find_by_id('loginButton').first.click()

time.sleep(3)

# Find the username form and fill it with the defined username
browser.find_by_name('username')
#.first.find_by_tag('input')
browser.fill('username', username)

# Find the password form and fill it with the defined password
browser.find_by_name('password')
#.first.find_by_tag('input')
browser.fill('password', password)

time.sleep(38)

browser.find_by_id('newText').first.click()

target = '' #Your Friend's number
message = "What's sup dude!"
browser.find_by_css("input.newConversationTextField").fill(target)
#browser.fill('recipients', target)
browser.find_by_id('message').first.type(message, slowly=False)
time.sleep(3)


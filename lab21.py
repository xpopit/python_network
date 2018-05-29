#!/usr/local/bin/python3.6
from robobrowser import RoboBrowser

browser = RoboBrowser()
browser.open('http://192.168.2.245/login')

# Get the signup form
signup_form = browser.get_form()
print(signup_form)         # <RoboForm user[name]=, user[email]=, ...

# Inspect its values
# signup_form['authenticity_token'].value     # 6d03597 ...

# Fill it out
signup_form['user[username]'].value = 'admin'
signup_form['user[secretkey]'].value = '1234'

# Submit the form
browser.submit_form(signup_form)

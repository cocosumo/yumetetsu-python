import os
from src.app.browser import chrome

def type_username():
  username = os.getenv('KINTONE_USER')
  username_element = chrome.find_element_by_name("username")
  username_element.send_keys(username)

def type_password():
  password = os.getenv('KINTONE_PASSWORD')
  password_element = chrome.find_element_by_name("password")
  password_element.send_keys(password)


def click_submit():
  submit_button_element = chrome.find_element_by_class_name("login-button")
  submit_button_element.click()

def navigate_to_import():
  chrome.get(('https://rdmuhwtt6gx7.cybozu.com/k/137/importRecord'))

def login_to_kintone():
  print("Logging in to kintone.")
  navigate_to_import()
  type_username()
  type_password()
  click_submit()



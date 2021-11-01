
from selenium.webdriver.support.select import Select
from src.app.browser import chrome
import os

def type_username():
  username = os.getenv('DONET_USER')
  username_element = chrome.find_element_by_class_name("username")
  username_element.send_keys(username)

def type_password():
  password = os.getenv('DONET_PASS')
  password_element = chrome.find_element_by_class_name("password")
  password_element.send_keys(password)

def select_shop():
  shop_select_element= chrome.find_element_by_id("fc_shop_id")
  select_object = Select(shop_select_element)
  select_object.select_by_value("157")

def click_submit():
  submit_button_element = chrome.find_element_by_class_name("login_btn")
  chrome.execute_script("$(arguments[0]).click();", submit_button_element)
  print(submit_button_element)
  submit_button_element


def login_to_donetwork():
  chrome.get(('https://manage.do-network.com/login/134'))
  type_username()
  type_password()
  select_shop()
  click_submit()


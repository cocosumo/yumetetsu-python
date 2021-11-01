from src.app.file import get_process_dir, rename_file
from src.donetwork.login import login_to_donetwork
from src.app.browser import chrome, wait_for_downloads
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


def navigate_to_properties():
  chrome.get('https://manage.do-network.com/estate?_reset')

def get_shop_select():
  return Select(chrome.find_element_by_id("m_estate_filters_fc_shop_id"))

def get_shops():

  shop_select = get_shop_select()
  options = shop_select.options
  shop_list = list(map(lambda el:el.text, options))
  shop_list.remove('')
  return shop_list

def isResultExist():
  try:
        chrome.find_element_by_id("kensakukekka")
  except NoSuchElementException:
      return False
  return True


def save_csv():
  chrome.execute_script("$('#m_estate_form').submit();")
  if isResultExist():
    print("Starting to download.")
    chrome.get("https://manage.do-network.com/estate/ListCsvDownload")
    return True
  else:
    print("No records. ")
    return False


def download_file_by_shop(shop):
  get_shop_select().select_by_visible_text(shop)
  print(f"Checking if {shop} have records")
  return save_csv()


def download_files():
  index = 0
  for shop in get_shops():
    if download_file_by_shop(shop):
      path = wait_for_downloads(get_process_dir())
      rename_file(path, str(index))
      print(f"Finished downloading {shop}.")
      index += 1


def download_from_donet_properties():
  print("Downloading from do network.")
  login_to_donetwork()
  navigate_to_properties()
  download_files()


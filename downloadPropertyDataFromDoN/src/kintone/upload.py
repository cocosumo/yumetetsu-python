
from src.kintone.login import login_to_kintone
from src.app.browser import chrome
from src.app.file import get_merged_file_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def upload_csv_by_cli():
  print("cliだとフィールドコードを設定しないといけないので、放置。")

def click_browse_file():
  print("Pressing upload.")
  chrome.execute_script("$('#fileKey-browse input').click();")


def upload_file():
  print("uploading file.")
  WebDriverWait(chrome, timeout=30).until(
    EC.presence_of_element_located((By.ID, "fileKey-browse"))
  )
  fileEl = chrome.find_element_by_xpath("//input[@type='file']")

  fileEl.send_keys(get_merged_file_path())

def confirm_first_line_is_header():
  print("Clicking YES")
  WebDriverWait(chrome, timeout=30).until(
        EC.presence_of_element_located((By.ID, "30"))
      )
  chrome.execute_script("$('#30').click()")

def set_chkbox_key():
  el = WebDriverWait(chrome, timeout=30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*=propertyId]"))
      )
  print("Found the mapper.")
  chrome.execute_script("arguments[0].click();", el)

def click_upload():
  chrome.find_element(By.CLASS_NAME, "button-submit-cybozu").click()


def upload_csv_by_browser():
  upload_file()
  confirm_first_line_is_header()
  set_chkbox_key()
  click_upload()


#Process
def upload_to_kintone():
  login_to_kintone()
  upload_csv_by_browser()
from selenium import webdriver
from src.app.file import get_process_dir
import time, logging, os
from fake_useragent import UserAgent

ua = UserAgent()
userAgent = ua.chrome
print(userAgent)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={userAgent}')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.images": 2,
    'download.default_directory': get_process_dir()
})


chrome = webdriver.Chrome(options=chrome_options)
chrome.maximize_window()

def get_browser():
  return chrome

def every_downloads_chrome(driver):
  print("Waiting all downloads to finish.")
  if not driver.current_url.startswith("chrome://downloads"):
      driver.get("chrome://downloads/")
  return driver.execute_script("""
      var items = document.querySelector('downloads-manager')
          .shadowRoot.getElementById('downloadsList').items;
      if (items.every(e => e.state === "COMPLETE"))
          return items.map(e => e.fileUrl || e.file_url);
      """)

def wait_for_downloads(dir):
    max_delay = 120
    interval_delay = 0.2
    total_delay = 0
    file = ''
    done = False
    while not done and total_delay < max_delay:
        files = [f for f in os.listdir(dir) if f.endswith('.crdownload')]
        if not files and len(file) > 1:
            done = True
        if files:
            file = files[0]
        time.sleep(interval_delay)
        total_delay += interval_delay
    if not done:
        logging.error("File(s) couldn't be downloaded")

    print(f"Waited for {round(total_delay, 2)} seconds." )
    return os.path.join(dir, file.replace(".crdownload", ""))

def close_browser():
  print("Closing browser.")
  chrome.close()

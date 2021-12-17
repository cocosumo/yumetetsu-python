
from src.app.browser import close_browser
from src.kintone.upload import upload_to_kintone
from src.donetwork.properties import download_from_donet_properties
from src.app.file import process_files, remove_dir
from dotenv import load_dotenv

load_dotenv()

def init_env():
  print("Starting program.")
  remove_dir()

def clean():
  close_browser()
  print("終りました！ｷﾝﾄｰﾝでアップロードが成功したか、ご確認ください。")
  remove_dir()
  exit()


def main():
  init_env()
  download_from_donet_properties()
  process_files()
  upload_to_kintone()
  clean()



if __name__ == "__main__":
  main()



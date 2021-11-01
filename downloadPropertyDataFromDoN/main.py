
from src.env.browser import close_browser
from src.kintone.upload import upload_to_kintone
from src.donetwork.properties import download_from_donet_properties
from src.env.file import process_files, remove_dir

def init_env():
  print("Starting program.")
  remove_dir()

def clean():
  close_browser()
  print("終りました！ｷﾝﾄｰﾝでアップロードが成功したか、ご確認ください。")
  remove_dir()


def main():
  init_env()
  download_from_donet_properties()
  process_files()
  upload_to_kintone()
  clean()


if __name__ == "__main__":
  main()
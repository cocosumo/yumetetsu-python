import os

from dotenv import load_dotenv
load_dotenv()

def getGroupIdByMailBox(mailBox):
  if (mailBox in ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp"]):
    return os.getenv('SLACK_CHANNEL_ID_FUJISAWA')
  elif (mailBox in ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]):
    return os.getenv('SLACK_CHANNEL_ID_TOYOKAWA')
  else:
    return os.getenv('SLACK_CHANNEL_ID_TEST')
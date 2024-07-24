import os

from dotenv import load_dotenv
load_dotenv()

_mailBoxesToyokawa = ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]
_mailBoxesFujisawa = ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp", "iwata@yumetetsu.jp"]
_mailBoxesToyota = ["house-do@toyota-do.com", "toyota@yumetetsu.jp"]
_mailBoxesNakagawa = ["yaguma@yumetetsu.jp", "chikusa@yumetetsu.jp"]
_mailBoxesTakahama = ["takahama@yumetetsu.jp"]
_mailBoxesNisshin = ["nisshin@yumetetsu.jp"]
_mailBoxesNagakute = ["nagakute@yumetetsu.jp"]
_mailBoxesGamagori = ["gamagoori@yumetetsu.jp"]

def getGroupIdByMailBox(mailBox):
  print(f"Retrieving Channel id : {mailBox}")
  if (mailBox in _mailBoxesFujisawa):
    return os.getenv('SLACK_CHANNEL_ID_FUJISAWA')
  elif (mailBox in _mailBoxesToyokawa):
    return os.getenv('SLACK_CHANNEL_ID_TOYOKAWA')
  elif (mailBox in _mailBoxesToyota):
    return os.getenv('SLACK_CHANNEL_ID_TOYOTA')
  elif (mailBox in _mailBoxesNakagawa):
    return os.getenv('SLACK_CHANNEL_ID_NAKAGAWA')
  elif (mailBox in _mailBoxesTakahama):
    return os.getenv('SLACK_CHANNEL_ID_TAKAHAMA')
  elif (mailBox in _mailBoxesNisshin):
    return os.getenv('SLACK_CHANNEL_ID_NISSHIN')
  elif (mailBox in _mailBoxesNagakute):
    return os.getenv('SLACK_CHANNEL_ID_NAGAKUTE')
  elif (mailBox in _mailBoxesGamagori):
    return os.getenv('SLACK_CHANNEL_ID_GAMAGORI')
  else:
    print("Failed to find Channnel Id. Fallback to test.")
    return os.getenv('SLACK_CHANNEL_ID_TEST')

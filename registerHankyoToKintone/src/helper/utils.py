import os

from dotenv import load_dotenv
load_dotenv()

#TODO
# Refactor redundant code.

_mailBoxesToyokawa = ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]
_mailBoxesFujisawa = ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp", "iwata@yumetetsu.jp"]
_mailBoxesToyota = ["house-do@toyota-do.com"]
_mailBoxesNakagawa = ["yaguma@yumetetsu.jp", "chikusa@yumetetsu.jp"]
_mailBoxesTakahama = ["takahama@yumetetsu.jp"]


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
  else:
    print("Failed to find Channnel Id. Fallback to test.")
    return os.getenv('SLACK_CHANNEL_ID_TEST')

#deprecated
def getAppIdByMailBox(mailBox):
  print("Resolving ID for ", mailBox)

  if (mailBox in _mailBoxesFujisawa):
    return os.getenv('KINTONE_APP_ID_FUJISAWA')
  elif (mailBox in _mailBoxesToyokawa):
    return os.getenv('KINTONE_APP_ID_TOYOKAWA')
  else:
    print("Invalid mailbox, defaulting to TEST.")
    return os.getenv('KINTONE_APP_ID_TEST')

#deprecated
def getAppTokenByMailBox(mailBox):
  if (mailBox in _mailBoxesFujisawa):
    return os.getenv('KINTONE_APP_TOKEN_FUJISAWA')
  elif (mailBox in _mailBoxesToyokawa):
    return os.getenv('KINTONE_APP_TOKEN_TOYOKAWA')
  else:
    return os.getenv('KINTONE_APP_TOKEN_TEST')
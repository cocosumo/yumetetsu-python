import os

from dotenv import load_dotenv
load_dotenv()

#TODO
# Refactor redundant code.

_mailBoxesToyokawa = ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]
_mailBoxesFujisawa = ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp"]
_mailBoxesToyota = ["house-do@toyota-do.com"]

def getGroupIdByMailBox(mailBox):
  print(f"Retrieving Channel id : {mailBox}")
  if (mailBox in _mailBoxesFujisawa):
    return os.getenv('SLACK_CHANNEL_ID_FUJISAWA')
  elif (mailBox in _mailBoxesToyokawa):
    return os.getenv('SLACK_CHANNEL_ID_TOYOKAWA')
  elif (mailBox in _mailBoxesToyota):
    return os.getenv('SLACK_CHANNEL_ID_TOYOTA')
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
import os

import pykintone

from src.model.Hankyo import Hankyo
from src.helper.slack import sendToSlackFormatted
from src.helper.args import getArgByIdx
from src.helper.utils import getAppIdByMailBox, getAppTokenByMailBox

#Environment variable loader
from dotenv import load_dotenv
load_dotenv()

#Initialize App
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve()



def registerToKintone(title, main, mailTo, mailFrom):
  #Still not sure how to use yml so I made separate settings. 2021/12/21

  account = pykintone.load(os.path.join(currentPath, f"account-{getAppIdByMailBox(mailTo)}.yml"))
  app = account.app()
  print(app, f"account-{getAppIdByMailBox(mailTo)}.yml", mailTo,  "TEST")
  try:
    print("Trying to register.")
    record = Hankyo()
    record.title = title
    record.main = main
    record.mail_to = mailTo
    record.mail_from  = mailFrom
    result = app.create(record)
    print(result.record_id, "result")
    return result.record_id
  except:
    print("Failed")



def main():

  # ArgsIdx
  # 1 = title
  # 2 = main
  # 3 = mailTo
  # 4 = mailFrom

  _title = getArgByIdx(1)
  _mailTo = getArgByIdx(3)
  _mailFrom = getArgByIdx(4)

  _recordId = registerToKintone(title=_title, main=getArgByIdx(2), mailTo=_mailTo, mailFrom=getArgByIdx(4))

  sendToSlackFormatted(_recordId, _title, _mailTo, _mailFrom)

if __name__ == "__main__":
  main()
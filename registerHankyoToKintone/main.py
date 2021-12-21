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
account = pykintone.load(os.path.join(currentPath, "account.yml"))


def registerToKintone(title, main, mailTo, mailFrom):
  app = account.app(app_id=getAppIdByMailBox(mailTo), api_token=getAppTokenByMailBox(mailTo))

  try:
    print("Trying to register.")
    record = Hankyo()
    record.title = title
    record.main = main
    record.mail_to = mailTo
    record.mail_from  = mailFrom
    result = app.create(record)
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
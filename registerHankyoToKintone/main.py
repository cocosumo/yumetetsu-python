import sys
import os

import pykintone

from src.model.Hankyo import Hankyo
from src.helper.slack import sendToSlackFormatted
from src.helper.args import getArgByIdx

#Environment variable loader
from dotenv import load_dotenv
load_dotenv()

#Initialize App
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve()
account = pykintone.load(os.path.join(currentPath, "account.yml"))
app = account.app()

def registerToKintone(title, main, mail_to, mail_from):
  try:
    print("Trying to register.")
    record = Hankyo()
    record.title = title
    record.main = main
    record.mail_to = mail_to
    record.mail_from  = mail_from
    result = app.create(record)
    return result.record_id
  except:
    print("Failed")

def main():
  _title = getArgByIdx(1)
  record_id = registerToKintone(title=_title, main=getArgByIdx(2), mail_to=getArgByIdx(3), mail_from=getArgByIdx(4))

  sendToSlackFormatted(record_id, _title)

if __name__ == "__main__":
  main()
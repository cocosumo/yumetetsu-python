import os
import pykintone
from src.controller.kintone.record import register, putSlack
from src.controller.slack.sendToSlack import sendToSlackFormatted
from src.helper.args import getArgByIdx
from src.helper.utils import getAppIdByMailBox


#Environment variable loader
from dotenv import load_dotenv
load_dotenv()

#Initialize App
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve()

def main():

  # ArgsIdx
  # 1 = title
  # 2 = main
  # 3 = mailTo
  # 4 = mailFrom

  _title = getArgByIdx(1)
  _mailTo = getArgByIdx(3)
  _mailFrom = getArgByIdx(4)

  _account = pykintone.load(os.path.join(currentPath, "account.yml"))

  _recordId = register(account=_account, title=_title, main=getArgByIdx(2), mailTo=_mailTo, mailFrom=getArgByIdx(4))

  print("New Kintone recordId: ",_recordId)
  postMessageResult = sendToSlackFormatted(_recordId, _title, _mailTo, _mailFrom)
  print("slackMessage Sent: ", postMessageResult)

  putSlack(account=_account,recordId=_recordId, slackPostMessageResult=postMessageResult)



if __name__ == "__main__":
  main()
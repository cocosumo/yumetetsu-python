

import pykintone
from src.model.Hankyo import Hankyo


def register(account: pykintone, title, main, mailTo, mailFrom):
  # Still not sure how to use yml so I made separate settings. 2021/12/21
  # Decision between or hankyo or not is processed at Outlook.

  isTest = ("テスト" in title)

  # Do not register to kintone if テスト is found in title. Good when testing other parts of the process.
  #if isTest: return

  app = account.app()

  try:
    print("Trying to register.")
    record = Hankyo()
    record.title = title
    record.main = main
    record.mail_to = mailTo
    record.mail_from = mailFrom
    result = app.create(record)
    print(result.record_id, "result")
    return result.record_id
  except:
    print("Failed")


def putSlack(account: pykintone, recordId, slackPostMessageResult):
  app = account.app()

  try:
    print("Trying to register.")
    records = app.select(f"$id=\"{recordId}\"").models(Hankyo)
    record = records[0]
    record.slackChannel = slackPostMessageResult["channel"]
    record.slackTS = slackPostMessageResult["ts"]
    app.update(record)
  except Exception as e:
    print(f"Failed: {e}")
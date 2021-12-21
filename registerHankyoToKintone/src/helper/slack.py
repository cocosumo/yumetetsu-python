import os

from src.helper.utils import getAppIdByMailBox, getGroupIdByMailBox

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from dotenv import load_dotenv
load_dotenv()


_slack_token = os.getenv('SLACK_BOT_KEY')
_slackMainFile = os.getenv('PATH_TO_SLACK_SENDER')
_kintoneDomain = os.getenv('KINTONE_DOMAIN')

_client = WebClient(token=_slack_token)

def generateEditLink(record_id):
  # 例：https://rdmuhwtt6gx7.cybozu.com/k/155/show#record=23
  return f"{_kintoneDomain}/k/155/show#record={record_id}"

#deprecated
def sendToSlack(recordId, title):
  print(f"Sending record to slack: {recordId}" )
  print(_slackMainFile)
  message = f"\"新たな反響がありました。*{title}* {generateEditLink(recordId)} \""
  os.system(f"py {_slackMainFile} {message}")

def sendToSlackFormatted(recordId, title, mailTo, mailFrom):

  message = f"\"新たな反響がありました。*{title}* {generateEditLink(recordId)} \""
  _channel_id = getGroupIdByMailBox(mailTo)
  _app_id = getAppIdByMailBox(mailTo)

  print(f"Sending to {mailTo} : {_channel_id} ")

  try:
      # Call the conversations.list method using the WebClient

      result = _client.chat_postMessage(
          channel=_channel_id,
          text=message,
          blocks=[
            {
            "type": "header",
             "text":
              {
                "type": "plain_text",
                "text": "新たな反響がありました。"
              }
            },
            {
            "type": "section",
            "text":
              {
                "type": "mrkdwn",
                "text": f"*差出人：* {mailFrom} \n *宛先：* {mailTo} \n *件名：* {title}"
              }
            },
            {
            "type": "section",
            "text":
              {
                "type": "mrkdwn",
                "text": f"*<{_kintoneDomain}/k/{_app_id}/show#record={recordId}|Kintoneで開く>*"
              },
            },

          ]

      )
      # Print result, which includes information about the message (like TS)
      print(result)
  except SlackApiError as e:
      print(f"Error: {e}")
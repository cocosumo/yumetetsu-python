import os

from src.helper.utils import getGroupIdByMailBox

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

def sendToSlackFormatted(recordId, title, mailTo):

  message = f"\"新たな反響がありました。*{title}* {generateEditLink(recordId)} \""
  _channel_id = getGroupIdByMailBox(mailTo)

  print(f"Sending to {mailTo} : {_channel_id} ")

  try:
      # Call the conversations.list method using the WebClient

      result = _client.chat_postMessage(
          channel=_channel_id,
          text=message,
          blocks=[
            {
            "type": "section",
             "text":
              {
                "type": "plain_text",
                "text": "新な反響がありました。"
              }
            },
            {
            "type": "header",
            "text":
              {
                "type": "plain_text",
                "text": title
              }
            },
            {
            "type": "section",
            "text":
              {
                "type": "mrkdwn",
                "text": f"*<{_kintoneDomain}/k/155/show#record={recordId}|Kintoneで開く>*"
              }
            }

          ]

      )
      # Print result, which includes information about the message (like TS)
      print(result)
  except SlackApiError as e:
      print(f"Error: {e}")
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from dotenv import load_dotenv
load_dotenv()

_channel_id = "C02R6P88K7E"
_slack_token = os.getenv('SLACK_BOT_KEY')
_slackMainFile = os.getenv('PATH_TO_SLACK_SENDER')
_kintoneDomain = os.getenv('KINTONE_DOMAIN')

_client = WebClient(token=_slack_token)
_api_response = _client.api_test()

def generateEditLink(record_id):
  # 例：https://rdmuhwtt6gx7.cybozu.com/k/155/show#record=23
  return f"{_kintoneDomain}/k/155/show#record={record_id}"

def sendToSlack(record_id, title):
  print(f"Sending record to slack: {record_id}" )
  print(_slackMainFile)
  message = f"\"新たな反響がありました。*{title}* {generateEditLink(record_id)} \""
  os.system(f"py {_slackMainFile} {message}")

def sendToSlackFormatted(record_id, title):

  message = f"新たな反響がありました。*{title}* {generateEditLink(record_id)} "

  print(message)

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
                "text": f"*<{_kintoneDomain}/k/155/show#record={record_id}|Kintoneで開く>*"
              }
            }

          ]

      )
      # Print result, which includes information about the message (like TS)
      print(result)
  except SlackApiError as e:
      print(f"Error: {e}")
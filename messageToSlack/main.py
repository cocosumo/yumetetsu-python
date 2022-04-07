
import sys
import os
import argparse
# Enable debug logging

import logging
logging.basicConfig(level=logging.WARNING)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()


slack_token = os.getenv('SLACK_BOT_KEY')
default_channel_id = "C02R6P88K7E"

client = WebClient(token=slack_token)
api_response = client.api_test()

def sendMessage(message, channelId):
  try:
      # Call the conversations.list method using the WebClient
      result = client.chat_postMessage(
          channel=channelId,
          type="plain_text",
          text=message,

          blocks=[
            {
              "type": "section",
              "text": {
                "type": "mrkdwn",
                "text": f"{message}"

              }
            }
          ]
          # You could also use a blocks[] array to send richer content
      )
      # Print result, which includes information about the message (like TS)
      print(result)

  except SlackApiError as e:
      print(f"Error: {e}")


def main():
  parser = argparse.ArgumentParser(description='Sends message to slack.')
  parser.add_argument('-m', '--message', required=True)
  parser.add_argument('-cid', '--channelid', default=default_channel_id)
  args = parser.parse_args()

  # ID of channel you want to post message to
  print(args.message)

  sendMessage(args.message, args.channelid)

if __name__ == "__main__":
  main()


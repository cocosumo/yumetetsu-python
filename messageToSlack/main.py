
import sys
import os
# Enable debug logging

import logging
logging.basicConfig(level=logging.WARNING)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()


slack_token = os.getenv('SLACK_BOT_KEY')
channel_id = "C02R6P88K7E"

client = WebClient(token=slack_token)
api_response = client.api_test()

def sendMessage(message):
  try:
      # Call the conversations.list method using the WebClient
      result = client.chat_postMessage(
          channel=channel_id,
          text=message,
          blocks=[
            {"type": "section", "text": {"type": "mrkdwn", "text": "*message*"}}
          ]
          # You could also use a blocks[] array to send richer content
      )
      # Print result, which includes information about the message (like TS)
      print(result)

  except SlackApiError as e:
      print(f"Error: {e}")


def main():
  print(len(sys.argv), sys.argv[1])

  # ID of channel you want to post message to

  if(len(sys.argv)>1):
    message = sys.argv[1]
    sendMessage(message)

if __name__ == "__main__":
  main()


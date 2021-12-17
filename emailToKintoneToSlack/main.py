# test.py
import sys
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
from slack_sdk import WebClient
client = WebClient()
api_response = client.api_test()
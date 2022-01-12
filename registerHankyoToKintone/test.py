from src.controller.slack.sendToSlack import sendToSlackFormatted
postMessageResult = sendToSlackFormatted(10, "テスト", "info@yumetetsu.jp", "test@test.com")

print(postMessageResult)
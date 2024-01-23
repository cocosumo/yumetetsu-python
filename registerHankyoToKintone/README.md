
## Before Starting:
1. Check/Fill out .env
2. Check/Fill out account.yml

## Usage:
Accepts arguments in following order. All must be present.

py main.py <title> <content> <mail_to> <mail_from>

## Add or edit Store

- Add stores at helper/utils

## Add or edit slack channel

- See .env file and edit helper/utils according to spec.

## Testing

 TODO: Following is manual. Need to improve testing method
 Adding "テスト" to the first argument, sends it to test channel in slack.

 1. Open terminal on registerHankyoKintone
 2. Edit test.py accordingly.
 3. Optionally. Return test.py to its original form to prevent running it on prod.

```
     py main.py <title> <body> <mailTo@mail.com> <mailFrom@mail.com>
```

## Contributing

This was a port of uipath implementation.
Feel free to optimize or port it to another technology.
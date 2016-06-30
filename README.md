# Slack-Bot-Python
A simple python slack bot

###To use the bot:

- Install python and virtualenv.

- Clone the project and go to the directory and write the following in the terminal:

  1. source iobot/bin/activate  (if everithing goes OK you should see (iobot) in first place in terminal

  2. export SLACK_BOT_TOKEN='your slack token here'

  3. python print.py                   // Now copy the ID value that is printed in the terminal

  4. export SLACK_BOT_ID='ID printed with anterior commnad'

  5. python IOBot.py

If everithing goes fine you should see the message: "IOBot connected and running!"


### To expand the bot:

The bot connects to slack RTM API. You can take a look to API documentation in https://api.slack.com/rtm and https://api.slack.com/methods
for simple expansion.


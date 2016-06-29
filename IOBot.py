import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = 'U1MC6HRL3'
SLACK_BOT_TOKEN = 'xoxb-55414603683-hcLvO3rAuX52ctGGf1F7iOAp'
# constants
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(SLACK_BOT_TOKEN)


def handle_command(messageTest, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    if(AT_BOT in messageTest):
        response = "Que quiere pesao?"
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)
        return

    if("┬──┬ ノ( ゜-゜ノ)" in messageTest):
        time.sleep(2.1)
        response = "(╯°□°）╯︵ ┻━┻"
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)
        return

    if("Picate con slackbot"):
        response = "(╯°□°）╯︵ ┻━┻"
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)
        return


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                # return text after the @ mention, whitespace removed
                return output['text'], \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 0.2 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
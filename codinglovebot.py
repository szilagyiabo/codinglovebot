from slackclient import SlackClient
import time
import requests
from bs4 import BeautifulSoup # sudo pip install beautifulsoup4
import unicodedata
import os

# Slack constants
_SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
_BOT_ID = os.environ.get("SLACK_BOT_ID")
_BOT_NAME = os.environ.get("SLACK_BOT_NAME") or 'codinglovebot'

# constants
AT_BOT = "<@" + _BOT_ID + ">:"
EXAMPLE_COMMAND = "send"


# initialize
slack_client = SlackClient(_SLACK_BOT_TOKEN)


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with some nice message."

    command = strip_accents(command)

    if command.startswith(EXAMPLE_COMMAND):
        response = get_random_post()
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


def get_random_post():
    raw_html = requests.get("http://thecodinglove.com/random")
    parsed_html = BeautifulSoup(raw_html.text, 'html.parser')
    title = parsed_html.find("div", {"id": "post1"}).find("h3")
    img = parsed_html.find("div", {"id": "post1"}).find("div", {"class": "bodytype"}).find("img")
    response = str("*" + title.string + "*") + "\n" + str(img['src'])
    return response


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("%s connected and running!" % _BOT_NAME)
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

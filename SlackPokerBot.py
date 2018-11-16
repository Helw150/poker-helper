import os
import sys
import time
import re
from slackclient import SlackClient
from AbstractGame import Game
from Constants import suits, valid_values


# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 5 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
channel = None

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            if event["channel"][0] == 'D':
                return event["text"], event["channel"]
    return None, None

def slackbot_input(request):
    """
    Says something and then waits for a response
    """
    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=request
    )
    command = None
    counter = 0
    while command == None:
        if counter == 1200:
            os.execl(sys.executable, sys.executable, *sys.argv)
        command, new_channel = parse_bot_commands(slack_client.rtm_read())
        if new_channel != channel:
            command = None
        time.sleep(0.5)
        counter += 1
    return command

def slackbot_print(message):
    """
    Simple Statement
    """
    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=message
    )

def getValuesFromInput(str_card):
    while True:
        r_input = slackbot_input(str_card +" as VALUE,SUIT: ")
        split_array = r_input.split(",")
        if len(split_array) != 2:
            continue
        value, suit = split_array
        value = value.lower()
        suit = suit.lower()
        if value in valid_values and suit in suits:
            return value, suit
        else:
            print("Malformed Input - try again")
    
if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while channel == None:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)
        print(channel)
        while True:
            num_players = int(slackbot_input("How many players? "))
            game = Game(num_players)
            first_value, first_suit = getValuesFromInput("First Pocket")
            second_value, second_suit = getValuesFromInput("Second Pocket")
            game.dealPockets(first_value, first_suit, second_value, second_suit)
            slackbot_print(game)
            while not game.isDone():
                next_value, next_suit =  getValuesFromInput("Next Dealt Card")
                game.placeToBoard(next_value, next_suit)
                slackbot_print(game)
            slackbot_input("Say Anything once you are Finished")
    else:
        print("Connection failed. Exception traceback printed above.")

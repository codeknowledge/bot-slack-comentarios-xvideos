import os

API_TOKEN = os.getenv('API_KEY')

DEFAULT_REPLY = "Tente a sorte grande, digite \"sorte do dia\""

PLUGINS = [
    'slackbot.plugins',
    'xvideos.plugins',
]
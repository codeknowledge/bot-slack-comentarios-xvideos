import re
from slackbot.bot import respond_to

@respond_to(r'\Aping\Z', re.IGNORECASE)
def sorte(message):
    # react with emoji
    message.react('huebr')
    message.reply('you have been ponged! :tennis:')
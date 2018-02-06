
import re
from slackbot.bot import Bot, respond_to, listen_to
from xvideos.xvideos import choose_random_porn_comment

@listen_to('Sorte do dia', re.IGNORECASE)
@respond_to('Sorte do dia', re.IGNORECASE)
def sorte_do_dia(message):
    comment = choose_random_porn_comment()
    message.reply(format_comment(*comment))
    # react with emoji
    # message.react(':ok_hand::skin-tone-3:')

def format_comment(author, content, title):
    mask = '"Sua sorte de hoje: {0}"'
    return mask.format(content)
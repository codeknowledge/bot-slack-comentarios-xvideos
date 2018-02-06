
import re
from slackbot.bot import Bot, respond_to, listen_to
from xvideos.xvideos import choose_random_porn_comment

@respond_to('sorte do dia$', re.IGNORECASE)
def sorte_do_dia(self, message):
    comment = choose_random_porn_comment()
    message.reply(format_sorte_de_hoje(comment.content))
    # react with emoji
    # message.react(':ok_hand::skin-tone-3:')

@listen_to('sorte do dia para (.*)$', re.IGNORECASE)
def sorte_do_dia_para(self, message, target):
    comment = choose_random_porn_comment()
    print(target)
    print(comment)
    self.say(format_sorte_de_hoje_para(target, comment.content))


def format_sorte_de_hoje(content):
    mask = 'Sua sorte de hoje é: "{0}"'
    return mask.format(content)

def format_sorte_de_hoje_para(target, content):
    mask = '{0} sua sorte para hoje é: "{1}"'
    return mask.format(target, content)
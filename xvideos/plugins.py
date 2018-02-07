
import re
from slackbot.bot import respond_to, listen_to
from xvideos.xvideos import choose_random_porn_comment

@respond_to(r'\Asorte ([\w\s]*)\Z', re.IGNORECASE)
def sorte(message, tipo_sorte):
    # react with emoji
    message.react('ok_hand::skin-tone-3')
    comment = choose_random_porn_comment()
    formated_message = format_sorte(tipo_sorte, comment[1])
    message.reply(formated_message)

@respond_to(r'\Asorte ([\w\s]*) para (.*)\Z', re.IGNORECASE)
def sorte_para(message, tipo_sorte, alvo_sorte):
    message.react('ok_hand::skin-tone-3')
    comment = choose_random_porn_comment()
    message.reply(format_sorte_para(tipo_sorte, alvo_sorte, comment[1]))


def format_sorte(tipo_sorte, content):
    mask = 'Sua sorte {0} é: "{1}"'
    return mask.format(tipo_sorte, content)

def format_sorte_para(tipo_sorte, alvo_sorte, content):
    mask = 'Aqui está a sorte {0} para {1}: "{2}"'
    return mask.format(tipo_sorte, alvo_sorte, content)
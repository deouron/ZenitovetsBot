import utils
from commands import ban_spartak


def check_spartak_fan(bot, message):
    for word in utils.BAN_WORDS:
        if word in message.text:
            ban_spartak(bot, message)
            break


def check_greeting_reply(bot, message, wait_answer_from):
    if message.from_user.id in wait_answer_from:
        bot.reply_to(message, "@" + message.from_user.username +
                     ' болеет за ' + message.text + ' (либо проигнорил мой вопрос 😢)')
        wait_answer_from.remove(message.from_user.id)

import utils
import commands


def check_admin(bot, message):
    is_admin = bot.get_chat_member(message.chat.id, message.from_user.id).status == 'administrator' or \
               bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator'
    if is_admin:
        return True
    bot.reply_to(message, text='Доступно только для админов!')
    return False


def is_replied(bot, message):
    if not message.reply_to_message:
        bot.reply_to(message, "Необходимо написать в ответ на сообщение пользователя!")
        return False
    return True


def check_spartak_fan(bot, message):
    for word in utils.BAN_WORDS:
        if word in message.text:
            commands.ban_spartak(bot, message)
            break


def check_greeting_reply(bot, message, wait_answer_from):
    if message.from_user.id in wait_answer_from:
        bot.reply_to(message, "@" + message.from_user.username +
                     ' болеет за "' + message.text + '" (либо проигнорировал мой вопрос 😢)')
        wait_answer_from.remove(message.from_user.id)

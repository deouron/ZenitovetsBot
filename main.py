import telebot
import utils
from utils import check_admin, is_replied
import parsers
from commands import send_helper_text, ban_user, unban_user, promote_user, send_statistics, leave_chat, send_matches, \
    send_table, send_news, ban_spartak
from checkers import check_greeting_reply, check_spartak_fan


def process_message(message):
    if message.text == '/help@zenitovets_bot':
        send_helper_text(bot, message)
    elif message.text == '/ban@zenitovets_bot':
        if is_replied(bot, message) and check_admin(bot, message):
            ban_user(bot, message)
    elif message.text == '/unban@zenitovets_bot':
        if is_replied(bot, message) and check_admin(bot, message):
            unban_user(bot, message)
    elif message.text == '/admin@zenitovets_bot':
        if is_replied(bot, message) and check_admin(bot, message):
            promote_user(bot, message)
    elif message.text == '/statistics@zenitovets_bot':
        send_statistics(bot, message)
    elif message.text == '/exit@zenitovets_bot' and check_admin(bot, message):
        leave_chat(bot, message)
    elif message.text == '/matches@zenitovets_bot':
        send_matches(bot, message)
    elif message.text == '/news@zenitovets_bot':
        send_news(bot, message)
    elif message.text == '/table@zenitovets_bot':
        send_table(bot, message)


bot = telebot.TeleBot(utils.TOKEN)
wait_answer_from = set()


@bot.message_handler(content_types=['text'])
def reply_message(message):
    check_greeting_reply(bot, message, wait_answer_from)
    check_spartak_fan(bot, message)
    process_message(message)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.send_message(message.chat.id, text='Привет, ' +
                                           message.new_chat_members[0].first_name + '! За какую команду болеешь?')
    wait_answer_from.add(message.new_chat_members[0].id)


bot.polling(none_stop=True, interval=0)

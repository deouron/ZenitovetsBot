import telebot
import utils
from commands import send_helper_text, ban_user_by_reply, unban_user_by_reply, promote_user, send_statistics, \
    leave_chat, send_matches, send_table, send_news, mute_user_by_reply, \
    unmute_user_by_replay, all_banned, all_muted
from checkers import check_greeting_reply, check_spartak_fan, check_admin, is_replied

bot = telebot.TeleBot(utils.TOKEN)
wait_answer_from = set()
banned_users = set()
muted_users = set()


def process_message(message):
    if message.text == '/help@zenitovets_bot':
        send_helper_text(bot, message)
    elif message.text == '/ban@zenitovets_bot':
        if check_admin(bot, message) and is_replied(bot, message):
            ban_user_by_reply(bot, message, banned_users)
    elif message.text == '/unban@zenitovets_bot':
        if is_replied(bot, message) and check_admin(bot, message):
            unban_user_by_reply(bot, message, banned_users)
    elif message.text == '/all_bannned@zenitovets_bot':
        all_banned(bot, message, banned_users)
    elif message.text == '/mute@zenitovets_bot':
        if is_replied(bot, message) and check_admin(bot, message):
            mute_user_by_reply(bot, message, muted_users)
    elif message.text == '/unmute@zenitovets_bot':
        if is_replied(bot, message) and check_admin(bot, message):
            unmute_user_by_replay(bot, message, muted_users)
    elif message.text == '/all_muted@zenitovets_bot':
        all_muted(bot, message, muted_users)
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


@bot.message_handler(content_types=['text'])
def reply_message(message):
    check_greeting_reply(bot, message, wait_answer_from)
    check_spartak_fan(bot, message)
    process_message(message)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    greeting_text = 'Привет, @' + message.new_chat_members[0].username + '! За какую команду болеешь?'
    bot.send_message(message.chat.id, text=greeting_text)
    wait_answer_from.add(message.new_chat_members[0].id)


bot.polling(none_stop=True, interval=0)

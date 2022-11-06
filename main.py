import telebot
import utils
import parser

bot = telebot.TeleBot(utils.TOKEN)


def check_admin(message):
    return bot.get_chat_member(message.chat.id, message.from_user.id).status == 'administrator' or \
           bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator'


def is_replied(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Необходимо написать в ответ на сообщение пользователя!")
        return False
    return True


@bot.message_handler(content_types=['text'])
def reply_message(message):
    for word in utils.ban_words:
        if word in message.text:
            bot.reply_to(message, "Любитель спартака " + message.from_user.first_name + " забанен!")
            bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

    if message.text == '/help@zenitovets_bot':
        bot.send_message(message.chat.id, text=utils.helper_text)
    elif message.text == '/ban@zenitovets_bot':
        if is_replied(message) and check_admin(message):
            bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
            bot.reply_to(message, "Пользователь " + message.reply_to_message.from_user.first_name + " забанен!")
    elif message.text == '/unban@zenitovets_bot':
        if is_replied(message) and check_admin(message):
            bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
            bot.reply_to(message, "Пользователь " + message.reply_to_message.from_user.first_name + " разбанен!")
    elif message.text == '/admin@zenitovets_bot':
        if is_replied(message) and check_admin(message):
            bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
            bot.reply_to(message, message.reply_to_message.from_user.first_name + " - новый админ!")
    elif message.text == '/statistics@zenitovets_bot':
        bot.send_message(message.chat.id, text='Участников в чате: '
                                               + str(bot.get_chat_member_count(message.chat.id))
                                               + '\nАдминов в чате: '
                                               + str(len(bot.get_chat_administrators(message.chat.id))))
    elif message.text == '/exit@zenitovets_bot' and check_admin(message):
        bot.send_message(message.chat.id, text='Я ухожу, всем пока')
        bot.leave_chat(message.chat.id)
    elif message.text == '/matches@zenitovets_bot':
        for match in parser.matches_parser():
            bot.send_message(message.chat.id, text=match)
    elif message.text == '/news@zenitovets_bot':
        for news in parser.news_parser():
            bot.send_message(message.chat.id, text=str(news[1]) + '\n' + news[0])
    elif message.text == '/table@zenitovets_bot':
        bot.send_message(message.chat.id, text=parser.table_parser())


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.send_message(message.chat.id, text='Привет, ' + message.from_user.first_name + '! За какую команду болеешь?')
    bot.delete_message(message.chat.id, message.message_id)


bot.polling(none_stop=True, interval=0)

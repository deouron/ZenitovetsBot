import telebot
import utils
import parser

bot = telebot.TeleBot(utils.TOKEN)
wait_answer = set()


def check_admin(message):
    is_admin = bot.get_chat_member(message.chat.id, message.from_user.id).status == 'administrator' or \
           bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator'
    if is_admin:
        return True
    bot.reply_to(message, text='Доступно только для админов!')
    return False


def is_replied(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Необходимо написать в ответ на сообщение пользователя!")
        return False
    return True


def count_admins(message):
    cnt = 0
    for admin in bot.get_chat_administrators(message.chat.id):
        if not admin.user.is_bot:
            cnt += 1
    return str(cnt)


def check_greeting_reply(message):
    if message.from_user.id in wait_answer:
        bot.send_message(message.chat.id, text=message.from_user.first_name +
                         ' болеет за ' + message.text +
                         ' (либо проигнорил мой вопрос 😢)')
        wait_answer.remove(message.from_user.id)


@bot.message_handler(content_types=['text'])
def reply_message(message):
    check_greeting_reply(message)

    for word in utils.ban_words:
        if word in message.text:
            bot.reply_to(message, "Любитель спартака " + message.from_user.first_name + " забанен!")
            bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            break

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
                                               + '\nАдминов в чате: ' + count_admins(message))
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
    bot.send_message(message.chat.id, text='Привет, ' + message.new_chat_members[0].first_name + '! За какую команду болеешь?')
    wait_answer.add(message.new_chat_members[0].id)


bot.polling(none_stop=True, interval=0)

import utils
import parser


def send_helper_text(bot, message):
    bot.send_message(message.chat.id, text=utils.HELPER_TEXT)


def kick_user(bot, message):
    bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    bot.reply_to(message, "Пользователь " + message.reply_to_message.from_user.first_name + " забанен!")


def bun_user(bot, message):
    bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    bot.reply_to(message, "Пользователь " + message.reply_to_message.from_user.first_name + " разбанен!")


def promote_user(bot, message):
    bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    bot.reply_to(message, message.reply_to_message.from_user.first_name + " - новый админ!")


def send_statistics(bot, message):
    bot.send_message(message.chat.id, text='Участников в чате: '
                                           + str(bot.get_chat_member_count(message.chat.id))
                                           + '\nАдминов в чате: ' + utils.count_admins(bot, message))


def leave_chat(bot, message):
    bot.send_message(message.chat.id, text='Я ухожу, всем пока')
    bot.leave_chat(message.chat.id)


def send_matches(bot, message):
    for match in parser.matches_parser():
        bot.send_message(message.chat.id, text=match)


def send_news(bot, message):
    for news in parser.news_parser():
        bot.send_message(message.chat.id, text=str(news[1]) + '\n' + news[0])


def send_table(bot, message):
    bot.send_message(message.chat.id, text=parser.table_parser())


def ban_spartak(bot, message):
    bot.reply_to(message, "Любитель спартака забанен!")
    bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
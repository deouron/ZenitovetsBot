import utils
import parsers


def send_helper_text(bot, message):
    bot.send_message(message.chat.id, text=utils.HELPER_TEXT)


def ban_user(bot, message):
    bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " забанен!")


def unban_user(bot, message):
    bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " разбанен!")


def promote_user(bot, message):
    try:
        bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,
                                can_change_info=True, can_invite_users=True, can_delete_messages=True,
                                can_restrict_members=True,
                                can_pin_messages=True, can_promote_members=True,
                                can_manage_chat=True, can_manage_video_chats=True, can_manage_voice_chats=True)
        bot.reply_to(message, "@" + message.reply_to_message.from_user.username + " - новый админ!")
    except Exception as e:
        bot.reply_to(message, "Ошибка, проверьте наличие прав у бота")


def send_statistics(bot, message):
    bot.send_message(message.chat.id, text='Участников в чате: '
                                           + str(bot.get_chat_member_count(message.chat.id))
                                           + '\nАдминов в чате (без ботов): ' + utils.count_admins(bot, message)[0]
                                           + '\nАдминов в чате (ботов): ' + utils.count_admins(bot, message)[1])


def leave_chat(bot, message):
    bot.send_message(message.chat.id, text='Я ухожу, всем пока')
    bot.leave_chat(message.chat.id)


def send_matches(bot, message):
    for match in parsers.matches_parser():
        bot.send_message(message.chat.id, text=match)


def send_news(bot, message):
    for news in parsers.news_parser():
        bot.send_message(message.chat.id, text=str(news[1]) + '\n' + news[0])


def send_table(bot, message):
    bot.send_message(message.chat.id, text=parsers.table_parser())


def ban_spartak(bot, message):
    bot.reply_to(message, "Любитель спартака забанен!")
    bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

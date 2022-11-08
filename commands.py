import utils
import parsers


def send_helper_text(bot, message):
    bot.send_message(message.chat.id, text=utils.HELPER_TEXT)


def ban_user_by_reply(bot, message, banned_users):
    if message.reply_to_message.from_user.username not in banned_users:
        try:
            bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
            banned_users.add(message.reply_to_message.from_user.username)
            bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " забанен!")
        except Exception as e:
            bot.reply_to(message, "Пользователя @" + message.reply_to_message.from_user.username + " нельзя банить!")
            print(e)
    else:
        bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " уже забанен!")


def unban_user_by_reply(bot, message, banned_users):
    if message.reply_to_message.from_user.username in banned_users:
        try:
            bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
            banned_users.remove(message.reply_to_message.from_user.username)
            bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " разбанен!")
        except Exception as e:
            bot.reply_to(message, "Пользователя @" + message.reply_to_message.from_user.username + " нельзя банить!")
            print(e)
    else:
        bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " уже разбанен!")


def all_banned(bot, message, banned_users):
    text = ''
    if len(banned_users) > 0:
        for user in banned_users:
            text += '@' + user + '\n'
        bot.reply_to(message, 'Пользователей в бане: ' + str(len(banned_users)) + '\n' + text)
    else:
        bot.reply_to(message, 'Никто не забанен!')


def mute_user_by_reply(bot, message, muted_users):
    if message.reply_to_message.from_user.username not in muted_users:
        try:
            bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
            muted_users.add(message.reply_to_message.from_user.username)
            bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " в муте!")
        except Exception as e:
            bot.reply_to(message, "Пользователя @" + message.reply_to_message.from_user.username + " нельзя мьютить!")
            print(e)
    else:
        bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " уже в муте!")


def unmute_user_by_replay(bot, message, muted_users):
    if message.reply_to_message.from_user.username in muted_users:
        try:
            bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,
                                     can_send_messages=True, can_send_media_messages=True, can_send_polls=True,
                                     can_send_other_messages=True, can_add_web_page_previews=True, can_change_info=True,
                                     can_invite_users=True, can_pin_messages=True)
            muted_users.remove(message.reply_to_message.from_user.username)
            bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " вышел из мута!")
        except Exception as e:
            bot.reply_to(message, "Пользователя @" + message.reply_to_message.from_user.username + " нельзя мьютить!")
            print(e)
    else:
        bot.reply_to(message, "Пользователь @" + message.reply_to_message.from_user.username + " уже вышел из мута!")


def all_muted(bot, message, muted_users):
    text = ''
    if len(muted_users) > 0:
        for user in muted_users:
            text += '@' + user + '\n'
        bot.reply_to(message, 'Пользователей в муте: ' + str(len(muted_users)) + '\n' + text)
    else:
        bot.reply_to(message, 'Никто не в муте!')


def promote_user(bot, message):
    try:
        bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,
                                can_change_info=True, can_invite_users=True, can_delete_messages=True,
                                can_restrict_members=True, can_pin_messages=True, can_promote_members=True,
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
    try:
        bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        bot.reply_to(message, "Любитель спартака забанен!")
    except Exception as e:
        bot.reply_to(message, "Этого любителя спартака нельзя забанить...")

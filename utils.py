import TOKEN


def count_users(bot, message):
    cnt = 0
    for user in bot.get_chat_member_count(message.chat.id):
        if not user.user.is_bot:
            cnt += 1
    return str(cnt)


def count_admins(bot, message):
    cnt = 0
    for admin in bot.get_chat_administrators(message.chat.id):
        if not admin.user.is_bot:
            cnt += 1
    return str(cnt)


def is_replied(bot, message):
    if not message.reply_to_message:
        bot.reply_to(message, "Необходимо написать в ответ на сообщение пользователя!")
        return False
    return True


def check_admin(bot, message):
    is_admin = bot.get_chat_member(message.chat.id, message.from_user.id).status == 'administrator' or \
               bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator'
    if is_admin:
        return True
    bot.reply_to(message, text='Доступно только для админов!')
    return False


BAN_WORDS = ['спартакчемпион', 'спартакЧемпион', 'спартак чемпион', 'спартак Чемпион', 'спартак-чемпион',
             'спартак-Чемпион', 'спартак- чемпион', 'спартак- Чемпион', 'спартак чемпион', 'спартак Чемпион',
             'спартак  чемпион', 'спартак  Чемпион', 'спартак -чемпион', 'спартак -Чемпион', 'спартак - чемпион',
             'спартак - Чемпион', 'Спартакчемпион', 'СпартакЧемпион', 'Спартак чемпион', 'Спартак Чемпион',
             'Спартак-чемпион', 'Спартак-Чемпион', 'Спартак- чемпион', 'Спартак- Чемпион', 'Спартак чемпион',
             'Спартак Чемпион', 'Спартак  чемпион', 'Спартак  Чемпион', 'Спартак -чемпион', 'Спартак -Чемпион',
             'Спартак - чемпион', 'Спартак - Чемпион']
TOKEN = TOKEN.TOKEN
MAX_NEWS_CNT = 3
TEAMS_CNT = 16
HELPER_TEXT = '/help@zenitovets_bot - помощь\n' + \
              '/ban@zenitovets_bot - забанить пользователя (написать в ответ на сообщение пользователя, которого надо забанить, только для админов)\n' + \
              '/unban@zenitovets_bot - разбанить пользователя (написать в ответ на сообщение пользователя, которого надо разбанить, только для админов)\n' + \
              '/admin@zenitovets_bot - сделать пользователя админом (написать в ответ на сообщение пользователя, которого надо сделать админом, только для админов)\n' + \
              '/statistics@zenitovets_bot - узнать сколько пользователей и сколько админов в чате (без ботов)\n' + \
              '/exit@zenitovets_bot - заставить бота самого уйти из чата (только для админов)\n' + \
              '/matches@zenitovets_bot - прислать результат прошедшего матча и анонс ближайшего\n' + \
              '/table@zenitovets_bot - прислать текущую таблицу Мир Российская Премьер-Лига Сезон 2022/2023\n' + \
              '/news@zenitovets_bot - узнать последние ' + str(MAX_NEWS_CNT) + ' новости про Зенит\n\n' + \
              'Доп. фишки:\n' + \
              '1) Зенит - чемпион! Поэтому пользователи, написавшие словосочетание' + \
              ' "Спартак - чемпион" (в любых вариациях), будут баниться!\n' + \
              '2) По приходу новых пользователей в чат бот спрашивает, за какую команду они болеют, а так же отвечает им'

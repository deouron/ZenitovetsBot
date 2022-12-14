import TOKEN


def count_admins(bot, message):
    people_cnt = 0
    bots_cnt = 0
    for admin in bot.get_chat_administrators(message.chat.id):
        if not admin.user.is_bot:
            people_cnt += 1
        else:
            bots_cnt += 1
    return str(people_cnt), str(bots_cnt)


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
              '/all_bannned@zenitovets_bot - вывести количество и список забаненых пользователей\n' + \
              '/mute@zenitovets_bot - замьютить пользователя (написать в ответ на сообщение пользователя, которого надо замьютить, только для админов)\n' + \
              '/unmute@zenitovets_bot - размьютить пользователя (написать в ответ на сообщение пользователя, которого надо размьютить, только для админов)\n' + \
              '/all_muted@zenitovets_bot - вывести количество и список замьюченых пользователей\n' + \
              '/admin@zenitovets_bot - сделать пользователя админом (написать в ответ на сообщение пользователя, которого надо сделать админом, только для админов)\n' + \
              '/statistics@zenitovets_bot - узнать сколько пользователей и сколько админов (без ботов) в чате\n' + \
              '/exit@zenitovets_bot - заставить бота самого уйти из чата (только для админов)\n' + \
              '/matches@zenitovets_bot - прислать результат прошедшего матча и анонс ближайшего\n' + \
              '/table@zenitovets_bot - прислать текущую таблицу Мир Российская Премьер-Лига Сезон 2022/2023\n' + \
              '/news@zenitovets_bot - узнать последние ' + str(MAX_NEWS_CNT) + ' новости про Зенит\n\n' + \
              'Доп. фишки:\n' + \
              '1) Зенит - чемпион! Поэтому пользователи, написавшие словосочетание' + \
              ' "Спартак - чемпион" (в любых вариациях), будут баниться!\n' + \
              '2) По приходу новых пользователей в чат бот спрашивает, за какую команду они болеют, а так же отвечает им\n' + \
              '3) Реализована обработка ошибок (бан уже забаненого пользователя, бан не админом, бан админа и т.д.)'

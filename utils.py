ban_words = ['спартакчемпион', 'спартакЧемпион', 'спартак чемпион', 'спартак Чемпион', 'спартак-чемпион',
             'спартак-Чемпион', 'спартак- чемпион', 'спартак- Чемпион', 'спартак чемпион', 'спартак Чемпион',
             'спартак  чемпион', 'спартак  Чемпион', 'спартак -чемпион', 'спартак -Чемпион', 'спартак - чемпион',
             'спартак - Чемпион', 'Спартакчемпион', 'СпартакЧемпион', 'Спартак чемпион', 'Спартак Чемпион',
             'Спартак-чемпион', 'Спартак-Чемпион', 'Спартак- чемпион', 'Спартак- Чемпион', 'Спартак чемпион',
             'Спартак Чемпион', 'Спартак  чемпион', 'Спартак  Чемпион', 'Спартак -чемпион', 'Спартак -Чемпион',
             'Спартак - чемпион', 'Спартак - Чемпион']
TOKEN = '5641502242:AAH1wHGI3Js9SmLR-M7LUJ4JruHIIe2QXw0'
max_news_cnt = 3
teams_cnt = 16
helper_text = '/help@zenitovets_bot - помощь\n' + \
              '/ban@zenitovets_bot - забанить пользователя (написать в ответ на сообщение пользователя, только для админов)\n' + \
              '/unban@zenitovets_bot - разбанить пользователя (написать в ответ на сообщение пользователя, только для админов)\n' + \
              '/admin@zenitovets_bot - сделать пользователя админом (написать в ответ на сообщение пользователя, только для админов)\n' + \
              '/statistics@zenitovets_bot - узнать сколько пользователей и сколько админов в чате\n' + \
              '/exit@zenitovets_bot - заставить бота самого уйти из чата (только для админов)\n' + \
              '/matches@zenitovets_bot - прислать результат прошедшего матча и анонс ближайшего\n' + \
              '/table@zenitovets_bot - прислать текущую таблицу Мир Российская Премьер-Лига Сезон 2022/2023\n' + \
              '/news@zenitovets_bot - узнать последние ' + str(max_news_cnt) + ' новости про Зенит\n\n' + \
              'Доп. фишки:\n' + \
              '1) Зенит - чемпион! Поэтому пользователи, написавшие словосочетание ' + \
              '"Спартак - чемпион", будут баниться!\n' + \
              '2) Бот удаляет все сообщения о вступлении в группу'

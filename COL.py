def skip():
    input("Введите Enter для продолжения...")
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("""                                                                                                                           
                      .-._   .-._.         .-.  
                    .: (_)`-' .;;.    .- ;' (_) 
                    ::       ;;  `;`-' .:'      
                    ::   _  ;;    :.  .:'       
                    `: .; );;     ;'.-:.    .-. 
                      `--' `;.__.' (_/ `;._.    

                   
                     <<<CounterOsintLibrary>>>
 
           от создателей: @adapterofcounter & @TooxanMarket
    ┌─────────────────────────────────────────────────────────────┐
    │  ПРИМЕЧАНИЕ!                                                │                     
    │  Данный инструмент не находит информацию, он лишь           │
    │  подсказывает каким сервисом лучше воспользоваться          │
    │  для анализа и поиска открытых данных в сети интернет!      │
    └─────────────────────────────────────────────────────────────┘                                                   
""")
    print("Если вы обнаружили ошибку в работе софта, обратитесь к владельцу приложения")
    print("")
    print('Какие данные у вас есть?')
    print('''
│ [1]Номер телефона │ [8]Транспорт       │ [15]Трекер
│ [2]Аккаунт        │ [9]Документы       │ [16]Wi-Fi
│ [3]E-mail         │ [10]Домен          │ [17]Серийный номер
│ [4]ФИО            │ [11]Файл           │ [18]IMAI
│ [5]Биометрия      │ [12]Номер кошелька │
│ [6]Адрес          │ [13]Пароль         │
│ [7]Никнейм        │ [14]Текст          │
    ''')
    data = input('[@]Select >')
    if data == '1':
        print('Номер телефона какой страны?')
        print('''
│ [1]России         │ [8]Великобритании  │ [15]Индии          │ [22]Нидерландов  │ [29]Швейцарии
│ [2]Украины        │ [9]Германии        │ [16]Канады         │ [23]Норвегии     │ [30]Эстонии
│ [3]Казахстана     │ [10]Гонконг        │ [17]Китая          │ [24]Польши       │ [31]Южной Кореи
│ [4]Австралии      │ [11]Дании          │ [18]Кубы           │ [25]Румынии      │ [32]Японии
│ [5]Белируси       │ [12]Италии         │ [19]Латвии         │ [26]США          │
│ [6]Бразилии       │ [13]Исландии       │ [20]Молдавии       │ [27]Франции      │ 
│ [7]Венгрии        │ [14]Испании        │ [21]Новой Зеландии │ [28]Швеции       │
    ''')
        country  = input('[@]Select >')
        if country == '1':
            print(r"""
1. @avinfo — находит аккаунты, недвижимость, автомобили, объявления, для бесплатного поиска есть канал @avinfopro с промо для поиска без оплаты
2. getcontact.com  — выдает как записан номер в контактах
3. list-org.com (https://www.list-org.com/?search=phone) — найдет организацию в РФ
4. SaveRuData (https://data.intelx.io/saverudata/) — покажет, полный адрес, имя, все из сервиса Яндекс Еда, СДЕК, траты на еду за 6 месяцев, работает через VPN
5. X-ray (https://x-ray.contact/platform/russian-search/)  — найдет имя, аккаунты, адреса, почту, вход из России запрещён, нужен VPN
6. @OsintKit (https://t.me/@osintkit_check_bot) — ищет в утечках, дает имена, адреса, почты и много другого 
7. @GetAirplane (https://t.me/getairplane_bot)  — авиаперелеты за 20 лет, еще покажет с кем часто летал человек
8. @HomoSpiens (https://t.me/findHOMOrobot) — ищет в утечках, в архивах с 1921 года, дает адреса, почту и прочее
9. @Chaos (https://t.me/chaosro_bot) — найдет адрес, ФИО, объявления, карты и прочее в утечках
10. @ExportBase (https://t.me/ExportBase_egrul_bot) — найдет компанию или ИП

    """)
            skip()
        elif country == '2':
            print('''
1. @InfoBaza (https://t.me/xx3738373_bot) — бесплатно найдет полное имя или его часть
2. spravochnik109.link (https://spravochnik109.link/ukraina) — поиск по городскому номеру телефона, найдет ФИО и адрес
3. @InfoLab (https://t.me/ProbivUniversal_New_Bot) — находит, имена, почты, адреса, бесплатно покажет только часть данных
4. searchyellowdirectory.com (https://www.searchyellowdirectory.com/reverse-phone/380/) — определит к какой области Украины принадлежит номер телефона
5. rol-x.ru (https://rol-x.ru/searh_by_phone.aspx) — найдет объявления на OLX
6. @HomoSpiens (https://t.me/findHOMOrobot) — ищет в утечках, в архивах с 1921 года, дает адреса, почту и прочее
7. @Рассвет (http://t.me/rasver91_bot) — ищет в утечках, находит имена, адреса, документы и прочее
8. @Chaos (https://t.me/chaosro_bot) — найдет адрес, ФИО, объявления, карты и прочее в утечках
    ''')
            skip()
        elif country == '3':
            print('''
1. fa-fa.kz (https://fa-fa.kz/search_ip_too/) — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд
2. spravochnik109.link (https://spravochnik109.link/kazahstan) — поиск по городскому номеру телефона, найдет ФИО и адрес
3. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
    ''')
            skip()
        elif country == '4':
            print('''
1. personlookup.com.au (https://personlookup.com.au/) — найдет имя и адрес
2. numlookup.com (https://numlookup.com/) — найдет имя
    ''')
            skip()
        elif country == '5':
            print('''
1. spravochnik109.link (https://spravochnik109.link/byelarus) — поиск по городскому номеру телефона, найдет ФИО и адрес
2. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
3. autobot.by (https://autobot.by/search/by-phone/) — сыщет удаленные и актуальные объявления о продаже авто
4. @faribybot — сыщет удаленные и актуальные объявления о продаже авто
    ''')
            skip()
        elif country == '6':
            print('''
1. sistemas.anatel.gov.br (http://sistemas.anatel.gov.br/sgmu/fiqueligado/tups.asp) — если номер телефона от таксофона, то найдет его на карте, время его работы, и прочее
2. telenumeros.com (https://telenumeros.com/) — найдет номер телефона, адрес, и полное имя
    ''')
            skip()
        elif country == '7':
            print('''
1. telekom.hu (https://www.telekom.hu/lakossagi/tudakozo) — найдет ФИО и адрес проживания
    ''')
            skip()
        elif country == '8':
            print('''
1. numlookup.com — найдет имя
    ''')
            skip()
        elif country == '9':
            print('''
1. herold.at (https://www.herold.at/telefonbuch/) — найдет ФИО и адрес владельца 
2. www.telefonabc.at (https://www.telefonabc.at/) — выдаст ФИО
3. numlookup.com (https://numlookup.com/) — найдет имя
    ''')
            skip()
        elif country == '10':
            print('''
1. @sgk2023_03_30bot — ищет ID аккаунта QQ, Weibo
2. @DATA_007bot — выдаст аккаунт QQ, телефон вводить без +83
3. @XingDun2Bot — найдет имя, профили, адрес, пол, для бесплатного поиска пригласите 5 пользователей по вашей реферальной ссылке
''')
            skip()
        elif country == '11':
            print('''
1. statstidende.dk (https://statstidende.dk/messages) — поиск в юридических документах, найдет данные о смене жительства, некрологи много всего полезного
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
3. krak.dk (https://www.krak.dk/) — найдет ФИО, местоположение на карте и фото дома.
''')
            skip()
        elif country == '12':
            print('''
1. paginebianche.it (https://www.paginebianche.it/) — найдет ФИО и адрес
2. numlookup.com (https://numlookup.com/) — найдет имя
''')
            skip()
        elif country == '13':
            print('''
1. ja.is (https://ja.is/) — найдет данные людей и компаний
    ''')
            skip()
        elif country == '14':
            print('''
1. numeracionyoperadores.cnmc.es (https://numeracionyoperadores.cnmc.es/portabilidad/movil) — найдет название оператора связи
2. numlookup.com (https://numlookup.com/) — найдет имя
3. listaspam.com (https://listaspam.com/) — найдёт жалобы от пользователей, рейтинг доверия
''')
            skip()
        elif country == '15':
            print('''
1. Mi Airit (https://play.google.com/store/apps/details?id=com.app.airit) — популярное Android приложении в Индии, после 
2. indiaonapage.com (http://www.indiaonapage.com/mobilenumbertrace) — покажет оператора связи и возможный город
3. numlookup.com (https://numlookup.com/) — найдет имя
    ''')
            skip()
        elif country == '16':
            print('''
1. www.canada411.ca (https://www.canada411.ca/search/) — возраст, ФИО, адрес проживания и другое
2. numlookup.com (https://numlookup.com/) — найдет имя
3. canadafinder.ca (https://www.canadafinder.ca/searchnumber.php) — даст имя, адрес регистрации
    ''')
            skip()
        elif country == '17':
            print('''
1. @sgk2023_03_30bot — ищет ID аккаунта QQ, Weibo
2. @DATA_007bot — выдаст аккаунт QQ, телефон вводить без +83
3. qcc.com (https://qcc.com/) — найдет компанию
4. @XingDun2Bot — найдет имя, профили, адрес, пол, для бесплатного поиска пригласите 5 пользователей по вашей реферальной ссылке
5. DetectDee (https://github.com/piaolin/DetectDee/) — покажет в каких сервисах зарегистрирован телефон
    ''')
            skip()
        elif country == '18':
            print('''
1. @ETECSABD_bot — найдет ФИО, дату рождения, адрес проживания
2. @directorio_etecsa_bot — найдет ФИО, дату рождения, адрес проживания
3. directorioetecsa.com (https://directorioetecsa.com/) — найдет ФИО, дату рождения, адрес проживания
    ''')
            skip()
        elif country == '19':
            print('''
1. spravochnik109.link (https://spravochnik109.link/latviya) — поиск по городскому номеру телефона, найдет ФИО и адрес
    ''')
            skip()
        elif country == '20':
            print('''
1. spravochnik109.link (https://spravochnik109.link/moldova) — поиск по городскому номеру телефона, найдет ФИО и адрес
    ''')
            skip()
        elif country == '21':
            print('''
1. numlookup.com (https://numlookup.com/) — найдет имя
    ''')
            skip()
        elif country == '22':
            print('''
1. crdc.be (http://crdc.be/crdcNLI/BrowserDefault.aspx?tabid=265) — найдет текущего оператора связи
2. acm.nl (https://www.acm.nl/nl/onderwerpen/telecommunicatie/telefoonnummers/nummers-doorzoeken) — дает название компании владеющая номером
3. numlookup.com (https://numlookup.com/) — найдет имя
    ''')
            skip()
        elif country == '23':
            print('''
1. gulesider.no (https://gulesider.no/) — даст ФИО, местоположение на карте и фото дома
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
    ''')
            skip()
        elif country == '24':
            print('''
1. ktodzvonil.com (https://ktodzvonil.com/) — публичные отзывы, рейтинг
2. ktoto.info (https://ktoto.info/) — публичные отзывы, рейтинг
3. bip.uke.gov.pl (https://bip.uke.gov.pl/wyszukiwarka-rejestr-premium) — найдет адрес компании, название услуги
    ''')
            skip()
        elif country == '25':
            print('''
1. www.carte-telefoane.info (https://www.carte-telefoane.info/) — найдет ФИО, контакты, адрес
    ''')
            skip()
        elif country == '26':
            print('''
1. zabasearch.com — найдет имя, адрес, и многое другое
2. truecaller.com  — телефонная книга, найдет имя и оператора телефона
3. cyberbackgroundchecks.com (https://www.cyberbackgroundchecks.com/phone) — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США
4. melissa.com (https://www.melissa.com/v2/lookups/personator) — найдет ФИО, дату рождения, адрес проживания, этнос и прочее
5. oldphonebook.com — найдет адрес и ФИО, записи 20-летней давности
6. anywho.com — найдет адрес где проживает владелец телефона
7. spydialer.com — найдет имя владельца телефона, город и штат проживания
8. smartbackgroundchecks.com — дает адреса, телефоны, биографию, семью, недвижимость, образование, почту, и прочее
9. reversephonecheck.com — находит адрес, фамилию и часть имени
10. cash.app  — найдет фото профиля, имя, никнейм, после регистрации, сделай попытку перевода по номеру телефона, используй VPN
11. fastpeoplesearch.com — выдаст полное имя, возраст, текущий домашний адрес, прошлые адреса, псевдонимы, родственников, предыдущие владельцы телефона и прочее, сайт не работает из России, нужен VPN
12. numlookup.com — найдет имя
13. calleridtest.com  — ищет имя владельца телефона из базы CNAM, город и тип связи, работает только с VPN из США
14. martinvigo.com (https://www.martinvigo.com/tools/phonerator/) — проверит все комбинации номера телефона с неизвестной частью и выдаст только существующие номера
    ''')
            skip()
        elif country == '27':
            print('''
1. www.118712.fr (https://www.118712.fr/annuaire-inverse-gratuit.html) — имя и адрес владельца номера телефона
2. www.pagesjaunes.fr (https://www.pagesjaunes.fr/) — найдет номер ФИО и адрес проживания, введите телефон в первое поле
3. numlookup.com (https://numlookup.com/) — найдет имя
    ''')
            skip()
        elif country == '28':
            print('''
1. eniro.se (https://www.eniro.se/) — найдет ФИО, местоположение на карте и фото дома
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
3. upplysning.se (https://www.upplysning.se/) — контактные данные людей и компаний
4. mrkoll.se (https://mrkoll.se/) — найдет дату рождения, адрес, ФИО, соседей, номер социального страхования, номера телефонов, корпоративное участие, примерный доход, история изменений ФИО
    ''')
            skip()
        elif country == '29':
            print('''
1. local.ch (https://www.local.ch/en/tel) — поиск в реестре бизнесов, найдет сайт, адрес, фото
2. tel.search.ch (https://tel.search.ch/) — поиск в реестре бизнесов, найдет сайт, адрес, фото
    ''')
            skip()
        elif country == '30':
            print('''
1. teatmik.ee (https://www.teatmik.ee/en/advancedsearch/contact) — поиск в базе организаций, ищет номер в контактах
    ''')
            skip()
        elif country == '31':
            print('''
1. 114.co.kr (https://114.co.kr/) — покажет адрес компании
2. kakaocorp.com (https://kakaocorp.com/) — создайте контакт и найдёте аккаунт в приложении
    ''')
            skip()
        elif country == '32':
            print('''
1. www.jpnumber.com (https://www.jpnumber.com/) — найдет отзывы, провайдера, область, возможно ФИО владельца
2. www.telnavi.jp (https://www.telnavi.jp/) — найдет наименование фирмы, ее адрес и прочее
    ''')
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == '2':
        print('Аккаунт где?')
        print('''

┌───────────────────┬───────────────────┬──────────────────┬────────────────────┬───────────────────┬───────────────────┬───────────────────┬───────────────────┬───────────────────┐
│ [ 1] VK           │ [ 8] Youtube      │ [15] Blogspot    │ [22] Flickr        │ [29] Keybase      │ [36] Nintendo     │ [43] Reddit       │ [50] Tumblr       │ [57] Wiebo        │
│ [ 2] Twitter      │ [ 9] Яндекс       │ [16] Chess.com   │ [23] Gravatar      │ [30] Kik          │ [37] OnlyFans     │ [44] SoundCloud   │ [51] Twitch       │ [58] WhatsApp     │
│ [ 3] Facebook     │ [10] Amzn.tu      │ [17] Clubhouse   │ [24] Google        │ [31] LinkedIn     │ [38] Pastebin     │ [45] Skype        │ [52] Tiny.cc      │ [59] Xiaomi       │
│ [ 4] Telegram     │ [11] Behance      │ [18] Cutt.ly     │ [25] GitHub        │ [32] Lolzteam     │ [39] Patreon      │ [46] Snapchat     │ [53] Tiny.pl      │ [60] XBox Live    │
│ [ 5] Instagram    │ [12] Bitbucket    │ [19] Discord     │ [26] habr          │ [33] Minecraft    │ [40] Pinterest    │ [47] Stackoverflow│ [54] Tinyurl.com  │                   │
│ [ 6] Tik-Tok      │ [13] Bit.du       │ [20] Eyeem       │ [27] Huawei        │ [34] mail.ru      │ [41] PlayStation  │ [48] Steam        │ [55] vc.ru        │                   │
│ [ 7] OK           │ [14] Bit.ly       │ [21] eBay        │ [28] ICQ           │ [35] Medium       │ [42] QQ           │ [49] Slack        │ [56] VimeWorld    │                   │
└───────────────────┴───────────────────┴──────────────────┴────────────────────┴───────────────────┴───────────────────┴───────────────────┴───────────────────┴───────────────────┘


''')
        acc = input('[@]Select >')
        if acc == '1':
            print('Что известно в VK?')
            print('[1]Аккаунт, [2]Сообщество/Группа, [3]Пост')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
1. 220vk.com  — определит средний возраст друзей, скрытых друзей, города друзей, дата регистрации и т.д
2. vk5.city4me.com — cтатистика онлайн активности, скрытые друзья
3. СybDetective.com (https://cybdetective.com/quickcacheandarhivesearch.html) — покажет архивированную версию аккаунта, даст 20+ прямых ссылок на сайты веб архивы
4. InfoApp (https://vk.com/app7183114) — найдет созданные группы, упоминания в комментариях, общих друзей, созданные приложения и комментарии к фото
5. vkdia.com — определит с кем из друзей переписывается человек
6. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — найдет фото приватного аккаунта в хорошем качестве, дату создания и прочее
7. vkpt.info  — мониторинг деятельности пользователя, поиск старых друзей, покажет, кому ставит лайки, все комментарии пользователя, скрытые друзья
8. api.vk.com (https://vk.com/dev/messages.getLastActivity) — покажет дату последней активности аккаунта
9. @Sherlok (https://t.me/x8152384_bot) — найдет номер телефона
10. @Vbiv (https://t.me/Vbib_bot)  — найдет удалённые фото аккаунта, иногда телефон и почту
11. @VKHistory (https://t.me/VKHistoryRobot) — история профиля с 2010 по 2023 год, есть даже аватары, вводить числовой ID страницы
12. @Detectiva (https://t.me/reserv_detectiva_bot) — даст статистику по городам и учебным заведениям друзей, найдет страницы с тем же именем, может выдать телефон
13. @SocialGraph (https://t.me/social_graph_osint_bot) — по публичному профилю составит граф из друзей, где видно кто с кем дружит, на графе видны группы родственников, коллег по работе, друзей по школе и так далее
14. Kribrum.io — найдет удаленные публикации, в поле автор укажите ID или адрес аккаунта
15. X-ray (https://x-ray.contact/platform/russian-search/)  — найдет телефоны, почты и прочие аккаунты, работает с VPN
16. @InfoLab (https://t.me/ProbivUniversal_New_Bot) — находит, телефоны, почты, адреса, документы, и прочее, бесплатно покажет только часть данных
17. @FriendlyGraph (https://t.me/friendly_graph_bot) — по публичному профилю составит граф из друзей, где видно кто с кем дружит, видны группы родственников, коллег по работе, друзей по школе
18. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет аккаунт на Мой Мир, дату изменения, создания и дату последнего статуса онлайн, архивные копии профиля, упоминание профиля в ВК и прочее

Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта ВК
2. 220vk.top — слежка за аккаунтом, после добавления будут доступны аватары, лайки, комментарии, друзья группы и т.д.
    ''')
                skip()
            elif popa == '2':
                print('''
1. InfoApp (https://vk.com/app7183114) — находит комментарии от имени сообщества, видеозаписи, упоминания
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу сообщества, даст 20+ прямых ссылок на сайты веб архивы
3. kribrum.io (https://kribrum.io/) — найдет удаленные публикации, в поле автор укажите ID или логин сообщества/группы
4. vk.barkov.net (https://vk.barkov.net/act.aspx) — покажет наиболее активных участников сообщества
''')
                skip()
            elif popa == "3":
                print('''
Парсеры

1. exportcomments.com (https://exportcomments.com/download-vk-comments) — скачивает комментарии в CSV файл
''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '2':
            print('Что известно в Twitter?')
            print('[1]Аккаунт, [2]Твит')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
1. tweeterid.com — по адресу аккаунта найдет ID аккаунта
2. keyhole.co  — анализ аккаунта, при регистрации нет проверок по email и телефону, вводите любые данные, 7 дней бесплатно
3. @UsersBox (https://t.me/us2us_bot) — бот, находит номер телефона, почту и много еще, бесплатный поиск для новых аккаунтов
4. tweettopicexplorer.neoformix.com — статистика наиболее употребляемых слов из твиттов пользователя
5. twitteraudit.com  — покажет количество настоящих и фальшивых подписчиков аккаунта
6. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
7. twiangulate.com (https://twiangulate.com/search/)  — поиск общих подписчиков и подписок между двумя аккаунтами, а также сравнит их охват по подписчикам
8. app.element.io (https://app.element.io/#/home)  — найдет сохранённую копию аккаунта по ID, это имя и аватар, после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск
9. tinfoleak.com — найдет в твитах утечки адресов, устройств, профилей, и прочего, составит статистику
10. kribrum.io — найдет удаленные публикации, в поле автор укажите юзернейм аккаунта
11. @Breachka (https://t.me/povozkaRobot) — найдет почту, телефон и прочее


Поиск через URL

1. https://twitter.com/intent/user?user_id=123456789 — найдет аккаунт в Twitter по ID, замените 123456789
2. https://spoonbill.io/twitter/data/USERNAME/  — история изменения имени, био и прочих данных профиля, замените USERNAME на имя пользователя
3. https://www.politwoops.com/p/*/USERNAME — удаленные твитты, работает с политиками, замените USERNAME на имя пользователя
4. https://web.archive.org/web/*/twitter.com/12345789/* — найдет архив твитов, замените 12356789 на ID аккаунта или на имя пользователя
5. https://lamentandotweets.com/USERNAME — найдет удалённые твиты, больше испанских аккаунтов, замените USERNAME на имя пользователя
6. https://api.memory.lol/v1/tw/USERNAME — найдет историю изменения имени профиля, замените USERNAME на имя пользователя twitter
7. https://twitter.com/USERNAME/lists/memberships — покажет в каких списках состоит пользователь, замените Username в ссылке на имя пользователя twitter


Инструменты

1. spoonbill.io  — следит за изменениями имени, био, ссылками аккаунта, на него нужно подписаться в Twitter
2. nitter.cz — просмотр профиля без регистрации, возможно работает только через VPN
3. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram


Поисковики

1. nitter.domain.glass — поиск по любым данным в твитах пользователя
2. twiangulate.com (https://twiangulate.com/search/)  — поиск  по любым данным в друзьях пользователя


Парсеры

1. phantombuster.com (https://phantombuster.com/automations/twitter/4130/twitter-follower-collector)  — скачает всех подписчиков аккаунта
2. tweetbeaver.com — скачает всех подписчиков, друзей, любимые посты и все историю аккаунта
3. exportcomments.com (https://exportcomments.com/export-twitter-followers) — скачает аккаунты на которые подписан пользователь
    ''')
                skip()
            elif popa == '2':
                print('''
1. treeverse.app (https://treeverse.app/) — визуализирует беседы в Твиттер в виде графа
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на твит
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '3':
            print('''
Поиск по аккаунту Facebook

1. findidfb.com — находит числовой ID аккаунта
2. graph.tips (https://graph.tips/beta/) — дает возможность просматривать, каким публикациям ставил лайки пользователь
3. whopostedwhat.com (https://www.whopostedwhat.com/) — найдет посты в Facebook
4. fb-sleep-stats (https://github.com/sqren/fb-sleep-stats)  — отслеживает онлайн / оффлайн статус людей, можно получить точную информацию о времени их сна 
5. keyhole.co  — анализ аккаунта, при регистрации нет проверок по email и телефону, вводите любые данные
6. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
7. @UsersBox (https://t.me/us2us_bot) — находит номер телефона, почту и много еще, бесплатный поиск для новых аккаунтов
8. @getfb_bot  — найдет номер телефона
9. app.element.io (https://app.element.io/#/home)  — найдет сохранённую копию аккаунта по ID, это имя и аватар, после регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск
10. @Vbib_bot  — найдет имя и номер телефона
11. @Detectiva (https://t.me/reserv_detectiva_bot) — вытаскивает часть номера телефона
12. kribrum.io — найдет удаленные публикации, в поле автор укажите только ID аккаунта
13. x-ray (https://x-ray.contact/search/)  — найдет адреса, телефоны, имена прочие аккаунты и многое другое, работает с VPN
14. @Breachka (https://t.me/povozkaRobot) — найдет почту, телефон и прочее


Поиск через URL

1. https://www.facebook.com/browse/fanned_pages/?id=USERID — найдет лайки пользователя, замените USERID на ID аккаунта
2. https://facebook.com/friendship/USERID/USERID — будут отображаться общие друзья, общие записи и фотографии, а также любые другие связанные данные, такие как родные города, школы и т. д., замените USERID на ID аккаунта
3. https://facebook.com/browse/mutual_friends/?uid=USERID&node=USERID — найдет общих друзей, которые имеют общедоступные списки друзей, если у одного из искомых пользователей есть общедоступный список друзей, замените USERID на ID аккаунта
4. https://my.mail.ru/fb/USERID — найдет аккаунт на Мой Мир, замените USERID в ссылке на ID аккаунта


Поисковики

Ищет по любым данным в контенте одного профиля

1. sowsearch.info — есть фильтр по дате, группе, и локации, можно найти посты пользователя, фото


Парсеры

1. phantombuster.com (https://phantombuster.com/automations/facebook/8369/facebook-profile-scraper)  — скачает всю публичную информацию аккаунта


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram
    ''')
            skip()
        elif acc == '4':
            print('Что известно в Telegram?')
            print('[1]Аккаунт, [2]Канал/Группа, [3]Стикер/Эмодзи, [4]Токен Бота')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
1. @usinfobot — по ID найдёт имя и ссылку акаунта, может показать архивные данные
2. cybdetective.com (https://cybdetective.com/quickcacheandarhivesearch.html) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
3. @SangMata (https://t.me/SangMata_beta_bot) — история изменения имени акаунта, для поиска отправьте в бот ID акаунта
4. @CreationDate (https://t.me/creationdatebot) — примерная дата создания аккаунт, бот принимает username, для поиска по ID можно переслать сообщение от искомого пользователя
5. TelegramOnlineSpy (https://github.com/Forichok/TelegramOnlineSpy)  — лог онлайн активности аккаунта, скажет когда был в сети
6. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдёт адреса почты, архивное имя, аватар еще ищет в других ботах
7. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — найдет часть номера телефона, историю изменения ссылки аккаунта
8. @Insight (https://t.me/ibhld_bot)  — даёт интересы акаунта, а платно выдаст историю изменения имени, номер телефона, группы и ссылки которые публиковал пользователь
9. @Unamer (https://t.me/unamer_search_bot) — покажет кто владел адресом акаунта в прошлом, может отобразить историю смены имен
10. @GetChatList (https://t.me/getchatlistbot) — знает в каких группах участвует пользователь 
11. @TlgGeoEarth (https://t.me/TlgGeoEarthBot) — найдет историю перемещений на карте, покажет координаты и дату
12. TGDB (https://www.tgdb.org/page/bot)  — покажет в каких группах был замечен, архивное имя акаунта
13. @Sherlok (https://t.me/x8152384_bot) — находит номер телефона, историю имен аккаунты кто получил подарки
14. @DataIS (https://t.me/@dataiszbot) — найдет историю имен, группы где был пользователь, его сообщения и прочее
15. @DateRegBot — покажет более точную дату регистрации аккаунта
    ''')
                skip()
            elif popa == '2':
                print('''
1. telemetr.me (https://telemetr.me/all_posts/) — поиск в 200+ млн постах Telegram каналов, сохраняет удаленные публикации 
2. tgstat.com (https://tgstat.com/ru/search) — даст статистику, упоминания и удаленные публикации, убери в фильтре постов галочку "скрывать удаленные публикации"
3. Telegago (https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg) — найдет упоминание в описании каналов/групп а так же сообщениях в группах и постах каналов
4. Exgram (https://yandex.ru/search/site/?text=%22HowToFind%22&searchid=2424333) — найдет упоминания
5. @ChatSearchRobot — на основе участников группы находит публичные чаты
6. Commentgram (https://cse.google.com/cse?cx=006368593537057042503:ig4r3rz35qi) — найдет упоминания, поиск в комментариях к постам
7. Commentdex (https://yandex.ru/search/site/?text=%22HowToFind_bot%22&searchid=2444312) — найдет упоминания, поиск в комментариях к постам
8. telemetr.io (https://telemetr.io/) — найдет удаленные публикации
9. telegramdb.org (https://telegramdb.org/) — по id канала/группы покажет ссылку, фото, описание группы/канала
10. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на канал/группу
11. @telesint_bot — по ссылке на группу выгрузит всех пользователей, даже если они скрыты
12. kribrum.io (https://kribrum.io/) — найдет удаленные публикации, в поле автор укажите юзернейм канала или группы
13. @FunStat (https://t.me/obzorstatBot) — по ссылке или id группы покажет историю изменений, удаленные сообщения, статистику участников 
14. @TeleScan (https://t.me/US2Telescan_Bot) — по ссылке на группу может найти скрытых администраторов группы

Поиск через URL

1. https://intelx.io/?s=https/t.me/USERNAME — найдет упоминание на сайтах и в слитых базах, замените USERNAME на адрес канала


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации канала
2. bibaandboba (https://github.com/andylvua/bibaandboba) — для группы, покажет корреляции между двумя участниками группы
3. filtered-chat-parser (https://github.com/cyb3rm4gus/telegram-filtered-chat-parser) — анализирует сообщения группы, помогает искать сообщения от конкретного пользователя, и прочее
    ''')
                skip()
            elif popa == '3':
                print('''
Поиск по стикеру Telegram

1. @SPOwnerBot — найдет Telegram ID владельца стикера, просто пришли боту стикер


Поиск по эмодзи Telegram

1. @SPOwnerBot — найдет Telegram ID владельца набора эмодзи, просто пришли боту эмодзи


Инструменты

1. @Stickerdownloadbot — скачает стикер в высоком разрешении в PNG формате
2. @EmojiDownloadBot — скачает эмодзи в высоком разрешении в PNG формате
    ''')
                skip()
            elif popa == '4':
                print('''
1. telegram-bot-dumper (https://github.com/soxoj/telegram-bot-dumper) — выгрузит все чаты с пользователями, имя бота, историю
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '5':
            print('Что известно в Instagram?')
            print('[1]Аккаунт, [2]Пост')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
1. fameswap (https://fameswap.com/tool-instagram-user-id) — определит ID аккаунта
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
3. @UsersBox (https://t.me/us2us_bot) — бот, находит номер телефона, почту и много еще, бесплатный поиск для новых аккаунтов
4. notjustanalytics.com (https://www.notjustanalytics.com/) — анализ аккаунта, покажет вовлеченность, рост количества подписчиков, графики взаимодействий и другое
5. @Detectiva (https://t.me/reserv_detectiva_bot) — вытаскивает часть номера телефона
6. kribrum.io — найдет удаленные публикации, в поле автор укажите юзернейм
7. @Sherlok (https://t.me/x8152384_bot) — найдет номер телефона
8. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет профиль на Faсebook


Парсеры

1. InsFo (https://chrome.google.com/webstore/detail/insfo-export-instagram-fo/bckleejkdhlponanidmjfjdigpahlado/related) — расширение для Chrome, скачивает всех подписчиков и подписки аккаунта
2. stevesie.com (https://stevesie.com/cloud/apis/instagram/scrape/user-posts)  — соберет все посты профиля и даст ссылки на фото
3. imginn.com — дает скачать истории, фото и просмотреть профиль без входа
4. piokok.com — дает скачать истории, IGTV, фото, просмотреть комментарии без регистрации и входа
5. @instagent_bot — скачивает посты, истории, igtv, коллекции


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram


Поиск через URL

1. https://www.instagram.com/example/?__a=1&__d=1 — страница в формате JSON, замените example на username аккаунта, покажет id, ссылки на фото и прочее. Работает если вы вошли в свой аккаунт в Instagram


Восстановление пароля

1. Instagram (https://www.instagram.com/accounts/password/reset/) — найдет часть почты или телефона
    ''')
                skip()
            elif popa == '2':
                print('''
По посту Instagram

1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на пост


Через URL

1. Добавьте /media/?size=l в конец ссылки чтобы получить изображение в лучшем качестве


Парсеры

1. exportcomments.com (https://exportcomments.com/export-instagram-comments) — скачивает комментарии в CSV файл
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '6':
            print('Что известно в Tiktok?')
            print('[1]Аккаунт, [2]Видео, [3]Короткая ссылка на видео' )
            popa = input('[@]Select >')
            if popa == '1':
                print('''
Поиск по аккаунту TikTok

1. app.tikbuddy.com (r) — слежка за аккаунтом, покажет статистику по лайкам, просмотрам, популярности, облако слов из комментарий, поиск в комментариях и другое
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
3. @TikTokOSINTbot — найдет ID, дату изменения имени, вечную ссылку на аккаунт, язык приложения, страну и прочее
4. @Sherlok (https://t.me/x8152384_bot) — найдет номер телефона


Парсеры

1. urlebird.com — покажет видео профиля, даст скачать его в лучшем качестве
2. TikTok-Scraper (https://github.com/drawrowfly/tiktok-scraper) — без входа скачает все видео аккаунта в лучшем качестве и с метаданными


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта и отправит в Telegram
    ''')
                skip()
            elif popa == '2':
                print('''
1. exportcomments.com (https://exportcomments.com/download-tiktok-comments) — скачивает комментарии у видео в CSV файл
    ''')
            
                skip()
            elif popa == '3':
                print('''
Для короткой ссылки на видео в Tiktok

Пример короткой ссылки:
https://vt.tiktok.com/ZSR77SDVA/


Дополнительные Методы

1. Найти аккаунт того кто поделился видео

[1] В браузере ПК, перейдите по вашей ссылке
[2] Откройте исходный код страницы (Ctrl+U)
[3] Запустите поиск по странице (Ctrl+F)
[4] Выполните поиск фразы 
sec_user_id=
[5] Если эта фраза есть в коде страницы, то скопируйте значение после знака равно. Это значение начинается с фразы MS4, оно длинное

Пример значения:

MS4wLjABAAAA70IeB6pal_oQkG4sUKQTs-Mz2xcOakKdxNDY2d8L0QNASlMGwOhrn9xbYOMRebrU

6. Подставьте значение в ссылку вместо <UserID>

https://www.tiktok.com/@<UserID>

Перейдите по полученной ссылке. Откроется профиль человека который создал короткую ссылку на видео
''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '7':
            print('''
1. ok.city4me.com — cтатистика онлайн активности, можно узнать когда был онлайн, с какого устройства, узнать с кем из друзей был онлайн, кого добавляет в друзья или удаляет из друзей, дата регистрации пользователя
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
3. socid_extractor (https://github.com/soxoj/socid_extractor)  — найдет числовой ID аккаунта
4. m.ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито
5. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет профиль на mailru, дату регистрации, даст ссылки на поисковики
6. @Detectiva (https://t.me/reserv_detectiva_bot) — находит часть номера телефона, дату регистрации
7. kribrum.io — найдет удаленные публикации, в поле автор укажите только ID аккаунта
8. @social_graph_osint_bot — анализирует друзей аккаунта, построит граф, покажет кто с кем дружит, поможет найди коллег по работе, одноклассников, и прочие группы
9. НЕ РАБОТАЕТ! @ГлазБога (http://t.me/yfzxzxqwqbot)  — найдет номер телефона
10. @Sherlok (https://t.me/x8152384_bot) — найдет номер телефона
    ''')
            skip()
        elif acc == '8':
            print('Что известно в YouTube?')
            print('[1]Канал, [2]Видео')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
Поиск по каналу YouTube

1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на канал
2. ytch.ru — история изменения имени канала, не все есть
3. mattw.io (https://mattw.io/youtube-metadata/) — точная дата создания канала
4. unlistedvideos.com — найдет unlisted видео канала
5. mattw.io (https://mattw.io/youtube-metadata/bulk) — скачает все видео канала, найдет в видео гео, теги, приватные ролики, ссылки, построит таблицу частоты загрузки видео и прочее
6. kribrum.io — найдет удаленные публикации, в поле автор укажите имя канала


Поисковики

1. ytcomment.kmcat.uk — позволяет искать комментарии к видео по всему каналу


Парсеры

1. tools.digitalmethods.net (https://tools.digitalmethods.net/netvizz/youtube/mod_channel_info.php) — дает ID, ссылки на аватарки, описание, название, количество подписчиков и просмотров
2. tools.digitalmethods.net (https://tools.digitalmethods.net/netvizz/youtube/mod_videos_list.php) — экспортирует все видео с канала в файл где есть описания, ссылки на обложки, даты загрузки и др.


Поиск через URL

1. https://web.archive.org/web/*/plus.google.com/+CHANNEL_NAME* — найдет профиль в закрытом сервисе Google Plus, замените CHANNEL_NAME на имя канала на латинице
1. https://www.altcensored.com/channel/ID — сохраненная копия канала, замените ID на ID канала, сайт может не работать в какой-то стране


Инструменты

1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram    ''')
                skip()
            elif popa == '2':
                print('''
Поиск по видео на YouTube

1. mattw.io (https://mattw.io/youtube-metadata/) — теги и дата загрузки видео
2. osintquest.pl (http://osintquest.pl/wp-content/uploads/youtube/mod_video_info.php) — дата создания видео, метаданные, таблица с комментариями, статистика по комментаторам, укажите только ID видео из ссылки
3. YouTubeAnnotations (https://archive.org/details/youtubeannotations?tab=collection) — архив аннотаций к миллиарду видео, выбери и скачай архив согласно ID видео на YouTube, ID указан в ссылке на видео, например если ID начинается с DE, то выбери архив DE и в архиве уже ищи полный ID
4. findyoutubevideo.thetechrobo.ca — ищет видео в 5 архивах, просто  укажи ссылку на видео


Парсеры

1. downsub.com — скачает субтитры
2. savesubs.com — скачает субтитры
3. invidious.domain.glass — скачает субтитры, видео


Инструменты

1. watchframebyframe.com — помогает по кадру просматривать видео


Поисковики

1. youtubecommentsdownloader.com — дает поиск в комментариях к видео
2. hadzy.com — дает поиск в комментариях к видео    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '9':
            print('Что известно в Яндексе?')
            print('[1]Аккаунт, [2]Ссылка Яндекс Поиска')
            popa = input('[@]Select >')
            if popa == '1':
                print('Аккаунт где?')
                print('[1]Музыка, [2]Отзывы, [3]Дзен, [4]Коллекции, [5]Народные карты, [6]Кью')
                popa1 = input('[@]Select >')
                if popa1 == '1':
                    print('''
[1] Откройте исходный код страницы аккаунта на Яндекс музыке (Ctrl+U)
[2] Найдите (Ctrl+F) там фразу "login": и скопируйте то что после этой фразы, это и будет логином
[3] Подставьте в ссылку этот логин вместо Login и перейдите по ней
https://api.music.yandex.net/users/login
[4] Найдите там строку SocialProfiles и перейдите по ссылке на страницу в соц. сети
    ''')
                    skip()
                elif popa1 == '2':
                    print('''
[1] Откройте исходный код страницы аккаунта на Яндекс музыке (Ctrl+U)
[2] Найдите (Ctrl+F) там фразу "login": и скопируйте то что после этой фразы, это и будет логином
[3] Подставьте в ссылку этот логин вместо Login и перейдите по ней
https://api.music.yandex.net/users/login
[4] Найдите там строку SocialProfiles и перейдите по ссылке на страницу в соц. сети
    ''')
                    skip()
                elif popa1 == '3':
                    print('''
[1] Перейдите на страницу аккаунта на Яндекс Дзен
[2] В URL сайта скопируйте все что после yandex.ru/users/
Это называется PublicID
[3] В ссылках вместо PublicID подставьте PublicID который вы нашли

Яндекс Народные карты:
https://n.maps.yandex.ru/#!/users/
PublicID

Яндекс.Кью:
https://yandex.ru/q/profile/PublicID

Яндекс.Отзывы:
https://yandex.ru/user/PublicID
    ''')
                    skip()
                elif popa1 == '4':
                    print('''
[1] Откройте исходный код страницы аккаунта на Яндекс Коллекции (Ctrl+U)
[2] Найдите (Ctrl+F) там фразу publicid и скопируйте после нее цифры
[3] В ссылках вместо PublicID подставьте PublicID который вы нашли

Яндекс Народные карты:
https://n.maps.yandex.ru/#!/users/
PublicID

Яндекс.Кью:
https://yandex.ru/q/profile/PublicID

Яндекс.Отзывы:
https://yandex.ru/user/PublicID

Яндекс.Дзен:
https://zen.yandex.ru/user/PublicID
    ''')
                    skip()
                elif popa1 == '5':
                    print('''
[1] Перейдите на страницу аккаунта на Народные Карты
[2] В URL сайта скопируйте все что после n.maps.yandex.ru/#!/users/
Это называется PublicID
[3] В ссылках вместо PublicID подставьте PublicID который вы нашли

Яндекс.Кью:
https://yandex.ru/q/profile/PublicID

Яндекс.Дзен:
https://zen.yandex.ru/user/PublicID

Яндекс.Отзывы:
https://yandex.ru/user/PublicID
    ''')
                    skip()
                elif popa1 == '6':
                    print('''
[1] Перейдите на страницу аккаунта на Яндекс Кью
[2] В URL сайта скопируйте все что после yandex.ru/q/profile/
Это называется PublicID
[3] В ссылках вместо PublicID подставьте PublicID который вы нашли

Яндекс Народные карты:
https://n.maps.yandex.ru/#!/users/
PublicID

Яндекс.Дзен:
https://zen.yandex.ru/user/PublicID

Яндекс.Отзывы:
https://yandex.ru/user/PublicID
    ''')
                    skip()
                else:
                    print('Попробуйте еще раз')
                    skip()
            elif popa == '2':
                print('''
1. Найти страну и город

[1] Найдите в ссылке Яндекс поиска цифры после фразы lr=
[2] Откройте каталог кодов

https://cloud.yandex.ru/ru/docs/search-api/reference/regions

[3] Найдите в нем известный вам код, вы получите регион или город
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '10':
            print('''
(https://amzn.to/)
1. Найти дату создания и полную ссылку

[1] Добавьте в конец ссылки знак +
[2] Откройте эту ссылку. Пример: https://amzn.to/theweeknd+
''')
            skip()
        elif acc == '11':
            print('''
1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    ''')
            skip()
        elif acc == '12':
            print('''
1. socid_extractor (https://github.com/soxoj/socid_extractor) (t) — найдет user ID, и дату создания аккаунта
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт


Поиск через URL

1. https://bitbucket.org/!api/2.0/repositories/USERNAME/REPO-NAME/refs/branches/master — покажет email адрес, замените USERNAME на имя пользователя, а REPO-NAME на имя репозитория который создал этот пользователь    ''')
            skip()
        elif acc == '13':
            print('''
(https://bit.do/)
1. Найти дату создания, статистику и полную ссылку

[1] Добавьте в конец ссылки знак -
[2] Откройте эту ссылку. Пример: https://bit.do/yeetyeet-
    ''')
            skip()
        elif acc == '14':
            print('''
(https://bit.ly/)
1. Найти статистику и узнать исходную ссылку

[1] Добавьте знак + в конце ссылки 

2. Найти e-mail создателя

[1] Откройте https://twitter.com/bitly и напишите в личных сообщениях следующий текст:

Hello. I can't recover access to my account. 
I tried password recovery but i don't get mail. 
My email is randomemailhere@gmail.com. 
i remember created link, it is bit[.]ly/example

где randomemailhere@gmail.com замените на любой email адрес, а bit[.]ly/example на нужную ссылку bit.ly.

Поддержка скажет, что email не привязан и попросит другой email адрес. 

[2] Скажите что вы знаете только этот email и ссылку bit.ly

Sorry, i remember only one email address and 
one created link by this account. 
I created http://bit[.]ly/example. Please send recovery mail.

Вам ответят что ссылка на восстановление доступа была отправлена на такой-то email адрес. Этот email адрес привязан к аккаунту который создал эту короткую ссылку bit.ly.
    ''')
            skip()
        elif acc == '15':
            print('''
1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID, qq_uID, fb_uID, Instagram, Twitter, сайт, Facebook
2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
Дополнительные методы

1. Найти профиль автора блога
[1] Откройте исходный код страницы блога (Ctrl+U)
[2] Найдите там фразу https://www.blogger.com/profile/
 ''')
            skip()
        elif acc == '16':
            print('''
1. https://www.chess.com/callback/recover-password-data/USERNAME — найдет часть почты аккаунта, в ссылке замените USERNAM
    ''')
            skip()
        elif acc == '17':
            print('''
1. clubhousedb.com (https://clubhousedb.com/) — дата регистрации, био, соц. сети, группы, кто пригласил
    ''')
            skip()
        elif acc == '18':
                print('''
    (https://cutt.ly/)
    1. Найти полную ссылку

    [1] Добавьте в конец ссылки знак @
    [2] Откройте эту ссылку. Пример: https://cutt.ly/gsuite@
        ''')
                skip()
        elif acc == '19':
            print('Что известно в Discord?')
            print('[1]Пользователь, [2]Сервер')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
Поиск по ID аккаунта Discord

1. support.discord.com (https://support.discord.com/hc/ru/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) — инструкция как найти Discord ID аккаунта
2. discord.id — показывает дату создания аккаунта и фото
3. @DiscordSensorbot — найдет удаленные сообщения, аватарки, сервера, друзей и никнеймы пользователя
4. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет профили на сторонних ресурсах, сообщения пользователя, его имена, сервера и прочее


Через URL

1. https://top.gg/user/1234567890987654321 — находит в каких серверах состоит, фото, описание профиля, и прочее, замени 1234567890987654321 на Discord ID аккаунта


По имени аккаунта Discord

1. discord-tracker.com (https://discord-tracker.com/onetime-functions/all/)  — найдет Discord ID и прочее
    ''')
                skip()
            elif popa == '2':
                print('''
Поиск по названию сервера

1. discordservers.com — дает ссылку на вступление
2. discord.center — дает ссылку на вступление, в базе 36К серверов
3. disboard.org — дает ссылку на вступление, в базе 700К+ серверов
4. discord.me — дает ссылку на вступление, в базе 30К+ серверов
5. discordbee.com — дает ссылку на вступление, в базе 5К+ серверов


Через URL

1. https://mee6.xyz/leaderboard/735708716128796763 — найдет аватарку сервера, участников сервера, замените 735708716128796763 на ID сервера


Парсеры

1. dht.chylex.com — загрузит историю выбранного текстового канала до первого сообщения и позволит вам загрузить его для просмотра в автономном режиме в вашем браузере
2. exportcomments.com (https://exportcomments.com/export-discord-conversation) — экспортирует весь чат из вашего канала Discord в файл CSV
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '20':
            print('''
    1. Как найти аккаунт на Facebook

    [1] Откройте профиль пользователя в браузере
    [2] Перейдите в исходный код страницы
    [3] Найдите там фразу graph.facebook.com и скопируйте длинное число после этого фрагмента
    [4] Подставьте это число в ссылку вместо USERID и перейдите по ней
    https://www.facebook.com/profile.php?id=USERID
    ''')
            skip()
        elif acc == '21':
            print('''
Поиск по аккаунту eBay

1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт


Поиск через URL

1. https://www.ebay.com/sch/ebayadvsearch/?_ec=104&_sofindtype=25&_userid=USERNAME — замените USERNAME на имя пользователя, отображает непонятно что

2. https://www.ebay.com/fdbk/feedback_profile/USERNAME — замените USERNAME на имя пользователя, отображает отзывы пользователя

3. https://www.ebay.com/usr/USERNAME замените USERNAME на имя пользователя, отображает дату создания аккаунта и страну заказчика


Восстановление доступа

1. ebay (https://signin.ebay.com/ws/eBayISAPI.dll?SignIn)
        ''')
            skip()
        elif acc == '22':
            print('''
    1. www.webfx.com (https://www.webfx.com/tools/idgettr/) — находит ID аккаунта
    ''')
            skip()
        elif acc == '23':
            print('''
    Найти упоминание пользователя

    [1] В адресе страницы пользователя скопируйте md5 хеш почты
    [2] Ищите по этому хешу md5 в поисковиках интернета вещей, список поисковиков - /se_iot
    ''')
            skip()
        elif acc == '24':
            print('Что известно в Google?')
            print('[1]Аккаунт, [2]Документ в Google Drive')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
    1. 🎖@UniversalSearch — найдет архивную копию профиля на google plus, и профиль на гугл картах с отзывами
    2. Ghunt (https://github.com/mxrch/GHunt) — найдёт имя аккаунта, возможно фото и почту
    Через URL

    1. https://www.google.com/maps/contrib/1234567890987654321 — найдет профиль на Google картах, замените в ссылке 1234567890987654321 на GAIA ID
    2. https://web.archive.org/web/*/plus.google.com/1234567890987654321 — найдет архивную копию профиля Google Plus, замените в ссылке 1234567890987654321 на GAIA ID
    ''')
                skip()
            elif popa == '2':
                print('''
Для документа в Google Drive

Пример документа: https://docs.google.com/spreadsheets/d/1DvZUE3tXJMFzZVElo5tLiFnis-ocDY4Y85CRzmx0nlU/view

1. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — даст прямые ссылки на архивную копию в Wayback Machine, кеш поисковиков и прочее


Дополнительные методы

1. Как найти почту владельца Google документа 

[1] Перейди в телефоне по ссылке на документ в приложение Документы/Таблицы/Диск от Google
[2] Нажми назад и вернись в список недавних документов 
[3] Нажми на ••• возле нужного документа и выбери Пожаловаться 

В самом низу списка появится адрес почты. Так вы гарантировано получите адрес почты владельца документа. Даже если он везде скрыт
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '25':
            print('Что известно в GitHub?')
            print('[1]Аккаунт, [2]Репризиторий')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
    1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    2. socid_extractor (https://github.com/soxoj/socid_extractor) (t) — найдет user ID
    3. gitcolombo (https://github.com/soxoj/gitcolombo) (t) — извлекает информацию о людях из репозиториев git
    4. thedatapack.com (https://thedatapack.com/tools/find-github-user-email/) — находит email адреса
    5. AmazingHiring (https://chrome.google.com/webstore/detail/amazinghiring/didkfdopbffjkpolefhpcjkohcpalicd) — расширение для браузера Chrome, дает профили в Facebook, LinkedIn, Gravatar и прочих
    6. nazifbara.com (https://repostimeline.nazifbara.com/) — покажет временную шкалу пользователя с изменениями: фотки, новые репозитории 
    7. emailaddress.github.io — найдет email


    Парсеры

    1. phantombuster.com (https://phantombuster.com/phantombuster?category=github) (r) — скачает всю публичную информацию аккаунта


    Поиск через URL

    1. https://api.github.com/users/USERNAME/events/public — покажет почту на которую зарегистрирован аккаунт, замените USERNAME на юзернейм аккаунта. После загрузки страницы нажмите Ctrl+F и введите email
    ''')
                skip()
            elif popa == '2':
                print('''
    1. Найти кто первый постпвил звёздочку в репозитории

    [1] Откройте и скопируйте скрипт
    [2] Перейдите в Graph explorer и войдите в свой аккаунт
    [3] Вставьте код из скрипта который вы скопировали вместо того что есть в первом поле
    [4] Замените sherlock-project на имя владельца репозитория. Замените sherlock на имя репозитория
    [5] Нажмите на треугольник начать

    Вы получите список пользователей кто первый лайкнул репозиторий
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '26':
            print('''
    1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID
    2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    ''')
            skip()
        elif acc == '27':
            print('''
    Восстановление доступа

    1. huawei.com
    2. cloud.huawei.com
    ''')
            skip()
        elif acc == '28':
            print('''
    Восстановление доступа

    1. icq.com
    ''')
            skip()
        elif acc == '29':
            print('''
    1. Узнать Email адрес
    [1] Поменяйте USERNAME в ссылке на username аккаунта
    https://keybase.io/USERNAME/pgp_keys.asc
    [2] Если по полученной ссылке PGP ключ есть, то скопируйте весь текст с сайта и вставьте его на сайт который достает почту из PGP ключа, например peegeepee
    ''')
            skip()
        elif acc == '30':
            print('''
    1. https://ws2.kik.com/user/username — дата изменения изображения аккаунта и ссылка на него, замените username на имя пользователя
    ''')
            skip()
        elif acc == '31':
            print('''
    Поиск по аккаунту LinkedIn

    1. icwatch.wikileaks.org — поиск по имени аккаунта LinkedIn из США, находит утекшую информацию, телефоны, почту 
    2. rocketreach.co (https://rocketreach.co/person)  — введите URL адрес в строку поиска и сервис даст соцсети, телефоны и другие данные
    3. Nubela.co (https://nubela.co/proxycurl/demo/linkedin-email-finder) — покажет часть почты, если зарегистрироваться то можно получить полную почту и телефон используя API этого сервиса


    Предосмотр страницы

    1. Nubela.co (https://nubela.co/proxycurl/demo/linkedin-profile-viewer) — покажет часть профиля анонимно


    Парсеры

    1. phantombuster.com (https://phantombuster.com/automations/linkedin/3112/linkedin-profile-scraper)  — скачает всю публичную информацию аккаунта
    2. raven (https://github.com/0x09AL/raven)  — сбор информации о сотрудниках организации из Google


    Дополнительные методы

    1. Почтовый индекс. 
    [1] Перейдите на страницу аккаунта
    [2] Откройте исходный код страницы (Ctrl+U)
    [3] Найдите (Ctrl+F) там строку с postalCode
    цифры после и есть почтовый индекс
''')
            skip()
        elif acc == '32':
            print('''
    1. @LZTbot — даст email, часовой пояс, ник и возможно номер телефона
    ''')
            skip()
        elif acc == '33':
            print('Что известно в Minecraft?')
            print('[1]Никнейм, [2]UUID')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
    1. namemc.com (https://namemc.com/) — найдет UUID аккаунта, историю изменения имени, любимые сервера, аватар, скин, ссылку на аккаунт Discord и прочее
    2. MineSight (https://github.com/Gobutsu/MineSight) — дает дату последней активности профиля, историю юзернеймов, язык, социальные сети и прочее    
    ''')
                skip()
            elif popa == '2':
                print('''
    1. namemc.com (https://namemc.com/) — найдет ник аккаунта, историю изменения имени, любимые сервера, аватар, скин, ссылку на аккаунт Discord и прочее
    2. skidsearch.net (https://skidsearch.net/) — в утечке найдет IP адрес, название слитой базы, на сайте выбери тип поиска по UUID
    3. MineSight (https://github.com/Gobutsu/MineSight) — дает дату последней активности профиля, историю юзернеймов, язык, социальные сети и прочее
    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '34':
            print('''
    1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID
    ''')
            skip()
        elif acc == '35':
            print('''
    1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID, Twitter username, Facebook ID аккаунта
    2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    ''')
            skip()
        elif acc == '36':
            print('''
    1. stratege.ru (https://www.stratege.ru/site_search) — находит статистику аккаунта, коллекцию игр, профили в других играх
    ''')
            skip()
        elif acc == '37':
            print('''
    1. fansmetrics.com (https://fansmetrics.com/) — дает число подписчиков, социальные сети, и прочее
    ''')
            skip()
        elif acc == '38':
            print('''
    1. Pastebin-bisque (https://github.com/bbbbbrie/pastebin-bisque) — скачает все pastes пользователя
    ''')
            skip()
        elif acc == '39':
            print('''
    1. graphtreon.com (https://graphtreon.com/) — статистика патронов и примерный доход
    2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    ''')
            skip()
        elif acc == '40':
            print('''
    1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    ''')
            skip()
        elif acc == '41':
            print('''
    1. stratege.ru (https://www.stratege.ru/site_search) — находит статистику аккаунта, коллекцию игр, профили в других играх
    ''')
            skip()
        elif acc == '42':
            print('''
    1. @DATA_007bot — дает номер телефона
    2. @sgk2023_03_30bot — дает номер телефона, пароль и адрес электронной почты
    3. @XingDun2Bot (https://t.me/XingDun2Bot?start=XZp6Gb) — найдет имя, профили, адрес, пол, для бесплатного поиска пригласите 5 пользователей по вашей реферальной ссылке
    ''')
            skip()
        elif acc == '43':
            print('Что известно на Reddit?')
            print('[1]Аккаунт, [2]Сабреддит')
            popa = input('[@]Select >')
            if popa == '1':
                print('''
    Поиск по аккаунту на Reddit

    1. reddit-user-analyser (https://atomiks.github.io/reddit-user-analyser/) — анализатор аккаунта
    2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    3. socid_extractor (https://github.com/soxoj/socid_extractor)  — найдет user ID акаунта
    4. redditcommentsearch.com — найдет все комментарии пользователя
    5. search.pullpush.io — покажет почти все удаленные посты и комментарии пользователя
    6. redective.com — статистика аккаунта, частые слова, сабредиты и время активности профиля
    7. redditmetis.com — анализ сообщений профиля, интересы, пол, статистика сообщений и прочее
    8. r00m101.com — ИИ анализ, даст интересы, пол, уровень дохода, хобби и прочее 


    Поисковики

    1. search.pullpush.io — поиск во всех комментариях и постах пользователя, в том числе удаленных, есть фильтры по дате


    Парсеры

    1. apify.com (https://apify.com/trudax/reddit-scraper)  — скачает посты, комментарии, пользователей
    2. redditdownloader.github.io — скачает посты, медиа пользователя


    Поиск через URL

    1. https://pholder.com/u/USERNAME — сохраненные посты аккаунта, замените USERNAME    ''')
                skip()
            elif popa == '2':
                print('''
    Поиск по сабреддиту

    1. subredditstats.com — статистика комментариев, подписчиков, сообщений, ключевых слов, связанные сабреддиты
    2. highervisibility.com (https://www.highervisibility.com/free-seo-tools/keyworddit/) — покажет наиболее часто упоминаемые ключевые слова
    3. ebof1223-reddit-timer.netlify.app — покажет график активности по времени и дате 


    Поисковики

    1. search.pullpush.io — поиск во всех комментариях и постах сабредита, в том числе удаленных, есть фильтры по дате


    Парсоры

    1. apify.com (https://apify.com/trudax/reddit-scraper)  — скачает посты, комментарии, пользователей
    2. redditdownloader.github.io — скачает медиа сабреддита


    Инструменты

    1. @AximoBot — сохранит новые публикации сабредита в Telegram

    ''')
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif acc == '44':
            print('''
    1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID
    2. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    ''')
            skip()
        elif acc == '45':
            print('''
    1. mostwantedhf.info (http://mostwantedhf.info/skype2email.php) — найдет почту
    2. webresolver.nl (https://webresolver.nl/) — найдет IP
    3. @UsersBox (https://t.me/UUserBBoxBBot) — находит номер телефона, почту и много еще, бесплатный поиск для новых аккаунтов
    4. vedbex.com (https://www.vedbex.com/tools/skype_resolver) — найдет IP
    5. skypeipresolver.net (https://skypeipresolver.net/) — найдет IP, работает с VPN
    ''')
            skip()
        elif acc == '46':
            print('''
    1. archive.org (https://archive.org/) — покажет архивированную версию аккаунта, пришли ссылку на аккаунт
    ''')
            skip()
        elif acc == '47':
            print('''
    1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID и stack_exchange_uid
    2. cse.google.com (https://cse.google.com/cse?cx=partner-pub-7396620608505330:xjbbr6-w0cu) — найдет упоминания на сайте Stackoverflow
    ''')
            skip()
        elif acc == '48':
            print('''
    1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    2. socid_extractor (https://github.com/soxoj/socid_extractor)  — найдет Steam ID, даже скрытого аккаунта
    3. steamid.uk — поиск по Steam ID, логину, Steam3, Community ID, найдет историю ников, дату создания, историю аватаров, статистику друзей
    4. rep.tf — агрегирует информацию об аккаунте из разных источников
    5. steamidfinder.com (https://steamidfinder.com/lookup/) — кешированная информация аккаунта
    6. steamid.io — найдет все ID, старый кастомный URL, имя и локацию
    7. findsteamid.com — найдет все ID, картинку аккаунта и дату его создания
    8. steamdb.info — найдет все ID, операционную систему и другое
    9. Steam-OSINT-TOOL (https://github.com/matiash26/Steam-OSINT-TOOL)  — покажет с какими другими аккаунтами Steam взаимодействовал искомый профиль, список публичных комментариев
    10. steamdb.info (http://steamdb.info/calculator/) — посчитает сколько потратил пользователь Steam на игры, даст статистику
    11. SteamHistory.net — история имени, история аватаров, история друзей, история комментариев и прочее
    12. Logs.tf — история матчей в игре TeamForces2
    13. Trends.tf — история имен в игре TeamForces2 и подробная статистика игрока
    14. rgl.gg — матчи в игре TeamForces2, может показать архивное имя и аватарку
    15. UgcLeague.com (https://www.ugcleague.com/playersearch.cfm) — найдет страну пользователя, отображается флаг возле имени пользователя, и прочее
    16. Сltf2.com (https://www.cltf2.com/users) — история вступления в команды TF2, покажет лиги и посты на форуме    ''')
            skip()
        elif acc == '49':
            print('''
    Для рабочего места в Slack

    1. SlackPirate (https://github.com/emtunc/SlackPirate) — агригирует пароли, адреса почт, и другую полезную информацию
    ''')
            skip()
        elif acc == '50':
            print('''
    1. www.tumbex.com (https://www.tumbex.com/) — покажет удаленные посты если они есть
    ''')
            skip()
        elif acc == '51':
            print('''
    Для аккаунта Twitch

    1. cipher387.github.io (https://cipher387.github.io/quickcacheandarchivesearch/) — покажет архивированную страницу, даст 20+ прямых ссылок на сайты веб архивы, поиск по ссылке на аккаунт
    2. twitchtracker.com — аналитика активности аккаунта, история трансляций, дата создания аккаунта и многое другое
    3. sullygnome.com — статистика, история стримов, лайки, подписчики и другое
    4. twitchdatabase.com (https://www.twitchdatabase.com/following) — покажет на какие каналы подписан пользователь
    5. pogu.live — сохраняет удаленные эфиры и стримы
    6. streamscharts.com (https://streamscharts.com/tools/followage) — найдет на какие каналы подписан пользователь
    7. tools.2807.eu — покажет на кого подписан аккаунт/канал


    Парсеры

    1. twitch-tools.rootonline.de (https://twitch-tools.rootonline.de/followerlist_viewer.php) — скачивает всех подписчиков, показывает статистику дат созданий аккаунтов, дает поиск по всему списку


    Инструменты

    1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram    ''')
            skip()
        elif acc == '52':
            print('''
    1. Найти полную ссылку

    [1] Добавьте в конец ссылки знак =
    [2] Откройте эту ссылку. Пример: https://tiny.cc/t1a1tz=

    2. Найти статистику

    [1] Добавьте в конец ссылки знак ~
    [2] Откройте эту ссылку. Пример: https://tiny.cc/t1a1tz~
    ''')
            skip()
        elif acc == '53':
            print('''
    1. Найти полную ссылку

    [1] Добавьте в конец ссылки знак !
    [2] Откройте эту ссылку. Пример: https://tiny.pl/9jkhm!
    ''')
            skip()
        elif acc == '54':
            print('''
    1. Найти полную ссылку

    [1] В ссылке добавьте preview. перед tinyurl.com
    [2] Откройте эту ссылку. Пример: https://preview.tinyurl.com/y53y8oq6
    ''')
            skip()
        elif acc == '55':
            print('''
    1. socid_extractor (https://github.com/soxoj/socid_extractor) — найдет user ID
    ''')
            skip()
        elif acc == '56':
            print('''
    1. @vimebasebot — найдет в утечке почту, IP адрес, пароли статистику аккаунта
    ''')
            skip()
        elif acc == '57':
            print('''
    1. @DATA_007bot — дает номер телефона
    2. @sgk2023_03_30bot — дает номер телефона
    3. @XingDun2Bot (https://t.me/XingDun2Bot?start=XZp6Gb) — найдет имя, профили, адрес, пол, для бесплатного поиска пригласите 5 пользователей по вашей реферальной ссылке
    ''')
            skip()
        elif acc == '58':
            print('''
    1. whatsapp-osint (https://github.com/jasperan/whatsapp-osint) — программа, отслеживает онлайн активность профиля
    ''')
            skip()
        elif acc == '59':
            print('''
    Восстановление доступа

    1. Xiaomi (https://account.xiaomi.com/pass/retrieve/applyManualRetrieve)
    ''')
            skip()
        elif acc == '60':
            print('''
    1. stratege.ru (https://www.stratege.ru/site_search) — находит статистику аккаунта, коллекцию игр, профили в других играх
    2. xboxgamertag.com (https://xboxgamertag.com/) — покажет в какие игры и когда играл пользователь
    ''')
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == '3':
        print('Какой почтовый сервис? Почтовый сервис указан после знака @ в адресе почты')
        print('''
┌─────────────────┬──────────────────┬
│ [ 1] Aol        │ [ 8] Web.de      │ 
│ [ 2] Gmail      │ [ 9] Rambler     │ 
│ [ 3] Mail.ru    │ [10] Yandex      │ 
│ [ 4] ProtonMail │ [11] Любая почта │
│ [ 5] Yahoo      │                  │
│ [ 6] QQ         │                  │
│ [ 7] GMX.net    │                  │
└─────────────────┴──────────────────┴

''')
        poc  = input('[@]Select >')
        if poc == "1":
            print('''
Восстановление доступа

1. Aol (https://login.aol.com/)
''')
            skip()
        elif poc == "2":
            print('''
Поиск по Email от Gmail

1. GHunt (https://github.com/mxrch/GHunt) (t) — инструмент достанет Google ID, устройства, имя аккаунта, найдет какие сервисы Google используется, данные из отзывов на Google картах
2. /email — список ресурсов для поиска по Email адресу любого почтового сервиса


Поиск через URL

1. https://calendar.google.com/calendar/u/0/embed?src=LOGIN@gmail.com — календарь с записями, замените LOGIN@gmail.com на email адрес Gmail


Восстановление доступа

1. Aol
 (https://login.aol.com/)2. Google (https://accounts.google.com/signin/v2/identifier) — покажет часть телефона, бренд устройства, уведомляет
''')
            skip()
        elif poc == "3":
            print('''
Поиск по Email от Mail.ru / inbox.ru / bk.ru / list.ru

1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса


Поиск через URL

1. https://love.mail.ru/ru/LOGIN — профиль на сайте знакомств, замените LOGIN на email адрес без @mail.ru
2. https://account.mail.ru/api/v1/user/password/restore?email=LOGIN@mail.ru — выдаст часть номера телефона, замените LOGIN на email адрес без @mail.ru, попробуйте поменять @mail.ru на @list.ru, @bk.ru, @inbox.ru
''')
            skip()
        elif poc == "4":
            print('''
Дополнительный методы

1. Как найти дату создания ProtonMail адреса

[1] Создайте или войдите в аккаунт на old.ProtonMail.com
[2] Откройте контакты (https://mail.protonmail.com/contacts) и нажмите на добавить контакт 
[3] В поле E-mail введите E-mail адрес ProtonMail
[4] Возле адреса появится шестеренка на которую нужно нажать
''')
            skip()
        elif poc == "5":
            print('''
Восстановление доступа

1. Aol
 (https://login.aol.com/)2. Yahoo (https://login.yahoo.com/?display=login)
''')
            skip()
        elif poc == "6":
            print('''
Поиск по Email почтового сервиса QQ.com

1. @sgk2023_03_30bot —  находит аккаунт QQ, его ID, имя пользователя и пароль
2. DetectDee (https://github.com/piaolin/DetectDee/) (t) — покажет в каких сервисах зарегистрирована почта, найдет профили
''')
            skip()
        elif poc == "7":
            print('''
Восстановление доступа

1. GMX (https://passwort.gmx.net/passwordrecovery)
''')
            skip()
        elif poc == "8":
            print('''
Восстановление доступа

1. Web.de (https://passwort.web.de/passwordrecovery/)
''')
            skip()
        elif poc == "9":
            print('''
Поиск через URL

1. https://avatars.rambler.ru/get/LOGIN@rambler.ru/default — картинка аккаунта, замените LOGIN@rambler.ru на email адрес
''')
            skip()
        elif poc == "10":
            print('''
1. Найти логин Яндекс почты если он скрыт номером телефона

Пример: 
По почте 79613502038@yandex.ru 
получить cyk4666@yandex.ru

[1] Перейдите в calendar.yandex.ru/event
[2] Найдите поле Участники
[3] Введите адрес Яндекс почты которая состоит из номера телефона


Поиск через URL

1. https://music.yandex.ru/users/LOGIN —  аккаунт в Яндекс Музыке, содержит имя и фото аккаунта. Замените LOGIN на юзернейм из адреса почты БЕЗ @yandex.ru
''')
            skip()
        elif poc == "11":
            print('''
1. haveibeenpwned.com — скажет с каких базах утекла почта
2. emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту
3. dehashed.com  — проверка почты в слитых базах
4. intelx.io — ищет в утечках, Tor, I2P и в крупных базах
5. @InfoBaza (https://t.me/xx3738373_bot) — бесплатно найдет часть ФИО и телефона гражданина Украины
6. MostWantedHF (https://mostwantedhf.info/email.php) — найдет аккаунт skype
7. email2phonenumber (https://github.com/martinvigo/email2phonenumber)  — автоматически собирает данные со страниц восстановления аккаунта, и находит номер телефона
8. @avinfo (https://t.me/avinfo?start=ref987328) — найдет аккаунт ВК и прочее,  для бесплатного поиска есть канал @avinfopro с промо для поиска без оплаты
9. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — найдет фото из аккаунтов пользователя и прочее
10. cyberbackgroundchecks.com (http://www.cyberbackgroundchecks.com/email) — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США
11. holehe (https://github.com/megadose/holehe) — инструмент проверяет аккаунты каких сайтов зарегистрированы на искомый email адрес, поиск по 30 источникам
12. tools.epieos.com — найдет Google ID, даст ссылки на профиль в Google карты, альбомы и календарь, найдет к каким сайтам привязана почта, профиль LinkedIn
13. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет профили, пароли, почты, ещё ищет в других ботах
14. rocketreach.co  — выдает имя, профили в социальных сетях, почты, часть телефона, и прочее
15. avatarapi.com — найдет аватар и никнейм из множества источников
16. WhoisXmlApi (https://tools.whoisxmlapi.com/reverse-whois-search#captcha=01955671254)  — найдет домены сайтов, поиск в истории whois
17. @LeakCheck (https://t.me/LeakCheck1_Bot) — покажет на каких сайтах утекли пароли
18. @Vbiv (https://t.me/Vbib_bot)  — выдаст ссылку на профиль Facebook
19. Melissa (https://www.melissa.com/v2/lookups/personator) — найдет ФИО, дату рождения, адрес проживания, этнос и прочее гражданина США
20. leak-lookup (https://leak-lookup.com/search)  — покажет на каких сайтах была утечка с искомым email
21. SpyDialer.com — находит имя владельца почты
22. X-Ray (https://x-ray.contact/platform/search/)  — поиск в русском сегменте утечек, найдет номер телефона, социальные сети, больше адресов почт, вход из России запрещён, нужен VPN
23. community.riskiq.com  — найдет сайты и домены у которых в whois искомый email адрес
24. 2ip.ru (https://2ip.ru/domain-list-by-email/) — найдет доменные имена сайтов, в whois которых, есть запись с искомым email адресом
25. SaveRuData (https://data.intelx.io/saverudata) — покажет из утечек полный адрес, имя, все из сервиса Яндекс Еда, СДЕК, аккаунт ВК, траты на еду за 6 месяцев, работает только с VPN
26. ScamSearch (http://scamsearch.io/#/search.php?f=1&hover_cle=yes&vm=01955671254&type=email)  — реестр мошенников, найдет bitcoin адрес, причину внесения в реестр, номер телефона, дату и прочее
27. @Detectiva (https://t.me/reserv_detectiva_bot) — найдет имена, телефоны и прочее в утечках
28. @OsintKit (https://t.me/@osintkit_check_bot) — ищет в утечках, дает имена, адреса, телефоны и много другого
29. osint.industries  — находит профили Skype, канал YouTube, Airbnb и другие, покажет где зарегистрирована, и где утекла
30. TruePeopleSearch.com — ищет сведения о гражданине США, выдает имя, адрес проживания, родственников и прочее, сайт доступен только с IP адреса США, используй VPN
31. reversecontact.com — выдаст LinkedIn аккаунт, а после регистрации ссылку на него
32. @IntelSec (http://t.me/intelligencesecurityiobot) — ищет в логах, находит сайт, логин Россиии пароль для входа, есть бесплатный запрос. В боте нажмите download file и введите почту, после качайте найденный файл, и в нем будет вся информация
33. @HomoSpiens (https://t.me/findHOMOrobot) — ищет в утечках, в архивах с 1921 года, дает адреса, почту и прочее
34. @Sherlok (https://t.me/x8152384_bot) — ищет в утечках, находит адреса, имена и прочее
35. @PasswordSearch (https://t.me/PasswordSearchBot) — найдет пароли из утечек
36. MinervaOSINT (https://minervaosint.com/)  — найдет аккаунты на большинство платформах, даст знать где есть регистрация, часть данных из восстановления пароля и прочее. Один запрос в день бесплатно.
37. IntelBase (https://intelbase.is/) — найдет аккаунты, даст знать где есть регистрация и прочее


Восстановление доступа

1. Etsy (https://www.etsy.com/join/email?ref=hdr-signin&from_action=signin-header&from_page=https%3A%2F%2Fwww.etsy.com%2F) — даст имя, аватар
2. ebay (https://signin.ebay.com/ws/eBayISAPI.dll?SignIn) — даст часть телефона
3. Apple (https://iforgot.apple.com/password/verify/appleid) — даст часть телефона
4. Yahoo (https://login.yahoo.com/?display=login) — даст часть почты, телефона
5. Adobe (https://account.adobe.com/) — даст часть почты, телефона
6. PayPal (https://www.paypal.com/authflow/password-recovery/) — даст часть телефона, карты
7. Mail.ru (https://account.mail.ru/recovery/) — даст часть телефона
8. Xiaomi (https://account.xiaomi.com/pass/retrieve/applyManualRetrieve) — даст часть ID аккаунта
9. Realme (https://id.realme.com/v2/find_password.html) — даст часть телефона, уведомляет
10. Huawei (https://id8.cloud.huawei.com/AMW/portal/appealSelf/applyChangeAccount.html) — даст возможные устройства
11. live.com (https://account.live.com/password/reset) — даст часть телефона
12. Ozon.ru — даст часть телефона, уведомляет
13. Samsung (https://account.samsung.com/accounts/odchb/resetPasswordGate?locale=ru_RU&clientId=j5p7ll8g33&countryCode=RUS&deepLinkMode=signIn&goBackMoveUri=samsungaccount:%2F%2FSignIn&state=accountcheckdogeneratedstatetext) — даст часть телефона
14. Facebook (https://www.facebook.com/login/identify?ctx=recover) — даст часть телефона, второй почты, имени
''')
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == '4':
        print('ФИО гражданина какой страны?')
        print('''
[1]России         | [8]Бразилии        | [15]Греции       | [22]Италии      | [29]Литвы          | [36]Польши        | [43]Турции        | [50]Швейцарии
[2]Казахстана     | [9]Бельгии         | [16]Дании        | [23]Канады      | [30]Люксембурга    | [37]Португалии    | [44]Таджикистана  | [51]Швеции
[3]Украины        | [10]Болгарии       | [17]Индии        | [24]Кипра       | [31]Мальты         | [38]Приднестровье | [45]Узбекистана   | [52]Эстонии
[4]Австралии      | [11]Великобритании | [18]Индонезии    | [25]Киргизии    | [32]Молдовы        | [39]Румынии       | [46]Франции       | [53]Южной Кореии
[5]Австрии        | [12]Венгрии        | [19]Ирландии     | [26]Китая       | [33]Нидерландов    | [40]Словакии      | [47]Финляндии     | [54]Японии
[6]Аргентины      | [13]Германии       | [20]Исландии     | [27]Кубы        | [34]Норвегии       | [41]Словении      | [48]Хорватии      |
[7]Беларуси       | [14]Гонконга       | [21]Испании      | [28]Латвии      | [35]Новой Зеландии | [42]США           | [49]Чехии         |
    ''')
        fio  = input('[@]Select >')
        if fio == "1":
            print('''
Поиск по ФИО гражданина России

1. @egrul_bot — найдет ИП и компании
2. reestr-zalogov.ru — поиск в реестре залогодателей, даст паспортные данные, место и дату рождения и т.д.
3. kad.arbitr.ru — найдет дела арбитражных судов
4. bankrot.fedresurs.ru — поиск в реестре банкротов, можно узнать ИНН, СНИЛС и адрес
5. spra.vkaru.net — телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове
6. fssp.gov.ru — проверка задолженностей, для физ. лица, нужно ввести дату рождения
7. reestr-dover.ru — поиск в списке сведений об отмене доверенности
8. notariat.ru — поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дело
9. 🪦@ГлазБога (r) — обратный поиск в GetContact, находит часть номера телефона
10. nalog.ru — найдет ИНН, необходимо указать дату рождения и паспортные данные, дату выдачи не обязательно верно
11. bigbookname.com — находит древние данные профилей ВК, есть фильтры по дате рождения, по стране и городу12. notariat.ru — если человек умер, то найдет дату смерти, номер наследственного дела, где оно было открыто и каким нотариусом 
13. wordstat.yandex.ru — покажет что ищут вместе с ФИ или ФИО в Яндексе
14. news.myseldon.com — находит упоминания в российских СМИ, строит дерево связей между медийными объектами, которое образуются на основе их совместного упоминания в тексте новости
15. list-org.com — найдет организацию в учредителях и руководителях
16. list-org.com — найдет предпринимателя, его госзакупки, дерево связей
17. elections.istra-da.ru — реестр кандидатов на выборы, есть более миллиона человек, найдет судимости, дату рождения, место жительства и работы, должность, образование и прочее
18. SaveRuData — покажет, полный адрес, телефон, почту, имя, все из сервиса Яндекс Еда, СДЕК, иногда работает через VPN, вводи фамилию и листай результаты
19. domspravka.com — найдет адрес регистрации, нужно указывать город20. declarator.org — реестр должностных лиц, покажет доходы, штук авто, площадь и количество недвижимости, должность и место работы
21. rupep.org — реестр публичных деятелей, найдет ИНН, дату рождения, место рождения, историю карьеры, декларации, авто, площадь недвижимости, связанные юр. лица
22. @OsintKit  — ищет в утечках, дает имена, адреса, почты и много другого
23. nalog.gov.ru — реестр должников, найдет ИНН, судебное дело, и прочее, вводите ФИО в поле для ответчика, а после и в поле для должника 
24. nalog.gov.ru — реестр субсидиарной ответственности, найдет судебные решения
25. @HomoSpiens — ищет в утечках, в архивах с 1921 года, дает адреса, почту и прочее
26. @Sherlok — из утечек достанет адреса, телефоны, инн, и прочее

Инструменты

1. translit.net — переведёт ФИО из кириллицы в латиницу и наоборот


Через URLhttps://www.gosuslugi.ru/api/posobie16/v1/orders/snils/lookup?lastName=ФАМИЛИЯ&firstName=ИМЯ&middleName=ОТЧЕСТВО&birthDate=ГГГГ-ММ-ДД — найдет СНИЛС гражданина до 18 лет, нужно знать дату рождения, замените ГГГГ-ММ-ДД на дату рождения, и Имя, Фамилия, Отчество в ссылке, важно открыть ссылку в браузере, где вы авторизованы в Госуслугах

''')
            skip()
        elif fio == "2":
            print('''
Поиск по ФИО гражданина Казахстана

1. spra.vkaru.net — телефонный справочник
2. fa-fa.kz (https://fa-fa.kz/search_ip_too/) — проверка наличия задолженностей, ИП, и ограничения на выезд
3. @ShtrafKZBot — найдет ИНН, дату рождения и много других данных
4. kgd.gov.kz (http://kgd.gov.kz/ru/services/taxpayer_search_unreliable) — поиск в базе неблагонадежных налогоплательщиков, найдет ИНН/БИН и РНН
5. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — обратный поиск по GetContact, находит часть номера телефона
6. bigbookname.com (https://bigbookname.com/search#) — находит древние данные профилей ВК, есть фильтры по дате рождения, по стране и городу
7. pk.adata.kz — выдаст ИНН в URL, дату рождения предпринимателя
8. @HomoSpiens (https://t.me/findHOMOrobot) — ищет в утечках, в архивах с 1921 года, дает адреса, почту и прочее

''')
            skip()
        elif fio == "3":
            print('''

Поиск по ФИО гражданина Украины

1. minjust.gov.ua (http://erb.minjust.gov.ua/#/search-debtors) — реестр должников, дату рождения, связь с исполнителем, номер ВП, категорию взыскания
2. usr.minjust.gov.ua (https://usr.minjust.gov.ua/content/free-search) — находит место жительства
3. spra.vkaru.net — телефонный справочник
4. data-ua.com (https://court.opendatabot.ua/#/) — поиск в судебных решениях
5. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — обратный поиск по GetContact, находит часть номера телефона, зарегистрированные организации, авто
6. bigbookname.com (https://bigbookname.com/search#) — находит древние данные профилей ВК, есть фильтры по дате рождения, по стране и городу
7. dolg.xyz — находит связанные лица и государственные органы
8. @InfoBaza (https://t.me/xx3738373_bot) — бесплатно найдет часть номера телефона и прочее
9. drrp.app (https://drrp.app/search) — найдёт адрес проживания
10. @OpenDataUABot — найдет собственность, компании, ФЛП, розыск, обязанности, долги, судебные иски
11. @InfoLab (https://t.me/ProbivUniversal_New_Bot) — выдаст паспортные данные, телефоны и прочее, бесплатно покажет только часть данных
12. @HomoSpiens (https://t.me/findHOMOrobot) — ищет в утечках, в архивах с 1921 года, дает адреса, почту и прочее
13. borgu.net.ua — найдет ИП, дату рождения в реестре должников

''')
            skip()
        elif fio == "4":
            print('''

Поиск по ФИО гражданина Австралии

1. personlookup.com.au — найдет адрес, телефон и соседей
2. revenue.nsw.gov.au (https://www.apps09.revenue.nsw.gov.au/erevenue/ucm/ucm_search.php) — база невостребованных денег Нового Южного Уэльса, дает адрес проживания
3. form.act.gov.au (https://form.act.gov.au/smartforms/servlet/SmartForm.html?formCode=1219) — база невостребованных денег ACT, дает адрес проживания
4. pt.qld.gov.au (https://www.pt.qld.gov.au/other-services/unclaimed-money/search-unclaimed-money/)— база невостребованных денег Квинсленда, дает адрес проживания
5. wa.gov.au (https://unclaimedmonies.treasury.wa.gov.au/ums/) — база невостребованных денег Западной Австралии, дает адрес проживания
6. sa.gov.au (https://www.treasury.sa.gov.au/Our-services/unclaimed-money/search-for-unclaimed-money) — база невостребованных денег Южной Австралии, дает адрес проживания
7, www.ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений

''')
            skip()
        elif fio == "5":
            print('''

Поиск по ФИО гражданина Австрии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
3. www.northdata.com — найдет названия компаний в Европе с которыми связано ФИО
4, www.ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений

''')
            skip()
        elif fio == "6":
            print('''

Поиск по ФИО гражданина Аргентины

1. cij.gov.ar (https://www.cij.gov.ar/buscador-de-fallos.html) — найдет судебные дела

''')
            skip()
        elif fio == "7":
            print('''

Поиск по ФИО гражданина Республики Беларусь

1. mmnt.ru — найдет упоминания в документах
2. spra.vkaru.net — телефонный справочник
3. portal.nalog.gov.by (http://www.portal.nalog.gov.by/grp/#!fl) — найдет сведения из гос. реестра плательщиков, такие как УНП и код инспекции, помимо ФИО нужно указать номер документа, удостоверяющего личность
4. service.court.by (http://service.court.by/ru/account/login?returnUrl=%2Fru%2Fjuridical%2Fjudgmentresults) (r) — найдет судебные постановления, при регистрации нет проверки данных
5. bankrot.gov.by (https://bankrot.gov.by/Debtors/DebtorsList/) — поиск в списках должников
6. mtkrbti.by (http://mtkrbti.by/local/TL/Licence.nsf/WEBSearchView1?SearchView) — поиск в базе готовых лицензий, найдет ФИО, адрес, почтовый индекс, УНП, номер транспортной лицензии, срок действия
7. mvd.gov.by (https://www.mvd.gov.by/ru/wanted#Service0329976453) — поиск в базе розыска
8. gr.rcheph.by (http://gr.rcheph.by/) — поиск в  сведениях о государственной регистрации товаров, найдет УНП, название предприятия и наименования продукта
9. egr.gov.by (http://egr.gov.by/egrn/index.jsp?content=Find) — поиск юридических лиц и индивидуальных предпринимателей в базе данных единого государственного регистра
10. justbel.info (https://justbel.info/Liquidation/FindMyRequest) — покажет данные о ликвидации юридических лиц
11. rupep.org — реест публичных деятелей, найдет инн, дату рождения, место рождения, историю карьеры, декларации, авто, площадь недвижимости, связанные юр. лица

''')
            skip()
        elif fio == "8":
            print('''
Поиск по ФИО гражданина Бразилии

1. sei.df.gov.br (https://sei.df.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0) — база юридических документов
2. escavador.com — найдет резюме и судебные иски
3. telenumeros.com — найдет номер телефона, адрес, и полное имя
4. portaltransparencia.gov.br (https://www.portaltransparencia.gov.br/pessoa-fisica/busca/lista?pagina=1&tamanhoPagina=10) — найдет город проживания, номер CPF, суммы кредита
5. falecidosnobrasil.org.br — реестр смертей, найдет дату смерти, имя матери, место смерти


''')
            skip()
        elif fio == "9":
            print('''

Поиск по ФИО гражданина Бельгии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. www.de1212.be — найдет номер телефона и адрес
3. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США

''')
            skip()
        elif fio == "10":
            print('''

Поиск по ФИО гражданина Болгарии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. vivacom.bg (https://www.vivacom.bg/bg/residential/polezni-syveti/ukazatel/telefonni-nomera) — покажет адрес и телефон, необходимо знать город
3. ukazatelite.com — реестр юрлиц, найдет карточку с контактами, адресами, и прочее

''')
            skip()
        elif fio == "11":
            print('''

Поиск по ФИО гражданина Великобритании

1. companieshouse.gov.uk (https://beta.companieshouse.gov.uk/search/officers) — коммерческий поиск, найдет дату рождения, национальность, компании и их адреса
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. www.northdata.com — найдет названия компаний с которыми связано ФИО
4. www.ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений
5. ukcensusonline.com (https://ukcensusonline.com/search/) — реестр переписи, рождений, браков и смерти с 1841 по 1911 годы, найдет даты, профессии, округа и полные имена
6. openpaymentsdata.cms.gov — платежи медицинских работников, найдет статистику по переводам, покажет финансирование, инвестиции, платы за исследования, компании, осуществляющие платеж
7. reversepp.com (r) — реестр планирования помещений, найдет адрес, дату и прочее

''')
            skip()
        elif fio == "12":
            print('''

Поиск по ФИО гражданина Венгрии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. telekom.hu (https://www.telekom.hu/lakossagi/tudakozo) — найдет номер телефона и адрес проживания

''')
            skip()
        elif fio == "13":
            print('''

Поиск по ФИО гражданина Германии

1. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
2. dastelefonbuch.de (https://personensuche.dastelefonbuch.de/) — найдет данные из профилей социальных сетей
3. northdata.de — находит должности в компаниях
4. www.northdata.com — найдет названия компаний с которыми связано ФИО
5, www.ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений

''')
            skip()
        elif fio == "14":
            print('''

Поиск по ФИО гражданина Гонконга

1. @sgk2023_03_30bot — найдет ID QQ, Weibo, email, нужно знать дату рождени

''')
            skip()
        elif fio == "15":
            print('''

Поиск по ФИО гражданина Греции

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "16":
            print('''

Поиск по ФИО гражданина Дании

1. datacvr.virk.dk (https://datacvr.virk.dk/data/visninger?) — найдет иностранный адрес
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. statstidende.dk (https://statstidende.dk/messages) — поиск в юридических документах, найдет данные о смене жительства, некрологи и много всего полезного
4. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
5. krak.dk (https://www.krak.dk/) —найдет телефон, местоположение на карте и фото дома

''')
            skip()
        elif fio == "17":
            print('''

Поиск по ФИО гражданина Индии

1. indianfinders.com — найдет возраст и город проживания
2. contactofindia.com (http://www.contactofindia.com/index.php) — найдет город и название компании которой владеет гражданин
3. knowyourgst.com (https://www.knowyourgst.com/gst-number-search/by-name-pan/) — найдет полное имя, компанию, номер GST, PAN и дату регистрации бизнеса

''')
            skip()
        elif fio == "18":
            print('''

Поиск по ФИО гражданина Индонезии

1. mahkamahagung.go.id (https://putusan3.mahkamahagung.go.id/) — найдет упоминание имени в судах, в поиске возмите имя в кавычки

''')
            skip()
        elif fio == "19":
            print('''

Поиск по ФИО гражданина Ирландии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "20":
            print('''

Поиск по ФИО гражданина Исландии

1. ja.is — найдет данные людей и компаний

''')
            skip()
        elif fio == "21":
            print('''

Поиск по ФИО гражданина Испании

1. datoscif.es — найдет компании, суды
2. infocif.economia3.com — найдет в каких компаниях человек является менеджером или директором, для поиска выбери поиск по деректорам
3. empresia.es — найдет в каких компаниях человек является менеджером или директором
4. librebor.me — найдет компанию, где упомянуто имя гражданин

''')
            skip()
        elif fio == "22":
            print('''

Поиск по ФИО гражданина Италии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базу должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
3. paginebianche.it (https://www.paginebianche.it/) — найдет номер телефона и адрес

''')
            skip()
        elif fio == "23":
            print('''

Поиск по ФИО гражданина Канады

1. justice.gov.bc.ca (https://justice.gov.bc.ca/cso/esearch/civil/partySearch.do) — находит судебные дела
2. www.canada411.ca (https://www.canada411.ca/search/) — возраст, номер телефона, адрнс и другое
3. www.ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений
4. wwwapps.tc.gc.ca (https://wwwapps.tc.gc.ca/Saf-Sec-Sur/4/vrqs-srib/eng/vessel-registrations/search) — найдет судно, его статистику, предыдущих владельцев, их адрес
5. openpaymentsdata.cms.gov — платежи медицинских работников, найдет статистику по переводам, покажет финансирование, инвестиции, платы за исследования, компании, осуществляющие платеж
6. justice.gov.bc.ca (https://justice.gov.bc.ca/cso/esearch/criminal/partySearchNew.do) — ищет в реестре преступников, находит документы, дату рождения и прочее
7. canadafinder.ca (https://www.canadafinder.ca/searchnumber.php) — даст телефон, адрес регистрации

''')
            skip()
        elif fio == "24":
            print('''

Поиск по ФИО гражданина Кипра

1. cylaw.org — поиск в базе правовой информации, найдет документы и записи
2. diadiktion.com (http://www.diadiktion.com/diadiktiondirectory-whitepagescyprus.htm) — найдет номер телефона и адрес

''')
            skip()
        elif fio == "25":
            print('''

Поиск по ФИО гражданина Киргизии

1. act.sot.kg (http://act.sot.kg/kg/search) — поиск в базе судебных документов, фамилию нужно ввести два раза, при первом поиске в Тарап 1 (первая сторона), а при втором в Тарап 2
2. www.osoo.kg — поиск в реестре компаний, есть учредители, директора, адреса, доходы и контактные данные
3. minjust.gov.kg (http://register.minjust.gov.kg/register/SearchAction.seam?logic=and&cid=204) — поиск в реестре компаний, находит базовую информацию об организации

''')
            skip()
        elif fio == "26":
            print('''

Поиск по ФИО гражданина Китая

1. @sgk2023_03_30bot — найдет ID QQ, Weibo, email, нужно знать дату рождения
2. s.weibo.com (https://s.weibo.com/user) — поиск по контенту из Weibo
3. zxgk.court.gov.cn (http://zxgk.court.gov.cn/zhzxgk) — судебные дела, в которых упоминается определенное имя, фамилия или название компании
4. qcc.com (r) — найдет компанию
5. cninfo.com.cn (http://www.cninfo.com.cn/new/index) — поиск в акционерах, директорах и руководителях компаний, найдет дату рождения, образование, акции

''')
            skip()
        elif fio == "27":
            print('''

Поиск по ФИО гражданина Кубы

1. @ETECSABD_bot — найдет номер телефона, дату рождения, адрес регистрации
2. @directorio_etecsa_bot — найдет номер телефона, дату рождения, адрес регистрации
3. directorioetecsa.com — найдет номер телефона, дату рождения, адрес регистрации

''')
            skip()
        elif fio == "28":
            print('''

Поиск по ФИО гражданина Лaтвии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела

''')
            skip()
        elif fio == "29":
            print('''

Поиск по ФИО гражданина Литвы

1. spra.vkaru.net — телефонный справочник
2. mmnt.ru — найдет упоминания в документах

''')
            skip()
        elif fio == "30":
            print('''

Поиск по ФИО гражданина Люксeмбурга

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. www.northdata.com — найдет названия компаний с которыми связано ФИО

''')
            skip()
        elif fio == "31":
            print('''

Поиск по ФИО гражданина Мальты

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "32":
            print('''

Поиск по ФИО гражданина Молдовы

1. spra.vkaru.net — телефонный справочник
2. mmnt.ru — найдет упоминания в документах

''')
            skip()
        elif fio == "33":
            print('''

Поиск по ФИО гражданина Нидерландов

1. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
2. telefoonboek.nl (https://www.telefoonboek.nl/personen/) — найдет адрес и номер телефона
3. detelefoongids.nl (https://www.detelefoongids.nl/) — находит номер телефона, адрес и местоположение на карте
4. wiewaswie.nl (https://www.wiewaswie.nl/nl/zoeken/) — голландская генеалогическая база с 17 века

''')
            skip()
        elif fio == "34":
            print('''

Поиск по ФИО гражданина Норвегии

1. proff.no (https://www.proff.no/rolles%C3%B8k?) — поиск по ФИО, найдет город, год рождения, бизнес и роли в бизнесе
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. gulesider.no — выдаст такие данные как телефон, местоположение на карте и фото дома

''')
            skip()
        elif fio == "35":
            print('''

Поиск по ФИО гражданина Новой Зеландии

1. companiesoffice.govt.nz (https://app.companiesoffice.govt.nz/companies/app/ui/pages/individual/search?) — найдет компании, адрес места жительства

''')
            skip()
        elif fio == "36":
            print('''

Поиск по ФИО гражданина Польши

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. northdata.com — найдет названия компаний с которыми связано ФИО
3. dlugi.info — найдет долги, город проживания
4. basia.famula.pl (http://www.basia.famula.pl/en/) — найдет записи от 19 века о крещении, браке, смерти, полные имена и даты, ФИО родителей
5. ri-poland.org (https://jri-poland.org/jriplweb.htm) — реестр еврейских записей от 19 по 20 века, даст полное имя, дату рождения, возраст, место рождения, ФИО родителей, семейный статус, девичью фамилию, род занятий и прочее
6. nazwiska-polskie.pl — по фамилии покажет на карте где чаще всего эта фамилия встречается
7. nlp.actaforte.pl (http://nlp.actaforte.pl:8080/Nomina/Ndistr) — по фамилии покажет на карте где чаще всего эта фамилия встречается
8. mogily.pl (http://mogily.pl/start) — реестр кладбищ, найдет место могилы, дату рождения и смерти, для поиска нажми в правом верхнем углу кнопку с лупой
9. grobonet.com (https://grobonet.com/) — реестр кладбищ, найдет место могилы, дату рождения и смерти
10. ksiegazmarlych24.pl — реестр кладбищ, найдет место могилы, дату рождения и смерти
11. webcmentarz.pl — реестр кладбищ, найдет место могилы, дату рождения и смерти
12. poszukiwani.policja.pl — поиск в базе розыска, найдет фото, характеристику, адрес регистрации и прочее
13. zaginieni.policja.pl — поиск в базе пропавших, найдет фото, характеристику черт лица, и прочее
14. indeksrepresjonowanych.pl (https://indeksrepresjonowanych.pl/int/wyszukiwanie/94,Wyszukiwanie.html) — поиск в базе репрессий, найдет второе имя, дату рождения и причину попадания в реестр 
15. crbr.podatki.gov.pl (https://crbr.podatki.gov.pl/adcrbr/#/wyszukaj) — найдет адрес регистрации предпринимателя, необходимо указать дату рождения, после ресурс даст полное имя, ИНН, KPS, организационная форма, почтовый индекс
16. rps.ms.gov.pl (http://rps.ms.gov.pl/pl-PL/Public#/home) — реестр преступников, совершивших преступления на сексуальной почве, найдет фото, дату рождения, детали дела, место рождения, текущий статус

''')
            skip()
        elif fio == "37":
            print('''

Поиск по ФИО гражданина Португалии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "38":
            print('''

Поиск по ФИО гражданина Приднестровье

1. data2b.md — реестр компаний, найдет директора, наименование организации, адрес, количество работников, филиалы и контакты
2. minfin.gospmr.org (https://minfin.gospmr.org/servisy-i-gosuslugu/prozrachnyj-biznes/) — покажет ИНН, статус, налоговый режим и прочее

''')
            skip()
        elif fio == "39":
            print('''

Поиск по ФИО гражданина Румынии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
3. portal.just.ro (http://portal.just.ro/SitePages/acasa.aspx) — упоминания человека в юридических документах
4. carte-telefoane.info (http://www.carte-telefoane.info/) — найдет индивидуальных предпринимателей их адрес и контактные данные

''')
            skip()
        elif fio == "40":
            print('''

Поиск по ФИО гражданина Словакии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "41":
            print('''

Поиск по ФИО гражданина Словении

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела

''')
            skip()
        elif fio == "42":
            print('''

Поиск по ФИО гражданин США

1. whitepages.com — найдет контактную  и справочную информацию 
2. peekyou.com — найдет публичные записи, Facebook, Instagram, Twitter, Email и изображения
3. fastpeoplesearch.com — аналог WhitePages
4. intelx.io (https://intelx.io/tools?tab=person) — создает ссылки на поисковые системы, которые находят людей
5. yasni.com — находит фото, телефонные номера и адреса, профили в соц. сетях, интересы и много еще чего полезного
6. clustrmaps.com (https://clustrmaps.com/p/) — находит адрес проживания, номер телефона, возраст, место работы, специальность и многое другое
7. xlek.com — поиск в whois и публичных реестрах, найдет много подробностей
8. courtlistener.com (https://www.courtlistener.com/) — найдет судебные дела
9. theknot.com (https://www.theknot.com/registry/couplesearch) — свадебный реестр и веб-сайт пары, год и месяц вводить не обязательно
10. registryfinder.com — реестр свадеб, выпускных и детей
11. thebump.com (https://www.thebump.com/search) — реестр свадеб
12. judyrecords.com — база судебных дела США
13. cyberbackgroundchecks.com (https://www.cyberbackgroundchecks.com/name) — найдет адрес проживания, членов семьи, историю изменения и другое, вход на сайт разрешен только с IP адреса США
14. littlesis.org — база данных, в которой подробно описаны связи между влиятельными людьми и организациями
15. bop.gov (https://www.bop.gov/inmateloc/) — поиск в тюрьмах, найдет возраст, расу, дату освобождения и регистрационный номер
16. inmateinfo.indy.gov (http://inmateinfo.indy.gov/IML) — поиск арестов, найдет дату рождения и освобождения, физические характеристики и другое
17. staterecords.org — найдет возраст, штат и город, можно выбрать любой штат, потом будет поиск по всем сразу
18. findagrave.com — найдет когда умер и где захоронен
19, ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений
20. industrydocuments.ucsf.edu — поиск в документах отраслевых компаний по производству табака, пищи, химии, фармакологии
21. gravelocator.cem.va.gov — ветераны, дата смерти и рождения, звание, крематорий
22. melissa.com (https://www.melissa.com/v2/lookups/personator) — найдет дату рождения, адрес проживания, этнос и прочее
23. radaris.com — выдаёт возраст, профили социальных сетей, судебные решения, адреса проживания и прочее
24. oldphonebook.com — найдет адрес и номер телефона, записи 20-летней давности
25. anywho.com — выдаст адрес проживания, возраст и часть номера телефона
26. stevemorse.org (https://stevemorse.org/ssdi/ssdi.html) — реестр регистрации смерти с 1936 гг. по 2014 гг., найдет дату рождения и смерти, номер SS, штат
27. spydialer.com — найдет номер телефона, имена соседей, членов семьи, город и штат проживания
28. recorder.dupageco.org (https://recorder.dupageco.org/Details.aspx) — найдет налоговые, ипотечные и прочие документы, поиск в округе Ду-Пейдж, штат Иллинойс
29. publicaccountability.org — найдет историю расходов и взносов, адрес проживания, род занятия, сумму
30. smartbackgroundchecks.com — дает адреса, телефоны, биографию, семью, недвижимость, образование, почту, и прочее
31. jailbase.com — найдет аресты, фото судимого и детали
32. ancestrydata.com — находит упоминание в реестрах смертей, рождений, переписи, ДНК, иммиграций, свадеб, семейного дерева, газет, разводов, военных и прочих
33. openpaymentsdata.cms.gov — платежи медицинских работников, найдет статистику по переводам, покажет финансирование, инвестиции, платы за исследования, компании, осуществляющие платеж
34. mugshots.com — поиск в реестре арестованных, найдет фото, физические характеристики, дату рождения и прочее
35. usa-official.com — ищет в записях регистрации избирателей, собственности, финансовые дела, продажи авто, таможня США, списки компаний и в прочих реестрах

''')
            skip()
        elif fio == "43":
            print('''

Поиск по ФИО гражданина Турции

1. turktelekom.com.tr (http://www.ttrehber.turktelekom.com.tr/?type=white) — найдет компании и людей с номером телефона и адресом
2. emsal.uyap.gov.tr (http://emsal.uyap.gov.tr/BilgiBankasiIstemciWeb/) — поиск в судебный делах

''')
            skip()
        elif fio == "44":
            print('''

Поиск по ФИО гражданина Таджикистана

1. andoz.tj (https://andoz.tj/Fehrist/SI?culture=ru-RU) — найдет сведения о регистрации индивидуальных предпринимателей

''')
            skip()
        elif fio == "45":
            print('''

Поиск по ФИО гражданина Узбекистана

1. lex.uz — поиск в базе судебных документов
2. orginfo.uz — найдет компании гражданина

''')
            skip()
        elif fio == "46":
            print('''

Поиск по ФИО гражданина Франции

1. dirigeants.bfmtv.com (https://dirigeants.bfmtv.com/recherche/) — найдет дату рождения, мандаты и бизнес
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. copainsdavant.linternaute.com (http://copainsdavant.linternaute.com/s/?advsrch) — найдет школу, фото, друзей, место рождения
4. www.pagesjaunes.fr (https://www.pagesjaunes.fr/pagesblanches/) — найдет номер телефона и адрес проживания
5. www.deces-en-france.fr — база смертей, найдет дату, место рождения и смерти
6. francais-a-londres.org (https://francais-a-londres.org/u) — найдет ник, фото, адреса квартир аренды и прочее

''')
            skip()
        elif fio == "47":
            print('''

Поиск по ФИО гражданина Финляндии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "48":
            print('''

Поиск по ФИО гражданина Хорватии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое

''')
            skip()
        elif fio == "49":
            print('''

Поиск по ФИО гражданина Чехии

1. justice.cz (https://or.justice.cz/ias/ui/rejstrik-$osoba?p%3A%3Asubmit=x&.%2Frejstrik-%24osoba=&prijmeni=Ivanov&jmeno=&narozeni=&obec=&angazma=&soud=&polozek=50&jenPlatne=VSECHNY) — поиск в государственном реестре вовлеченных физических лиц, найдет дату рождения, адрес, ICQ, организации, сборник документов
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
4. seznam.1188.cz — найдет адрес и телефон
5. isir.justice.cz (https://isir.justice.cz/isir/common/index.do) — поиск в базе должников

''')
            skip()
        elif fio == "50":
            print('''

Поиск по ФИО гражданина Швейцарии

1. moneyhouse.ch (https://www.moneyhouse.ch/de/search?activeMandates=true&tab=persons) — поиск в торговом реестре, найдет владения компаниями, город проживания
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. ti.chregister.ch (https://ti.chregister.ch/cr-portal/suche/suche.xhtml) — найдет организации принадлежащие этому человеку
4. www.northdata.com — найдет названия компаний с которыми связано ФИО
5. www.local.ch (https://www.local.ch/en/tel) — поиск в реестре бизнесов, найдет сайт, адрес, телефон, фото

''')
            skip()
        elif fio == "51":
            print('''

Поиск по ФИО гражданина Швеции

1. hitta.se — найдет адрес проживания, номер телефона, сожителей
2. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
3. eniro.se (https://www.eniro.se/) — найдет телефон, местоположение на карте и фото дома.
4. upplysning.se (https://www.upplysning.se/) — поиск в базе граждан и компаний, находит контактные данные людей и компаний
5, www.ancestry.com (https://www.ancestry.com/search/collections/60525/) — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений
6. mrkoll.se — найдет дату рождения, адрес, ФИО соседей, номер социального страхования, номера телефонов, корпоративное участие, примерный доход, история изменений ФИО

''')
            skip()
        elif fio == "52":
            print('''

Поиск по ФИО гражданина Эстонии

1. tva-recherche.lu (https://tva-recherche.lu/recherche/) — найдет номер НДС, адрес и многое другое
2. e-justice.europa.eu (https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1) — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела
3. teatmik.ee (https://www.teatmik.ee/ru/advancedsearch/private) — найдет дату рождения, юр. лица, деловую сеть

''')
            skip()
        elif fio == "53":
            print('''

Поиск по ФИО гражданина Южной Кореи

1. people.search.naver.com (https://people.search.naver.com/) — найдет фото, места учебы и работы, с кем состоит в браке, дата и место рождения

''')
            skip()
        elif fio == "54":
            print('''

Поиск по ФИО гражданина Японии

1. courts.go.jp (http://www.courts.go.jp/app/hanrei_jp/search2) — поиск по судам
2. jpon.xyz —  найдет номер телефона и адрес

''')
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == "5":
        print("""

Поиск по фото с лицом

1. search4faces.com — найдет профиль VK, OK, TikTok и Clubhouse, не точен
2. vk.watch — находит аккаунты ВКонтакте с похожими лицами, не точен, дождитесь загрузки фото
3. pimeyes.com — показывает фото с похожими лицами и клонов, иногда сайт работает только через VPN
4. @PimEyes (https://t.me/pimeyesbot) — найдет фото с лицом во всем интернете, результат приходит в течении 10 минут
5. camgirlfinder.net (https://camgirlfinder.net/search) — найдет веб-кам моделей, их ник и профиль
6. facecheck.id — сыщет лицо в социальных сетях, дает ссылку на источники, среднее качество распознавания лица
7. geometria.ru (https://geometria.ru/facesearch/)  — находит фото из баров и клубов
8. @ФотоБот (https://t.me/photo_face_found_bot) — найдёт аккаунт ВК с фото, работает нестабильно
9. @InfoLab (https://t.me/ProbivUniversal_New_Bot) — найдет гражданина Украины, выдает его телефоны, почты, адреса, документы, и прочее, бесплатно покажет только часть данных
10. @FindClone (https://t.me/FindClone_TG_bot) — ищет фото в профилях ВК
11. FaceSeek (https://faceseek.online/) — ищет фото на сайтах, даст другие фото человека
Инструменты

1. faceplusplus.com (https://www.faceplusplus.com/face-comparing/) — сравнит два лица и покажет уровень схожести, открывать в версии для ПК
2. IAT (https://play.google.com/store/apps/details?id=tk.silviomarano.imageanalysistoolset)  — сравнит два лица и покажет уровень схожести, в приложении раздел Face insight, после пункт compare в списке
3. mxface.ai (https://mxface.ai/face-comparing#Face_Detection_demo_section) — сравнит два лица и покажет уровень схожести
4. @DeepPaint (https://t.me/DeepPaintBot) — повышает качество фото лица
5. huggingface.co (https://huggingface.co/spaces/sczhou/CodeFormer) — улучшает фото с лицом
6. app.remini.ai — сделает фото лица четче


По видео с лицом

1. scanner.deepware.ai — выявляет дипфейк
""")
        skip()
    elif data == "6":
        print("Какой адрес?")
        print("[1]Физический адрес, [2]IP адрес, [3]MAC адрес")
        vib = input()
        if vib == "1":
            print("Какая страна?")
            print("""

[1]Любая          | [8]Бельгия         | [15]Испания      | [22]Нидерланды     | [29]Финляндия      | 
[2]Россия         | [9]Болгария        | [16]Исландия     | [23]Новая Зеландия | [30]Франция        | 
[3]Украина        | [10]Великобритания | [17]Казахстан    | [24]Норвегия       | [31]Чехия          | 
[4]Беласрусь      | [11]Венгрия        | [18]Кипр         | [25]Польша         | [32]Швеция         | 
[5]Австралия      | [12]Вьетнам        | [19]Китай        | [26]Приднестровье  | [33]Швейцария      | 
[6]Албания        | [13]Дания          | [20]Косово       | [27]США            | [34]Эстония        |
[7]Армения        | [14]Индия          | [21]Латвия       | [28]Турция         | [35]Южная Корея    |

""")
            vib_str = input()
            if vib_str == "1":
                print("""

Поиск по физическому адресу любой страны

1. 3wifi (https://3wifi.stascorp.com/map) — найдет wifi точки с паролями
2. kamerka (https://github.com/woj-ciech/kamerka)  — найдет на карте камеры, устройства интернета вещей, принтеры, твитты, Instagram фото, Flickr и другие открытые устройства
3. wigle.net — покажет SSID и BSSID Wi-Fi точки
4. osintcombine.com — найдет Facebook страницы организаций
5. trendsmap.com — карта трендов в Twitter
6. omnisci.com (https://www.omnisci.com/demos/tweetmap/) — покажет твитты на карте
7. mattw.io (https://mattw.io/youtube-geofind/location) — находит видео на YouTube
8. windy.com — множество камер с функцией поиска по истории, есть карта
9. opencellid.org — вышки сотовой связи, найдет MCC, MNC, LAC, CID
10. strava.com (https://www.strava.com/heatmap) — сайт показывает где бегают спортсмены
11. map.snapchat.com — найдет недавние видео из Snapchat
12. doogal.co.uk (https://www.doogal.co.uk/strava.php) — данные из Strava, показывает имена пользователей
13. udeuschle.de (https://www.udeuschle.de/panoramas/makepanoramas_en.htm) — составит панораму гор
14. whopostedwhat.com — находит фото в Instagram с фильтром по дате
15. onemilliontweetmap.com — покажет твиты за последние сутки на карте
16. SnapMap-OSINT (https://github.com/sc1341/SnapMap-OSINT)  — скачает все фото и видео из Snapchat в указанном на карте радиусе
17. Telegram-Trilateration (https://github.com/jkctech/Telegram-Trilateration)  — показывает точное местоположение пользователей Telegram включивших функцию "люди рядом"
18. flickr.com (https://www.flickr.com/map) — найдет снимки пользователей на карте, выберите место поиска, нажмите "search the map" а потом "go"
19. pastvu.com — исторические снимки места с 1826 по 2000 годы
20. photo-map.ru  — найдет фото из VK, радиус поиска от 10 метров
21. app.skylens.io  — найдет на карте фото Instagram, YouTube видео, твиты, фото из ВК, минимальный радиус поиска 1 км.
22. openaltimetry.org (http://openaltimetry.org/data/icesat2/) — показывает точный рельеф, подберите дату чтобы полоса точек попала на нужное место, выделите область "select region" и сервис даст точки отображающие выбранный рельеф
23. demo.f4map.com — покажет здания любого города в 3D, данные из OpenStreetMap
24. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — найдет пользователей VK и фото на карте
25. telegram-nearby-map (https://github.com/tejado/telegram-nearby-map)  — показывает точное местоположение пользователей Telegram включивших функцию "люди рядом", их имена и фото аккаунта
26. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — даст прямые ссылки на 10 карт где есть спутниковые снимки, погода, таймлапс, исторические спутниковые снимки и прочее
27. domofoto.ru (https://domofoto.ru/map.php) — найдет фото зданий, их серию и номер, больше снимков в России и Украине
28. live.sixfold.com — покажет состояние нагрузки границ стран Европы, покажет пропускные пункты суши, воды и уровень нагрузки
29. birdhunt.co — найдет твитты рядом, создаст ссылку на Twitter, где введен поисковый запрос с координатами и заданным радиусом
30. instahunt.co — отобразит фото из Instagram, скопируй полученный код и встать в поле на сайте чтобы увидеть результат
31. etomesto.ru — найдет исторические топографические карты, укажите точку на карте и найдется нужная старая карта


Спутниковые снимки

1. wikimapia.org — спутниковые снимки Google, Yandex, Bing и Yahoo, есть фильтр зданий по году постройки, по категориям, обозначение объектов которых нету на других картах
2. livingatlas.arcgis.com (https://livingatlas.arcgis.com/wayback/) — покажет исторические снимки
3. satellites.pro — есть карты Apple, MapBox, Yandex, Esri и Google
4. apps.sentinel-hub.com (https://apps.sentinel-hub.com/eo-browser/)  — база почти ежедневных снимков со спутника, можно делать таймлапс
5. zoom.earth — есть высококачественные изображения для этого выберите базовую карту, есть пожары, штормы, ветер и история этих данных по дате
6. orbtwz.users.earthengine.app (https://orbtwz.users.earthengine.app/view/csar-eye) — найдет и отметит изменения на спутниковых снимках в указанную дату
7. imagehunter.apollomapping.com — 64 датасета, фильтры по дате, качеству снимков, чтобы получить снимки выдели на карте область
8. retromap.ru (http://retromap.ru/closeby.php) — найдет исторические, топографические карты и спутниковые снимки с 12 века по настоящее время
9. map.openaerialmap.org — фото с дрона, ультравысокое качество картинки, до 3 см на пиксель, небольшое покрытие, использовать на ПК


Видеонаблюдение

1. windy.com — есть история записей
2. world-cam.ru (https://world-cam.ru/world/) — камеры в реальном времени 
3. cipher387.github.io (https://cipher387.github.io/webcamcse/) — по названию местности найдёт камеры в реальном времени, ищет среди 10 сайтов с трансляциями


Транспорт

1. vesselfinder.com — покажет все судна на карте
2. globe.adsbexchange.com — самолеты и вертолеты с историей передвижений


Просмотр улиц

1. Google (http://www.google.com/maps/) — просмотр в 360 градусов почти во все странах
2. Mapillary (https://www.mapillary.com/app/) — данные загружаются пользователями, не всегда есть обзор в 360 градусов
3. kartaview.org (http://kartaview.org/map) — данные загружаются пользователями, нету панорам
4. railcabrides.com (https://railcabrides.com/en/mapsearch) — видео из кабины поезда, нет крупных городов
5. 360cities.net (http://360cities.net/map) — панорамы


Инструменты

1. app.measuremaponline.com  — вычисляет площадь и периметр нужной области на карте
""")
                skip()
            elif vib_str == "2":
                print("Какой регион?")
                print("[1]Любой, [2]Москва, [3]Алтайский край")
                vib_str_ru = inpiut()
                if vib_str_ru == "1":    
                    print("""

Поиск по физическому адресу в России

1. Рос.реестр (https://rosreestr.ru/wps/portal/p/cc_ib_portal_services/online_request) — справочная информация по объектам недвижимости
2. spravochnik09tut.xyz (https://spravochnik09tut.xyz/rossiya/) — найдет жителей здания, их ФИО и телефон
3. dom.gosuslugi.ru (https://dom.gosuslugi.ru/#!/houses) — даст паспорт здания
4. bo.nalog.ru — найдет организацию и полную информацию о ней включая финансы
5. @VipiskaEGRNbot — находит по кадастровый карте данные стоимости и площади
6. cian.ru (http://www.cian.ru/map) — найдет объявления и планировку дома
7. map.gdeetotdom.ru — найдет объявления и планировку дома
8. russia.liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий
9. list-org.com (https://www.list-org.com/?search=address) — найдет организацию
10. domspravka.com (https://ts.domspravka.com/) — найдет ФИО
11. @OsintKit (https://t.me/@osintkit_check_bot) — ищет в утечках, дает имена, почты, телефоны и много другого
12. Realty.ya.ru (https://realty.ya.ru/otsenka-kvartiry-po-adresu-onlayn/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%98%D0%B7%D1%8E%D0%BC%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%2049%D0%BA3/) — найдет историю объявлений о продаже и аренде в доме, в поиске замените адрес на искомый
13. realtycloud.ru (https://realtycloud.ru/sale-history/) — найдет историю объявлений о продаже в доме
Транспорт

1. rasp.yandex.ru (https://rasp.yandex.ru/map/trains/) — найдет поезда, автобусы, самолеты в реальном времени их путь и номер транспорта


Просмотр улиц

1. Yandex (http://yandex.ru/maps/) —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей

    """)
                    skip()
                elif vib_str_ru == "2":
                    print("""

Поиск по физическому адресу в Москве

1. data.mos.ru (https://data.mos.ru/opendata) — покажет на карте объекты дорожной сети, строительства, пешеходную инфраструктуру, мосты, камеры и много другого


    """)
                    skip()
                elif vib_str_ru == "3":
                    print("""

Поиск по физическому адресу в России, Алтай

1. Система Город (https://play.google.com/store/apps/details?id=com.gorodok.mobile) (a) — при регистрации введите адрес и получите инициалы владельца недвижимости

""")
                    skip()
                else:
                    print('Попробуйте еще раз')
                    skip()
                
                
            elif vib_str == "3":
                print("""

Поиск по физическому адресу Украины

1. liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий
2. map.land.gov.ua —  кадастровая карта
3. @InfoLab (https://t.me/ProbivUniversal_New_Bot) — выдаст паспортные данные, телефоны и прочее, бесплатно покажет только часть данных
Транспорт

1. www.eway.in.ua — общественный транспорт на карте в реальном времени


Просмотр улиц

1. Yandex (http://yandex.ru/maps/) —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей

""")
                skip()
            elif vib_str == "4":
                print("""

Поиск по физическому адресу Беларуси

1. belarus.liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий
Просмотр улиц

1. Yandex (http://yandex.ru/maps/) —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей

""")
                skip()
            elif vib_str == "5":
                print("""

Поиск по физическому адресу Австралии

1. placenames.fsdf.org.au (https://placenames.fsdf.org.au/index.html) — карта топонимов, название природного объекта на Земле или объекта, созданного человеком на Земле
2. pedestrian.melbourne.vic.gov.au (http://www.pedestrian.melbourne.vic.gov.au/) — количество пешеходов в городе Мельбурн, есть история
3. personlookup.com.au — дает ФИО и номер телефона
4. planningportal.nsw.gov.au (https://www.planningportal.nsw.gov.au/spatialviewer/#/find-a-property/address) — кадастровая карта, есть номера лотов домов, данные о высоте зданий
5. www.onthehouse.com.au — объявления о продаже недвижимости и других вещей
Видеонаблюдение

1. webcamsydney.com — онлайн камера гавани Сиднея, нет истории
2. www.thesebelquaywestsydney.com.au (https://www.thesebelquaywestsydney.com.au/webcam.html) — залив Сиднея, с другого ракурса, есть просмотр истории
3. insecam.org (https://www.insecam.org/en/bycountry/AU/) — IP камеры, нету точного указания расположения камеры, только название населенного пункта


Спутниковые снимки

1. actmapi.act.gov.au (https://app.actmapi.act.gov.au/actmapi/index.html?viewer=hp) — качественные снимки

""")
                skip()
            elif vib_str == "6":
                print("""

Поиск по физическому адресу на территории Албании

1. qkr.gov.al (http://www.qkr.gov.al/kerko/kerko-ne-regjistrin-tregtar/kerko-per-subjekt/) — найдет компанию и даст подробную информацию о ней

""")
                skip()
            elif vib_str == "7":
                print("""

Просмотр улиц

1. Yandex (http://yandex.ru/maps/) —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей

""")
                skip()
            elif vib_str == "8":
                print("""

Поиск по физическому адресу в Бельгии

1. de1212.be — найдет номер телефона и ФИО
Транспорт

1. trainmap.belgiantrain.be — поезда, электрички и автобусы на карте в реальном времени

""")
                skip()
            elif vib_str == "9":
                print("""

Поиск по физическому адресу в Болгарии

1. ukazatelite.com — найдет юридическое лицо с искомым адресом

""")
                skip()
            elif vib_str == "10":
                print("""

Поиск по физическому адресу Великобритании

1. londonpicturearchive.org.uk (http://londonpicturearchive.org.uk/london-picture-map) — найдет фото улиц на карте Лондона с 19 века по настоящее время
2. reversepp.com (r) — реестр планирования помещений, найдет ФИО, дату и прочее
Спутниковые снимки

1. historicengland.org.uk (https://historicengland.org.uk/images-books/archive/collections/aerial-photos/) — снимки с 1940 года по настоящее время


Транспорт

1. raildar.co.uk (http://raildar.co.uk/radar.html) — по карте движутся поезда, можно кликнуть на поезд и узнать расписание его движения
2. tracker.geops.ch — показывает общественный транспорт, можно посмотреть историю или предсказать передвижение транспорта
3. crashmap.co.uk (https://www.crashmap.co.uk/Search) — на карте покажет все автомобильные аварии за 23 года, их уровень опасности, точное место, дату, дает за плату полный отчет 
4. roadcrash.co.uk (https://www.roadcrash.co.uk/map) — на карте покажет все автомобильные аварии с 2005 года, их уровень опасности, точное место, дату, полный отчет с потерями и автомобилями


Видеонаблюдение

1. tfljamcams.net — записи с камер Лондона

""")
                skip()
            elif vib_str == "11":
                print("""

Поиск по физическому адресу Венгрии

1. telekom.hu (https://www.telekom.hu/lakossagi/tudakozo) — найдет номер телефона и ФИО
2. adoszam.hu — находит данные о компании (адрес, род деятельности)
Транспорт

1. vonatinfo.mav-start.hu — найдет поезда на карте в реальном времени и их номера

""")
                skip()
            elif vib_str == "12":
                print("""

Поиск по физическому адресу Вьетнама

1. daln.gov.vn (https://daln.gov.vn/coastal/#8/9.273/104.684/c3c4c5c6c9c10) — карта с объектами береговой защиты (дамбы, волноломы), маяками, метеостанциями и прочими объектами в прибрежных районах и водах
Камеры

1. hochiminhcity.gov.vn (https://chongngap.hochiminhcity.gov.vn/baongap/) — город Ho Chi Minh

""")
                skip()
            elif vib_str == "13":
                print("""

Поиск по физическому адресу Дании

1. statstidende.dk (https://statstidende.dk/messages) — поиск в юридических документах, найдет данные о смене жительства гражданина, некрологи и много всего полезного
2. datacvr.virk.dk (https://datacvr.virk.dk/data/) — поиск в сведениях о зарегистрированных предпринимателях и компаниях
3. dingeo.dk — даст информацию о здании такую как цена дома, заложен ли он (и сумма долга) подробная сводка по экологии, сводка о социальном положении соседей и многое другое
4. krak.dk (https://www.krak.dk/) — найдет ФИО, телефон и фото дома
5. tinglysning.dk (https://www.tinglysning.dk/m/soeg) — найдет ФИО владельца, долю, стоимость, дату оценки, коммуну, земельные книги, кредиты, ипотеки
Транспорт

1. dinoffentligetransport.dk (https://dinoffentligetransport.dk/trafikinfo/her-og-nu/kort-med-bus-tog-og-metro) — карта движения поездов и автобусов в реальном времени

""")
                skip()
            elif vib_str == "14":
                print("""

Просмотр улиц

1. maps.mapmyindia.com (r) — высокое качество снимков, при регистрации нет проверки почты

""")
                skip()
            elif vib_str == "15":
                print("""

Поиск по физическому адресу Испании

1. sedecatastro.gob.es (https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx) — кадастровая карта Испании

""")
                skip()
            elif vib_str == "16":
                print("""

Видеонаблюдение

1. vegasja.vegagerdin.is (https://vegasja.vegagerdin.is/eng/) — статичные за текущий день


Просмотр улиц

1. en.ja.is (https://en.ja.is/kort/) — обзор в 360 градусов, качественные снимки

""")
                skip()
            elif vib_str == "17":
                print("""

Поиск по физическому адресу Казахстана

1. spravochnik09tut.xyz (https://spravochnik09tut.xyz/kazahstan) — найдет жителей здания, их ФИО и телефон

Просмотр улиц

1. Yandex (http://yandex.ru/maps/) —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей

Как найти e-mail организации на карте

[1] Откройте 2GIS — 2gis.ru
[2] Найдите нужную организацию и нажмите на нее
[3] Прокрутите в низ и нажмите на "Это моя компания"

Появится страница с регистрацией личного кабинета, там в строке e-mail будет адрес с несколькими звездочками

""")
                skip()
            elif vib_str == "18":
                print("""

Поиск по физическому адресу Кипра

1. eservices.dls.moi.gov.cy (http://eservices.dls.moi.gov.cy/#/national/geoportalmapviewer) — кадастровая карта

""")
                skip()
            elif vib_str == "19":
                print("""

Поиск по физическому адресу Китая

1. qcc.com — найдет компанию, её название и прочее
Просмотр улиц

1. map.qq.com — улицы в 360, используйте мобильную версию
2. map.baidu.com — обзор в 360 градусов, качество снимков выше

""")
                skip()
            elif vib_str == "20":
                print("""

Просмотр улиц

1. gjirafa.biz — просмотр в 360 градусов, есть почти все улицы страны

""")
                skip()
            elif vib_str == "21":
                print("""

Поиск по физическому адресу Латвии

1. kadastrs.lv (https://www.kadastrs.lv/) — кадастровая карта, поиск без карты

""")
                skip()
            elif vib_str == "22":
                print("""

Поиск по физическому адресу Нидерландов

1. detelefoongids.nl (https://www.detelefoongids.nl/) — находит номер телефона и ФИО

""")
                skip()
            elif vib_str == "23":
                print("""

Поиск по физическому адресу Новой Зеландии

1. heartofthecity.co.nz (http://www.heartofthecity.co.nz/pedestrian-count/) — количество пешеходов в городе Окленд, есть история

""")
                skip()
            elif vib_str == "24":
                print("""

Поиск по физическому адресу Норвегии

1. gulesider.no — даст ФИО, телефон, и фото дома
Транспорт

1. banenor.no (https://www.banenor.no/Jernbanen/togkart/) — поезда на карте в реальном времени


Видеонаблюдение

1. webcamsinnorway.com (http://www.webcamsinnorway.com/map) — только в реальном времени


""")
                skip()
            elif vib_str == "25":
                print("""

Поиск по физическому адресу в Польше

1. prod.ceidg.gov.pl (http://prod.ceidg.gov.pl/ceidg/ceidg.public.ui/Search.aspx) — найдет компании, даст основную, контактную информацию, банкротства, и историю изменений данных о компании

Транспорт

1. portalpasazera.pl (https://portalpasazera.pl/MapaOL) — поезда на карте в реальном времени
2. czynaczas.pl — публичный транспорт, Варшава
3. buslive.pl — автобусы в реальном времени, нужно скачать приложение


Видеонаблюдение

1. worldcam.pl (http://www.worldcam.pl/mapa) — камеры в реальном времени

""")
                skip()
            elif vib_str == "26":
                print("""

Поиск по физическому адресу Приднестровье

1. data2b.md — реестр компаний, найдет наименование, адрес, количество работников, филиалы и контакты

""")
                skip()
            elif vib_str == "27":
                print("""

Поиск по физическому адресу в США

1. radaris.com (https://radaris.com/#findAddrH) — найдет организации по адресу и информацию о них
2. landgrid.com (https://landgrid.com/parcelverse#b=counties) — кадастровая карта
3. cellphonetrackers.org (https://cellphonetrackers.org/gsm/cell-search.php?lat=40.204178&lon=-75.528529) — покажет все сотовые вышки
4. qpublic.schneidercorp.com — кадастровая карта, показывает имя владельца, продажи земли и многое другое
5. progressivedirect.com — найдет количество, год, и марку автомобиля, на сайте выберите авто и в контактных данных укажите нужный адрес и любое имя
6. cyberbackgroundchecks.com (https://www.cyberbackgroundchecks.com/address) — найдет все данные гражданина США проживающий по адресу, вход на сайт разрешен только с IP адреса США
7. crimemapping.com (https://www.crimemapping.com/map) — карта эксцессов и правонарушений
8. usa.liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий
9. melissa.com (https://www.melissa.com/v2/lookups/personator) — найдет ФИО, дату рождения, адрес проживания, этнос и прочее
10. livingatlas.arcgis.com (http://livingatlas.arcgis.com/topoexplorer/index.html) — история топографических карт геологической службы США с 1882 по 2006 гг.
11. anywho.com — выдаст имена и номера телефонов всех кто живёт по адресу 
12. homemetry.com — найдет фото, количество комнат, характеристики, фото дома, стоимость, дату постройки и продажи контакты предыдущих жителей и регистрации компаний
13. publicaccountability.org — найдет регистрации людей и компании, их расходы и взносы
14. whoownswhat.justfix.nyc — только для Нью-Йорка, найдет всех владельцев здания, нарушения, выселения, связи с другими адресами, и много другого
15. smartbackgroundchecks.com — дает адреса, телефоны, биографию, семью, недвижимость, образование, почту, и прочее
16. zillow.com — найдет на карте проданные и продающиеся, сдающиеся помещения, найдет план и описание, чтобы открыть карту нужно ввести адрес в поиск
17. fastpeoplesearch.com — выдаст полное имя, возраст жильцов, прошлые адреса, псевдонимы, родственников, предыдущие владельцы и прочее, сайт не работает из России, нужен VPN
18. city-data.com (http://www.city-data.com/indexes/assessments/) — найдет имена предыдущих владельцев, фото, оценку стоимости
19. TruePeopleSearch.com — ищет сведения о гражданине США, выдает имя, email, телефон, родственников и прочее, сайт доступен только с IP адреса США, используй VPN
Спутниковые снимки

1. descarteslabs.com (https://www.descarteslabs.com/company/geovisual/) — визуальный поиск, находит похожие места по небольшой территории


Видеонаблюдение

1. publicrecords.onlinesearches.com (https://www.publicrecords.onlinesearches.com/Traffic-Cameras-and-Reports.htm) — дает ссылки на карты с камерами у дорог, 10 тысяч камер по стране, используй VPN если не открывается сайт 
2. otc.armchairresearch.org (https://otc.armchairresearch.org/map) —  покажет на карте где около дорог есть камеры видеонаблюдения, дает картинку, не везде работает трансляция


Типографические карты

1. ngmdb.usgs.gov (https://ngmdb.usgs.gov/topoview/viewer/) — карты с 1945 года

""")
                skip()
            elif vib_str == "28":
                print("""

Просмотр улиц

1. Yandex (http://yandex.ru/maps/) —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей

""")
                skip()
            elif vib_str == "29":
                print("""

Поиск по физическому адресу Финляндии

1. fonecta.fi (https://www.fonecta.fi/haku/#/) — найдет компании и их контакты
2. asiointi.maanmittauslaitos.fi (https://asiointi.maanmittauslaitos.fi/karttapaikka/) — кадастровая карта
Транспорт

1. junatkartalla.vr.fi (https://junatkartalla.vr.fi/?lang=fi-FI&follow=11) — показывает поезда на карте в реальном времени

""")
                skip()
            elif vib_str == "30":
                print("""

Видеонаблюдение

1. www.autoroutes.fr (http://www.autoroutes.fr/en/webcams.htm) — в реальном времени

""")
                skip()
            elif vib_str == "31":
                print("""

Поиск по физическому адресу Чехии

1. seznam.1188.cz — найдет телефон и ФИО владельца недвижимости

""")
                skip()
            elif vib_str == "32":
                print("""

Поиск по физическому адресу Швеции

1. eniro.se (https://www.eniro.se/) — найдет телефон, ФИО и фото дома
2. upplysning.se (https://www.upplysning.se/) — находит контактные данные людей и компаний
3. hitta.se (https://www.hitta.se/kartan?usergeo=1) — находит жителей дома, данные о воровстве, уровне жизни и многое другое

""")
                skip()
            elif vib_str == "33":
                print("""

Поиск по физическому адресу Швейцарии

1. ti.chregister.ch (https://ti.chregister.ch/cr-portal/suche/suche.xhtml) — найдет данные об организации
2. map.geo.admin.ch (https://map.geo.admin.ch/mobile.html?topic=swisstopo&lang=en&bgLayer=voidLayer&layers=ch.swisstopo.zeitreihen&layers_timestamp=19161231&X=212150.00&Y=636700.00&zoom=2&time=1916) — топографическая карта с историей с начала 1844 года по настоящее время
3. ge.ch (https://ge.ch/terextraitfoncier/) — найдет имена владельца недвижимости, назначение здания, площадь, год постройки, схему на кадастровой карте и прочее

Транспорт

1. tracker.geops.ch — показывает общественный транспорт, можно посмотреть историю или предсказать передвижение транспорта


Видеонаблюдение

1. en.swisswebcams.ch (http://en.swisswebcams.ch/verzeichnis/alle/schweiz) — реальное время с архивом
2. www.bergfex.com (http://www.bergfex.com/schweiz/webcams) — реальное время с архивом

""")
                skip()
            elif vib_str == "34":
                print("""

Поиск по физическому адресу на территории Эстонии

1. teatmik.ee (https://www.teatmik.ee/ru/advancedsearch) — найдет компании
2. xgis.maaamet.ee (https://xgis.maaamet.ee/xgis2/page/app/maainfo) — кадастровая карта

""")
                skip()
            elif vib_str == "35":
                print("""

Поиск по физическому адресу Южной Кореи

1. koreas.liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий

Спутниковые снимки

1. map.kakao.com — показывает исторические снимки до 2008 года


Просмотр улиц

1. m.map.kakao.com — просмотр в 360 градусов, отличное качество снимков и покрытия, с ПК просмотр улиц не работает

""")
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif vib == "2":
            print("""

Поиск по IP адресу

1. HostHunter (https://github.com/SpiderLabs/HostHunter)  — обнаружение и извлечение имен хостов из набора целевых IP-адресов
2. censys.io — находит какие серверы и устройства выставлены в сети
3. cyberhubarchive (https://github.com/cyberhubarchive/archive) — архив утекших данных, в нем есть IP адреса аккаунтов Skype
4. iknowwhatyoudownload (http://iknowwhatyoudownload.com/) — покажет что скачивают в интернете
5. check.torproject.org (https://check.torproject.org/cgi-bin/TorBulkExitList.py) — найдет список всех выходных узлов Tor за последние 16 часов, которые мог связаться с IP
6. dnslytics.com (https://dnslytics.com/reverse-ip) — найдет домены
7. metrics.torproject.org (https://metrics.torproject.org/exonerator.html) — проверяет использовался ли IP-адрес в качестве узла для передачи трафика в Tor, требуется указать дату
8. talosintelligence.com — покажет сколько писем было отправлено с адреса и его репутацию
9. intelx.io — найдет упоминание в файлах из утечек
10. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — даст прямые ссылки на 20+ ресурсов где можно найти историю Whois, домены, адрес и еще 20+ видов данных, покажет сколько результатов в других ботах
11. wikipedia.org (https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%96%D1%83%D1%80%D0%BD%D0%B0%D0%BB%D1%8B?type=&user=&page=%D0%A3%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA%3A1.1.1.1&wpdate=&tagfilter=&wpfilters%5B%5D=newusers) — поиск в журнале правок, банов, регистрации участников wikipedia, замените 1.1.1.1 в поле цель
12. leak-lookup.com (https://leak-lookup.com/search)  — покажет на каких сайтах была утечка искомым IP


Инструменты

1. app.huntintel.io  — на карте покажет список до ста введённых IP адресов, открывать в версии для ПК, на карте тыкни на любое место, нажми на знак плюса и выбери Find IP address
2. ipinfo.io (https://ipinfo.io/tools/map) — найдет любое количество IP адресов на карте


Через URL

https://en.wikipedia.org/wiki/Special:Contributions/IP — найдет пользователя, замените IP, используйте похожую ссылку только на других языках, так как аккаунт на этом может не найтись
https://en.wikipedia.org/wiki/User_talk:/IP — найдет пользователя, замените IP, используйте похожую ссылку только на других языках, так как аккаунт на этом может не найтись

""")
            skip()
        elif vib == "3":
            print("""

Поиск по MAC адресу

1. alexell.ru (https://alexell.ru/network/mac-geo/) — тоже покажет местоположение
2. wigle.net (http://wigle.net/search)  — находит Wi-Fi точку, ее физический адрес и название


Поиск через URL

1. https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:CC:00:CC:00:CC — найдет координаты точки на карте, замените 00:CC:00:CC:00:CC на MAC-адрес

""")
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == "7":
        print("""

Поиск по никнейму

1. Maigret (https://github.com/soxoj/maigret)  — найдет аккаунты с таким же ником среди 3000+ сайтов
2. namecheckup.com — найдет искомый ник на сайтах
3. instantusername.com — найдет искомый ник на сайтах
4. suip.biz (https://suip.biz/ru/?act=sherlock) — найдет искомый ник на 300+ сайтах, работает очень медленно, дождитесь ответа
5. namechk.com — найдет искомый ник на сайтах и в доменах
6. sherlock (http://github.com/sherlock-project/sherlock)  — найдет искомый ник на сайтах
7. whatsmyname.app — найдет искомый ник на сайтах
8. boardreader.com — найдет искомый ник на форумах
9. yasni.com (http://www.yasni.com/) — находит упоминание ника в Google и прочих поисковиках
10. social-searcher.com — найдет упоминания в соц. сетях и на сайтах
11. socialmention.com — найдет упоминания ника
12. mailcat (https://github.com/sharsil/mailcat)  — перебирает почтовые сервисы чтобы найти действительные email адреса
13. leak-lookup.com (https://leak-lookup.com/search)  — покажет на каких сайтах была утечка с искомым ником
14. @DATA_007bot — выдаст аккаунт QQ, регион
15. Nexfil (https://github.com/thewhiteh4t/nexfil)  — найдет аккаунты с идентичным ником среди 350 медиа платформ, можно отправить крупный список ников
16. analyzeid.com (http://analyzeid.com/username/) — найдет аккаунты с идентичным ником среди 100 сайтов, из профилей выведет все имена, страны, и даты создания в один список
17. findaccountsbyusername.com — выдаст существующие аккаунты с похожим ником, используется Sherlok
18. Marple (https://github.com/soxoj/marple)  — ищет в 10+ поисковых системах аккаунты с похожим ником 
19. Social Scanner (https://rapidapi.com/hailbytes-hailbytes-default/api/social-scanner/)  — найдет аккаунты с идентичным ником среди 900+ платформ, после регистрации введи ник в поле username и нажми Test Endpoint
20. blackbird-osint.herokuapp.com — проверит 500 платформ и где есть такой же ник выдаст ссылку с кратким описанием профиля
21. DetectDee (https://github.com/piaolin/DetectDee/)  — найдет профили в китайских онлайн серверах
22. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — проверит ник в утечках, еще ищет в других ботах


Восстановление доступа

1. Twitter (https://twitter.com/account/begin_password_reset)
2. Microsoft (https://account.live.com/acsr)

""")
        skip()
    elif data == "8":
        print("Данные какого транспорта?")
        print("[1]Автомобиля, [2]Самолёта, [3]Мотоцикла, [4]Поезда, [5]Судна, [6]Грузового контейнера")
        vib_tr = input()
        if vib_tr == "1":
            print("Авто какой страны?")
            print('''
│ [1]России         │ [8]Беларуси        │ [15]Испании      │ [22]Нигерии     │ [29]Слоакии        │ [36]Эстонии          │ 
│ [2]Украины        │ [9]Вьетнама        │ [16]Италии       │ [23]Нидерландов │ [30]США            │ [37]Эквадора         │
│ [3]Казахстана     │ [10]Великобритании │ [17]Израиля      │ [24]Норвегии    │ [31]Финляндии      │ [38]Японии           │
│ [4]Австралии      │ [11]Дании          │ [18]Канады       │ [25]Перу        │ [32]Франции        │ [39]Определить страну│
│ [5]Армении        │ [12]Индии          │ [19]Киргизии     │ [26]Польши      │ [33]Чехии          │                      │
│ [6]Боливии        │ [13]Индонезии      │ [20]Китая        │ [27]Португалии  │ [34]Швеции         │                      │
│ [7]Бразилии       │ [14]Ирландии       │ [21]Монголии     │ [28]Румании     │ [35]Швейцарии      │                      │

    ''')
            vib_tr_str = input()
            if vib_tr_str == "1":
                print("""

Поиск по регистрационному знаку или VIN авто в России

1. @avinfo (https://t.me/avinfo?start=ref987328) — дает крупный отчет с данными владельца, историей авто и фото, бесплатный поиск по промокоду из @avinfopro
2. vinformer.su (http://vinformer.su/#/Cheack-Vehicle/Captcha=0329976453/&_dm=no) — проверка ПТС, поиск по VIN
3. nomerogram.ru — найдет фото автомобиля, поиск по гос. номеру
4. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — находит полис, часть номера телефона, СТС и адреса парковок в Москве
5. checkvehicle.sfri.ru (https://checkvehicle.sfri.ru/AppCheckVehicle/app/main#cmdr0329976453) — сервис проверки управляемых инвалидом авто или используемых для перевозки инвалида
6. avtocod.ru — марка, модель, часть VIN
7. ГИБДД.РФ (https://xn--90adear.xn--p1ai/check/auto) — по VIN находит технические характеристики, периоды владения транспортным средством, участие в дорожно-транспортных происшествиях, розыск, ограничения, проверка наличия диагностической карты технического осмотра
8. 230km.ru (https://230km.ru/%D0%93%D0%BE%D1%81%D0%9D%D0%BE%D0%BC%D0%B5%D1%80%D0%B0) — по госномеру найдет фото и комментарий к авто
9. reestr-zalogov.ru (http://www.reestr-zalogov.ru/search/index) — по VIN найдет ФИО владельца транспорта, паспорт, адрес регистрации, дату рождения, дату окончания кредита, описание транспорта и историю изменения этих данных
10. autoins.ru (https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfo.htm) — по госномеру или VIN находит часть ФИО владельца, номер водительского удостоверения, ОСАГО, адрес использования авто, и кто регистрировал
11. @TaxiRegister (https://t.me/taxi_reestr_bot) — проверит авто на использование в такси, каршеринге, лизинге, аренде, найдет марку, модель, компанию где использовалось авто
12. @OsintKit (https://t.me/@osintkit_check_bot) — ищет в утечках, дает имена, почты, телефоны и много другого
13. @HomoSpiens (https://t.me/findHOMOrobot) — ищет в утечках, в архивах с 1921 года, дает ФИО владельца, ДТП, полис и прочее
14. @Sherlok (https://t.me/x8152384_bot) — по гос номеру даст имя владельца авто, телефон и прочее
15. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot)  — по номерному знаку даст VIN, СТС, фото авто и прочее, ищет в других ботах

Поиск по регистрационному знаку или номеру СТС в России

1. гибдд.рф (https://xn--90adear.xn--p1ai/check/fines) — найдет штрафы на авто, даст причину, фото нарушения
2. Штрафы ГИБДД (https://vk.com/services?w=app6253254) (r) — найдет историю оплаты штрафа, фамилию плательщика, меняйте СТС и номер авто в настройках

""")
                skip()
            elif vib_tr_str == "2":
                print("""

По украинскому гос номеру или VIN авто

1. @OpenDataUABot — поиск по номерному знаку, выдаст VIN, технические характеристики авто и прочее 
2. Traffic Tickets UA (https://play.google.com/store/apps/details?id=com.shtrafua.android.shtrafua)  — поиск по регистрационному номеру, находит штрафы
3. policy-web.mtsbu.ua — найдет страховой полис, VIN модель и марку
4. unda.com.ua (http://www.unda.com.ua/proverka-gosnomer-UA/#6) — покажет адрес регистрации и данные автомобиля
5. @InfoBaza (https://t.me/xx3738373_bot) — бесплатно найдет характеристики авто, и часть фио владельца авто
6. @ShtrafyPDRbot — покажет штрафы, необходимо указать серию и номер ВУ или налоговый номер или серию и номер паспорта или серию и номер свидетельства о регистрации ТС
7. @CarPlatesUkraineBot — по номеру знаку авто выдаст модель, цвет и прочее
8. unda.com.ua (http://www.unda.com.ua/proverka-gosnomer-UA/) — по госномеру или VIN проверит в розыск, даст сведения о регистрации, VIN, марку, характеристики авто, место регистрации и прочее
9. @InfoLab (https://t.me/ProbivUniversal_New_Bot) — находит, имена, почты, адреса, документы, и прочее, бесплатно покажет только часть данных


Поиск по характеристикам авто

Например: марка, модель, цвет

1. baza-gai.com.ua (https://baza-gai.com.ua/search) — база с 12M автомобилей, находит регистрационный знак. Можно выбрать область

""")
                skip()
            elif vib_tr_str == "3":
                print("""

По казахстанскому номеру авто

1. qamqor.gov.kz (http://qamqor.gov.kz/portal/page/portal/POPageGroup/Services/Trans) — по номерному знаку или VIN авто, проверит на участие в дорожно-транспортных происшествиях

""")
                skip()
            elif vib_tr_str == "4":
                print("""

По номеру авто Австралии

1. service.nsw.gov.au (https://my.service.nsw.gov.au/MyServiceNSW/index#/rms/freeRegoCheck/details) — поиск по штату NSW, предоставляет данные об авто: модель, марка год производства, последние 4 цифры VIN и дату регистрации
2. vicroads.vic.gov.au (https://www.vicroads.vic.gov.au/registration/buy-sell-or-transfer-a-vehicle/check-vehicle-registration/vehicle-registration-enquiry) — поиск по штату VIC, выбор транспотра, предоставляет данные об авто: VIN, Статус регистрации и срок действия, Номер двигателя, регистрационный серийный номер
3. nt.gov.au (https://nt.gov.au/driving/rego/check,-renew-or-transfer-your-registration/rego-check) — поиск по штату NT, предоставляет данные об авто: модель, год, цвет, статус и дату след. проверки
4. transport.tas.gov.au (http://transport.tas.gov.au/MRSWebInterface/public/regoLookup/registrationLookup.jsf) — поиск по штату TAS, предоставляет данные об авто: марка, модель, год выпуска, цвет, статус регистрации, номер двигателя автомобиля
5. ecom.transport.sa.gov.au (https://www.ecom.transport.sa.gov.au/et/checkHighPoweredVehicleStatus.do) — поиск по штату SA, предоставляет данные об авто: цвет, дату оканчания регистрации
6. online.transport.wa.gov.au (https://online.transport.wa.gov.au/webExternal/registration/?0) — поиск по штату WA

""")
                skip()
            elif vib_tr_str == "5":
                print("""

По номеру авто Армении

1. @ArcNET_osint_bot — даст марку, модель, VIN, ФИО и дату рождения владельца, город

""")
                skip()
            elif vib_tr_str == "6":
                print("""

По номеру авто Боливии

1. ruat.gob.bo (https://www.ruat.gob.bo/vehiculos/consultageneral/InicioBusquedaVehiculo.jsf) — найдет номер старого или нового образца если поиск по старому, то даст марку, цвет, характеристики, штрафы, налоги

""")
                skip()
            elif vib_tr_str == "7":
                print("""

По номеру авто Бразилии

1. keplaca.com — по номерному знаку авто выдаст технические характеристики, цвет, марка, часть VIN, и регион использования транспорта
2. consultarplaca.com.br — по номерному знаку авто выдаст цвет, модель бренда, год выпуска и часть VIN

""")
                skip()
            elif vib_tr_str == "8":
                print("""

По номеру авто Белоруси

1. mvd.gov.by (https://mvd.gov.by/ru/service/15) — база утраченных регистрационных знаков
2. osgovts.btib.org (https://osgovts.btib.org/ords/buro/f?p=CHECK_BY_SIGN) — проверка наличия действующего договора обязательного страхования
3. gto.by (https://gto.by/services/permission-check/) — по регистрационному номеру авто выдаст марку/модель, дату окончания действия разрешения на допуск авто к участию в дорожном движении

""")
                skip()
            elif vib_tr_str == "9":
                print("""

По номеру авто Вьетнама

1. dktructuyen.moj.gov.vn (https://dktructuyen.moj.gov.vn/dtn_str/search/public/) — поиск по VIN, дает все информацию о владельце и автомобиля
2. thuxe.vn (http://thuxe.vn/xe/tra-cuu-so-khung) — поиск по VIN, находит модель автомобиля, страну и год постановки на учет

""")
                skip()
            elif vib_tr_str == "10":
                print("""

По номеру авто Великобритании

1. vehicleenquiry.service.gov.uk — марка, цвет, год производства авто
2. www.caranalytics.co.uk — год, цвет, марка, модель и история миль авто
3. checkcardetails.co.uk (https://www.checkcardetails.co.uk/number-plate-check)— год, цвет, марка, модель, место регистрации, пробег
4. rate-driver.co.uk — покажет комментарии от других водителей
5. cazana.com (https://cazana.com/uk/car) — дата регистрации, ориентировочный пробег и когда был выставлен на продажу
6. ownvehicle.askmid.com — проверит действительность, даст марку
7. www.carcheck.co.uk — бренд, марка, цвет, история ТО
8. ownvehicle.askmid.com — проверит в базе автострахования и выдаст статус страховки


По части номера авто

1. www.partialnumberplate.co.uk — найдет цвет, бренд, и полный номер авто, замените неизвестный знак вопросом

""")
                skip()
            elif vib_tr_str == "11":
                print("""

По номеру авто Дании

1. www.nummerplade.net — дата последнего техосмотра, наличие страховки, залога, краткие технические характеристики и т.д.
2. tinglysning.dk (https://www.tinglysning.dk/tmv/forespoergul) — по VIN выдает регистрационный номер и бренд авто

""")
                skip()
            elif vib_tr_str == "12":
                print("""

По номеру авто Индии

1. carinfo.app (https://www.carinfo.app/rc-search) (r) — найдет имя владельца, штрафы и характеристики авто

""")
                skip()
            elif vib_tr_str == "13":
                print("""

По номеру авто Индонезии

1. esamsat.acehprov.go.id — поиск по региону Ачех, найдет бренд, срок исполнения и информация о налоге
2. infonjkbdiy.com — поиск по региону Джокьякарта, найдет стоимость продажи, срок использования

""")
                skip()
            elif vib_tr_str == "14":
                print("""

Поиск по номерному знаку транспортного средства в Ирландии

1. motorcheck.ie — находит марку и модель автомобиля

""")
                skip()
            elif vib_tr_str == "15":
                print("""

По номеру авто Испании

1. oscaro.es — найдет название модели и марку автомобиля
2. seisenlinea.com — по VIN, выдаст технические данные авто, историю владельца, аренда и кражи

""")
                skip()
            elif vib_tr_str == "16":
                print("""

По номеру авто Италии

1. sevim.it (https://www.sevim.it/gratis/targa.asp) — по номерному знаку выдаст регион регистрации и техническое данные

""")
                skip()
            elif vib_tr_str == "17":
                print("""

Поиск по гос номеру авто Израиля

1. meshumeshet.com (https://meshumeshet.com/about) — найдет VIN и базовую информацию
2. Vehicle details (https://play.google.com/store/apps/details?id=com.lidor.iCar) (a) — найдет, VIN, технические характеристики авто, отчеты техосмотра, неточен
3. gov.il (https://www.gov.il/he/departments/dynamiccollectors/private-and-commercial-vehicles) — даст модель и марку, цвет, год выпуска и прочее
4. gov.il (https://www.gov.il/he/Departments/DynamicCollectors/private_vehicle_history_1) — покажет дату регистрации, номер двигателя, и прочее
5. gov.il (https://www.gov.il/he/Departments/DynamicCollectors/private_vehicle_history_2) — отобразит даты владения авто

Как найти фото, имя владельца и его номер телефона по гос номеру авто Израиля

[1] Введите номер авто здесь - meshumeshet.com
[2] Скопируйте объем двигателя, модель, год выпуска, мощность
[3] Введите все эти данные на сайте по поиску всех исторических объявлений - www.ad.co.il/car

В результате вы получите список всех объявлений о продаже такого же авто. В объявлениях есть фото с номерами, имена владельца и его номер телефона

""")
                skip()
            elif vib_tr_str == "18":
                print("""

По номеру авто в Канаде

1. sgi.sk.ca (http://www.sgi.sk.ca/) — по VIN найдет повреждения и штрафы
2. pic-cipc.ca (https://www.cpic-cipc.ca/sve-rve-eng.htm) — по VIN проверит авто в реестре украденных машин

""")
                skip()
            elif vib_tr_str == "19":
                print("""

По номеру авто в Киргизии

1. portal.srs.kg (https://portal.srs.kg/ru/service/eform/d1a29582-8014-4196-ac3b-956c4855f352) — поиск по госномеру, найдет штрафы, модель, цвет даты владения
2. mashina.kg (https://m.mashina.kg/carcheck/)  — найдет фото авто, объявления

""")
                skip()
            elif vib_tr_str == "20":
                print("""

По номеру авто Китая

1. tools.2345.com (http://tools.2345.com/carlist.htm) — по регистрационному номеру авто находит город регистрации автомобиля
2. m.tk.cn (http://m.tk.cn/carTKInsure/#/insureProcess/userinformation) — найдет VIN, модель, номер двигателя и прочее, введите гос номер авто и остальные поля сами заполнятся

""")
                skip()
            elif vib_tr_str == "21":
                print("""

По номеру авто Монголии

1. torguuli.police.gov.mn — информация об оплаченных и неоплаченных штрафа

""")
                skip()
            elif vib_tr_str == "22":
                print("""

По номеру авто Нигерии

1. nvis.frsc.gov.ng (https://nvis.frsc.gov.ng/VehicleManagement/VerifyPlateNo) — найдет цвет и марку авто

""")
                skip()
            elif vib_tr_str == "23":
                print("""

По номеру авто в Нидерландах

1. ovi.rdw.nl (https://ovi.rdw.nl/default.aspx) — найдет цвет, категорию, бренд, марку, дату регистрации и многое другое
2. kentekencheck.nl — модель автомобиля и цена нового, технические характеристики, дата последнего ТО и дата постановки на учет

""")
                skip()
            elif vib_tr_str == "24":
                print("""

По номеру авто Норвегии

1. vegvesen.no (https://www.vegvesen.no/Kjoretoy/Kjop+og+salg/Kj%C3%B8ret%C3%B8yopplysninger) — наиподробнейший отчет о техническом состоянии автомобиля. Например: экологический класс и величина выбросов углекислого газа, максимальная нагрузка в кг, оптимальная нагрузка в кг, маскимальная нагрузка на крышу. Всего более сотни параметров.

""")
                skip()
            elif vib_tr_str == "25":
                print("""

По номеру авто Перу

1. sunarp.gob.pe (https://www.sunarp.gob.pe/seccion/servicios/detalles/0/c3.html) — найдёт VIN, имя владельца, характеристики авто, цвет и модель

""")
                skip()
            elif vib_tr_str == "26":
                print("""

По номеру авто Польши

1. historiapojazdu.gov.pl  (https://historiapojazdu.gov.pl/strona-glowna)— покажет всю истории авто, требуется VIN, номер авто, дата первой регистрации авто
2. verso.pl (http://www.verso.pl/lu/spis/spis_rej.php) — по номерному знаку найдет фото авто
3. piraci-drogowi.pl (http://piraci-drogowi.pl/index.php?strona=search) — по номерному знаку найдет ДТП, место происшествия, описание ситуации и прочее

""")
                skip()
            elif vib_tr_str == "27":
                print("""

По номеру авто Португалии

1. asf.com.pt (http://www.asf.com.pt/isp/Templates/Atendimento/PesquisaVeiculoSeguro.aspx?FRAMELESS=false&NRNODEGUID=%7B09089E16-115D-4C82-9C64-FDA43D5FF098%7D) — найдет информацию о страховке

""")
                skip()
            elif vib_tr_str == "28":
                print("""

По номеру авто Румынии

1. politiaromana.ro (https://www.politiaromana.ro/ro/auto-furate) — поиск по VIN или номерному знаку в реестре угнанных авто, найдет цвет и дату и место кражи

""")
                skip()
            elif vib_tr_str == "29":
                print("""

По номеру авто Словакии

1. www.stkonline.sk — поиск по VIN, номерному знаку, дает часть VIN, бренд, марку, цвет

""")
                skip()
            elif vib_tr_str == "30":
                print("""

По номеру авто США

1. carvana.com (https://www.carvana.com/sellyourcar/getoffer/vehicle?licensePlate=SOME&licenseplate=SOME&plateState=FL&state=FL) — по номерному знаку автомобиля, нужен VPN, работает только для IP США, необходимо знать штат, есть поиск по VIN
2. faxvin.com (https://www.faxvin.com/license-plate-lookup) — по номерному знаку автомобиля, найдет VIN, модель, год
3. vincheck.info (https://vincheck.info/free-license-plate-lookup/) — по номерному знаку автомобиля найдет VIN, модель, год, отчеты об авариях, отчеты о продажах, кражи, аукционы, подробную информацию о модели,
4. iseecars.com (https://www.iseecars.com/vin) (r) — по VIN огромный отчет, где место продажи, количество владельцев
5. poctra.com — по номерному знаку автомобиля или VIN найдет на аукционе разбитых авто марку модель, фото и ссылку на сайт-аукцион
6. howsmydrivingny.nyc — по номерному знаку автомобиля найдет адрес и дату нарушения, штраф
7. findbyplate.com — по номерному знаку найдет фото, видео, нарушения и комментарий от пользователей, ресурс работает через VPN
8. vehiclehistory.com — по VIN найдет технические характеристики авто, историю продаж, отзывы, аукционы, история владельцев, сайт работает только с IP адреса США, используй VPN

""")
                skip()
            elif vib_tr_str == "31":
                print("""

По номеру авто Финляндии

1. biltema.fi (https://www.biltema.fi/auton-varaosahaku/) — марка, модель, дата регистрации, краткие технические характеристики

""")
                skip()
            elif vib_tr_str == "32":
                print("""

По номеру авто Франции

1. siv-auto.fr — по номерному знаку выдаст марку, модель, цвет, VIN и дату ввода в эксплуатацию

""")
                skip()
            elif vib_tr_str == "33":
                print("""

По номеру авто Чехии

1. spz.penize.cz — регион регистрации, марка автомобиля, страховая компания, дата начала страхования, страховой рейтинг

""")
                skip()
            elif vib_tr_str == "34":
                print("""

По номеру авто Швеции

1. car.info (https://www.car.info/en-se/search-car-registry) — найдет объявления о продаже и полную информацию об авто
2. fu-regnr.transportstyrelsen.se (https://fu-regnr.transportstyrelsen.se/extweb/UppgifterAnnatFordon) — по номерному знаку выдаст имя владельца, его адрес проживания, VIN, цвет, бренд и прочее

""")
                skip()
            elif vib_tr_str == "35":
                print("""

По номеру авто Швейцарии

1. linker.ch — список сайтов которые предоставляют данные об авто, разделено по регионам, есть платные и бесплатные сервисы
2. viacar.ch (https://www.viacar.ch/eindex/Result.aspx) — по номерному знаку авто или мотоцикла найдет адрес и ФИО владельца
3. ocn.ch (https://www.ocn.ch/fr/conduire/plaques-et-carte-grise/auto-index-trouver-un-detenteur-ou-une-detentrice-de-vehicule) — по номерному знаку авто или мотоцикла во Фрибурге найдет адрес и ФИО владельца
4. ti.ch (https://www4.ti.ch/di/sc/veicoli/elenco-targhe) — по номерному знаку авто или мотоцикла найдет ФИО владельца и его адрес регистрации

""")
                skip()
            elif vib_tr_str == "36":
                print("""

По номеру авто Эстонии

1. eteenindus.mnt.ee (https://eteenindus.mnt.ee/public/soidukTaustakontroll.jsf) — по VIN или номерному знаку даст ограничения и историю использования
2. www.lkf.ee (https://www.lkf.ee/et/kahjukontroll) — по VIN или номерному знаку проверит авто на дорожно-транспортные происшествия.

""")
                skip()
            elif vib_tr_str == "37":
                print("""

По номеру авто Эквадора

1. www.consultavehicular.ame.gob.ec (https://www.consultavehicular.ame.gob.ec/consultas/) — найдет VIN, дату регистрации, налоги, историю продаж, RAMV

""")
                skip()
            elif vib_tr_str == "38":
                print("""

По номеру авто Японии

1. nplate.html.xdomain.jp — огромный справочник по устройству систему автомобильных номеров, определения региона регистрации по первым цифрам номера

""")
                skip()
            elif vib_tr_str == "39":
                print("""

Как определить какой страны регистрационный знак автомобиля

1. worldlicenseplates.com — каталог регистрационных знаков всех стран и историей изменения
2. platerecognizer.com — по фото определит страну, номер, и распознает даже нечеткое изображение


Дополнительные методы

1. Используйте обратный поиск по изображению регистрационного номера в Yandex (https://yandex.ru/images/) или Google (https://www.google.com/imghp)

""")
                skip()
            else:
                print('Попробуйте еще раз')
                skip()
        elif vib_tr == "2":
            print("Какие именно данные самолета известны?")
            print("[1]Позывной, [2]Модель")
            vib_tr_sam = input()
            if vib_tr_sam == "1":
                print("""

Поиск по позывному самолета

1. de.flightaware.com — найдет историю перелетов, даст общую информацию о воздушном судне
2. globe.adsbexchange.com — найдет на карте все самолеты в воздухе с таким позывным, есть военные воздушные судна
3. planespotters.net (https://www.planespotters.net/production-list/index) — находит историю самолета, тех. состояние, авиакомпании
4. avherald.com — история инцидентов самолета
5. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США
6. data.ntsb.gov (https://data.ntsb.gov/carol-main-public/basic-search) — информация о несчастных случаях, крушениях и расследований, поиск во всех странах
7. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, найдет детали самолета, спасательную информацию, владельца и держателя самолета

""")
                skip()
            elif vib_tr_sam == "2":
                print("""

Поиск по модели самолета

1. rzjets.net/aircraft — база моделей джетов, найдет владельца, регистрационный номер и многое другое
2. radarbox.com (https://www.radarbox.com/data/aircraft/) — найдет все самолеты в небе
3. globe.adsbexchange.com — найдет на карте все самолеты в воздухе такой модели, есть военные воздушные судна
4. seatguru.com (https://seatguru.com/browseairlines/browseairlines.php) — схема сидений самолета, есть номера мест
5. planespotters.net (https://www.planespotters.net/production-list/index) — находит историю самолета, позывные, тех. состояние, авиакомпании
6. avherald.com — история инцидентов самолета
7. data.ntsb.gov (https://data.ntsb.gov/carol-main-public/query-builder) — информация о несчастных случаях, крушениях и расследований, поиск во всех странах
8. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, найдет детали самолета, спасательную информацию, владельца и держателя самолета


Как найти историю перелётов по модели самолёта

1. Скопируйте модель самолёта и откройте ссылку:

http://avionictools.com/icao.php

2. Введите в поле с параметром “N number” модель и нажмите Calc
3. Скопируй значение Hex
4. Подставь значение Hex в ссылку вместо HEX:

https://globe.adsbexchange.com/?icao=HEX

5. Открой эту ссылку, если самолёт нашёлся найти и открой вкладку History в карточке самолёта

Теперь можно листать или указать нужную дату, а сайт покажет перелёт на карте

""")
                skip()
        elif vib_tr == "3":
            print("Пока поиск доступен только по Индии")
            print("""

По номеру мотоцикла Индии

1. acko.com (https://www.acko.com/lp/new-bike) — найдет бренд, можешь и год производства мотоцикла

""")
            skip()
        elif vib_tr == "4":
            print("""


Поиск по номеру поезда в Европе

1. pass.rzd.ru (https://pass.rzd.ru/tablo/public/ru?STRUCTURE_ID=5199) — показывает график следования, необходимо указать станцию прибытия на территории России
2. www.sncf.com (https://www.sncf.com/en/booking-itinerary/search-train-number/) — показывает расписание движения поезда в конкретную дату на территории Франции
3. bahn.de (https://reiseauskunft.bahn.de/bin/bhftafel.exe/en) — расписание движения поезда в конкретную дату на территории Германии
4. junatkartalla.vr.fi (https://junatkartalla.vr.fi/?lang=en-US) — фактическое движение поезда на карте в реальном времени, есть расписание остановок на территории Финляндии


Поиск по номеру вогона

1. gdevagon.ru (https://www.gdevagon.ru/scripts/references/check_car_number.php) (r) — проверит действительность номера

Поиск по номеру поезда в Азии

1. railyatri.in (https://www.railyatri.in/live-train-status) — расписание остановок поезда и фактический график движения с платформами прибытия и временем стоянки на территории Индии

""")
            skip()
        elif vbr_tr == "5":
            print("""

Поиск по имени судна

1. marinetraffic.com — найдет позывной, MMSI, IMO, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. www.vesselfinder.com — найдет судно на карте в реальном времени
4. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США
5. data.ntsb.gov (https://data.ntsb.gov/carol-main-public/query-builder) — информация о несчастных случаях, крушениях и расследований, поиск во всех странах
6. wwwapps.tc.gc.ca (https://wwwapps.tc.gc.ca/Saf-Sec-Sur/4/vrqs-srib/eng/vessel-registrations/search) — для судов Канады найдет историю владельцев, их имена и адреса, характеристики судна, его номера и прочее
7. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона

Поиск по IMO судна

1. marinetraffic.com — найдет позывной, MMSI, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. gisis.imo.org (https://gisis.imo.org/Public/Default.aspx) (r) — найдет адрес и название компании, сводку по эксплуатации кораблей
4. vesselfinder.com — найдет судно на карте в реальном времени
5. portcalltable.marinet.ru — покажет название, MMSI, позывной, характеристики, собственников, владельцев, даты заходов/выходов из российских портов, для поиска открой вкладку суды
6. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона

Поиск по MMSI судна

1. marinetraffic.com — найдет позывной, IMO, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона

Поиск по позывному судна

1. marinetraffic.com — найдет MMSI, IMO, рейсы и историю имени судна
2. maritime-connector.com (http://maritime-connector.com/ship/) — найдет базовую информацию и данные о владельце
3. vesselfinder.com — найдет судно на карте в реальном времени
4. portcalltable.marinet.ru — покажет название, MMSI, позывной, характеристики, собственников, владельцев, даты заходов/выходов из российских портов, для поиска открой вкладку суды
5. inmarsat.com (https://www.inmarsat.com/en/support-and-info/support/ships-directory.html) — найдет контактный номер телефона

Поиск по номерному знаку судна

1. ocn.ch (https://www.ocn.ch/fr/conduire/plaques-et-carte-grise/auto-index-trouver-un-detenteur-ou-une-detentrice-de-vehicule) — по номерному знаку судна во Фрибурге, Швейцариия, найдет адрес и ФИО его владельца

""")
            skip()
        elif vbr_tr == "6":
            print("""

Поиск по номеру грузового контейнера

1. panjiva.com (http://panjiva.com/search) — найдет содержимое и вес контейнера, имя компании грузоотправителя и грузополучателя, адрес грузополучателя и отгрузки, название судна, номер коносамента и другие данные
2. www.searates.com (https://www.searates.com/container/tracking/) — покажет дату и место отправки и прибытия, текущее местонахождение контейнера
3. www.track-trace.com (http://www.track-trace.com/container) — дает прямую ссылку на сайт транспортной компании где есть резюме контейнера, его маршруты, и детальный отчет о оборудовании и задержаниях

""")
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == "9":
        print("Чьи документы?")
        print("[1]ИП и компании,[2]Физ.лица")
        vibd = input()
        if vibd == "1":
            print("""

Поиск по документам юридических лиц любой страны

1. opencorporates.com — по наименованию организаций, агрегатор данных компаний со всего мира
2. dnb.com — по наименованию компании в базах всех стран
3. aleph.occrp.org — по наименованию компании и другим данным в базах данных, файлам, реестрам компаний, утечкам, и другим источникам
4. offshoreleaks.icij.org — по наименованию организаций в базе данных оффшорных утечек, найдет имена, адреса, связи
5. privatization.lot-online.ru (https://privatization.lot-online.ru/) — по наименованию компании в электронной торговой площадке
6. munscanner.com (https://munscanner.com/dbs/) — по наименованию компании в реестрах организаций разных стран
7. gisis.imo.org (https://gisis.imo.org/Public/Default.aspx) (r) — по наименованию компании найдет IMO, сводку по эксплуатации кораблей и адрес компании
8. news-explorer.mybluemix.net — по наименованию компании, поиск в СМИ, найдет ассоциации между компаниями, публикациями и личностями
9. sanctionssearch.ofac.treas.gov — по наименованию компании, поиск в санкционном списке США
10. crosslinked (https://github.com/m8r0wn/crosslinked) (t) — по наименованию компании, найдет список имен и фамилий сотрудников компании
11. en.52wmb.com (r) — по наименованию компании, покажет где и чем торгует компании на мировом рынке
12. supplychaindive.com (https://www.supplychaindive.com/search/) — по наименованию компании, находит упоминания в пресс-релизах и новостях, есть фильтр по теме
13. panjiva.com (http://panjiva.com/search) — по наименованию компании, покажет где и чем торгует компании на мировом рынке
14. search.gleif.org — найдет историю изменений компании, даст знать кто кем владеет, есть фильтры по стране
15. tmdn.org (https://www.tmdn.org/tmdsview-web/#/dsview) — по названию компании найдет чертежи и описание промышленных образцов
16. app02.bazl.admin.ch (https://app02.bazl.admin.ch/web/bazl/en/#/lfr/search) — реестр Швейцарии, по названию компании найдет зарегистрированые самолёты и вертолеты
17. importyeti.com — по названию компании найдёт поставки, импорт, адреса, продукцию, статистику и прочие
18. opensanctions.org — по названию компании найдет в списке санкций, даст имя директора, регистрационный номер, попробуй ввести название латиницей
19. register.openownership.org — найдет имена бенефициаров, владельцев, историю изменений, построит граф связей
20. app.snov.io (r) — по названию компании даёт Email, имена и должности сотрудников, инвесторов
21. archivesportaleurope.net (https://www.archivesportaleurope.net/advanced-search/search-in-archives/) — найдет упоминание в национальных архивах стран Европы, можно найти в сделки, контракты, письма и прочее

""")
            skip()
        elif vibd == "2":
            print("""

Поиск по документам физических лиц Европы

1. ec.europa.eu (https://ec.europa.eu/taxation_customs/tin/#/check-tin) — по ИНН проверит его действительность, только страны ЕС

Для документов физических лиц Казахстана

1. kgd.gov.kz (http://kgd.gov.kz/ru/services/taxpayer_search) — данные налогоплательщиков, поиск по РНН, ИИН, ФИО, для ИП поиск по названию, РНН и ИИН/БИН; найдет ИИН. Сервис иногда недоступен
2. fa-fa.kz (https://fa-fa.kz/search_ip_too/) — по ИИН, БИН, проверит задолженностей, ИП, и ограничения на выезд
3. @ShtrafKZBot (https://t.me/ShtrafKZBot?start=c4038c17dfc742a4b) — по ИИН найдет правонарушения, задолженности, ограничения на выезд, статус социальных выплат, имущества на торгах, руководитель компаний, розыск, реестр педофилов
4. kgd.gov.kz (http://kgd.gov.kz/ru/services/ndspayer_search) — по ИИН/БИН и РНН данные о плательщиках НДС
5. pk.adata.kz — по ИИН/БИН, находит государственные договора
6. aisoip.adilet.gov.kz (https://aisoip.adilet.gov.kz/forCitizens/findArest) — по ИИН или БИН проверит аресты счета, имущества, запреты на выезд и регистрацию
7. imei.rfs.gov.kz (https://imei.rfs.gov.kz/index_ru.php) — по ИИН найдет название оператора и число зарегистрированных телефонных номеров
8. idp.egov.kz (https://idp.egov.kz/idp/register.jsp) — по ИИН, форма регистрации, найдет часть номера телефона

Для документов физических лиц США

1. intelx.io — по SSN, находит документы
2. stevemorse.org (https://stevemorse.org/ssn/ssn.html) — декодирует SSN, может показать дату выпуска номера
3. stevemorse.org (https://stevemorse.org/dl/dl.html) —  декодирует SSN, может показать дату рождения и начало ФИО
4. stevemorse.org (https://stevemorse.org/ssdi/ssdi.html) — реестр регистрации смерти с 1936 гг. по 2014 гг., найдет по SSN дату рождения и смерти, ФИО, штат

""")
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == "10":
        print("""

Поиск по любому домену

1. hunter.io  — дает email адреса
2. @WhoisDomBot — узнайте базовую информацию о домене
3. community.riskiq.com  — найдет сертификаты, историю whois, трекеры, reverse DNS и многое другое
4. Knock Subdomain Scan (https://github.com/guelfoweb/knock)  — находит поддомены и FTP
5. builtwith.com — технологический профиль сайта, взаимосвязи между сайтами
6. urlscan.io — сервис для сканирования и анализа сайтов
7. dnsdumpster.com — обнаруживает хосты связанные с доменом
8. censys.io (https://search.censys.io/) — находит какие серверы и устройства выставлены в сети
9. virustotal.com — служба пассивного DNS, поиск под доменов, найдет whois и историю сертификатов SSL
10. atsameip.intercode.ca — одинаковые IP у сайта, можно узнать под домены
11. dirhunt (https://github.com/Nekmo/dirhunt)  — поиск директорий сайта без брута
12. Amass (https://github.com/OWASP/Amass)  — сетевое картирование поверхностей атаки и обнаружение внешних ресурсов с использованием методов сбора информации с открытым исходным кодом и активных методов разведки
13. Photon (https://github.com/s0md3v/Photon)  — найдет на сайте файлы, секретные ключи, JS файлы, URL с параметрами 
14. dnslytics.com (https://dnslytics.com/reverse-analytics) — вытаскивает трекеры из сайта
15. domainwat.ch — найдет в Whois имя регистранта, адрес, номер телефона, адрес электронной почты из информации WHOIS и историю изменений
16. findomain (https://github.com/Edu4rdSHL/findomain)  — найдет под домены
17. shodan.io — найдет IP адреса и сайты с упоминанием искомого сайта
18. phonebook.cz  — найдет email, под домены, директории сайта
19. visualsitemapper.com (http://www.visualsitemapper.com/) — визуализация карты сайта одним графиком
20. dorks.faisalahmed.me — составляет дорки для Google и Яндекс
21. synapsint.com — хорошо ищет поддомены 
22. analyzeid.com — находит на странице идентификаторы аналитики и по ним ищет другие сайты
23. FavFreak (https://github.com/devanshbatham/FavFreak)  — находит все сайты схожим favicon
24. completedns.com (https://completedns.com/dns-history/) — история DNS за двадцать лет
25. pidrila (https://github.com/enemy-submarine/pidrila)  — находит директории сайта
26. osint.sh — поддомены, история DNS, сканер NMAP и много другого
27. mmhdan.herokuapp.com — вычислит хеш значка сайта и даст ссылки на ресурсы где можно найти похожие сайты с одинаковыми значками
28. o365chk (https://github.com/nixintel/o365chk/)  — проверит наличие у сайта Microsoft Office365, выдаст email, облачное имя и ссылку для в хода в офис
29. pagexray.fouanalytics.com — найдет к каким сайтам делаются запросы для трекинга и аналитики, делает скриншот сайта
30. metagoofil (https://github.com/laramies/metagoofil)  — найдет метаданные во всех документах на сайте
31. email-format.com (https://www.email-format.com/i/search/) — даст email, дату их обнаружения и источник
32. tools.whoisxmlapi.com (https://tools.whoisxmlapi.com/whois-history-search) — найдет всю историю изменений whois домена
33. link-assistant.com (https://www.link-assistant.com/seo-spyglass/free-backlink-checker-tool.html) — найдет источники упоминания домена и их анализ
34. talosintelligence.com (https://talosintelligence.com/reputation_center/) — покажет сколько писем было отправлено с домена и его репутацию
35. leak-lookup.com (https://leak-lookup.com/search)  — покажет на каких сайтах была утечка с искомым доменом
36. app.netlas.io  — поддомены, устройства, IP адреса, CVE и уязвимости
37. domaincodex.com (https://www.domaincodex.com/search.php) — выдает поддомены, whois, файлы и прочее
38. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — даст прямые ссылки на 50+ ресурсов где есть история Whois, IP, DNS, Nameserver, сертификаты, трекеры, похожие домены, контакты, архивы, дорки и прочее
39. SourceWolf (https://github.com/ksharinarayanan/SourceWolf)  — ищет в исходном коде и скриптах сайта ссылки на соцсети и эндпоинты
40. omnisint.io — найдет поддомены, регистрация без проверки
41. pulsedive.com — найдет историю DNS, SSL и Whois, почту, технологии, регистратора домена, порты, угрозы, поддомены, почтовые сервера и прочее
42. tenantresolution.pingcastle.com — покажет другие домены владельца сайта на основе Azure ID
43. seckrd.com (https://seckrd.com/subdomain-finder) — достанет поддомены
44. hudsonrock.com (https://cavalier.hudsonrock.com/passwords) — покажет число утекших паролей сайта и некоторые его директории


Поиск через URL

1. https://psbdmp.ws/api/search/domain/example.com — упоминания в утечках на Pastebin, замените example.com, сайт выдаст id страниц, подставь этот ID в ссылку pastebin.com/ID


Архив

1. timetravel.mementoweb.org — найдет сохраненные копии сайта среди 30 ресурсов для архивации 
2. web.archive.org — показывает сохранённые копии страниц, исходный код, все директории сайта, статистику и много другого
3. cachedview.com — найдет копию сайта из кэша Google
4. oldweb.today —  найдет исторические версии сайтов, можно выбрать вид браузера и дату
5. arquivo.pt — есть расширенный поиск по сайту
6. archive.md — помимо HTML версии архивирует скриншот сайта
7. trove.nla.gov.au — найдет копию страницы, откройте расширенный поиск и укажите домен, можно искать в архиве страниц по ключевому слову


Парсеры

1. waybackpack (https://github.com/jsvine/waybackpack)  — загружает весь архив Wayback Machine
2. archivarix.com — восстанавливает полную копию сайта из веб-архива на определенную дату, до 200 файлов бесплатно


Инструменты

1. followthatpage.com  — следит за сайтом, сообщит о изменениях страницы на почту
2. @suzanne_archiver_bot — архивирует сайт в 3 веб-архивах
3. @watch_bot — следит за изменениями на сайте, отправляет уведомление вам в Telegram
4. visualping.io — следит за изменениями сайта, также можно выбрать область где следить, отправляется уведомление на почту

Поисковые операторы для поиска по домену

Операторы поиска Google и Яндекс — это символы и слова, с помощью которых можно уточнить и сузить поиск. Они бывают простыми и сложными и могут комбинироваться друг с другом. Некоторые поисковые операторы Google совпадают с теми, что используются в Яндекс, а некоторые работают только для конкретного поисковика


Дорки для Google

Замените site.com на домен

1. site:*.site.com

2. cache:site.com

3. inurl:site.com

4. site:site.com ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv

5. site:site.com intitle:index.of

6. site:site.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env

7. site:site.com ext:sql | ext:dbf | ext:mdb

8. site:site.com ext:log

9. site:site.com ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup

10. site:site.com inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth

11. site:site.com intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"

12. site:site.com "PHP Parse error" | "PHP Warning" | "PHP Error"

13. site:site.com ext:php intitle:phpinfo "published by the PHP Group"

14. site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com "site.com"

15. site:github.com | site:gitlab.com "site.com"

16. site:site.com inurl:signup | inurl:register | intitle:Signup





Поиск по домену с .ru

1. backorder.ru — найдет историю изменений записей whois, возраст домена, покажет траффик посещений сайта и прочее


Поиск по домену с .onion

1. darktracer.io — находит настоящий IP адрес
2. pidrila (https://github.com/enemy-submarine/pidrila)  — выявляет директории сайта


Поиск через URL

1. https://osint.party/api/onion/DOMAIN — найдет метаданные сайта, замените DOMAIN на адрес сайта без .onion


""")
        skip()
    elif data == "11":
        print("Какой файл?")
        print("[1]Картинка, [2]Видео, [3]Документ, [4]HAR, [5]DS_STORE, [6]Приложение, [7]CSV, [8]Любой")
        vib_f = input()
        if vib_f == "1":
            print("""

Для файла формата изображение

1. metadata2go.com (https://www.metadata2go.com/view-metadata) — покажет EXIF и метаданные картинки
2. stolencamerafinder.com — определит EXIF и по этим данным найдет какие еще фото были сделаны этим устройством
3. 29a.ch (https://29a.ch/photo-forensics/#level-sweep) —  фото-форензика, анализ изображения на изменения
4. stylesuxx.github.io (https://stylesuxx.github.io/steganography/) — декодирует скрытое сообщение в изображении
5. Depix (https://github.com/beurtschipper/Depix)  — депикселизирует текст на картинке, помогает узнать слова и буквы которые были замазаны с помощью пикселизации
6. focusmagic.com  — восстановит детали и резкость размытых фотографий
7. forensicdots.de — ищет на скане документа желтые точки являющиеся уникальным идентификатором принтера
8. diffchecker.com (https://www.diffchecker.com/image-diff/) — помогает найти различия двух картинок
9. compress-or-die.com (https://compress-or-die.com/analyze-process) — показывает ICC_Profile, в нем можно по скриншоту на Mac узнать дату последнего обновления системы, есть EXIF и таблица квантования яркости
10. exiftool.org  — программа для чтения, записи и редактирования метаинформации, определит производителя многих цифровых камер
11. exif-py (https://github.com/ianare/exif-py)  — выгружает метаданные из большого объёма изображений 


Поиск по картинке

1. Yandex
 (https://yandex.ru/images/)2. Google (https://www.google.com/imghp) — открывать на ПК
3. Bing
 (https://www.bing.com/visualsearch)4. Tineye
 (http://tineye.com/)5. agent.earthkit.app  — найдет место съемки, дает очень хорошие результаты
6. Numlookup (https://www.numlookup.com/reverse-image-search)
7. searchbyimage.app  — находит товары в многих интернет-магазинах
8. thieve.co (http://thieve.co/tools/image-search) — находит товары в Aliexpress
9. aliseeks.com (https://www.aliseeks.com/search/)— находит товары в Aliexpress и eBay
10. labs.tib.eu (https://labs.tib.eu/geoestimation/) — найдет примерное место съемки фото
11. image.baidu.com
12. image.so.com
13. saucenao.com
14. depositphotos.com (https://depositphotos.com/search/by-images.html)
15. Osintleak (https://osintleak.com/dashboard/tools/rimage)  — надет источник изображения

Инструменты

1. magiceraser.io — качественно удалит выделенную область на фото, необходимо для подготовки фото к поиску по картинке
2. waifu2x.booru.pics — улучшает качество картинки
3. app.remini.ai — сделает картинку четче
4. upscayl (https://upscayl.github.io/)  — улучшает качество картинки

""")
            skip()
        elif vib_f == "2":
            print("""

Для файла формата видео

1. videoindexer.ai (r) — сохраняет лица, слова, темы, и эмблемы из видео
2. app.remini.ai — сделает видео четче
3. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — можно отправить как файл и посмотреть метаданные и EXIF
4. metadata2go.com (https://www.metadata2go.com/view-metadata) — достает метаданные и EXIF

""")
            skip()
        elif vib_f == "3":
            print("""

Для файла формата документ

1. @mediainforobot — извлекает EXIF, отправь в бот файл
2. www.forensicdots.de — ищет на скане документа желтые точки являющиеся уникальным идентификатором принтера
3. exiftool.org (t) — программа для чтения, записи и редактирования метаинформации

Инструменты

1. draftable.com (https://draftable.com/compare) — сравнивает два документа показывает разницу
2. diffchecker.com (https://www.diffchecker.com/excel-diff/) — сравнивает документы PDF, таблицы Excel и показывает отличия между ними

""")
            skip()
        elif vib_f == "4":
            print("""

Для файла формата HAR

1. stevesie.com (https://stevesie.com/har-file-web-scraper) — покажет содержимое файла в удобном виде
2. googleapps.com (https://toolbox.googleapps.com/apps/har_analyzer/) — покажет содержимое файла в удобном виде

""")
            skip()
        elif vib_f == "5":
            print("""

Для файла формата DS_STORE

1. intelx.io (https://intelx.io/tools?tab=filetool) — узнайте имена файлов скрытые в файле

""")
            skip()
        elif vib_f == "6":
            print("""

Для Андройд приложения 

1. bevigil.com (https://bevigil.com/scanApp) (r) — покажет строки, ссылки, API методы приложения
2. beta.pithus.org — покажет строки, ссылки, API методы приложения, домены, анализ кода, уязвимости
3. appetize.io (r) — запускает в эмуляторе приложение, дает отследить его запросы

""")
            skip()
        elif vib_f == "7":
            print("""

Для файла формата CSV

1. moderncsv.com (t) — отобразит содержание файла, работает даже с огромными размерами, можно удобно редактировать и искать в содержимом, подходит для утечек

""")
            skip()
        elif vib_f == "8":
            print("""

Для файла любого расширения

1. AstroGrep (https://sourceforge.net/projects/astrogrep/files/latest/download) (t) — поможет искать в огромных файлах, для больших баз, на Windows, удобный интерфейс
2. dnGrep (http://dngrep.github.io/) (t) — дает поиск в файлах любого размера на Windows, удобный интерфейс
3. aGrep (https://play.google.com/store/apps/details?id=jp.sblo.pandora.aGrep) (a) — поможет искать в огромных файлах, для больших баз, на Android
4. Virustotal.com — проверит на вирусы, альтернативные имена, рейтинг файла, поведение, связи с другими файлами


Метаданные

1. get-metadata.com — извлекает метаданные
2. exiftool.org (t) — программа для чтения, записи и редактирования метаинформации
3. media-info (https://play.google.com/store/apps/details?id=net.mediaarea.mediainfo) (a) — приложение на Android, достанет EXIF и метаданные почти любого файла

""")
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    elif data == "12":
        print("К каким категориям данные относятся?")
        print("[1]Криптокошельки,[2]Платёжные системы,[3]Номер банковской карты")
        vibno = input()
        if vibno == "1":
            print("""

Поиск по адресу крипто кошелька Bitcoin

1. intelx.io (https://intelx.io/tools?tab=bitcoin) — найдет упоминания в утечках и БД
2. www.blockchain.com — покажет все транзакции
3. live.blockcypher.com — покажет все транзакции
4. blockchair.com — покажет все транзакции
5. maltego (http://maltego.com/downloads/) (t) — визуальное представление и анализ транзакций
6. oxt.me (r) — визуальное представление и анализ транзакций в браузере, не работает мобильная версия
7. learnmeabitcoin.com (https://learnmeabitcoin.com/tools/path/) — цепочка транзакций между двумя кошельками
8. awebanalysis.com (https://awebanalysis.com/en/bitcoin-multiple-address-check-balance/) — загружаете список адресов и получаете таблицу с данными текущего баланса за все время
9. blockpath.com — покажет транзакции кошелька в виде графа, можно добавлять несколько адресов
10. @cryptoaml_bot — узнает источники поступления средств на крипто кошелёк и дает оценку риска, 1 бесплатный поиск на аккаунт
11. explorer.crystalblockchain.com — покажет граф транзакций, определяет владельца кошелька, можно добавлять несколько кошельков чтобы найти общие связи
12. opensanctions.org — упоминание в санкционном списке
13. tvhsyd.onion.ly (http://pdcdvggsz5vhzbtxqn2rh27qovzga4pnrygya4ossewu64dqh2tvhsyd.onion.ly/) — проанализирует цепочки переводов и покажет какой процент обменников, майнеров, миксеров и грязных денег есть на балансе адреса
14. breadcrumbs.app (https://www.breadcrumbs.app/home) — построит удобный граф транзакции кошелька, выявляет адреса кошельков бирж и мошенников, дает статистику входов и выходов, работает только с VPN
15. scamsearch.io — реестр мошенников, найдет почту, причину внесения в реестр, номер телефона, дату и прочее
16. @pwIPbot — найдет отзывы в двух источниках, санкции США, может найти связь между двумя адресами
17. @green_stage_bot — AML, опередит риски, скажет сколько переводов связано с даркнетом, обменниками, миксерами, азартными играми и прочим
18. tokenscope.com (r) — построит путевую карту и граф транзакций кошелька
19. metasleuth.io — отобразит граф транзакций
20. glasschain.org — определит биржу кошелька, или обменник, покажет отзывы


Инструменты

1. cryptocurrencyalerting.com (https://cryptocurrencyalerting.com/wallet-watch.html) (r) — следит за изменениями баланса кошелька, отправляет уведомление на Email, SMS, Discord или в Telegram

Поиск по адресу крипто кошелька TON

1. tonviewer.com — найдет все транзакции, комментарии к переводам
2. @cryptoaml_bot — узнает источники поступления средств на крипто кошелёк и дает оценку риска, 1 бесплатный поиск на аккаунт
3. @EyeOfTON (https://t.me/istoneyebot) — анализирует блокчейны и найдет анонимные номера, имена пользователя, адреса криптобирж, связанные кошельки, покупки Telegram Stars и прочие


Инструменты

1. @tontracker_bot — пришлет уведомление о новых транзакциях кошелька

Поиск по адресу крипто кошелька в сети Tron

1. metasleuth.io — отобразит граф транзакций
2. @cryptoaml_bot — узнает источники поступления средств на крипто кошелёк и дает оценку риска, 1 бесплатный поиск на аккаунт


Поиск по адресу крипто кошелька в сети Binance Smart Chain

1. metasleuth.io — отобразит граф транзакций
2. scopescan.ai — построит граф транзакций, посчитает риск AML и прочее
3. @cryptoaml_bot — узнает источники поступления средств на крипто кошелёк и дает оценку риска, 1 бесплатный поиск на аккаунт """)
            skip()
        elif vibno == "2":
            print("""

Поиск по данным аккаунта Webmoney

1. passport.webmoney.ru (https://passport.webmoney.ru/asp/VerifyWMID.asp) — поиск по WM идентификатору или кошельку, покажет инфо о кошельке webmoney


Через URL

1. https://arbitrage.webmoney.ru/asp/claims.asp?wmid=1234567890 — претензии, отзывы, иски аккаунта, замените 1234567890 на WMID кошелька
2. https://passport.webmoney.ru/asp/CertviewSu.asp?wmid=1234567890 — покажет статус обслуживания, замените 1234567890 на WMID кошелька

Поиск по данным аккаунта Venmo

1. Venmo-OSINT (https://github.com/sc1341/Venmo-OSINT) (t) — найдет транзакции пользователя

""")
            
            skip()
        elif vibno == "3":
            print("""

Поиск по номеру на пластиковой карте любого банка

1. binlist.net — определит к какому банку принадлежит карта
2. bindb.com (https://www.bindb.com/bin-database) — определит к какому банку принадлежит карта
3. @XXLeakCheckBot — может найти фио, номер телефона
4. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет название банка карты и страну

Поиск по номеру банковской карты Альфа-Банка

1. auth.alfabank.ru (https://private.auth.alfabank.ru/passport/cerberus-mini-blue/dashboard-blue/card_account?response_type=code&client_id=newclick-web&scope=openid%20newclick-web&acr_values=card_account%3Asms&non_authorized_user=true) — покажет последние 4 цифры номера телефона владельца карты, отправляет уведомление на телефон владельца карты

Поиск по номеру банковской карты банка ВТБ

1. online.vtb.ru (https://online.vtb.ru/restore-password) — покажет часть номера телефона владельца карты, отправляет уведомление на телефон владельца карты

Часть телефона по номеру банковской карты любого банка

[1] Определите к какому банку относится карта, например с помощью ресурсов в каталоге HowToFind
[2] Найдите сайт или приложение этого банка
[3] Попробуйте найти функцию восстановления доступа к личному кабинету в банке через номер карты.

В большинстве банков будет отправлено уведомление на телефон который привязан к карте; но вы получите последние цифры этого номера телефона

Номер телефона по номеру пластиковой карты любого банка

Не работает с картой Qiwi, Sberbank, Alpha, Россельхозбанк, ЮMoney

[1] Открой card2card.kz (https://www.card2card.kz/)
[2] Где "Отправитель" введи карту номер телефона которой хочешь узнать. А CVC и срок действия укажи любой
[3] Где  "Получатель" укажи всякую карту, например 4893 4704 7283 6532
[4] Введи различную сумму и нажми перевести

Откроется сайт 3DS где указывается часть номера телефона и в редких случаях логин или email.

ФИО по номеру пластиковой карты любого банка

[1] Определи банк карты. Найди приложение этого банка или сайт. На нем отправь деньги на эту карту.



""")
            skip()
        else:
            print('Попробуйте еще раз')
            skip()
    
    elif data == "13":
        print("""

Поиск по паролю

1. @sgk2023_03_30bot — найдет аккаунты QQ и email адреса. поиск в китайской базе утечек
2. leakpeek.com   — найдет часть имени пользователя и email, название утечки, открывать через VPN
3. 🪦@ГлазБога (http://t.me/yfzxzxqwqbot)  — найдет часть номера телефона и email, поиск работает по команде /pas
4. haveibeenpwned.com (https://haveibeenpwned.com/Passwords) — даст знать утекал ли пароль
5. leak-lookup.com (https://leak-lookup.com/search)  — покажет на каких сайтах была утечка с искомым паролем
6. checkleaked.cc (https://checkleaked.cc/dehashed/check)  — найдет в утечках связанные с паролем почты, никнеймы, IP адреса, имена и т.п.
7. @vimebasebot — ищет в утечке игрового сервиса VimeWorld, находит ник игрока, пароль, почту и прочее
8. irbis.espysys.com  — находит почту, профиль ВК и прочее
9. 🎖@UniversalSearch (http://t.me/UniversalSearchOpenBot) — найдет адрес почты, имя, еще ищет в других ботах

""")
        skip()
    elif data == "14":
        print("""

Для текста

1. istio.com (https://istio.com/rus/text/analyz/) — семантический анализ текста, выявит ошибки, частотность слов и количество символов
2. miratext.ru (https://miratext.ru/seo_analiz_text) — семантический анализ текста, количество повторений словосочетаний и слов
3. voyant-tools.org — анализирует текст, показывает частые взаимосвязи слов, повторения фраз и много другого, можно загружать огромные тексты
4. JGAAP (https://github.com/evllabs/JGAAP)  — анализа текста, категоризации текста и атрибуции авторства, стилометрия и текстометрия
5. antiplagiat.ru (https://users.antiplagiat.ru/cabinet)  — найдет где еще был опубликован текст, дает ссылки, проверка 6 минут
6. text.ru (https://text.ru/antiplagiat) — найдет где еще был опубликован текст, дает ссылки, проверка идет 3 минуты


Инструменты

1. copyscape.com (https://www.copyscape.com/compare.php) — сравнит 2 текста и покажет разницу
2. diffchecker.com — сравнит 2 текста и покажет разницу


""")
        skip()
    elif data == "15":
        print("""

Поиск по номеру трекера от любой площадки

1. shodan.io — найдет IP адреса и сайты с упоминанием кода трекера
2. analyzeid.com — принимает трекеры pub, UA, ищет другие сайты


Поиск через URL

1. https://www.shodan.io/search?query=http.html%3AUA-12345678-1 — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера


Поиск через URL

1. http://top.mail.ru/visits?id=12345678 — покажет посещаемость сайта, аналитику аудитории, содержимое сайта, можно выявить админа как первого посетителя. Замените 12345678 на ID трекера, аналитика может быть закрыта паролем

Поиск через URL

1. https://metrika.yandex.ru/dashboard?id=12345678 — покажет возраст, директории сайта, примерное место нахождения пользователей, можно выявить админа как первого посетителя. Требуется вход в свой аккаунт. Замените 12345678 на ID Яндекс Метрики, аналитика может быть закрыта

Поиск по номеру трекера от Google

Трекеры с UA – Google Analytics
Трекеры с pub – Google AdSense

1. spyonweb.com — найдет сайты с искомым трекером UA. pub
2. intelx.io (https://intelx.io/tools?tab=analytics) — найдет сайты с искомым трекером UA, 6 источников поиска
3. osint.sh (https://osint.sh/analytics/) — найдет сайты с искомым трекером UA
4. osint.sh (https://osint.sh/adsense/) — найдет сайты с искомым трекером pub

Поиск через URL

1. https://host.io/api/domains/googleanalytics/UA-2345678?limit=5&token=TOKEN (r) — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера, замените TOKEN на API токен который вы получите после регистрации


""")
        skip()
    elif data == "16":
        print("""

Поиск по SSID / ESSID / Имя точки доступа

1. wigle.net (http://wigle.net/search) (r) — находит Wi-Fi точку, ее физический адрес и BSSID

Поиск по MAC адресу

1. alexell.ru (https://alexell.ru/network/mac-geo/) — тоже покажет местоположение
2. wigle.net (http://wigle.net/search)  — находит Wi-Fi точку, ее физический адрес и название


Поиск через URL

1. https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:CC:00:CC:00:CC — найдет координаты точки на карте, замените 00:CC:00:CC:00:CC на MAC-адрес

""")
        skip()
    elif data == "17":
        print("""

Поиск по серийному номеру техники

1. warrantycheck.epson.eu — техника бренда Epson, даст номер модели, номер материала
2. dysonseriallookup.com (http://dysonseriallookup.com/BedBathBeyond) — техника бренда Dyson, даст дату поставки и продавца
3. wwwp.medtronic.com (http://wwwp.medtronic.com/productperformance/serialLookup.html?serialNumber) — техника бренда Medtronic, выдает модель и тип медицинского оборудования
4. www.bobswatches.com (https://www.bobswatches.com/rolex-serial-numbers) — по серийному номеру часов Rolex выдает год производства
5. pcsupport.lenovo.com (https://pcsupport.lenovo.com/us/en/warrantylookup#/) — техника бренда Lenovo, выдает модель, а если залогиниться то и информацию о гарантии
6. www.imei.info (https://www.imei.info/apple-sn-check/) — техника бренда Apple, выдет модель, цвет, объем накопителя, время изготовления, место производства
7. www.vega.com (https://www.vega.com/en/products/serialnumber-search) — техника бренда Vega, различные датчики и системы контроля систем водоснабжения, отопления и прочего связанного с ЖКХ, даст подробную информацию о модели, дате поставки и дате тестирования

""")
        skip()
    elif data == "18":
        print("""

Поиск по IMEI

1. checkmi.info — показывает страну регистрации Mi-аккаунта, часть номера телефона для восстановления и часть email-адреса
2. imei.info — характеристики устройства
3. imeipro.info — определит iPhone, его модель, статус активации, технической поддержки, гарантии, статус iCloud, право на участие в программе AppleCare и покрытие
4. sndeep.info — покажет бренд, модель, дату изготовления телефона, серийный номер, статус украденного

""")
        skip()
    else:
        print('Попробуйте еще раз')
        skip()

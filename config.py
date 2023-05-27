import os
from aiogram.utils.markdown import bold, italic, underline, link
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

welcome = ['👋', '🖐', '✋']

forbidden_countries = ['россия','рашка','русский','раша','российская федерация','крым',
                       'афганистан','ангола','канада','центрально-африканская республика',
                        'конго','куба','берег слоновой кости','гвинея-бисау','иран','сирия','венесуэла','йемен','зимбабве','крым','днр','лнр','донецкая народная республика','луганская народная республика','сомалиленд','северная корея','ливан','либерия','ливия','мали','мьянма','никарагуа','сомали','южный судан','судан',

                       'crimea','crimea region of','afghanistan','angola','canada','central african republic','congo','congo(dem.rep.)','cuba','ivory coast','guinea-bissau','iran','syria','syrian arab republic','venezuela','yemen','zimbabwe','DNR','LNR',"donetsk people's republic","luhansk people's republic","somaliland",'north korea','korea (north)','lebanon','liberia','lybia','mali','myanmar','necaragua','somalia','south sudan','sudan']

countries = ['австралия', 'австрия', 'азербайджан', 'албания', 'алжир', 'андорра', 'аргентина',     'армения','бангладеш', 'барбадос', 'бахрейн', 'белоруссия', 'бельгия', 'болгария', 'боливия',
             'босния', 'ботсвана', 'бразилия', 'бруней', 'бутан', 'венгрия', 'венесуэла', 'вьетнам', 'габон', 'гаити',
             'гайана', 'гамбия', 'гватемала', 'гвинея', 'германия', 'гондурас', 'гренада', 'греция', 'грузия', 'дания',
             'египет', 'замбия', 'зимбабве', 'израиль', 'индия', 'индонезия', 'иордания', 'ирак', 'иран', 'ирландия',
             'исландия', 'испания', 'италия', 'йемен', 'кабо-верде', 'казахстан', 'камбоджа', 'камерун', 'канада',
             'катар', 'кения', 'кипр', 'китай', 'колумбия', 'корея', 'куба', 'кувейт', 'кыргызстан', 'латвия',
             'либерия', 'ливан', 'ливия', 'литва', 'лихтенштейн', 'люксембург', 'маврикий', 'мавритания', 'мадагаскар',
             'малайзия', 'мали', 'мальдивы', 'мальта', 'марокко', 'маршалловы', 'мексика', 'мозамбик', 'молдавия',
             'монако', 'монголия', 'мьянма', 'намибия', 'науру', 'непал', 'нигер', 'нигерия', 'нидерланды', 'новая',
             'норвегия', 'сша', 'америка', 'соединенные штаты америки', 'пакистан', 'парагвай', 'перу', 'польша',
             'португалия', 'россия', 'румыния', 'северная корея', 'сербия', 'сингапур', 'сирия', 'словакия', 'словения',
             'судан', 'суринам', 'таджикистан', 'тайланд', 'тунис', 'туркменистан', 'турция', 'уганда', 'узбекистан',
             'украина', 'уругвай', 'филиппины', 'финляндия', 'франция', 'хорватия', 'черногория', 'чехия', 'чили',
             'швейцария', 'швеция', 'эквадор', 'эстония', 'эфиопия', 'ямайка', 'япония',

             'australia', 'austria', 'azerbaijan', 'albania', 'algeria', 'angola', 'andorra', 'argentina', 'armenia',
             'bangladesh', 'barbados', 'bahrain', 'belarus', 'belgium', 'bulgaria', 'bolivia',
             'bosnia', 'botswana', 'brazil', 'brunei', 'bhutan', 'hungary', 'venezuela', 'vietnam', 'gabon', 'haiti',
             'guyana', 'gambia', 'guatemala', 'guinea', 'germany', 'honduras', 'grenada', 'greece', 'georgia', 'denmark',
             'egypt', 'zambia', 'zimbabwe', 'israel', 'india', 'indonesia', 'jordan', 'iraq', 'iran', 'irland',
             'iceland', 'spain', 'italy', 'yemen', 'cape verde', 'kazakhstan', 'cambodia', 'cameroon',
             'qatar', 'kenya', 'cyprus', 'china', 'colombia', 'korea', 'cuba', 'kuwait', 'kyrgyzstan', 'latvia',
             'liberia', 'lebanon', 'livia', 'lithuania', 'lichtenstein', 'luxembourg', 'mauritania', 'madagascar',
             'malaysia', 'mali', 'maldives', 'malta', 'morocco', 'marshallow', 'mexico', 'mozambique', 'moldavia',
             'monaco', 'mongolia', 'myanmar', 'nambia', 'nauru', 'nepal', 'niger', 'nigeria', 'netherlands', 'new',
             'norway', 'usa', 'america', 'united states of america','usa', 'pakistan', 'paraguay', 'peru', 'poland',
             'portugal', 'russia', 'romania', 'north korea', 'serbia', 'singapore', 'syria', 'slovakia', 'slovenia',
             'sudan', 'suriname', 'tajikistan', 'thailand', 'tunisia', 'turkmenistan', 'turkey', 'uganda', 'uzbekistan',
             'ukraine', 'uruguay', 'philippines', 'finland', 'france', 'croatia', 'montenegro', 'czech republic', 'chile',
             'switzerland', 'sweden', 'ecuador', 'estonia', 'ethiopia', 'jamaica', 'japan']

forbidden_regions = ['крым','днр','лнр', 'республика крым', 'донецкая народная республика','луганская народная республика',
                     'crimea','dnr','lnr', 'crimea region of ukraine','republic of crimea']

bad_reaction = ['😔', '😟', '☹', '🥺', '😞']
incorrect_reaction = ['🙃', '🙂', '🤔', '🙂']
lying_reaction = ['🤭', '🤨', '😕']


FAQ_info = bold('🔹 Для чего создан этот бот?') + '\n\n' + 'Бот создан для заработка на акциях различных сервисов, в частности ' + link(title='coinlist', url='https://coinlist.co') + '\n\n\n' + \
           bold('🔹 Как всё это работает?') + '\n\n' + 'Всё очень просто\!' + '\n\n' + \
           'Мы регистрируем аккаунты на Вас в различных сервисах по нашей реферальной ссылке' + '\n\n' + bold('Регистрируем только 18+') + '\n\n' + \
           'За верификацию аккаунта нам начисляют бонус, который мы с Вами делим 😉' + \
           '\n\n\n' + bold('🔹 Как заработать?') + '\n\n' + 'Ещё проще\!' + '\n\n' + 'После того как Вы начинаете работу с ботом и жмете на ' + bold('регистрация') + \
           ', бот последовательно предложит Вам ввести необходимые данные '+bold('(нужно вводить на английском языке и латиницей):') + '\n' + bold('➖ Страну') + '\n' + bold('➖ Регион') + '\n' + bold('➖ Город') + '\n' + bold('➖ Имя') + '\n' + bold('➖ Отчество') + '\n' + bold('➖ Фамилия') + '\n'+ bold('➖ Адрес') + ' \(как в паспорте\): город, улица, дом \(' + bold('квартира не нужна') + \
           '\)' + '\n' + bold('➖ Индекс') + ' \(можно узнать в интернете по своему адресу\)' +'\n' + bold('➖ Дата Рождения') + '\n' + bold('➖ Номер Паспорта/Вод. Лицензии') + '\n' + bold('➖ Телефон') + \
           ' \(он нужен для регистрации\)' + '\n\n\n' + bold('🔹 Что дальше?') + '\n\n' + 'А дальше вам остается ждать когда на Ваши данные создадут аккаунт ⏰' + \
           '\n' + 'В среднем процесс занимает ' + underline('30-40 минут') + '\. Через ±30 минут после начала работы с аккаунтом мы спросим Вас, готовы ли Вы пройти верификацию' + '\n\n' + \
           bold('Очень важно успеть пройти верификацию за 5-10 минут') + ', т\.к\. это заметно повышает шанс на успех с первой же попытки' + '\n\n' + \
           'После того как бот получит Ваши данные, через выше озвученное время с Вами свяжется менеджер, который удостоверится в факте создания аккаунта, а также предоставит Вам ссылку для верификации' + \
           '\n\n' + 'На данном этапе Вам необходимо:' + '\n' + bold('➖ Перейти по ссылке') + '\n' + bold('➖ Сфотографировать паспорт') + ' так, чтобы в кадре были ' + bold('все 4 угла документа') + \
           '\. Перед этапом настоятельно рекомендуем ' + underline('протереть камеру') + ', так чёткость фотографий будет выше' + '\n' + bold('➖ Сфотографировать свое лицо') + \
           '\. Так же не забудьте ' + underline('протереть') + ' фронтальную камеру' + '\n\n' + bold('❗Не переживайте, НИ ОДИН человек не увидит Ваши фотографии') + '\n\n' +\
           'Верификация происходит на облачном сайте, где ' + bold('сканер (машина)') + ' сравнивает введённые ранее данные с данными в документе, а также лицо с фотографией в документе' + '\n\n' + \
           'После ' + underline('успешной') + ' верификации личности Вы получаете ' + bold('10') + ' $ 💸' + 'Переводим Ваши ' + bold('честно заработанные') + ' на:' + '\n' + bold('➖ Любые карты')+ '\n' + bold('➖ Баланс телефона') + '\n' + bold('➖ Любые кошельки') + '\n' + \
           bold('➖ Криптовалюта') + '\n\n\n' + bold('🔹 Как заработать больше одного раза?') + '\n\n' + \
           'Вы можете предложить своим ' + bold('друзьям') + ' \| ' + bold('родственникам') + ' \| ' + bold('знакомым') + ' \| ' + bold('коллегам') + ' \| ' + bold('одногруппникам') + \
           ' \.\.\. пройти регистрацию в нашем боте, а полученные деньги 💵поделить между собой по вашему усмотрению' + '\n\n' + \
           bold('❗️ Не стоит вводить чужие данные со своего аккаунта телеграмма') + \
           ' \(если Вы уже ' + underline('ранее регистрировали') + ' свои\), т\.к\. бот с большой долей вероятности запретит Вам пройти регистрацию, оценив её как ' + underline('повторную') + \
           '\n\n\n' + bold('🔹 А это законно?') + '\n\n' + 'Все ' + bold('законно') + ' и ' + bold('честно') + ', Вы ' + bold('ничем не рискуете') + ', так как ' + bold('ничего не нарушаете') + \
           '\. Ваши данные просто используется для регистрации аккаунтов' + '\n\n' + bold('❗Больше нигде и ни при каких обстоятельствах') + '\n\n\n' + \
           bold('🔹 А это не обман?') + '\n\n' + 'Мы занимаемся этим уже ' + bold('3 года') + ' и сейчас расширяемся\!' + \
           '\n\n' + 'Мы дорожим своей репутацией и чистотой имени, поэтому всегда стараемся разрешить любую конфликтную ситуацию' + '\n\n' + \
           bold('За один только 2022 мы сделали больше 3000! аккаунтов и каждый человек получил свои деньги') + '\n\n\n' + bold('✅ Теперь переходите к регистрации и начните зарабатывать с нами!') + \
           '\n\n'
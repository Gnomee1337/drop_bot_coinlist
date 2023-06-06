localization = {
    'en':{
        "Привет!" : "Hello! ",
        " привет, прочитай информацию!" : " hello, read Information!",
        "!\nМеню менеджера!" : "!\nManager menu!",
        "Менеджер Меню" : "Manager Menu" ,
        "\nВаша статистика" : "\nYour stats" ,
        "\nРеферальная ссылка: " : "\nReferral link: ",
        "\nНовых участников: " : "\nNewbie members: ",
        "\nПрошедших регистрацию: " : "\nFinished registration: ",
        "Вы уже давали свои данные!" : "You've already given your details!",
        "Введите свою страну на английском языке.\n(Пример: Ukraine)" : "Please enter your country in English.\n(Example: Ukraine)",
        "Введите название вашей области на английском языке.\n(Пример: Kyivska Oblast)" : "Please enter the name of your region in English.\n(Example: Kyivska Oblast)",
        "Извините, но я не знаю такую страну, попробуйте написать иначе " : "Sorry, but I don't know such a country, try writing it differently ",
        "Извините, но регистрация недоступна для граждан вашей страны" : "Sorry, registration is not available for citizens of your country",
        "Введите название города на английском языке.\n(Пример: Kyiv)":"Enter the name of the city in English.\n(Example: Kyiv)",
        "Пожалуйста, укажите данные на английском языке и латинскими буквами " : "Please enter the data in English and in Latin letters ",
        "Введите ваше Имя на английском языке, как указано в вашем документе.\n(Пример: Oleksandr)":"Enter your Name in English as it appears in your document.\n(Example: Oleksandr)",
        "Ваше Имя содержит некорректные символы, попробуйте еще раз ":"Your First Name contains invalid characters, try again ",
        "Введите ваше Отчество на английском языке, как указано в вашем документе.\n(Пример: Oleksandrovych)":"Enter your Middle Name in English as it appears in your document.\n(Example: Oleksandrovych)",
        "Ваше Отчество содержит некорректные символы, попробуйте еще раз ":"Your Middle Name contains invalid characters, try again ",
        "Введите вашу Фамилию на английском языке, как указано в вашем документе.\n(Пример: Boiko)" : "Enter your Surname in English as it appears in your document.\n(Example: Boiko)",
        "Ваша Фамилия содержит некорректные символы, попробуйте еще раз ":"Your Surname contains invalid characters, try again ",
        "Введите ваш Адрес проживания, на английском языке, как указано в вашем документе.\n(Пример: St Khreshchatyk 10)":"Enter your Address of Residence, in English, as indicated in your document.\n(Example: St Khreshchatyk 10)",
        "Укажите ваш Почтовый Индекс (Postcode).\nЕсли вы не знаете ваш почтовый индекс, то найдите его в интернете.\n(Пример: 03148)":"Enter your Postcode.\nIf you don't know your Postcode, look it up online.\n(Example: 03148)",
        "Укажите свою Дату Рождения в формате День-Месяц-Год\n(Пример: 05-04-1980)" : "Enter your Date of Birth in Day-Month-Year format\n(Example: 05-04-1980)",
        "Выберите тип вашего документа.\nНажмите на тип документа снизу:" : "Select your document type.\nClick on the document type below:",
        "Укажите номер вашего документа, как указано в вашем документе" : "Provide your document number, as indicated in your document",
        "Укажите номер вашего документа, как указано в вашем документе.\n(Пример: На изображении загранпаспорта Номер Документа выделен зеленым цветом)" : "Indicate your document number as it appears on your document.\n(Example: on passport image, Passport Number is highlighted in green)",
        "Укажите полный номер вашего Мобильного Телефона (с кодом страны).\n(Пример: +380637775511 или +48225559999)" : "Please specify your cell Phone Number (with country code).\n(Example: +380637775511 or +48225559999)",
        "Извините, но вы уже указывали данный номер телефона " : "Sorry, but you have already sumbitted this phone number",
        "Некорректный номер телефона, возможно вы ошиблись " : "Incorrect phone number, you may be mistaken",
        "Пожалуйста укажите + в начале номера " : "Please enter + at the beginning of the number ",
        "Вы уверены, что указали данные верно?\nПроверьте пожалуйста!\n" : "Are you sure that you entered the data correctly?\nPlease check data again!\n",
        "Поздравляю, информация сохранена!":"Congratulations, the information is saved!",
        "Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰":"A manager will contact you soon for verification and payment 💰",

        #Drop manager
        " заполнил свои данные и ждет прохождения верификации!" : " has filled in his details and is waiting to be verified!",
        " перешел по вашей реферальной ссылке в бота!":"followed your referral link to the bot!",

        ## Documents keyboard
        "Загран Паспорт" : "Passport",
        "Водительское Удостоверение" : "Driver's license",
        "ID-Карта" : "Identity card",

        ## Keyboards
        "Информация" : "FAQ",
        "Про процесс" : "About",
        "Регистрация" : "Registration",
        "Моя статистика" : "My stats"
    }
}

def set_localization(text, language = 'ru'):
    if language == 'ru':
        return text
    else:
        global localization
        try:
            return localization[language][text]
        except:
            return text
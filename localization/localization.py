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
        "Введите, пожалуйста, свою страну" : "Please, enter your country",
        "Введите название вашей области" : "Enter the name of your region",
        "Извините, но я не знаю такую страну, попробуйте написать иначе " : "Sorry, but I don't know such a country, try writing it differently ",
        "Извините, но регистрация недоступна для граждан вашей страны" : "Sorry, registration is not available for citizens of your country",
        "Введите название города":"Enter the name of a city",
        "Пожалуйста, укажите данные на английском языке и латинскими буквами " : "Please enter the data in English and in Latin letters ",
        "Введите ваше Имя":"Enter your First Name",
        "Ваше Имя содержит некорректные символы, попробуйте еще раз ":"Your First Name contains invalid characters, try again ",
        "Введите ваше Отчество":"Enter your Middle Name",
        "Ваше Отчество содержит некорректные символы, попробуйте еще раз ":"Your Middle Name contains invalid characters, try again ",
        "Введите вашу Фамилию" : "Enter your Surname",
        "Ваша Фамилия содержит некорректные символы, попробуйте еще раз ":"Your Surname contains invalid characters, try again ",
        "Введите ваш Адрес проживания":"Enter your Address of residence",
        "Укажите ваш Почтовый Индекс (Postcode)":"Enter your Postcode",
        "Укажите свою Дату Рождения в формате День-Месяц-Год (05-04-1980)" : "Enter your Date of Birth in Day-Month-Year format (05-04-1980)",
        "Выберите тип вашего документа" : "Choose your document type",
        "Укажите номер вашего документа" : "Provide your document number",
        "Укажите номер вашего Мобильного Телефона" : "Enter your Cell Phone Number",
        "Извините, но вы уже указывали данный номер телефона " : "Sorry, but you have already sumbitted this phone number",
        "Некорректный номер телефона, возможно вы ошиблись " : "Incorrect phone number, you may be mistaken",
        "Пожалуйста укажите + в начале номера " : "Please enter + at the beginning of the number ",
        "Вы уверены, что указали данные верно?" : "Are you sure that you entered the data correctly?",
        "Поздравляю, информация сохранена!":"Congratulations, the information is saved!",
        "Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰":"A manager will contact you soon for verification and payment 💰",

        #Drop manager
        " заполнил свои данные и ждет прохождения верификации!" : " has filled in his details and is waiting to be verified!",
        " перешел по вашей реферальной ссылке в бота!":"followed your referral link to the bot!",

        ## Documents keyboard
        "Паспорт" : "Passport",
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
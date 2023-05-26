localization = {
    'ru':{
        "FAQ" : "инфо",
        "About" : "про",
        "Registration" : "регистрация"
    }
}

def set_localization(text, language = 'en'):
    if language == 'en':
        return text
    else:
        global localization
        try:
            return localization[language][text]
        except:
            return text
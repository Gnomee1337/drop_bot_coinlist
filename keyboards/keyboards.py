from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from localization.localization import set_localization

#Language
langRU = InlineKeyboardButton(text='🇷🇺 Русский', callback_data='lang_ru')
langEN = InlineKeyboardButton(text='🇺🇸 English', callback_data='lang_en')
#LanguageMenu
langMenu = InlineKeyboardMarkup(resize_keyboard = True)
langMenu.add(langRU, langEN)

def mainMenu(lang='ru'):
    mainMenu = InlineKeyboardMarkup(resize_keyboard = True)
    
    btnFAQ = InlineKeyboardButton(set_localization("Информация", lang),callback_data='FAQ')
    #btnAbout = InlineKeyboardButton(set_localization("About", lang),callback_data='coinlistinfo')
    btnRegistration = InlineKeyboardButton(set_localization("Регистрация", lang), callback_data='reg')
    
    mainMenu.add(btnFAQ, btnRegistration)

    return mainMenu

def documentMenu(lang='ru'):
    documentMenu = InlineKeyboardMarkup(resize_keyboard = True, row_width=1)

    btnPassport = InlineKeyboardButton(set_localization("Паспорт", lang),callback_data='passportid')
    btnDriver = InlineKeyboardButton(set_localization("Водительское Удостоверение", lang),callback_data='driverid')
    btnIdentif = InlineKeyboardButton(set_localization("ID-Карта", lang),callback_data='identifnumberid')
    
    documentMenu.add(btnPassport, btnDriver, btnIdentif)
    return documentMenu

def managerMenu(lang='ru'):
    managerMenu = InlineKeyboardMarkup(resize_keyboard = True)

    btnShowStats = InlineKeyboardButton(set_localization("Моя статистика", lang),callback_data='managerstats')

    managerMenu.add(btnShowStats)

    return managerMenu

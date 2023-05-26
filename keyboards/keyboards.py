from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from localization.localization import set_localization

#Language
langRU = InlineKeyboardButton(text='🇷🇺 Русский', callback_data='lang_ru')
langEN = InlineKeyboardButton(text='🇺🇸 English', callback_data='lang_en')
#LanguageMenu
langMenu = InlineKeyboardMarkup(resize_keyboard = True)
langMenu.add(langRU, langEN)

def mainMenu(lang='en'):
    mainMenu = InlineKeyboardMarkup(resize_keyboard = True)
    
    btnFAQ = InlineKeyboardButton(set_localization("FAQ", lang),callback_data='FAQ')
    #btnAbout = InlineKeyboardButton(set_localization("About", lang),callback_data='coinlistinfo')
    btnRegistration = InlineKeyboardButton(set_localization("Registration", lang), callback_data='reg')
    
    mainMenu.add(btnFAQ, btnRegistration)

    return mainMenu

def managerMenu(lang='en'):
    managerMenu = InlineKeyboardMarkup(resize_keyboard = True)

    btnShowStats = InlineKeyboardButton(set_localization("My stats", lang),callback_data='managerstats')

    managerMenu.add(btnShowStats)

    return managerMenu

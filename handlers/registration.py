## Based on https://github.com/SoDeepASMR/CoinListBot

import random, string
from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.deep_linking import get_start_link, decode_payload
from aiogram import types, Dispatcher
import logging
import config
#from config import ADMINS
from localization.localization import set_localization
from keyboards import keyboards as nav
from database.database import Database
from bot_init import dp, bot, db

def isEnglish(s):
  return s.isascii()

class RegStates(StatesGroup):
    #general = State()
    country = State()
    region = State()
    city = State()
    firstname = State()
    middlename = State()
    surname = State()
    #fullname = State()
    address = State()
    postcode = State()
    date_of_birth = State()
    document_id = State()
    phonenumber = State()

# @dp.message_handler(commands='start')
async def cm_start(message: types.Message, state: FSMContext):
    await message.answer(random.choice(config.welcome))
    ## If user exists
    if(db.user_exists(message.from_user.id)):
        ## Send user to main menu
        user_language = db.get_user_language(message.from_user.id)
        await state.set_state(None)
        await message.answer(set_localization('Привет ',user_language), parse_mode="html", reply_markup=nav.mainMenu(user_language))
        ## If user manager
        if(db.is_user_manager(message.from_user.id)):
            await state.set_state(None)
            await message.answer(set_localization('Привет ',user_language)+message.from_user.username +"!\nМеню менеджера!", parse_mode="html", reply_markup=nav.managerMenu(user_language))
    else:
    ## If user not exists
        ## Get referral id
        args = message.get_args()
        reference = decode_payload(args)
        ## Init user to DB
        db.add_user_empty(message.from_user.id, message.from_user.username, reference ,"new")
        ## Notify drop manager
        drop_manager_id = db.get_user_referral(message.from_user.id)
        if(drop_manager_id != ""):
            manager_language = db.get_user_language(drop_manager_id)
            await bot.send_message(drop_manager_id, "@" + message.from_user.username + set_localization(" перешел по вашей реферальной ссылке в бота!",manager_language))
        ## Send user to language panel
        await message.answer('Привет. Выберите язык использования!\nHello. Choose your language!', parse_mode="html", reply_markup=nav.langMenu)

## Create ref link
async def get_ref(user_id):
    ## result: 'https://t.me/MyBot?start='
    ## After the = sign will be encoded nickname of the user who created the ref link, instead of it you can insert his id
    link = await get_start_link(str(user_id), encode=True)
    logging.debug(link)
    return str(link)

#@dp.message_handler(state = '*', commands=['cancel'])
#@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    #Allow user to cancel any action
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    #await message.reply('Отмена.\nCancelled.', reply_markup=types.ReplyKeyboardRemove())
    await message.reply('Отмена.\nCancelled.', reply_markup=nav.mainMenu())

async def clear_chat(start_id: int, chat_id: int) -> None:
    return 0
    # for _ in range(start_id, start_id - 20, -1):
    #     try:
    #         await bot.delete_message(chat_id, _)
    #     except Exception:
    #         pass

@dp.callback_query_handler(text_contains = "lang_", state=None)
async def setLanguage(callback: types.CallbackQuery, state: FSMContext):
    logging.debug("###DEBUG### setLanguage started")
    lang = callback.data[5:]
    db.change_user_language(callback.from_user.id, lang)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, callback.from_user.username + nav.set_localization("Hello ", lang), reply_markup=nav.mainMenu(lang))
    logging.debug("###DEBUG### setLanguage finished")

@dp.callback_query_handler(text_contains = "managerstats", state=None)
async def managerStats(callback: types.CallbackQuery, state: FSMContext):
    logging.debug("###DEBUG### managerstats started")
    user_language = db.get_user_language(callback.from_user.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 
                           nav.set_localization("Привет ", str(user_language)) + str(callback.from_user.username) 
                            +set_localization("\nВаша статистика",user_language)
                            +set_localization("\nРеферальная ссылка: ",user_language)+ await get_ref(callback.from_user.id)
                            +set_localization("\nНовых участников: ",user_language)+str(db.get_manager_invites(callback.from_user.id, user_status="new"))
                            +set_localization("\nПрошедших регистрацию: ",user_language)+str(db.get_manager_invites(callback.from_user.id, user_status="filled")),
                           reply_markup=nav.mainMenu(user_language),parse_mode="html")
    ## If user manager
    if(db.is_user_manager(callback.from_user.id)):
        await state.set_state(None)
        await bot.send_message(callback.from_user.id,set_localization("Manager Menu",user_language), parse_mode="html", reply_markup=nav.managerMenu(user_language))
    await clear_chat(callback.message.message_id, callback.message.chat.id)
    logging.debug("###DEBUG### managerstats finished")

@dp.callback_query_handler()
#@dp.callback_query_handler(lambda x: x.data and x.data.startswith("reg "))
async def main_menu(call: types.CallbackQuery, state: FSMContext):
    logging.debug(await state.get_state())
    if call.message:
        user_language = db.get_user_language(call.from_user.id)
        if call.data == 'reg':
            if db.user_registered(call.message.chat.id):
                await call.message.answer(set_localization("Вы уже давали свои данные!",user_language)+random.choice(config.lying_reaction), reply_markup=nav.mainMenu(user_language))
                await clear_chat(call.message.message_id, call.message.chat.id)
                await state.set_state(None)
                return
            else:
                await call.message.answer(set_localization("Введите, пожалуйста, свою страну",user_language))
                await RegStates.country.set()
                await clear_chat(call.message.message_id, call.message.chat.id)
        if call.data == 'FAQ':
            await call.message.answer(config.FAQ_info, parse_mode=types.ParseMode.MARKDOWN_V2, reply_markup=nav.mainMenu(user_language))
            ## If user manager
            if(db.is_user_manager(call.from_user.id)):
                await state.set_state(None)
                await call.message.answer(set_localization('Привет ',user_language)+call.message.chat.username +"!\nМеню менеджера!", parse_mode="html", reply_markup=nav.managerMenu(user_language))
                await clear_chat(call.message.message_id, call.message.chat.id)
        # elif call.data == 'coinlistinfo':
        #     await call.message.answer('конлист', reply_markup=nav.mainMenu())
        #     await clear_chat(call.message.message_id, call.message.chat.id)

async def input_country(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    ## Check if country is allowed
    ## Country not allowed
    if message.text.lower() in config.forbidden_countries:
        await message.answer(set_localization("Извините, но регистрация недоступна для граждан вашей страны", user_language) +random.choice(config.bad_reaction), reply_markup=nav.mainMenu(user_language))
        await state.finish()
        return
    ## Country allowed
    elif message.text.lower() in config.countries:
        await state.update_data(tg_username=None)
        if message.chat.username:
            tg_username = message.chat.username
            await state.update_data(tg_username=tg_username)
            await state.update_data(tg_id=message.from_user.id)
        if (not isEnglish(message.text.lower())):
            await message.answer(set_localization(
            "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
            return
        ## Save country to state data
        await state.update_data(country=message.text.lower())
        await RegStates.region.set()
        await message.answer(set_localization("Введите название вашей области",user_language))
    ## Country not from expected list
    else:
        await message.answer(set_localization(
            "Извините, но я не знаю такую страну, попробуйте написать иначе ",user_language)+random.choice(config.bad_reaction))
        return

async def input_region(message: types.Message, state: FSMContext):
        user_language = db.get_user_language(message.from_user.id)
        if message.text.lower() in config.forbidden_regions:
            await message.answer(set_localization("Извините, но регистрация недоступна для граждан вашего региона", user_language) +random.choice(config.bad_reaction), reply_markup=nav.mainMenu(user_language))
            await state.finish()
            return
        else:
            if (not isEnglish(message.text.lower())):
                await message.answer(set_localization(
                    "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
                return
            ## Save region to state data
            await state.update_data(region=message.text.lower())
            await RegStates.city.set()
            await message.answer(set_localization('Введите название города',user_language))

async def input_city(message: types.Message, state: FSMContext):
        user_language = db.get_user_language(message.from_user.id)
        if (not isEnglish(message.text.lower())):
            await message.answer(set_localization(
            "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
            return
        ## Save city to state data
        await state.update_data(city=message.text.lower())
        await RegStates.firstname.set()
        await message.answer(set_localization('Введите ваше Имя',user_language))

# async def input_fullname(message: types.Message, state: FSMContext):
#     user_language = db.get_user_language(message.from_user.id)
#     for _ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '"', '@', '\\', '|', '/', '!', '#', '$', '%', '^',
#               '&', '*', '_', '=', '+', '?', '>', ',', '.']:
#         if _ in message.text.lower():
#             message.answer(f'Некорректное ФИО, попробуйте еще раз {random.choice(config.incorrect_reaction)}')
#             return
#     await state.update_data(full_name=message.text)
#     await RegStates.address.set()
#     await message.answer('Введите адрес проживания')

async def input_firstname(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
            "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    for _ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '"', '@', '\\', '|', '/', '!', '#', '$', '%', '^',
              '&', '*', '_', '=', '+', '?', '>', ',', '.']:
        if _ in message.text.lower():
            await message.answer(set_localization("Ваше Имя содержит некорректные символы, попробуйте еще раз ",user_language)+random.choice(config.incorrect_reaction))
            return
    await state.update_data(first_name=message.text)
    await RegStates.middlename.set()
    await message.answer(set_localization("Введите ваше Отчество",user_language))

async def input_middlename(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
            "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    for _ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '"', '@', '\\', '|', '/', '!', '#', '$', '%', '^',
              '&', '*', '_', '=', '+', '?', '>', ',', '.']:
        if _ in message.text.lower():
            await message.answer(set_localization("Ваше Отчество содержит некорректные символы, попробуйте еще раз ",user_language)+random.choice(config.incorrect_reaction))
            return
    await state.update_data(middle_name=message.text)
    await RegStates.surname.set()
    await message.answer(set_localization("Введите вашу Фамилию",user_language))

async def input_surname(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
            "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    for _ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '"', '@', '\\', '|', '/', '!', '#', '$', '%', '^',
              '&', '*', '_', '=', '+', '?', '>', ',', '.']:
        if _ in message.text.lower():
            await message.answer(set_localization("Ваша Фамилия содержит некорректные символы, попробуйте еще раз ",user_language)+random.choice(config.incorrect_reaction))
            return
    await state.update_data(surname=message.text)
    await RegStates.address.set()
    await message.answer(set_localization("Введите ваш Адрес проживания",user_language))

async def input_address(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    await state.update_data(address=str(message.text))
    await RegStates.postcode.set()
    await message.answer(set_localization("Укажите ваш Почтовый Индекс (Postcode)",user_language))

async def input_postcode(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    await state.update_data(postcode=str(message.text))
    await RegStates.date_of_birth.set()
    await message.answer(set_localization("Укажите свою Дату Рождения в формате День-Месяц-Год",user_language))
 
async def input_date_of_birth(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    await state.update_data(date_of_birth=str(message.text))
    await RegStates.document_id.set()
    await message.answer(set_localization("Укажите номер вашего Паспорта или Водительской Лицензии",user_language))

async def input_document_id(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    await state.update_data(document_id=str(message.text))
    await RegStates.phonenumber.set()
    await message.answer(set_localization("Укажите номер вашего Мобильного Телефона",user_language))

async def input_phonenumber(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if db.phone_exists(message.text):
        await message.answer(set_localization("Извините, но вы уже указывали данный номер телефона ",user_language)+random.choice(config.lying_reaction), reply_markup=nav.mainMenu(user_language))
        await state.finish()
        await clear_chat(message.message_id, message.chat.id)
        return
    if 11 >= len(str(message.text)) >= 13:
        await message.answer(set_localization("Некорректный номер телефона, возможно вы ошиблись",user_language)+ random.choice(config.incorrect_reaction))
        return
    for _ in str(message.text):
        if _ not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']:
            await message.answer(set_localization(
                "Некорректный номер телефона, возможно вы ошиблись ",user_language)+random.choice(config.incorrect_reaction))
            return
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    ## Update user data in table
    db.add_user_account(data['tg_id'],
                        data['tg_username'],
                        data['country'],
                        data['region'],
                        data['city'],
                        #data['full_name'],
                        data['first_name'],
                        data['middle_name'],
                        data['surname'],
                        data['address'],
                        data['postcode'],
                        data['date_of_birth'],
                        data['document_id'],
                        data['phone_number'])
    logging.debug("DB user data update in table!")
    ## Notify drop manager about filled user
    drop_manager_id = db.get_user_referral(data['tg_id'])
    if(drop_manager_id != ""):
        manager_language = db.get_user_language(drop_manager_id)
        await bot.send_message(drop_manager_id, "@" + data['tg_username'] + set_localization(" заполнил свои данные и ждет прохождения верификации!", manager_language))
    ## Notify top manager for new filled user
    top_managers = db.get_top_managers()
    try:
        for manager in top_managers[0]:
            manager_language = db.get_user_language(manager)
            await bot.send_message(manager, 
                                   "@" + data['tg_username'] + "<b>"+set_localization(" заполнил свои данные и ждет прохождения верификации!", manager_language) + "</b>" +
                                   "\nСтрана: " + str(data['country']) +
                                   "\nРегион: " + str(data['region']) +
                                   "\nГород: " + str(data['city']) +
                                   "\nИмя: " + str(data['first_name']) +
                                   "\nОтчество: " + str(data['middle_name']) +
                                   "\nФамилия: " + str(data['surname']) +
                                   "\nАдрес: " + str(data['address']) +
                                   "\nПочтовый индекс: " + str(data['postcode']) +
                                   "\nДата рождения: " + str(data['date_of_birth']) +
                                   "\nДокумент ID: " + str(data['document_id']) +
                                   "\nТелефон: " + str(data['phone_number'])
                                   , parse_mode="html")
    except:
        pass
    await state.finish()
    await message.answer('🎉')
    await clear_chat(message.message_id, message.chat.id)
    await message.answer(set_localization("Поздравляю, информация сохранена!",user_language))
    await message.answer(set_localization("Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰",user_language), reply_markup=nav.mainMenu(user_language))

def register_handlers_registration(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state=None)
    dp.register_message_handler(cancel_handler, state = '*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(input_country, state=RegStates.country)
    dp.register_message_handler(input_region, state=RegStates.region)
    dp.register_message_handler(input_city, state=RegStates.city)
    #dp.register_message_handler(input_fullname, state=RegStates.fullname)
    dp.register_message_handler(input_firstname, state=RegStates.firstname)
    dp.register_message_handler(input_middlename, state=RegStates.middlename)
    dp.register_message_handler(input_surname, state=RegStates.surname)
    dp.register_message_handler(input_address, state=RegStates.address)
    dp.register_message_handler(input_postcode, state=RegStates.postcode)
    dp.register_message_handler(input_date_of_birth, state=RegStates.date_of_birth)
    dp.register_message_handler(input_document_id, state=RegStates.document_id)
    dp.register_message_handler(input_phonenumber, state=RegStates.phonenumber)

## Based on https://github.com/SoDeepASMR/CoinListBot

import random, string, os
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
    document_type = State()
    document_id = State()
    phonenumber = State()
    submitdata = State()

# @dp.message_handler(commands='start')
async def cm_start(message: types.Message, state: FSMContext):
    await message.answer(random.choice(config.welcome))
    ## If user exists
    if(db.user_exists(message.from_user.id)):
        ## Send user to main menu
        user_language = db.get_user_language(message.from_user.id)
        await state.set_state(None)
        await message.answer(set_localization('Привет ',user_language) + str(message.from_user.username), parse_mode="html", reply_markup=nav.mainMenu(user_language))
        ## If user manager
        if(db.is_user_manager(message.from_user.id)):
            await state.set_state(None)
            await message.answer(set_localization('Привет ',user_language)+message.from_user.username +set_localization("!\nМеню менеджера!",user_language), parse_mode="html", reply_markup=nav.managerMenu(user_language))
    else:
    ## If user not exists
        ## Get referral id
        args = message.get_args()
        reference = decode_payload(args)
        if(reference == ""):
            reference = 0
        ## Init user to DB
        db.add_user_empty(message.from_user.id, message.from_user.username, reference ,"new")
        ## Notify drop manager
        drop_manager_id = db.get_user_referral(message.from_user.id)
        if(drop_manager_id != 0):
            manager_language = db.get_user_language(drop_manager_id)
            new_invited_users = db.get_manager_invites(drop_manager_id, "")
            db.update_manager_invites(drop_manager_id, new_invited_users)
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
    await bot.send_message(callback.from_user.id, callback.from_user.username + " " +nav.set_localization("привет, прочитай информацию!", lang), reply_markup=nav.mainMenu(lang))
    logging.debug("###DEBUG### setLanguage finished")

## Manager Menu (Manager Stats)
@dp.callback_query_handler(text_contains = "managerstats", state=None)
async def managerStats(callback: types.CallbackQuery, state: FSMContext):
    logging.debug("###DEBUG### managerstats started")
    user_language = db.get_user_language(callback.from_user.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 
                           set_localization("Привет ", user_language) + str(callback.from_user.username) 
                            +set_localization("\nРеферальная ссылка: ",user_language) + await get_ref(callback.from_user.id) + "\n"
                            +"<b>" + set_localization("\nВаша статистика",user_language) + "</b>"
                            +set_localization("\nВсего рефералов: ",user_language)+str(db.get_manager_invites(callback.from_user.id))
                            +set_localization("\nНе зарегистрированных: ",user_language)+str(db.get_manager_invites(callback.from_user.id, user_status="new"))
                            +set_localization("\nПрошедших регистрацию: ",user_language)+str(db.get_manager_invites(callback.from_user.id, user_status="registered"))
                            +set_localization("\nПодтвержденных: ",user_language)+str(db.get_manager_invites(callback.from_user.id, user_status="approved")) + "\n"
                            +set_localization("\nВыплаченных: ",user_language)+str(db.get_manager_invites(callback.from_user.id, paid_status="paid"))
                            +set_localization("\nПодтвержден, но <b>НЕ</b> выплачен: ",user_language)+str(db.get_manager_invites(callback.from_user.id, user_status="approved", paid_status="unpaid")),
                           reply_markup=nav.mainMenu(user_language),parse_mode="html")
    ## If user manager
    if(db.is_user_manager(callback.from_user.id)):
        await state.set_state(None)
        await bot.send_message(callback.from_user.id,set_localization("Менеджер Меню",user_language), parse_mode="html", reply_markup=nav.managerMenu(user_language))
    await clear_chat(callback.message.message_id, callback.message.chat.id)
    logging.debug("###DEBUG### managerstats finished")

## Manager Menu (Add User)
@dp.callback_query_handler(text_contains = "manageradduser", state=None)
async def managerAddUser(callback: types.CallbackQuery, state: FSMContext):
    logging.debug("###DEBUG### managerAddUser started")
    user_language = db.get_user_language(callback.from_user.id)
    await callback.message.answer(set_localization("Введите свою страну на английском языке.\n(Пример: Ukraine)",user_language))
    await RegStates.country.set()
    ## Registration by Manager
    await state.update_data(reg_by_manager = 1)
    await clear_chat(callback.message.message_id, callback.message.chat.id)
    logging.debug("###DEBUG### managerAddUser finished")

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
                await call.message.answer(set_localization("Введите свою страну на английском языке.\n(Пример: Ukraine)",user_language))
                await RegStates.country.set()
                ## Registration not by Manager
                await state.update_data(reg_by_manager = 0)
                await clear_chat(call.message.message_id, call.message.chat.id)
        if call.data == 'FAQ':
            if(user_language == "en"):
                await call.message.answer(config.FAQ_info_en, parse_mode=types.ParseMode.MARKDOWN_V2, reply_markup=nav.mainMenu(user_language))
            else:
                await call.message.answer(config.FAQ_info, parse_mode=types.ParseMode.MARKDOWN_V2, reply_markup=nav.mainMenu(user_language))
            ## If user manager
            if(db.is_user_manager(call.from_user.id)):
                await state.set_state(None)
                await call.message.answer(set_localization('Привет ',user_language)+call.message.chat.username +set_localization("!\nМеню менеджера!",user_language), parse_mode="html", reply_markup=nav.managerMenu(user_language))
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
        await message.answer(set_localization("Введите название вашей области на английском языке.\n(Пример: Kyivska Oblast)",user_language))
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
        await message.answer(set_localization("Введите название города на английском языке.\n(Пример: Kyiv)",user_language))

async def input_city(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
        "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    ## Save city to state data
    await state.update_data(city=message.text.lower())
    await RegStates.firstname.set()
    await message.answer(set_localization("Введите ваше Имя на английском языке, как указано в вашем документе.\n(Пример: Oleksandr)",user_language))

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
    await message.answer(set_localization("Введите ваше Отчество на английском языке, как указано в вашем документе.\n(Пример: Oleksandrovych)",user_language))

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
    await message.answer(set_localization("Введите вашу Фамилию на английском языке, как указано в вашем документе.\n(Пример: Boiko)",user_language))

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
    await message.answer(set_localization("Введите ваш Адрес проживания, на английском языке, как указано в вашем документе.\n(Пример: St Khreshchatyk 10)",user_language))

async def input_address(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
        "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    await state.update_data(address=str(message.text))
    await RegStates.postcode.set()
    await message.answer(set_localization("Укажите ваш Почтовый Индекс (Postcode).\nЕсли вы не знаете ваш почтовый индекс, то найдите его в интернете.\n(Пример: 03148)",user_language),parse_mode="html")

async def input_postcode(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
        "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    await state.update_data(postcode=str(message.text))
    await RegStates.date_of_birth.set()
    await message.answer(set_localization("Укажите свою Дату Рождения в формате День-Месяц-Год\n(Пример: 05-04-1980)",user_language))
 
async def input_date_of_birth(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
        "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    await state.update_data(date_of_birth=str(message.text))
    await RegStates.document_type.set()
    await message.answer(set_localization("Выберите тип вашего документа.\nНажмите на тип документа снизу:",user_language), reply_markup=nav.documentMenu(user_language))

@dp.callback_query_handler(state=RegStates.document_type)
async def input_document_type(call: types.CallbackQuery, state: FSMContext):
    # if (not isEnglish(callmessage.text.lower())):
    #     await message.answer(set_localization(
    #     "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
    #     return
    try:
        if(call.data == "passportid"):
            await state.update_data(document_type = "F.Passport | ")
        elif(call.data == "driverid"):
            await state.update_data(document_type = "Driver-ID | ")
        elif(call.data == "identifnumberid"):
            await state.update_data(document_type = "ID-Card | ")
        else:
            return
        if(call.message != None):
            user_language = db.get_user_language(call.message.from_user.id)
            await RegStates.document_id.set()
            try:
                fpassphotopath = os.path.join( os.path.dirname(__file__), "..", "images_for_users", "zagran-pass-example.jpg" )
                fpassphoto = open(fpassphotopath, "rb")
                await call.message.answer_photo(fpassphoto, 
                                                caption=set_localization("Укажите номер вашего документа, как указано в вашем документе.\n(Пример: На изображении загранпаспорта Номер Документа выделен зеленым цветом)", user_language),
                                                parse_mode="html")
            except:
                logging.error("Error occurred while sending fpass photo")
                await call.message.answer(set_localization("Укажите номер вашего документа, как указано в вашем документе", user_language))
                pass
            #await call.message.answer(set_localization("Укажите номер вашего документа", user_language))
    except:
        pass

async def input_document_id(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if (not isEnglish(message.text.lower())):
        await message.answer(set_localization(
        "Пожалуйста, укажите данные на английском языке и латинскими буквами ", user_language)+random.choice(config.bad_reaction))
        return
    await state.update_data(document_id = str(message.text))
    await RegStates.phonenumber.set()
    await message.answer(set_localization("Укажите полный номер вашего Мобильного Телефона (с кодом страны).\n(Пример: +380637775511 или +48225559999)",user_language))

async def input_phonenumber(message: types.Message, state: FSMContext):
    user_language = db.get_user_language(message.from_user.id)
    if db.phone_exists(message.text):
        await message.answer(set_localization("Извините, но вы уже указывали данный номер телефона ",user_language)+random.choice(config.lying_reaction), reply_markup=nav.mainMenu(user_language))
        await state.finish()
        await clear_chat(message.message_id, message.chat.id)
        return
    if 11 >= len(str(message.text)) >= 13:
        await message.answer(set_localization("Некорректный номер телефона, возможно вы ошиблись ",user_language)+ random.choice(config.incorrect_reaction))
        return
    for _ in str(message.text):
        if _ not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']:
            await message.answer(set_localization(
                "Некорректный номер телефона, возможно вы ошиблись ",user_language)+random.choice(config.incorrect_reaction))
            return
    if(str(message.text[0]) != '+'):
        await message.answer(set_localization(
                "Пожалуйста укажите + в начале номера ",user_language)+random.choice(config.incorrect_reaction))
        return
    await state.update_data(phone_number=message.text)
    await RegStates.submitdata.set()
    try:
        data = await state.get_data()
        await message.answer("<b>" + set_localization("Вы уверены, что указали данные верно?\nПроверьте пожалуйста!\n",user_language) + "</b>"
                             + "\n"
                             + set_localization("Страна: ",user_language) + str(data['country']) + "\n"
                             + set_localization("Область: ",user_language) + str(data['region']) + "\n"
                             + set_localization("Город: ",user_language) + str(data['city']) + "\n"
                             + set_localization("Имя: ",user_language) + str(data['first_name']) + "\n"
                             + set_localization("Отчество: ",user_language) + str(data['middle_name']) + "\n"
                             + set_localization("Фамилия: ",user_language) + str(data['surname']) + "\n"
                             + set_localization("Адрес: ",user_language) + str(data['address']) + "\n"
                             + set_localization("Почтовый Индекс: ",user_language) + str(data['postcode']) + "\n"
                             + set_localization("Дата Рождения: ",user_language) + str(data['date_of_birth']) + "\n"
                             + set_localization("Номер документа: ",user_language) + str(data['document_id']) + "\n"
                             + set_localization("Номер телефона: ",user_language) + str(data['phone_number']),
                             parse_mode="html",
                             reply_markup=nav.submitMenu(user_language))
    except:
        await message.answer(set_localization("Вы уверены, что указали данные верно?\nПроверьте пожалуйста:",user_language), parse_mode="html", reply_markup=nav.submitMenu(user_language))
        logging.error("Error occurred while showing user information BEFORE submit")
        pass


    @dp.callback_query_handler(state=RegStates.submitdata)
    async def submit_data(call: types.CallbackQuery, state: FSMContext):
        if call.message:
            try:
                user_language = db.get_user_language(call.message.from_user.id)
            except:
                logging.warning("Warning while getting user language in Submit Data stage")
                pass
            if call.data == "submitdata":
                data = await state.get_data()
                if(data['reg_by_manager'] == 1):
                    ## Add user as manager in table
                    db.add_user_by_manager(
                                            #data['tg_id'],
                                            #data['tg_username'],
                                            data['tg_id'],
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
                                            data['document_type'] + data['document_id'],
                                            data['phone_number']
                                        )
                    logging.debug("DB user ADDED in table by Manager!")
                else:
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
                                        data['document_type'] + data['document_id'],
                                        data['phone_number'])
                    logging.debug("DB user data update in table!")
                    ## Notify drop manager about filled user
                    drop_manager_id = db.get_user_referral(data['tg_id'])
                    if(drop_manager_id != 0):
                        try:
                            manager_language = db.get_user_language(drop_manager_id)
                            await bot.send_message(drop_manager_id, "@" + data['tg_username'] + set_localization(" заполнил свои данные и ждет прохождения верификации!", manager_language))
                        except:
                            pass
                ## Notify top manager for new filled user
                try:
                    top_managers = db.get_top_managers()
                    for manager_tup in top_managers:
                        manager = manager_tup[0]
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
                                               "\nДокумент ID: " + str(data['document_type']) + str(data['document_id']) +
                                               "\nТелефон: " + str(data['phone_number'])
                                               , parse_mode="html")
                except:
                    logging.error("Error occurred while sending User Info to Top-Manager")
                    pass
                await bot.send_message(data['tg_id'],'🎉')
                #await message.answer('🎉')
                #await clear_chat(message.message_id, message.chat.id)
                await bot.send_message(data['tg_id'], set_localization("Поздравляю, информация сохранена!",user_language))
                #await message.answer(set_localization("Поздравляю, информация сохранена!",user_language))
                await bot.send_message(data['tg_id'], set_localization("Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰",user_language), reply_markup=nav.mainMenu(user_language))
                #await message.answer(set_localization("Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰",user_language), reply_markup=nav.mainMenu(user_language))
                await state.finish()
            if call.data == "declinedata":
                try:
                    data = await state.get_data()
                except:
                    pass
                #Allow user to cancel any action
                current_state = await state.get_state()
                if current_state is None:
                    return
                logging.info('Cancelling state %r', current_state)
                # Cancel state and inform user about it
                await state.finish()
                # And remove keyboard (just in case)
                #await message.reply('Отмена.\nCancelled.', reply_markup=types.ReplyKeyboardRemove())
                await bot.send_message(data['tg_id'],'Отмена.\nCancelled.', reply_markup=nav.mainMenu(user_language))


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
    dp.register_message_handler(input_document_type, state=RegStates.document_type)
    dp.register_message_handler(input_document_id, state=RegStates.document_id)
    dp.register_message_handler(input_phonenumber, state=RegStates.phonenumber)

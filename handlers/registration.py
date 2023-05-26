# https://github.com/SoDeepASMR/CoinListBot

import random
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

class RegStates(StatesGroup):
    #general = State()
    country = State()
    region = State()
    city = State()
    fullname = State()
    address = State()
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
        await message.answer('Привет!', parse_mode="html", reply_markup=nav.mainMenu(user_language))
        ## If user manager
        if(db.is_user_manager(message.from_user.id)):
            await state.set_state(None)
            await message.answer('Привет '+message.from_user.username +'!\nМенеджер меню!', parse_mode="html", reply_markup=nav.managerMenu(user_language))
    else:
    ## If user not exists
        ## Get referral id
        args = message.get_args()
        reference = decode_payload(args)
        ## Init user to DB
        db.add_user_empty(message.from_user.id, message.from_user.username, reference ,"new")
        ## Send user to language panel
        await message.answer('Привет. Выберите язык использования!\nHello. Choose your language!', parse_mode="html", reply_markup=nav.langMenu)

# ## Create ref link
# @dp.message_handler(commands=["ref"])
# async def get_ref(message: types.Message):
#     link = await get_start_link(str(message.from_user.id), encode=True)
#     # result: 'https://t.me/MyBot?start='
#     ## после знака = будет закодированный никнейм юзера, который создал реф ссылку, вместо него можно вставить и его id 
#     await message.answer(f"Ваша реф. ссылка {link}")

## Create ref link
async def get_ref(user_id):
    link = await get_start_link(str(user_id), encode=True)
    # result: 'https://t.me/MyBot?start='
    ## после знака = будет закодированный никнейм юзера, который создал реф ссылку, вместо него можно вставить и его id
    print(link)
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
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())

async def clear_chat(start_id: int, chat_id: int) -> None:
    for _ in range(start_id, start_id - 20, -1):
        try:
            await bot.delete_message(chat_id, _)
        except Exception:
            pass

@dp.callback_query_handler(text_contains = "lang_", state=None)
async def setLanguage(callback: types.CallbackQuery, state: FSMContext):
    logging.debug("###DEBUG### setLanguage started")
    lang = callback.data[5:]
    db.change_user_language(callback.from_user.id, lang)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, callback.from_user.username + nav.set_localization("Привет!", lang), reply_markup=nav.mainMenu(lang))
    logging.debug("###DEBUG### setLanguage finished")

@dp.callback_query_handler(text_contains = "managerstats", state=None)
async def managerStats(callback: types.CallbackQuery, state: FSMContext):
    logging.debug("###DEBUG### managerstats started")
    user_language = db.get_user_language(callback.from_user.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 
                           nav.set_localization("Привет!", str(user_language)) + str(callback.from_user.username) 
                            +"\nВаша статистика "
                            +"\nРеферальная ссылка: "+ await get_ref(callback.from_user.id)
                            +"\nПустых участников: "+str(db.get_manager_invites(callback.from_user.id, user_status="new"))
                            +"\nЗаполненых участников: "+str(db.get_manager_invites(callback.from_user.id, user_status="filled")),
                           reply_markup=nav.mainMenu(user_language),parse_mode="html")
    ## If user manager
    if(db.is_user_manager(callback.from_user.id)):
        await state.set_state(None)
        await bot.send_message(callback.from_user.id,'Менеджер меню!', parse_mode="html", reply_markup=nav.managerMenu(user_language))
    await clear_chat(callback.message.message_id, callback.message.chat.id)
    logging.debug("###DEBUG### managerstats finished")

@dp.callback_query_handler()
#@dp.callback_query_handler(lambda x: x.data and x.data.startswith("reg "))
async def main_menu(call: types.CallbackQuery, state: FSMContext):
    logging.debug(await state.get_state())
    if call.message:
        #user_language = db.get_user_language(call.message.from_user.id)
        if call.data == 'reg':
            if db.user_registered(call.message.chat.id):
                await call.message.answer(f'Извините, но вы уже давали свои данные {random.choice(config.lying_reaction)}', reply_markup=nav.mainMenu())
                await clear_chat(call.message.message_id, call.message.chat.id)
                await state.set_state(None)
                return
            else:
                await call.message.answer('Введите, пожалуйста, свою страну')
                await RegStates.country.set()
                await clear_chat(call.message.message_id, call.message.chat.id)
        if call.data == 'FAQ':
            await call.message.answer(config.FAQ_info, parse_mode=types.ParseMode.MARKDOWN_V2, reply_markup=nav.mainMenu())
            await clear_chat(call.message.message_id, call.message.chat.id)
        # elif call.data == 'coinlistinfo':
        #     await call.message.answer('конлист', reply_markup=nav.mainMenu())
        #     await clear_chat(call.message.message_id, call.message.chat.id)

async def input_country(message: types.Message, state: FSMContext):
    ## Check if country is allowed
    ## Country not allowed
    if message.text.lower() in 'россиярашкарусскийрашароссийская федерация':
        await message.answer(f'Извините, но регистрация недоступна для граждан РФ {random.choice(config.bad_reaction)}', reply_markup=nav.mainMenu())
        await state.finish()
        return
    ## Country allowed
    elif message.text.lower() in config.countries:
        await state.update_data(tg_username=None)
        if message.chat.username:
            tg_username = message.chat.username
            await state.update_data(tg_username=tg_username)
            await state.update_data(tg_id=message.from_user.id)
        ## Save country to state data
        await state.update_data(country=message.text.lower())
        await RegStates.region.set()
        await message.answer('Введите название области')
    ## Country not from expected list
    else:
        await message.answer(
            f'Извините, но я не знаю такую страну, попробуйте написать иначе {random.choice(config.bad_reaction)}')
        return

async def input_region(message: types.Message, state: FSMContext):
        ## Save region to state data
        await state.update_data(region=message.text.lower())
        await RegStates.city.set()
        await message.answer('Введите название города')

async def input_city(message: types.Message, state: FSMContext):
        ## Save city to state data
        await state.update_data(city=message.text.lower())
        await RegStates.fullname.set()
        await message.answer('Введите полное ФИО')

async def input_fullname(message: types.Message, state: FSMContext):
    for _ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '"', '@', '\\', '|', '/', '!', '#', '$', '%', '^',
              '&', '*', '_', '=', '+', '?', '>', ',', '.']:
        if _ in message.text.lower():
            message.answer(f'Некорректное ФИО, попробуйте еще раз {random.choice(config.incorrect_reaction)}')
            return
    await state.update_data(full_name=message.text)
    await RegStates.address.set()
    await message.answer('Введите адрес проживания')

async def input_address(message: types.Message, state: FSMContext):
    await state.update_data(address=str(message.text))
    await RegStates.date_of_birth.set()
    await message.answer('Укажите свою дату рождения')

async def input_date_of_birth(message: types.Message, state: FSMContext):
    await state.update_data(date_of_birth=str(message.text))
    await RegStates.document_id.set()
    await message.answer('Укажите номер вашего паспорта/вод лицензии')

async def input_document_id(message: types.Message, state: FSMContext):
    await state.update_data(document_id=str(message.text))
    await RegStates.phonenumber.set()
    await message.answer('Укажите номер вашего телефона')

async def input_phonenumber(message: types.Message, state: FSMContext):
    if db.phone_exists(message.text):
        await message.answer(f'Извините, но вы уже указывали данный номер телефона {random.choice(config.lying_reaction)}', reply_markup=nav.mainMenu())
        await state.finish()
        await clear_chat(message.message_id, message.chat.id)
        return
    if 11 >= len(str(message.text)) >= 13:
        await message.answer(f'Некорректный номер телефона, возможно вы ошиблись {random.choice(config.incorrect_reaction)}')
        return
    for _ in str(message.text):
        if _ not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']:
            await message.answer(
                f'Некорректный номер телефона, возможно вы ошиблись {random.choice(config.incorrect_reaction)}')
            return
    await state.update_data(phone_number=message.text)

    data = await state.get_data()
    ## Update user data in table
    db.add_user_account(data['tg_id'],
                        data['tg_username'],
                        data['country'],
                        data['region'],
                        data['city'],
                        data['full_name'],
                        data['address'],
                        data['date_of_birth'],
                        data['document_id'],
                        data['phone_number'])
    logging.debug("DB user data update in table!")

    ## Notify manager about filled user
    manager_id = db.get_user_referral(data['tg_id'])
    if(manager_id != ""):
        manager_language = db.get_user_language(manager_id)
        await bot.send_message(manager_id, "@" + data['tg_username'] + set_localization(" заполнил свои данные и ждет вас для прохождения верификации!",manager_language))

    await state.finish()
    await message.answer('🎉')
    await clear_chat(message.message_id, message.chat.id)
    await message.answer('Поздравляю, информация сохранена!')
    await message.answer('Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰', reply_markup=nav.mainMenu())


## def main_buttons(rows: int) -> types.InlineKeyboardMarkup:
##     markup = types.InlineKeyboardMarkup(row_width=rows)
##     button = [types.InlineKeyboardButton('FAQ', callback_data='FAQ'),
##               types.InlineKeyboardButton('О coinlist', callback_data='coinlistinfo'),
##               types.InlineKeyboardButton('РЕГИСТРАЦИЯ', callback_data='reg')]
##     markup.add(*button)
##     return markup


# @dp.message_handler(Text(equals='хорошая работа олег', ignore_case=True))
# async def secret_download(message: types.Message):
#     await message.answer_document(open('users_data.txt', 'rb'))


# @dp.callback_query_handler()
# async def main_menu(call: types.CallbackQuery):
#     if call.message:
#         if call.data == 'FAQ':
#             await call.message.answer(config.FAQ_info, parse_mode=types.ParseMode.MARKDOWN_V2, reply_markup=nav.mainMenu())
#             await clear_chat(call.message.message_id, call.message.chat.id)

#         elif call.data == 'coinlistinfo':
#             await call.message.answer('конлист - тема, пушка', reply_markup=nav.mainMenu())
#             await clear_chat(call.message.message_id, call.message.chat.id)

#         elif call.data == 'reg':
#             await reg_start(call.message)

def register_handlers_registration(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state=None)
    dp.register_message_handler(cancel_handler, state = '*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(input_country, state=RegStates.country)
    dp.register_message_handler(input_region, state=RegStates.region)
    dp.register_message_handler(input_city, state=RegStates.city)
    dp.register_message_handler(input_fullname, state=RegStates.fullname)
    dp.register_message_handler(input_address, state=RegStates.address)
    dp.register_message_handler(input_date_of_birth, state=RegStates.date_of_birth)
    dp.register_message_handler(input_document_id, state=RegStates.document_id)
    dp.register_message_handler(input_phonenumber, state=RegStates.phonenumber)

# https://github.com/SoDeepASMR/CoinListBot

import random
from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
import logging
import config
from config import ADMINS
from keyboards import keyboards as nav
from database.database import Database
from bot_init import dp, bot, db

test_data = None

class RegStates(StatesGroup):
    nationality = State()
    fullname = State()
    phonenumber = State()
    address = State()
    postcode = State()
    #photo = State()

# @dp.message_handler(commands='start')
async def cm_start(message: types.Message, state: FSMContext):
    await message.answer(random.choice(config.welcome))
    await message.answer('Привет!', reply_markup=nav.mainMenu())
    if(message.from_user.id in ADMINS):
        await bot.send_message(message.from_user.id,"<b>Admin Menu</b>", reply_markup=nav.adminMenu(), parse_mode="html")
    await state.set_state(None)

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

@dp.callback_query_handler()
#@dp.callback_query_handler(lambda x: x.data and x.data.startswith("reg "))
async def reg_start(call: types.CallbackQuery, state: FSMContext):

    # global test_data
    # try:
    #     file = open('users.txt', 'a+', encoding='utf-8')
    #     test_data = [_.strip() for _ in file.readlines()]
    #     file.close()
    # except FileNotFoundError:
    #     pass

    # if call.message.chat.username:
    #     if newdb.user_exists(call.message.from_user.id):
    #         await call.message.answer(f'Извините, но вы уже давали свои данные {random.choice(config.lying_reaction)}', reply_markup=nav.mainMenu())
    #         await clear_chat(call.message.message_id, call.message.chat.id)
    #         await state.set_state(None)
    #         return
    if call.message:
        if call.data == 'reg':
            newdb = Database()
            if newdb.user_exists(call.message.chat.id):
                await call.message.answer(f'Извините, но вы уже давали свои данные {random.choice(config.lying_reaction)}', reply_markup=nav.mainMenu())
                await clear_chat(call.message.message_id, call.message.chat.id)
                await state.set_state(None)
                return
            else:
                await call.message.answer('Введите, пожалуйста, свою национальность (страну)')
                await RegStates.nationality.set()
                await clear_chat(call.message.message_id, call.message.chat.id)
        if call.data == 'FAQ':
            await call.message.answer(config.FAQ_info, parse_mode=types.ParseMode.MARKDOWN_V2, reply_markup=nav.mainMenu())
            await clear_chat(call.message.message_id, call.message.chat.id)
        elif call.data == 'coinlistinfo':
            await call.message.answer('конлист - тема, пушка', reply_markup=nav.mainMenu())
            await clear_chat(call.message.message_id, call.message.chat.id)

#@dp.message_handler(state=RegStates.nationality)
async def nationality(message: types.Message, state: FSMContext):
    if message.text.lower() in 'россиярашкарусскийрашароссийская федерация':
        await message.answer(f'Извините, но регистрация недоступна для граждан РФ {random.choice(config.bad_reaction)}', reply_markup=nav.mainMenu())
        await state.finish()
        return
    elif message.text.lower() in config.countries:
        await state.update_data(tg_username=None)

        if message.chat.username:
            tg_username = message.chat.username
            await state.update_data(tg_username=tg_username)
            await state.update_data(tg_id=message.from_user.id)

        await state.update_data(country=message.text.lower())
        await RegStates.next()
        await message.answer('Введите полное ФИО как в паспорте')
    else:
        await message.answer(
            f'Извините, но я не знаю такую страну, попробуйте написать иначе {random.choice(config.bad_reaction)}')
        return

#@dp.message_handler(state=RegStates.fullname)
async def fullname(message: types.Message, state: FSMContext):
    for _ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'", '"', '@', '\\', '|', '/', '!', '#', '$', '%', '^',
              '&', '*', '_', '=', '+', '?', '>', ',', '.']:
        if _ in message.text.lower():
            message.answer(f'Некорректное ФИО, попробуйте еще раз {random.choice(config.incorrect_reaction)}')
            return
    await state.update_data(full_name=message.text)
    await RegStates.next()
    await message.answer('Введите номер телефона')

#@dp.message_handler(state=RegStates.phonenumber)
async def phonenumber(message: types.Message, state: FSMContext):
    newdb = Database()

    if newdb.phone_exists(message.text):
        await message.answer(f'Извините, но вы уже давали свои данные {random.choice(config.lying_reaction)}', reply_markup=nav.mainMenu())
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
    await RegStates.next()
    await message.answer('Введите полный адрес прописки как в паспорте')


#@dp.message_handler(state=RegStates.address)
async def address(message: types.Message, state: FSMContext):
    await state.update_data(address=str(message.text))
    await RegStates.next()
    await message.answer('Введите свой почтовый индекс (можно посмотреть в интернете, привязан к улице)')


#@dp.message_handler(state=RegStates.postcode)
async def postcode(message: types.Message, state: FSMContext):
    await state.update_data(postcode=str(message.text))

    data = await state.get_data()
    newdb = Database()
    db.add_user_account(data['tg_id'],
                        data['tg_username'],
                        data['country'],
                        data['full_name'],
                        data['phone_number'],
                        data['address'],
                        data['postcode'])
    print("DB user data added to table!")

    await state.finish()

    await message.answer('🎉')
    await clear_chat(message.message_id, message.chat.id)
    await message.answer('Поздравляю, информация сохранена!')
    await message.answer('Скоро с вами свяжется менеджер для прохождения верификации и выплаты 💰', reply_markup=nav.mainMenu())

    # users = open('users.txt', 'a+', encoding='utf-8')
    # if data['profile'] is not None:
    #     users.write(str(data['profile']) + '\n')
    # users.write(str(data['number']) + '\n')
    # users.close()
    # print('Файл users.txt дополнен')

    # users_data = open('users_data.txt', 'a+', encoding='utf-8')
    # users_data.write(';'.join([str(_[1]) for _ in data.items()]) + '\n')
    # users_data.close()
    # print('Файл users_data.txt дополнен')


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
    dp.register_message_handler(nationality, state=RegStates.nationality)
    dp.register_message_handler(fullname, state=RegStates.fullname)
    dp.register_message_handler(phonenumber, state=RegStates.phonenumber)
    dp.register_message_handler(address, state=RegStates.address)
    dp.register_message_handler(postcode, state=RegStates.postcode)

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, Dispatcher, bot
from aiogram import types
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb

class FSMadmin(StatesGroup):
    sub_name = State()
    sub_mark = State()


# async def only_for_btn(message: types.Message):
#     await bot.send_message(message.from_user.id, "Що треба?", reply_markup=admin_kb.kb_admin)
#     await message.delete

#@dp.message_handler(commands='Записати', state=None)
async def cm_start(message : types.Message):
    await FSMadmin.sub_name.set()
    await message.reply('Напиши назву предмету, "cancel" для відміни')
    #await FSMadmin.next()

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


#@dp.message_handler (state=FSMadmin.sub_name)
async def load_sub_name(message : types.Message, state : FSMContext):
    global usr_id
    usr_id = message.from_user.id
    async with state.proxy() as data:
        data['id'] = usr_id
        data['sub_name'] = message.text
    await FSMadmin.next()
    await message.reply('Тепер введи оцінку, "cancel" для відміни')
    

#@dp.message_handler (state=FSMadmin.sub_mark)
async def load_sub_mark(message : types.Message, state : FSMContext):
    #pizdets error --------------------------------------------------------------------------------------------------------------------------------------------------------------
    async with state.proxy() as data:
        data['sub_mark'] = message.text
    await FSMadmin.next()
    await message.reply('Готово')
    
    
    #data to tg
    async with state.proxy() as data:
        await message.reply(str(data))
    
    #data to sql
    await sqlite_db.sql_add_command(state)

    await state.finish()



def reg_handlers_admin(dp : Dispatcher):
    #dp.register_message_handler(only_for_btn, commands=['add'], state=None)
    dp.register_message_handler(cm_start, commands=['add'], state=None)
    #dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    #dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_sub_name, state=FSMadmin.sub_name)
    #dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    #dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_sub_mark, state=FSMadmin.sub_mark)
    #dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    #dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')



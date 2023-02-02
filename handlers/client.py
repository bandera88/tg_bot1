from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
import sqlite3 as sq
from data_base import sqlite_db


def reg_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_info, commands=['info'])
    dp.register_message_handler(command_show, commands=['show'])
    dp.register_message_handler(dm, commands=['dm'])


async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привіт, це бот-помічник по організації оцінок 2 семестру.', reply_markup=kb_client)
    except:
        await message.answer('Напиши боту в ЛС: http://t.me/cumpuss_bot')
        await message.delete()


async def command_info(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Це гавнобот, який є в розробці. Пропозиції: https://t.me/muhammad_abdull', reply_markup=kb_client)
    except:
        await message.answer('Напиши боту в ЛС: http://t.me/cumpuss_bot')
        await message.delete()

async def command_show(message: types.Message):
    global base, cur, usr_id
    usr_id = message.from_user.id
    base = sq.connect('base.db')
    cur = base.cursor()
    cur.execute("SELECT name, mark FROM menu WHERE id = ?", (usr_id, ))
    result = cur.fetchall()
    #arr = [result]
    await message.reply(f'Ваш айді {usr_id}, \n Ваші оцінки \n {result}')


# async def cm_start(message : types.Message):
#     await FSMadmin.sub_name.set()
#     await message.reply('Напиши назву предмету, "cancel" для відміни')
#     #await FSMadmin.next()

# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('OK')


# #@dp.message_handler (state=FSMadmin.sub_name)
# async def load_sub_name(message : types.Message, state : FSMContext):
#     global usr_id
#     usr_id = message.from_user.id
#     async with state.proxy() as data:
#         data['id'] = usr_id
#         data['sub_name'] = message.text
#     await FSMadmin.next()
#     await message.reply('Тепер введи оцінку, "cancel" для відміни')


async def dm(message: types.Message):
    await message.reply('Тепер введи оцінку, "cancel" для відміни')
    global usr_id
    base = sq.connect('base1.db')
    usr_id = message.from_user.id
    print(message.text)
    data = (usr_id, message.text)
    sqlite_db.cur.execute('INSERT INTO menu(id ,dm) VALUES (?,?)', data)
    base.commit()
    print('Success commit')
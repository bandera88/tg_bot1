from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
import sqlite3 as sq


def reg_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_info, commands=['info'])
    dp.register_message_handler(command_show, commands=['show'])


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
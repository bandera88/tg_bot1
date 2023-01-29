from aiogram import types, Dispatcher
import json, string
from create_bot import dp

def reg_handlers_other(dp : Dispatcher):
    dp.register_message_handler(ban)


async def ban(message : types.Message):
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('C:\\Users\\dimam\\tg_bot\\words.json')))) != set():
        await message.reply('Бан по причині підарас')
    #await message.answer(message.text)
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)
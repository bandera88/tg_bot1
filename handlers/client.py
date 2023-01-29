from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


def reg_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_info, commands=['info'])


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
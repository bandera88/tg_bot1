from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b_help = KeyboardButton('/help')
b_info = KeyboardButton('/info')
b_add = KeyboardButton('/add')
b_show = KeyboardButton('/show')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b_help, b_info, b_add, b_show)
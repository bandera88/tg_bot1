from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b_help = KeyboardButton('/help')
b_info = KeyboardButton('/info')
b_add = KeyboardButton('/add')
b_show = KeyboardButton('/show')
b_del = KeyboardButton('/delete')
b_dm = KeyboardButton('/dm')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b_help, b_info, b_add, b_show, b_del, b_dm)
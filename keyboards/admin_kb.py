from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b_help = KeyboardButton('/help')
b_info = KeyboardButton('/info')
b_add = KeyboardButton('/add')
b_delete = KeyboardButton('/delete')
b_show = KeyboardButton('/show')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_admin.row(b_help, b_info, b_add, b_delete, b_show)
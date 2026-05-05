from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Заявки на рассмотрении')],
    [KeyboardButton(text='Правила админа')]
],
resize_keyboard=True)

admin_accept_deny_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Принять',style='success'),KeyboardButton(text='Отклонить',style='danger')]
],
resize_keyboard=True)



from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Законы'), KeyboardButton(text='Заявка')],
    [KeyboardButton(text='Информация'), KeyboardButton(text='Донат')]
],
resize_keyboard=True)


new_zayavka_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Шаблон оформления'),KeyboardButton(text='Создать заявку')],
    [KeyboardButton(text='Главное меню')]
],
resize_keyboard=True)


under_consideration_zayavka_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Шаблон оформления'),KeyboardButton(text='Редактировать')],
    [KeyboardButton(text='Главное меню')]
],
resize_keyboard=True)


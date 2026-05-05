import os
from dotenv import load_dotenv
from aiogram import Router, F
from buttons import user_main_menu_keyboard
from admin_buttons import admin_main_menu_keyboard

load_dotenv() 

admin_id = os.getenv("ADMIN_ID")


main_router = Router()



@main_router.message(F.text=="/start")
async def cmd_start(message):
    print(message.from_user.id)
    if message.from_user.id != admin_id:
        await message.answer("Добро пожаловать в бота", reply_markup=user_main_menu_keyboard)
    if message.from_user.id == admin_id:
        await message.answer("Добро пожаловать в бота админ легенда", reply_markup=admin_main_menu_keyboard)


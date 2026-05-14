from database import writing_file
from aiogram import Router,F
from config import database_file_name
from database import reading_file
from admin_buttons import admin_accept_deny_keyboard
from admin_buttons import admin_main_menu_keyboard
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from admin_buttons import admin_otmena_keyboard
from aiogram.types import CallbackQuery


admin_router = Router()

class States(StatesGroup):
    waiting_id = State()


@admin_router.callback_query(F.data == "otmena")
async def handle_btn1(callback: CallbackQuery,state: FSMContext):
    await callback.answer("Эль примо")
    await state.clear()
    await callback.message.delete()





@admin_router.message(F.text=='Правила админа')
async def pravila_admina(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("1 правило никогда не рассказывать про первое правило 2 правило никогда не рассказывать про второе правило")

@admin_router.message(F.text=='Заявки на рассмотрении',)
async def zayavki_na_rassmotrnii(message,state: FSMContext):
    message_text = "Пользователи с заявками на рассмотрении:  \n"
    for i in reading_file(database_file_name):
        if i["status"] == "Under consideration":
            message_text = message_text + f'\n - `{str(i["tg_id"])}`  '


    message_text = message_text + '\n Введите нужный вам айдишник'
    

    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer(message_text,parse_mode = 'markdown',reply_markup = admin_otmena_keyboard)
    await state.set_state(States.waiting_id)
    message.from_user.id

@admin_router.message(States.waiting_id)
async def button_two(message,state: FSMContext):
    for i in reading_file(database_file_name):
        if message.text == str(i['tg_id']):
            await state.clear()
            await state.update_data(user_id=message.text)
            await message.answer(i['text'],reply_markup = admin_accept_deny_keyboard)
            
            return
            
            
    await message.answer('такого ID не существует или нету в базе данных, введите другой ID ')


@admin_router.message(F.text=='Принять')
async def button_two(message,state: FSMContext):
    all_zayavki = reading_file(database_file_name)
    temp_data = await state.get_data()
    for i in all_zayavki:
        print(temp_data['user_id'],str(i['tg_id']))
        if temp_data['user_id'] == str(i['tg_id']):
            i['status'] = 'Accept'
            writing_file(file_name=database_file_name,file_contents=all_zayavki)
            await message.answer("Заявка принята!")
            await zayavki_na_rassmotrnii(message,state)
            break

# @admin_router.message(F.text=='')
# async def button_two(message,state: FSMContext):
#     all_zayavki = reading_file(database_file_name)
#     temp_data = await state.get_data()
#     print(temp_data['user_id'],str(i['tg_id']))
#     for i in all_zayavki:
#         if temp_data['user_id'] == str(i['tg_id']):
#             i['status'] = ''
#             writing_file(file_name=database_file_name,file_contents=all_zayavki)
#             break
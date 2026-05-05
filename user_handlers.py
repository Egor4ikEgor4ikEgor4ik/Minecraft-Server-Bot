from pprint import pprint
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Bot,Router,F
from aiogram.types import Message
from buttons import user_main_menu_keyboard
from buttons import new_zayavka_keyboard
from buttons import under_consideration_zayavka_keyboard
from database import reading_file
from database import writing_file
from config import database_file_name


user_router = Router()


class States(StatesGroup):
    waiting_zayavka = State()
    waiting_updated_zayavka = State()




@user_router.message(F.text=='Законы')
async def button_one(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("""
Ванильный геймплей - без модов, только ванильный Minecraft с возможными админскими плагинами для защиты.
•	*Цивилизационный формат* - игроки объединяются в города/государства, развивают экономику, дипломатию, воюют или сотрудничают.
Честная игра - читы, баги, дюпы, использование стороннего ПО (читы, макросы, X-Ray) запрещены.
•	*Объявление войны* - перед началом военных действий необходимо публично объявить войну (в чат / дискорд) с указанием причины. Внезапные нападения без объявления — запрещены.
•	*Мирные игроки* - игроки, не входящие в воюющие цивилизации, не могут быть атакованы (если иное не согласовано).
•	*Перемирие и мир* - можно заключать мирные договоры через администрацию или личные соглашения.
•	Шпионаж разрешён, но без использования читов (например, нельзя залезать в чужие Discord-каналы для шпионажа).
•	Захват территорий возможен только в состоянии войны.
•	Запрещено уничтожать или забирать имущество цивилизации, которая капитулировала или проиграла войну, без договорённости (или по правилам, установленным перед войной).
•	*Режим "рейда"* - можно грабить сундуки, убивать, ломать постройки в пределах вражеской территории только во время официальной войны.
Запрещено ломать, строить, поджигать, заливать лавой, ставить кристаллы эндера на территориях других цивилизаций без объявления войны.
•	*Запрещено убивать мирных игроков без их согласия (PvP-зоны могут быть оговорены отдельно).
•	*Запрещено воровать из сундуков, ферм, складов чужих цивилизаций в мирное время.
•	*Запрещено строить неприличные, оскорбительные или мешающие игровому процессу постройки на общей территории.
•	*Территориальные границы - каждая цивилизация должна чётко обозначать свои границы (стенами, столбами, табличками) или зарегистрировать их у администрации через плагин.
•	*Дистанция между цивилизациями - новые цивилизации должны основываться на расстоянии не менее 500 блоков от границ других (если нет договорённости).
•	*Общественные ресурсы - шахты, нейтральные деревни, порталы в Энд/Ад считаются нейтральными территориями, разрушать их или блокировать доступ запрещено.
•	*Торговля между игроками разрешена в любой форме (обмен, алмазы, изумруды, услуги).
•	*Мошенничество при торговле (обман, невыполнение обязательств) наказывается.
•	*Администрация не несёт ответственности за итоги сделок, но может помочь в спорных ситуациях при наличии доказательств.
•	Запрещено использование:
o	*X-Ray-текстур пакетов, модов, клиентов (Wurst, Impact и т.п.)
o	*Автокликеры, макросы, авто-фермы с использованием макросов.
o	*Использование багов игры (дюпы, бессмертие, полёты в ванилле).
o	*Любые программы, дающие игровое преимущество.
•	Допустимо:
o	*Оптимизационные моды (OptiFine, Sodium)
o	*Моды на мини-карту, если они не показывают игроков/сундуки (только карту местности)
o	*Ресурс-паки, изменяющие только графику
•	*Уважение* - оскорбления, дискриминация, травля, провокации запрещены.
•	Спам, флуд, реклама других серверов - бан.
•	*Общий чат* - для дипломатии, торговли, общих вопросов.
•	*Локальный чат* (/msg, /tell) - для приватных переговоров.                        
""",parse_mode = 'Markdown')                    
                         



 

@user_router.message(F.text=='Заявка')
async def button_two(message):
    zayavka = None
    for i in reading_file(database_file_name):
        if message.from_user.id == i['tg_id']:
            zayavka = i
        
    if zayavka==None:
        await message.answer("Вы еще не оставляли заявку на получения доступа к серверу",reply_markup = new_zayavka_keyboard)    

    if zayavka!=None and zayavka["status"]=='Accept':
        await message.answer("Ваша заявка была принята!")
    
    if zayavka!=None and zayavka['status']=='Under consideration':
        await message.answer("Ваша заявка на рассмотрении!",reply_markup = under_consideration_zayavka_keyboard)
    
    if zayavka!=None and zayavka['status']=='Deny':
        await message.answer("Ваша заявка была отклонена, отредактируйте ее!",reply_markup = under_consideration_zayavka_keyboard)
    
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    





@user_router.message(F.text=='Информация')
async def button_three(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("""
    
    🎛️𝐒𝐄𝐑𝐕𝐄𝐑 𝐈𝐏 - 
📲𝐂𝐨𝐧𝐭𝐚𝐜𝐭𝐬:
- @jurgenxd1
- @SilentBuilder
🏔️𝐋𝐢𝐧𝐤 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐬𝐞𝐫𝐯𝐞𝐫 - 
🪪𝐒𝐞𝐫𝐯𝐞𝐫 𝐬𝐢𝐭𝐞 - 26.22.155.218:1111


        """)
@user_router.message(F.text=='Донат')
async def button_four(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("Задонать новому серверу: (ссылка на донейт алертс)")

@user_router.message(F.text=='Главное меню')
async def button_two(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer("Возвращаемся в главное меню...",reply_markup = user_main_menu_keyboard)

@user_router.message(F.text=='Шаблон оформления')
async def button_two(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer('''```
Имя:
Контактные данные (дискорд,стим,телеграм):
Опыт игры:
Текст заявки (краткое о себе):
```''',parse_mode = 'Markdown')

@user_router.message(F.text=='Статус заявки')
async def button_two(message):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer()

@user_router.message(F.text=='Создать заявку',)
async def button_two(message,state: FSMContext):
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer('Начните писать заявку')
    await state.set_state(States.waiting_zayavka)
    

@user_router.message(States.waiting_zayavka)
async def button_two(message,state: FSMContext):
    a = (reading_file(database_file_name))
    zayavka = {'tg_id': message.from_user.id, 'status': 'Under consideration', 'text': message.text}
    a.append(zayavka)
    writing_file(database_file_name,a)
    await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
    await message.answer('Ваша заявка принята, и находится на рассмотрении',reply_markup = user_main_menu_keyboard)
    await state.clear()

@user_router.message(F.text=='Редактировать')
async def button_two(message,state: FSMContext):
    for user_zayavka in reading_file(database_file_name):
        if message.from_user.id==user_zayavka['tg_id']:
            
    
            await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
            await message.answer(f'Вот текущий текст вашей заявки, напишите новый:\n\n`{user_zayavka['text']}`',parse_mode = 'Markdown')
            await state.set_state(States.waiting_updated_zayavka)

@user_router.message(States.waiting_updated_zayavka)
async def update_zayavka(message):
    all_zayavki = reading_file(database_file_name)
    for user_zayavka in all_zayavki:
        if message.from_user.id==user_zayavka['tg_id']:
            user_zayavka['text']=message.text
            writing_file(file_name=database_file_name,file_contents=all_zayavki)
           
            await message.delete() # удаляет сообщение пользователя в котором содержится просто текст кнопки
            await message.answer('Текст заявки изменен!')


















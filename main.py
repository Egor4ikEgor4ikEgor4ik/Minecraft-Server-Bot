import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot,Dispatcher
from user_handlers import user_router
from main_handlers import main_router
from admin_handlers import admin_router
from database import reading_file
from database import create_empty_file
from config import database_file_name

load_dotenv() 

token = os.getenv("TOKEN")



dp = Dispatcher()





async def main():
    try :
        reading_file(database_file_name)
    except:
        create_empty_file(database_file_name)
    bot = Bot(token)
    dp.include_router(user_router)
    dp.include_router(main_router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)

   


if __name__ == "__main__":
    asyncio.run(main())


































import asyncio
from aiogram import Bot, Dispatcher
from handlers import rt

bot = Bot(token='7487503300:AAHK_IVccuduTjH-t_it7pGykav8gJU0XGo')
async def main():
    dp = Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
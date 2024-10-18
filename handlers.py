from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from random import randint
from requests import set_user, set_review, get_review
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


from keyboards import keys, inline_keys


rt = Router()



class ReviewState(StatesGroup):
    waiting = State()

@rt.message(CommandStart())
async def command_start_handler(message: Message):
    await set_user(message.from_user.id)
    await message.answer(f"🦜- Чик Чирик!", reply_markup=keys)
        
@rt.message(F.text == 'Дать зерна')
async def command_feed_handler(message: Message):
    for i in range(0, 20):
        await message.answer(f"Чик Чирик!")
        await asyncio.sleep(randint(0, 20))

@rt.message(F.text == 'Оставить/Изменить отзыв')
async def command_ask_review_handler(message: Message, state: FSMContext):
    review = await get_review(message.from_user.id)
    if review:
        await message.answer(f"🦜- Вы уже оставили нам отзыв!\n\n{review.text}", reply_markup=inline_keys)
    else:
        await message.answer("🦜- Напишите ваш отзыв!\nРасскажите что вам понравилось.\nА за что разраба расстрелять.")
        await state.set_state(ReviewState.waiting)
    
@rt.message(F.text == 'Поддержка')
async def command_problem_handler(message:Message):
    await message.answer('🦜- В разработке!')

@rt.callback_query(F.data == 'rewrite')
async def command_rewrite_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer(':D')
    await callback.message.answer('🦜- Дерзайте!')
    await state.set_state(ReviewState.waiting)

@rt.message(ReviewState.waiting)
async def command_review_handler(message: Message, state: FSMContext, bot:Bot):
    a = await set_review(message.from_user.id, message.text)
    await message.answer(f"🦜- Ваш отзыв N{str(a)} проверяется!\nМы уведомим вас.", reply_markup=keys)
    await state.clear()
    
    msg = f"Отзыв N{str(a)} от {message.from_user.id}\n\n{message.text}"
    await bot.send_message(1045039269, msg)
    
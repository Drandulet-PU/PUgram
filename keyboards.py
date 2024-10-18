from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton

keys = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Дать зерна')], \
                               [KeyboardButton(text='Оставить/Изменить отзыв')], \
                               [KeyboardButton(text='Поддержка')]], \
                               resize_keyboard=True, \
                               input_field_placeholder='Выберите пункт меню...')
                               
inline_keys = InlineKeyboardMarkup(
                        inline_keyboard=[[InlineKeyboardButton(text='Переписать', \
                        callback_data='rewrite')]]
                        )
                               

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

def menu_frep(user_id):
    main_kb = [
        [KeyboardButton(text="Получить гороскоп")]
    ]
    main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)
    
    return main

    
class Paginator(CallbackData, prefix='pag'):
    action: str
    page: int
    
def paginator(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data=Paginator(action='prev', page=page).pack()),
        InlineKeyboardButton(text="Вперед", callback_data=Paginator(action='next', page=page).pack()),
        InlineKeyboardButton(text="Выбрать", callback_data=Paginator(action='get', page=page).pack()),
        width=2
    )
    return builder.as_markup()
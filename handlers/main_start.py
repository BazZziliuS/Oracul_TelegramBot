from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards.reply_all import menu_frep, paginator, Paginator
from library.constants import zodiac_sign_library
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from services.API_ORAKUL import HTTP_request

start_router = Router(name=__name__)


@start_router.message(F.text.in_(['⬅ Главное меню', '/start']))
@start_router.message(CommandStart())
async def main_start(message: Message):
    await message.answer(
        "🔸 Бот готов к использованию.\n🔸 Если не появились вспомогательные кнопки\n▶ Введите /start", 
        reply_markup=menu_frep(message.from_user.id)
    )

@start_router.callback_query(Paginator.filter(F.action.in_(['prev', 'next', 'get'])))
async def paginator_callback(call: CallbackQuery, callback_data: Paginator):
    action = callback_data.action
    page_num = int(callback_data.page)
    
    zodiac = [key for key in zodiac_sign_library.keys()]
    
    if action == 'next':
        page = page_num + 1 if page_num < len(zodiac_sign_library) else page_num
    
    if action == 'prev':
        page = page_num - 1 if page_num > 0 else 0
    
    if action == 'get':
        result = await HTTP_request(zodiac=zodiac[page_num])
        await call.message.answer(text=f'*{zodiac[page_num]}*\n\n{result}')
        
    elif action in ('next', 'prev'):
        with suppress(TelegramBadRequest):
            await call.message.edit_text(
                text=f'*Выбран: {zodiac[page]}*', 
                reply_markup=paginator(page)
            )
    
    await call.answer()
        

@start_router.message(F.text == 'Получить гороскоп')
async def zodiac(message: Message):
    zodiac = [key for key in zodiac_sign_library.keys()]
    await message.answer(
        f'Выбран: *{zodiac[0]}*', 
        reply_markup=paginator()
    )

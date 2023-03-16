from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


inlayn_markup = InlineKeyboardMarkup(row_width=1,inline_keyboard=[
    [InlineKeyboardButton(text="🎙 Audio tinglash",callback_data="tts")]
])
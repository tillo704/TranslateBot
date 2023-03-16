from aiogram import types
from loader import dp
from states.main import TranslateText
from aiogram.dispatcher import FSMContext
from googletrans import Translator
from keyboards.inline.main import inlayn_markup 

translator = Translator()


@dp.message_handler(state=TranslateText.translate)
async def translte_text(message: types.Message,state : FSMContext):
    data = await state.get_data()
    text = message.text
    langs=data.get("langs")
    lang1,lang2 = langs.split("-")
    taranslated =translator.translate(text,srq=lang1, dest=lang2)
    await state.update_data({"text":taranslated.text,"lang2":lang2})
    await message.answer(taranslated.text,reply_markup=inlayn_markup)
    await TranslateText.next()
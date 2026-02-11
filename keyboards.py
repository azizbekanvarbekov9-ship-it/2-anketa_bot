from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

boshlash_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📝 Anketani boshlash")]],
    resize_keyboard=True
)

telefon_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(
        text="📞 Telefon raqamni yuborish",
        request_contact=True
    )]],
    resize_keyboard=True
)

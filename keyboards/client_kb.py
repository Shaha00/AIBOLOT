from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
)

start_button = KeyboardButton("/start")
button1 = KeyboardButton('/record')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Наша Геолокация')


start_markup.add(button1, button2, button3)

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("Хирург"),
    KeyboardButton("Терапевт"),
    KeyboardButton("Уролог"),
    KeyboardButton("Гинеколог"),
    KeyboardButton("Стоматолог"),
    KeyboardButton("Окулист"),
    KeyboardButton("Травматолог"),
)

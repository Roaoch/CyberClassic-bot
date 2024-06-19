from aiogram.types import \
    InlineKeyboardButton, \
    InlineKeyboardMarkup, \
    KeyboardButton,\
    ReplyKeyboardMarkup

menu_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='GitHub', url='https://github.com/Roaoch'),
        InlineKeyboardButton(text='HuggingHub', url='https://huggingface.co/Roaoch')
    ]
])
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сгенерировать предложение')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Нажми кнопку.'
)
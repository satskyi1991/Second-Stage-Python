from telebot import TeleBot, types
from config import TOKEN, BUTTONS

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def begin(message):

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    buttons = [
        types.KeyboardButton(text=BUTTONS['go_to_inline']),
        types.KeyboardButton(text=BUTTONS['contact'], request_contact=True),
        types.KeyboardButton(text=BUTTONS['location'], request_location=True)
    ]

    kb.add(*buttons)

    bot.send_message(
        message.chat.id,
        'Hello',
        reply_to_message_id=message.message_id,
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: m.text == BUTTONS['go_to_inline'], content_types=['text'])
def hello_handler(message):

    kb = types.InlineKeyboardMarkup(row_width=1)

    buttons = [
        types.InlineKeyboardButton(
            text='Товар 1',
            callback_data='345',

        ),
        types.InlineKeyboardButton(
            text='Товар 2',
            callback_data='346'
        )
    ]

    kb.add(*buttons)
    bot.send_message(message.chat.id, 'Инлайн клавиатура!', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def testing_inline(call):
    goods = {
        '345': {
            'title': 'Телефон',
            'description': 'Описание телефона'
            },
        '346': {
            'title': 'Ноутубук',
            'description': 'Описание ноутбука'
        }
    }

    good = goods[call.data]
    bot.send_message(
        call.message.chat.id,
        f'Вы выбрали товар <b>{good["title"]}</b>\nОписание <b>{good["description"]}</b>',
        parse_mode='HTML',
    )


@bot.message_handler(content_types=['text'])
def messaging(message):

    bot.send_message(
        message.chat.id,
        message.text[::-1]
    )


bot.polling()

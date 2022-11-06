from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello : {message.from_user.full_name}')

@dp.message_handler(commands=['games'])
async def games_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая задача",
                                         callback_data='next_task1')
    markup.add(button_call_1)
    question = 'Назовите ткань, изображённую на рисунке'
    answers = ['Мышечная', 'Эпителиальная', 'Проводящая', 'Нервная']
    photo = open('media/img1.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
                        question=question,
                        options=answers,
                        correct_option_id=1,
                        is_anonymous = False,
                        type='quiz',
                        reply_markup=markup,
                        open_period=30,
                        explanation='Это очень легкий вопрос, если не знаешь, то загугли',
                        explanation_parse_mode = ParseMode.MARKDOWN_V2
    )

@dp.callback_query_handler(lambda func: func.data == 'next_task1')
async def games_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая задача', callback_data='next_task2')
    markup.add(button_call_2)
    question2 = 'Что изображено на рисунке?'
    answers = ['Лейкоциты', 'Тромбоциты', 'Эритроциты', 'Мембрана']
    photo = open('media/img2.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question2,
                            options=answers,
                            correct_option_id=2,
                            open_period=30,
                            explanation='Эритр...',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'next_task2')
async def task_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая задача", callback_data='next_task3')
    markup.add(button_call_3)
    question3 = 'Лимфа - это...(ответов несколько, будьте внимательны!)' \
                'картинка просто для общего развития, чтобы вы имели представление, ' \
                'что это такое. к заданию не имеет отношения'

    answers3 = ['Лимфатиеские мешки и узлы', 'Плазма+форменные элементы', 'Лимфатические узлы', ' Лимфатические сосуды']
    photo = open('media/img3.jpg', 'rb')
    await  bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question3,
                            options=answers3,
                            correct_option_id=3,
                            open_period=30,
                            explanation='Сосуды...',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

@dp.callback_query_handler(lambda func: func.data == 'next_task3')
async def task_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Следующая задача", callback_data='next_task4')
    markup.add(button_call_4)
    question4 = 'Укажите название ткани, изображённой на рисунке'
    answers4 = ['Мышечная', 'Жировая', 'Проводящая', 'Запасающая']
    photo = open('media/img4.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question4,
                            options=answers4,
                            correct_option_id=1,
                            open_period=30,
                            explanation='Подсказака в картинке',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

@dp.callback_query_handler(lambda func: func.data == 'next_task4')
async def task_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task5')
    markup.add(button_call_5)
    question5 = 'Укажите название ткани, изображённой на рисунке'
    answers5 = ['Гладкая мышечная', 'Поперечно-полосатая скелетная мышечная', 'Проводящая', 'Покровная']
    photo = open('media/img5.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question5,
                            options=answers5,
                            correct_option_id=0,
                            open_period=30,
                            explanation='Гладкость...',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'next_task5')
async def task_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task6')
    markup.add(button_call_5)
    question5 = 'Укажите вид ткани, изображённый на рисунке'
    answers5 = ['Проводящая', 'Нервная', 'Эпителиальная', 'Покровная']
    photo = open('media/img6.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question5,
                            options=answers5,
                            correct_option_id=1,
                            open_period=30,
                            explanation='Нерв...',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)




from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
from datetime import datetime

bot = Bot('5358931325:AAHYDSqB3CgZnljXWMo3LgAXMracui6M8AU')

disp = Dispatcher(bot)

@disp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Hello')
    await message.answer("I'm TecHeresBot")

@disp.message_handler(text=['time'])
async def show_time(message: types.Message):
    await message.reply(f'Now it is {datetime.now().time()}')

@disp.message_handler(text=['date'])
async def show_date(message: types.Message):
    await message.reply(f'Today it is {datetime.now().date()}')

@disp.message_handler(commands=['show'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(*['time', 'date'])
    await message.reply('Choose what to show', reply_markup=keyboard)

@disp.message_handler(commands=['inline_show'])
async def inline_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(text=i.split('/')[-1],
                                          url=i) for i in ['https://github.com/TecHeReTiC3141/Dungetic',
                                                           'https://github.com/TecHeReTiC3141/learning_pysimpleGUI',
                                                           'https://github.com/TecHeReTiC3141/System-of-road-accidents-analytics']]
    keyboard.add(*buttons)
    await message.answer('My repos:', reply_markup=keyboard)
    await message.answer('Also please visit my GitHub-account: https://github.com/TecHeReTiC3141')


executor.start_polling(disp, skip_updates=True)


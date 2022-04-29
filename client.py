from bot import *

@disp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply('Hello')
    await message.answer("I'm TecHeresBot")
    await message.delete()


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


@disp.message_handler(content_types=types.ContentType.PHOTO)
async def echo_photo(message: types.Message):
    await message.reply_photo(message.photo[0].file_id)


@disp.message_handler()
async def anything(message: types.Message):
    banned = await handle_banned(message.text.split())
    if banned:
        await message.reply(f'Праукраинские слова {banned} запрещены')
        await message.delete()

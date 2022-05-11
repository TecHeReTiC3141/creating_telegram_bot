from bot import *


async def start(message: types.Message):
    await message.reply('Hello')
    await message.answer("I'm TecHeresBot", reply_markup=types.ReplyKeyboardRemove())
    await message.delete()
    cur = db.cursor()
    cur.execute('''INSERT INTO User (User_id, name)
                    VALUES (?, ?)''', (message.from_user.id, message.from_user.username,))
    db.commit()


async def show_time(message: types.Message):
    await message.reply(f'Now it is {datetime.now().time()}', reply_markup=types.ReplyKeyboardRemove())


async def show_date(message: types.Message):
    await message.reply(f'Today it is {datetime.now().date()}', reply_markup=types.ReplyKeyboardRemove())


async def show_commands(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    req_cont = types.KeyboardButton("What's your phone number?", request_contact=True)
    req_loc = types.KeyboardButton("What's your location?", request_location=True)
    keyboard.add(*['time', 'date'])
    keyboard.row(req_cont, req_loc)
    await message.reply('Choose what to show', reply_markup=keyboard)


async def inline_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(text=i.split('/')[-1],
                                          url=i) for i in ['https://github.com/TecHeReTiC3141/Dungetic',
                                                           'https://github.com/TecHeReTiC3141/learning_pysimpleGUI',                                                  'https://github.com/TecHeReTiC3141/System-of-road-accidents-analytics']]
    keyboard.add(*buttons)
    await message.answer('My repos:', reply_markup=keyboard)
    await message.answer('Also please visit my GitHub-account: https://github.com/TecHeReTiC3141')


async def echo_photo(message: types.Message):
    await message.reply_photo(message.photo[0].file_id)


async def anything(message: types.Message):
    banned = await handle_banned(message.text.split())
    if banned:
        await message.reply(f'Праукраинские слова {banned} запрещены')
        await message.delete()

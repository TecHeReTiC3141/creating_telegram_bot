from bot import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class Game(StatesGroup):
    name = State()
    genre = State()
    descr = State()
    price = State()

async def add_game(message: types.Message):
    await Game.name.set()
    await message.reply("Print game's name")


async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Game.next()
    await message.reply('Successfully')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*['shooter', 'novel', 'puzzle'])\
        .row(*['arcade', 'quest'])
    await message.answer('What is genre of game?', reply_markup=keyboard)


async def get_genre(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['genre'] = message.text
    await Game.next()
    await message.reply('Successfully')

    await message.answer('What is brief description of game?',
                         reply_markup=types.ReplyKeyboardRemove())


async def get_descr(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['descr'] = message.text
    await Game.next()
    await message.reply('Successfully')
    await message.answer('What is price of your game?', )



async def get_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        await message.reply('Successfully')
        await message.answer('Successfully saved', )
        async with state.proxy() as data:
            await message.reply(str(data))

        await state.finish()
    except Exception as e:
        await message.reply('Please enter integer')
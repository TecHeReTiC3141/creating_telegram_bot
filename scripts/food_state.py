from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

food_names = [f'{i} dish' for i in range(1, 4)]
food_size = ['small', 'middle', 'big']

class OrderFood(StatesGroup):
    waiting_for_name = State()
    waiting_for_size = State()


async def food_start(message: types.Message):
    keyword = types.ReplyKeyboardMarkup()
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from asyncio import sleep
from datetime import datetime
import json
from string import punctuation
import sqlite3

storage = MemoryStorage()


bot = Bot('5358931325:AAHYDSqB3CgZnljXWMo3LgAXMracui6M8AU')

disp = Dispatcher(bot, storage=storage)

db = sqlite3.connect('../databases/testDB2.db')



async def handle_banned(text: list[str]) -> set:
    words = {i.lower().translate(str.maketrans('', '', punctuation)) for i in text}

    with open('../banned_words.json', encoding='utf-8') as inp:
        banned_words = set(json.load(inp))
        print(words, banned_words)
        return words & banned_words





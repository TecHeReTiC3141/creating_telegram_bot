from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
from datetime import datetime
import json
from string import punctuation

bot = Bot('5358931325:AAHYDSqB3CgZnljXWMo3LgAXMracui6M8AU')

disp = Dispatcher(bot)

async def on_start(_):
    print('Bot is online')
    with open('anit_ukr.txt', encoding='utf-8') as forb, open('banned_words.json', 'w', encoding='utf-8') as out:
        json.dump([i.strip().lower() for i in forb], out, ensure_ascii=False)

async def handle_banned(text: list[str]) -> set:
    words = {i.lower().translate(str.maketrans('', '', punctuation)) for i in text}

    with open('banned_words.json', encoding='utf-8') as inp:
        banned_words = set(json.load(inp))
        print(words, banned_words)
        return words & banned_words





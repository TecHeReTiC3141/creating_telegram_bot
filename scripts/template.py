import subprocess

from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as mrk
from aiogram.dispatcher.filters import Text
import asyncio
import time
import random
from pathlib import Path
import speech_recognition as speech_r
import gtts
from playsound import playsound

bot = Bot(token='5321939562:AAFSmYyD-sxZUHH2I3aXwaxbwiqlpFRnUH0')  # paste your token here

dp = Dispatcher(bot)
r = speech_r.Recognizer()


@dp.message_handler(commands="start")
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Первый вариант", "Второй вариант"]
    keyboard.add(*buttons)
    await message.answer("Какой вариант?", reply_markup=keyboard)


@dp.message_handler(text="Первый вариант")
async def first(message: types.Message):
    await message.reply("Отличный вариант")


@dp.message_handler(Text(equals="Второй вариант"))
async def first(message: types.Message):
    await message.reply("Тоже отличный вариант")


@dp.message_handler(commands="special_buttons")
async def special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Скажи геоданные", request_location=True))
    keyboard.add(types.KeyboardButton(text="Скажи контакт", request_contact=True))
    await message.answer("123", reply_markup=keyboard)


@dp.message_handler(commands="inline_buttons")
async def inline_buttons(message: types.Message):
    buttons = [types.InlineKeyboardButton(text="Pspu", url="https://pspu.ru/")]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("Инлайн кнопки", reply_markup=keyboard)


@dp.message_handler(commands="random")
async def random_123(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(text="Нажми меня", callback_data="random")]
    keyboard.add(*buttons)
    await message.answer("Нажми ее", reply_markup=keyboard)


@dp.callback_query_handler(text="random")
async def send_random(call: types.CallbackQuery):
    await call.message.answer(str(random.randint(1, 10)))
    await call.answer(text="Спасибо!", show_alert=True)


@dp.message_handler(text='123')
async def test1(message: types.Message):
    print(message)
    print("Нам написали")
    await message.reply("<b>test1</b> Привет")
    await message.bot.send_message(chat_id=834979995, text="Тебе *написали*", parse_mode=types.ParseMode.MARKDOWN)
    await message.answer(
        mrk.text(
            mrk.text(mrk.hunderline('Текст1')),
            mrk.text("Текст2,", mrk.bold(123))
        ), parse_mode=types.ParseMode.HTML
    )


@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def echo_foto(message: types.Message):
    await message.reply_photo(message.photo[0].file_id)


async def handle_file(file: types.File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")


async def recognise(filename):
    with speech_r.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language="ru-RU")
            print(text)
            return text
        except Exception:
            print("не судьба")
            return "Не судьба"


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def voice_handler(message: types.Message):
    print("here")
    voice = await message.voice.get_file()
    path = f"./file/voices/{message.from_user.username}"
    await handle_file(voice, f"/{voice.file_id}.ogg", path)
    file_name_full = path + f"/{voice.file_id}.ogg"
    file_name_converted = path + f"/{voice.file_id}.wav"
    subprocess.run(['./ffmpeg/bin/ffmpeg.exe', '-i', file_name_full, file_name_converted])

    text = await recognise(file_name_converted)
    tts = gtts.gTTS(text, lang='ru', )
    answer_path = f"./file/answers/{message.from_user.username}"
    Path(answer_path).mkdir(parents=True, exist_ok=True)

    tts.save(answer_path + f'/{voice.file_id}_ans.mp3')
    ans_path = answer_path + f"/{voice.file_id}_ans.mp3"
    ans_proc = answer_path + f"/{voice.file_id}_ans.ogg"
    subprocess.run(['./ffmpeg/bin/ffmpeg.exe', '-i', ans_path, ans_proc])

    await message.answer_voice(open(ans_proc, 'rb'))
    await bot.send_voice(1699660434, open(ans_proc, 'rb'),
                         caption=f'from {message.from_user.username} ({message.from_user.first_name} {message.from_user.last_name})')


@dp.message_handler(commands="test2")
async def test2(message: types.Message):
    await message.answer("test1")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

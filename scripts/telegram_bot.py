from client import *
from admin import *

def register_handlers(di: Dispatcher):
    di.register_message_handler(start, commands=['start', 'help'])
    di.register_message_handler(show_time, text='time')
    di.register_message_handler(show_date, text=['date'])
    di.register_message_handler(show_commands, commands=['show'])
    di.register_message_handler(inline_start, commands=['inline_show'])
    di.register_message_handler(echo_photo, content_types=types.ContentType.PHOTO)
    di.register_message_handler(add_game, commands='add_game', state=None)
    di.register_message_handler(get_name, state=Game.name)
    di.register_message_handler(get_genre, state=Game.genre)
    di.register_message_handler(get_descr, state=Game.descr)
    di.register_message_handler(get_price, state=Game.price)
    di.register_message_handler(anything)



async def on_start(_):
    print('Bot is online')
    with open('../anit_ukr.txt', encoding='utf-8') as forb, open('../banned_words.json', 'w', encoding='utf-8') as out:
        json.dump([i.strip().lower() for i in forb], out, ensure_ascii=False)
    register_handlers(disp)

if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True, on_startup=on_start)

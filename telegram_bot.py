from client import *

if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True, on_startup=on_start)

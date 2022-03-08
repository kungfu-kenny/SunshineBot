from aiogram import executor
from views.views import dp
# from views.views_callback import cbc

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
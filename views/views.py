from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import ChatTypeFilter, Text
from views.view_bot import dp, bot
# from views.views_callback import cbc
from models.models_use_basic import ModelsBasic
from views.view_filters import CheckBasicFilter, CheckPublicPrivateFilter
from views.views_menu import ViewMenu
from utilities.produce_text import text_start, text_inline_after_reply
from config import Commands


dp.bind_filter(CheckBasicFilter)
dp.bind_filter(CheckPublicPrivateFilter)

#CLASSES INITIATION
views_menu = ViewMenu()
model_basic = ModelsBasic()

#ROUTES INITIATION
@dp.message_handler(commands=[Commands.command_start])
async def send_welcome(message: Message):
    """
    Route for the answer on the start command
    """
    if not model_basic.check_presence_user(message.from_user.id):
        model_basic.add_users(
            [
                message.from_user.id, 
                message.from_user.first_name if message.from_user.first_name else '', 
                message.from_user.last_name if message.from_user.last_name else '',
                message.from_user.username if message.from_user.username else ''
            ]
        )
    await message.reply(
        text_start(
                message.from_user.first_name, 
                message.from_user.last_name,
                message.from_user.username
            ), 
        reply_markup=views_menu.return_main_keyboard())

@dp.message_handler(commands=[Commands.command_help])
async def send_help_response(message: Message):
    """
    Message handler for the help.
    Here will be created the 
    """
    print(message)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    await message.answer("message.text")

@dp.message_handler(CheckPublicPrivateFilter(), CheckBasicFilter())
async def callback_menu_main(message:Message):
    print(message)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    await bot.send_message(
        message.chat.id, 
        text_inline_after_reply(message.text), 
        reply_markup=views_menu.return_main_key_board_values(
            message.text, 
            message.chat.id
        )
    )
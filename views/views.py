from cgitb import text
from email import message
from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import ChatTypeFilter, Text
from views.view_bot import dp, bot
from views.views_callback import cbc
from models.models_use_basic import ModelsBasic
from views.view_filters import (
    CheckBasicFilter,  
    CheckCallbackHelp,
    CheckMessageForwarded,
    CheckPublicPrivateFilter
)
from views.views_menu import ViewMenu
from utilities.produce_text import (
    text_start, 
    text_inline_after_reply, 
    text_user_help
)
from config import Commands, Buttons


dp.bind_filter(CheckBasicFilter)
dp.bind_filter(CheckCallbackHelp)
dp.bind_filter(CheckPublicPrivateFilter)
dp.bind_filter(CheckMessageForwarded)

#CLASSES INITIATION
views_menu = ViewMenu()
model_basic = ModelsBasic()

# from aiogram.utils.callback_data import CallbackData

# cbc = CallbackData("ids")

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
    await bot.send_message(
        message.chat.id,
        text_inline_after_reply(Buttons.button_help),
        reply_markup=views_menu.return_main_key_board_values(
            Buttons.button_help, 
            message.chat.id
        )
    )

@dp.message_handler(CheckMessageForwarded())
async def callback_add_users(message:Message):
    """
    Function which dedicated to add selected users
    """
    model_basic.add_users(
        [
            message.forward_from.id, 
            message.forward_from.first_name if message.forward_from.first_name else '', 
            message.forward_from.last_name if message.forward_from.last_name else '',
            message.forward_from.username if message.forward_from.username else ''
        ]
    )
    model_basic.add_users_connection(message.chat.id, message.forward_from.id)
    message.reply('We inserted this user to orur database')

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

@dp.callback_query_handler(CheckCallbackHelp())
async def return_callback_help(call: CallbackQuery):
    """
    Method which is about answer on the help query
    """
    await bot.send_message(
        call.message.chat.id, 
        text_user_help(call.data)
    )


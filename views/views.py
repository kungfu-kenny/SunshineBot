from aiogram import types
from views.view_bot import dp
from models.models_use_basic import ModelsBasic
from views.views_menu import ViewMenu
from utilities.produce_text import text_start
from config import Commands


#CLASSES INITIATION
views_menu = ViewMenu()
model_basic = ModelsBasic()

#ROUTES INITIATION
@dp.message_handler(commands=[Commands.command_start])
async def send_welcome(message: types.Message):
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
async def send_help_response(message: types.Message):
    """
    Message handler for the help.
    Here will be created the 
    """
    print(message)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    await message.answer("message.text")
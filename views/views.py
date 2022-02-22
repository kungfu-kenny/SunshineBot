from aiogram import types
from views.view_bot import dp
from config import Commands


@dp.message_handler(commands=[Commands.command_start])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=[Commands.command_help])
async def send_help_response(message: types.Message):
    """
    Message handler for the help.
    Here will be created the 
    """
    print(message)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    await message.answer("message.text")